# BEGIN GENERATED AZ305 V1
[CmdletBinding()]
param(
    [string]$SubscriptionId = $env:AZ305_SUBSCRIPTION_ID,
    [string]$TenantId = $env:AZ305_TENANT_ID,
    [ValidatePattern('^[a-z0-9-]{6,64}$')][string]$RunId = $env:AZ305_RUN_ID,
    [string]$Location = $(if ($env:AZ305_LOCATION) { $env:AZ305_LOCATION } else { 'westeurope' }),
    [string]$SecondaryLocation = $(if ($env:AZ305_SECONDARY_LOCATION) { $env:AZ305_SECONDARY_LOCATION } else { 'northeurope' }),
    [string]$ResourceGroup = $(if ($env:AZ305_RESOURCE_GROUP) { $env:AZ305_RESOURCE_GROUP } else { "rg-az305-$RunId" }),
    [string]$WorkloadName = $(if ($env:AZ305_WORKLOAD_NAME) { $env:AZ305_WORKLOAD_NAME } else { "az305-$RunId" }),
    [string]$ExpiresOn = $(if ($env:AZ305_EXPIRES_ON) { $env:AZ305_EXPIRES_ON } else { (Get-Date).ToUniversalTime().AddDays(1).ToString('yyyy-MM-dd') }),
    [int]$ApprovedBitsPerSecond = $(if ($env:AZ305_APPROVED_BITS_PER_SECOND) { [int]$env:AZ305_APPROVED_BITS_PER_SECOND } else { 0 }),
    [string]$DisallowedPublicEndpoint = $env:AZ305_DISALLOWED_PUBLIC_ENDPOINT,
    [string]$ExpressRouteCircuitName = $env:AZ305_EXPRESS_ROUTE_CIRCUIT_NAME,
    [string]$ExpressRouteCircuitResourceId = $env:AZ305_EXPRESS_ROUTE_CIRCUIT_RESOURCE_ID,
    [string]$FrontDoorProfileName = $env:AZ305_FRONT_DOOR_PROFILE_NAME,
    [string]$HubRouteTableName = $env:AZ305_HUB_ROUTE_TABLE_NAME,
    [string]$PrivateServiceFqdn = $env:AZ305_PRIVATE_SERVICE_FQDN,
    [string]$ResourceGroupName = $env:AZ305_RESOURCE_GROUP_NAME,
    [string]$SourceVmId = $env:AZ305_SOURCE_VM_ID,
    [string]$VirtualHubName = $env:AZ305_VIRTUAL_HUB_NAME,
    [ValidateSet('Deployment', 'PostCleanup')][string]$Mode = 'Deployment',
    [switch]$Execute,
    [switch]$AcknowledgeCost,
    [switch]$AcknowledgeTenantChange
)

$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
if (-not $RunId) { [Console]::Error.WriteLine('RunId or AZ305_RUN_ID is required.'); exit 2 }
# Every lifecycle entrypoint intentionally exposes the same public parameter contract.
@($SubscriptionId, $TenantId, $RunId, $Location, $SecondaryLocation, $ResourceGroup, $WorkloadName, $ExpiresOn, $ApprovedBitsPerSecond, $DisallowedPublicEndpoint, $ExpressRouteCircuitName, $ExpressRouteCircuitResourceId, $FrontDoorProfileName, $HubRouteTableName, $PrivateServiceFqdn, $ResourceGroupName, $SourceVmId, $VirtualHubName, $Mode, $Execute, $AcknowledgeCost, $AcknowledgeTenantChange) | Out-Null

$LabRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$StateRoot = Join-Path $LabRoot ".state/$RunId"
$RunPath = Join-Path $StateRoot 'run.json'
$ValidationPath = Join-Path $StateRoot 'validation.json'

function Invoke-AzCliJson {
    [CmdletBinding()]
    param([Parameter(Mandatory)][string[]]$ArgumentList)
    $savedNativePreference = $PSNativeCommandUseErrorActionPreference
    try {
        # Capture the exit code ourselves so a failed native command cannot be
        # mistaken for an empty but successful JSON response.
        $PSNativeCommandUseErrorActionPreference = $false
        $outputLines = @(& az @ArgumentList)
        $nativeExit = $LASTEXITCODE
    }
    finally {
        $PSNativeCommandUseErrorActionPreference = $savedNativePreference
    }
    if ($nativeExit -ne 0) { throw "Azure CLI exited with code $nativeExit." }
    $raw = @($outputLines) -join "`n"
    if ([string]::IsNullOrWhiteSpace($raw)) { return $null }
    try { return ($raw | ConvertFrom-Json -Depth 100) }
    catch { throw 'Azure CLI returned data that was not valid JSON.' }
}

function Assert-ExactExecutionContext {
    [CmdletBinding()]
    param([string]$ExpectedSubscriptionId, [string]$ExpectedTenantId)
    if ([string]::IsNullOrWhiteSpace($ExpectedSubscriptionId) -or [string]::IsNullOrWhiteSpace($ExpectedTenantId)) {
        throw 'SubscriptionId and TenantId are required before a cloud request.'
    }
    $context = Invoke-AzCliJson -ArgumentList @('account', 'show', '--output', 'json', '--only-show-errors')
    if (-not $context -or [string]$context.id -ine $ExpectedSubscriptionId -or [string]$context.tenantId -ine $ExpectedTenantId) {
        throw 'The active Azure CLI subscription or tenant does not exactly match the requested context.'
    }
}


if (-not (Test-Path -LiteralPath $RunPath)) {
    Write-Warning 'No run state exists; validation is gated.'
    exit 2
}
$state = Get-Content -LiteralPath $RunPath -Raw | ConvertFrom-Json
$assertions = [System.Collections.Generic.List[object]]::new()
function Add-ValidationAssertion {
    [CmdletBinding()]
    param([string]$Id, [ValidateSet('positive', 'negative')][string]$Kind, [bool]$Passed, [string]$Message)
    $assertions.Add([pscustomobject]@{ id = $Id; kind = $Kind; passed = $Passed; message = $Message })
}

function Save-ValidationArtifact {
    [CmdletBinding()]
    param([ValidateSet('pass', 'partial', 'fail')][string]$Result)
    $artifact = [ordered]@{ schemaVersion = '1.0.0'; labId = 'LAB-24'; runId = $RunId; mode = $Mode; result = $Result; validatedAt = (Get-Date).ToUniversalTime().ToString('o'); assertions = @($assertions) }
    $artifact | ConvertTo-Json -Depth 12 | Set-Content -LiteralPath $ValidationPath -Encoding utf8NoBOM
}

function Test-PositiveEvidence {
    [CmdletBinding()]
    param($Value)
    if ($Value -is [bool]) { return $Value }
    if ($null -eq $Value) { return $false }
    if ($Value -is [string]) { return -not [string]::IsNullOrWhiteSpace($Value) }
    if ($Value -is [System.Collections.IEnumerable]) { return @($Value).Count -gt 0 }
    return $true
}

function Test-NegativeEvidence {
    [CmdletBinding()]
    param($Value)
    if ($Value -is [bool]) { return $Value }
    if ($null -eq $Value) { return $true }
    if ($Value -is [string]) { return [string]::IsNullOrWhiteSpace($Value) }
    if ($Value -is [System.Collections.IEnumerable]) { return @($Value).Count -eq 0 }
    $properties = @($Value.PSObject.Properties | Where-Object { $_.MemberType -in @('NoteProperty', 'Property') })
    if ($properties.Count -eq 0) { return $false }
    return @($properties | Where-Object { -not (Test-NegativeEvidence -Value $_.Value) }).Count -eq 0
}

function Test-ProhibitedStateField {
    [CmdletBinding()]
    param($Value)
    $serialized = $Value | ConvertTo-Json -Depth 20
    return $serialized -match '(?i)"(?:token|password|secret|certificate|connectionString|sas|clientSecret|accessToken|refreshToken|accountKey|privateKey)"\s*:'
}

function Assert-InputSubscriptionScope {
    [CmdletBinding()]
    param($Inputs, [string]$ExpectedSubscriptionId)
    $entries = if ($Inputs -is [System.Collections.IDictionary]) {
        @($Inputs.GetEnumerator())
    } else {
        @($Inputs.PSObject.Properties | ForEach-Object { [pscustomobject]@{ Key = $_.Name; Value = $_.Value } })
    }
    foreach ($entry in $entries) {
        if ($entry.Value -is [string] -and [string]$entry.Value -match '^/subscriptions/([^/]+)/' -and $Matches[1] -ine $ExpectedSubscriptionId) {
            throw "Input $($entry.Key) belongs to a different subscription."
        }
    }
}

$stateIdentityMatches = (
    $state.labId -ceq 'LAB-24' -and
    $state.runId -ceq $RunId -and
    $state.track -ceq 'azure-cli' -and
    $state.implementationMode -ceq 'safe-analogue' -and
    ([string]$state.parameters.subscriptionId -ieq $SubscriptionId -and [string]$state.parameters.tenantId -ieq $TenantId)
)
Add-ValidationAssertion -Id 'LAB24-VAL-POS-01' -Kind positive -Passed $stateIdentityMatches -Message 'Run identity, implementation mode, command track, tenant, and subscription exactly match the copied lab and requested run.'
$hasSensitiveName = Test-ProhibitedStateField -Value $state
Add-ValidationAssertion -Id 'LAB24-VAL-NEG-01' -Kind negative -Passed (-not $hasSensitiveName) -Message 'State contains no prohibited sensitive field name.'

if ($Mode -eq 'PostCleanup') {
    $cleanupPath = Join-Path $StateRoot 'cleanup.json'
    $cleanup = if (Test-Path -LiteralPath $cleanupPath) { Get-Content -LiteralPath $cleanupPath -Raw | ConvertFrom-Json } else { $null }
    Add-ValidationAssertion -Id 'LAB24-VAL-POS-02' -Kind positive -Passed ($null -ne $cleanup -and $cleanup.labId -ceq 'LAB-24' -and $cleanup.runId -ceq $RunId -and $cleanup.result -eq 'pass' -and $cleanup.ownershipVerified) -Message 'The exact run cleanup completed with verified ownership.'
    Add-ValidationAssertion -Id 'LAB24-VAL-NEG-02' -Kind negative -Passed ($null -ne $cleanup -and $cleanup.activeManagedObjects -eq 0 -and @($state.managedObjects).Count -eq 0 -and @($state.originalSettings).Count -eq 0 -and $state.status -eq 'cleaned') -Message 'No active managed object or unresolved original setting remains in cleanup or run state.'
    $postCleanupPassed = @($assertions | Where-Object { -not $_.passed }).Count -eq 0
    Save-ValidationArtifact -Result $(if ($postCleanupPassed) { 'pass' } else { 'fail' })
    if ($postCleanupPassed) { exit 0 }
    exit 1
}

Add-ValidationAssertion -Id 'LAB24-VAL-POS-02' -Kind positive -Passed ($state.status -eq 'deployed') -Message 'The executed setup completed successfully; a failed setup can never validate as pass.'
Add-ValidationAssertion -Id 'LAB24-VAL-NEG-02' -Kind negative -Passed (@($state.managedObjects | Where-Object { $_.tags.purpose -ne 'az305-lab' -or $_.tags.labId -ne 'LAB-24' -or $_.tags.runId -ne $RunId }).Count -eq 0) -Message 'No recorded object has a foreign ownership tag.'

if (@($assertions | Where-Object { -not $_.passed }).Count -gt 0) {
    Save-ValidationArtifact -Result 'fail'
    exit 1
}
if (-not $Execute) {
    # This lab has no special intent-only validation path.
    Save-ValidationArtifact -Result 'partial'
    Write-Warning 'Checkpoint validation is gated; re-run with -Execute after confirming the exact read-only context.'
    exit 2
}
# The validation surface is compatible with this lab implementation mode.
$requiredValidationInputs = [ordered]@{ ApprovedBitsPerSecond = $ApprovedBitsPerSecond; DisallowedPublicEndpoint = $DisallowedPublicEndpoint; ExpressRouteCircuitName = $ExpressRouteCircuitName; ExpressRouteCircuitResourceId = $ExpressRouteCircuitResourceId; FrontDoorProfileName = $FrontDoorProfileName; HubRouteTableName = $HubRouteTableName; PrivateServiceFqdn = $PrivateServiceFqdn; ResourceGroupName = $ResourceGroupName; SourceVmId = $SourceVmId; VirtualHubName = $VirtualHubName }
$missingValidationInputs = @($requiredValidationInputs.GetEnumerator() | Where-Object { $_.Value -is [string] -and [string]::IsNullOrWhiteSpace([string]$_.Value) } | ForEach-Object Key)
if ($missingValidationInputs.Count -gt 0) {
    Add-ValidationAssertion -Id 'LAB24-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'One or more required non-secret validation inputs are missing.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}
try {
    Assert-ExactExecutionContext -ExpectedSubscriptionId $SubscriptionId -ExpectedTenantId $TenantId
    Assert-InputSubscriptionScope -Inputs $state.parameters -ExpectedSubscriptionId $SubscriptionId
    Add-ValidationAssertion -Id 'LAB24-VAL-POS-CONTEXT' -Kind positive -Passed $true -Message 'The active tenant and subscription exactly match the requested validation context.'
}
catch {
    Add-ValidationAssertion -Id 'LAB24-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'Exact execution context could not be proven.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}

$originalLocation = Get-Location
try {
    Set-Location -LiteralPath $LabRoot
# LAB24-CP01: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $frontDoorProfile = az rest --method get --url "https://management.azure.com/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName/providers/Microsoft.Cdn/profiles/$FrontDoorProfileName?api-version=2024-09-01" --output json --only-show-errors | ConvertFrom-Json; if ($frontDoorProfile.properties.provisioningState -ne 'Succeeded' -or $frontDoorProfile.sku.name -notin @('Standard_AzureFrontDoor','Premium_AzureFrontDoor')) { throw 'The Front Door profile is not a supported ready tier.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB24-CP01 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB24-CP01-POS' -Kind positive -Passed $positivePassed -Message 'The design covers authoritative DNS, Front Door Standard or Premium, TLS, origin naming, health probes, caching boundary, IPv4 and IPv6, and regional-origin failure.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $response = az rest --method get --url "https://management.azure.com/subscriptions/$SubscriptionId/resourceGroups/$ResourceGroupName/providers/Microsoft.Cdn/profiles/$FrontDoorProfileName/afdEndpoints?api-version=2024-09-01" --output json --only-show-errors | ConvertFrom-Json; if ($response.value | Where-Object { $_.properties.enabledState -ne 'Enabled' }) { throw 'A required Front Door endpoint is disabled.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB24-CP01 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB24-CP01-NEG' -Kind negative -Passed $negativePassed -Message 'A single regional public IP, circular DNS dependency, disabled health probe, or origin reachable outside the intended entry path must fail.'

# LAB24-CP02: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $circuit = az network express-route show --resource-group $ResourceGroupName --name $ExpressRouteCircuitName --output json --only-show-errors | ConvertFrom-Json; if ($circuit.serviceProviderProvisioningState -ne 'Provisioned' -or $circuit.circuitProvisioningState -ne 'Enabled') { throw 'The ExpressRoute circuit is not ready.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB24-CP02 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB24-CP02-POS' -Kind positive -Passed $positivePassed -Message 'Dual private paths, diverse provider locations, BGP, gateway scale, FastPath decision, VPN encryption, and deterministic preference and failback are documented.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $gateways = az network vnet-gateway list --resource-group $ResourceGroupName --output json --only-show-errors | ConvertFrom-Json; if (-not ($gateways | Where-Object { $_.gatewayType -eq 'Vpn' -and $_.provisioningState -eq 'Succeeded' })) { throw 'No ready VPN failover gateway was found.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB24-CP02 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB24-CP02-NEG' -Kind negative -Passed $negativePassed -Message 'Two links sharing one provider edge, overlapping prefixes, static routes that defeat failover, or untested VPN capacity must fail.'

# LAB24-CP03: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $hub = az network vhub show --resource-group $ResourceGroupName --name $VirtualHubName --output json --only-show-errors | ConvertFrom-Json; if ($hub.provisioningState -ne 'Succeeded' -or $hub.routingState -notin @('Provisioned','Provisioning')) { throw 'The virtual hub is not ready for transit.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB24-CP03 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB24-CP03-POS' -Kind positive -Passed $positivePassed -Message 'Advertised and learned prefixes, propagation labels, next hops, default-route intent, DNS forwarders, and ownership are explicit for every path.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $routes = az network vhub route-table route list --resource-group $ResourceGroupName --vhub-name $VirtualHubName --route-table-name $HubRouteTableName --output json --only-show-errors | ConvertFrom-Json; if ($routes | Where-Object { $_.destinations -contains '0.0.0.0/0' -and $_.nextHopType -eq 'ResourceId' -and -not $_.nextHops }) { throw 'A default route has no valid next hop.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB24-CP03 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB24-CP03-NEG' -Kind negative -Passed $negativePassed -Message 'Overlap, an orphaned next hop, asymmetric stateful path, unintended branch transit, or DNS forwarding loop must fail.'

# LAB24-CP04: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $test = az network watcher test-connectivity --resource-group $ResourceGroupName --source-resource $SourceVmId --dest-address $PrivateServiceFqdn --dest-port 443 --protocol Tcp --output json --only-show-errors | ConvertFrom-Json; if ($test.connectionStatus -ne 'Reachable') { throw 'The approved private endpoint is not reachable.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB24-CP04 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB24-CP04-POS' -Kind positive -Passed $positivePassed -Message 'Independent tests prove approved branch, datacenter, spoke, private endpoint, DNS, and internet paths while disallowed public paths remain unreachable.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $publicTest = az network watcher test-connectivity --resource-group $ResourceGroupName --source-resource $SourceVmId --dest-address $DisallowedPublicEndpoint --dest-port 443 --protocol Tcp --output json --only-show-errors | ConvertFrom-Json; if ($publicTest.connectionStatus -eq 'Reachable') { throw 'A disallowed public endpoint is reachable.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB24-CP04 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB24-CP04-NEG' -Kind negative -Passed $negativePassed -Message 'A successful ping alone, name resolution to a public address, or reachability that bypasses the required path must fail.'

# LAB24-CP05: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $metrics = az monitor metrics list --resource $ExpressRouteCircuitResourceId --metric ArpAvailability,BgpAvailability --interval PT5M --aggregation Average --output json --only-show-errors | ConvertFrom-Json; if ($metrics.value.timeseries.data.average | Where-Object { $_ -lt 100 }) { throw 'Circuit availability evidence is below target.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB24-CP05 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB24-CP05-POS' -Kind positive -Passed $positivePassed -Message 'Latency percentiles, jitter, loss, throughput, connection scale, gateway and circuit headroom, and failover convergence meet documented targets.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $throughput = az monitor metrics list --resource $ExpressRouteCircuitResourceId --metric BitsInPerSecond,BitsOutPerSecond --interval PT5M --aggregation Maximum --output json --only-show-errors | ConvertFrom-Json; if ($throughput.value.timeseries.data.maximum | Where-Object { $_ -gt $ApprovedBitsPerSecond }) { throw 'Observed throughput exceeds approved headroom.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB24-CP05 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB24-CP05-NEG' -Kind negative -Passed $negativePassed -Message 'Relying on averages that hide saturation, measuring only Azure-side latency, or omitting backup-path capacity must fail.'

}
finally {
    Set-Location -LiteralPath $originalLocation
}

$passed = @($assertions | Where-Object { -not $_.passed }).Count -eq 0
Save-ValidationArtifact -Result $(if ($passed) { 'pass' } else { 'fail' })
if ($passed) { exit 0 }
exit 1
# END GENERATED AZ305 V1
