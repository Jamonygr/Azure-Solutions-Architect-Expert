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
    [string]$ControlVmSku = $env:AZ305_CONTROL_VM_SKU,
    [string]$ResourceGroupName = $env:AZ305_RESOURCE_GROUP_NAME,
    [string]$WorkerVmSku = $env:AZ305_WORKER_VM_SKU,
    [ValidateSet('Deployment', 'PostCleanup')][string]$Mode = 'Deployment',
    [switch]$Execute,
    [switch]$AcknowledgeCost,
    [switch]$AcknowledgeTenantChange
)

$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
if (-not $RunId) { [Console]::Error.WriteLine('RunId or AZ305_RUN_ID is required.'); exit 2 }
# Every lifecycle entrypoint intentionally exposes the same public parameter contract.
@($SubscriptionId, $TenantId, $RunId, $Location, $SecondaryLocation, $ResourceGroup, $WorkloadName, $ExpiresOn, $ControlVmSku, $ResourceGroupName, $WorkerVmSku, $Mode, $Execute, $AcknowledgeCost, $AcknowledgeTenantChange) | Out-Null

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
    $artifact = [ordered]@{ schemaVersion = '1.0.0'; labId = 'LAB-18'; runId = $RunId; mode = $Mode; result = $Result; validatedAt = (Get-Date).ToUniversalTime().ToString('o'); assertions = @($assertions) }
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
    $state.labId -ceq 'LAB-18' -and
    $state.runId -ceq $RunId -and
    $state.track -ceq 'azure-cli' -and
    $state.implementationMode -ceq 'reference-deployable' -and
    ([string]$state.parameters.subscriptionId -ieq $SubscriptionId -and [string]$state.parameters.tenantId -ieq $TenantId)
)
Add-ValidationAssertion -Id 'LAB18-VAL-POS-01' -Kind positive -Passed $stateIdentityMatches -Message 'Run identity, implementation mode, command track, tenant, and subscription exactly match the copied lab and requested run.'
$hasSensitiveName = Test-ProhibitedStateField -Value $state
Add-ValidationAssertion -Id 'LAB18-VAL-NEG-01' -Kind negative -Passed (-not $hasSensitiveName) -Message 'State contains no prohibited sensitive field name.'

if ($Mode -eq 'PostCleanup') {
    $cleanupPath = Join-Path $StateRoot 'cleanup.json'
    $cleanup = if (Test-Path -LiteralPath $cleanupPath) { Get-Content -LiteralPath $cleanupPath -Raw | ConvertFrom-Json } else { $null }
    Add-ValidationAssertion -Id 'LAB18-VAL-POS-02' -Kind positive -Passed ($null -ne $cleanup -and $cleanup.labId -ceq 'LAB-18' -and $cleanup.runId -ceq $RunId -and $cleanup.result -eq 'pass' -and $cleanup.ownershipVerified) -Message 'The exact run cleanup completed with verified ownership.'
    Add-ValidationAssertion -Id 'LAB18-VAL-NEG-02' -Kind negative -Passed ($null -ne $cleanup -and $cleanup.activeManagedObjects -eq 0 -and @($state.managedObjects).Count -eq 0 -and @($state.originalSettings).Count -eq 0 -and $state.status -eq 'cleaned') -Message 'No active managed object or unresolved original setting remains in cleanup or run state.'
    $postCleanupPassed = @($assertions | Where-Object { -not $_.passed }).Count -eq 0
    Save-ValidationArtifact -Result $(if ($postCleanupPassed) { 'pass' } else { 'fail' })
    if ($postCleanupPassed) { exit 0 }
    exit 1
}

Add-ValidationAssertion -Id 'LAB18-VAL-POS-02' -Kind positive -Passed ($state.status -eq 'deployed') -Message 'The executed setup completed successfully; a failed setup can never validate as pass.'
Add-ValidationAssertion -Id 'LAB18-VAL-NEG-02' -Kind negative -Passed (@($state.managedObjects | Where-Object { $_.tags.purpose -ne 'az305-lab' -or $_.tags.labId -ne 'LAB-18' -or $_.tags.runId -ne $RunId }).Count -eq 0) -Message 'No recorded object has a foreign ownership tag.'

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
$requiredValidationInputs = [ordered]@{ ControlVmSku = $ControlVmSku; ResourceGroupName = $ResourceGroupName; WorkerVmSku = $WorkerVmSku }
$missingValidationInputs = @($requiredValidationInputs.GetEnumerator() | Where-Object { $_.Value -is [string] -and [string]::IsNullOrWhiteSpace([string]$_.Value) } | ForEach-Object Key)
if ($missingValidationInputs.Count -gt 0) {
    Add-ValidationAssertion -Id 'LAB18-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'One or more required non-secret validation inputs are missing.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}
try {
    Assert-ExactExecutionContext -ExpectedSubscriptionId $SubscriptionId -ExpectedTenantId $TenantId
    Assert-InputSubscriptionScope -Inputs $state.parameters -ExpectedSubscriptionId $SubscriptionId
    Add-ValidationAssertion -Id 'LAB18-VAL-POS-CONTEXT' -Kind positive -Passed $true -Message 'The active tenant and subscription exactly match the requested validation context.'
}
catch {
    Add-ValidationAssertion -Id 'LAB18-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'Exact execution context could not be proven.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}

$originalLocation = Get-Location
try {
    Set-Location -LiteralPath $LabRoot
# LAB18-CP01: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $skus = az vm list-skus --location $Location --size $ControlVmSku --all --output json --only-show-errors | ConvertFrom-Json; if (-not $skus -or $skus[0].restrictions.Count -gt 0) { throw 'The selected control VM SKU is unavailable or restricted.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB18-CP01 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB18-CP01-POS' -Kind positive -Passed $positivePassed -Message 'The requirement matrix captures instruction set, vCPU, memory, scratch space, network, image, job duration, concurrency, availability, quota, and data-gravity needs.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $skus = az vm list-skus --location $Location --size $WorkerVmSku --all --output json --only-show-errors | ConvertFrom-Json; if (-not ($skus[0].locationInfo.zones)) { throw 'The worker SKU has no documented zone capability.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB18-CP01 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB18-CP01-NEG' -Kind negative -Passed $negativePassed -Message 'Selecting a familiar SKU before checking batch-window throughput, quota, or regional restrictions must fail.'

# LAB18-CP02: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $template = az bicep build --file artifacts/main.bicep --stdout --only-show-errors | ConvertFrom-Json; $types = @($template.resources.type); $vmss = $template.resources | Where-Object type -eq 'Microsoft.Compute/virtualMachineScaleSets'; if ('Microsoft.Batch/batchAccounts' -notin $types -or 'Microsoft.Batch/batchAccounts/pools' -notin $types -or -not $vmss.properties.virtualMachineProfile) { throw 'The compiled template lacks the Batch pool or complete VMSS profile.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB18-CP02 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB18-CP02-POS' -Kind positive -Passed $positivePassed -Message 'Compilation succeeds and the template contains a tagged, parameterized, three-zone-capable VMSS at zero capacity plus a private, zero-node Batch pool, networking, identity, and no embedded secret.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $template = az bicep build --file artifacts/main.bicep --stdout --only-show-errors | ConvertFrom-Json; if ($template.resources | Where-Object { $_.properties -and ($_.properties | ConvertTo-Json -Depth 20) -match 'password|accountKey' }) { throw 'The template appears to contain an inline secret.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB18-CP02 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB18-CP02-NEG' -Kind negative -Passed $negativePassed -Message 'An unpinned image, unrestricted management ingress, missing shutdown control, or plaintext credential must fail lint review.'

# LAB18-CP03: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $preview = az deployment group what-if --resource-group $ResourceGroupName --template-file artifacts/main.bicep --parameters artifacts/parameters.example.json runId=$RunId expiresOn=$ExpiresOn --result-format ResourceIdOnly --output json --only-show-errors | ConvertFrom-Json; if (-not ($preview.changes | Where-Object changeType -eq 'Create')) { throw 'What-if produced no owned resource creation.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB18-CP03 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB18-CP03-POS' -Kind positive -Passed $positivePassed -Message 'What-if contains only new run-owned resources, zero control and worker capacity, no public IP allocation, and the required ownership and expiry tags.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $preview = az deployment group what-if --resource-group $ResourceGroupName --template-file artifacts/main.bicep --parameters artifacts/parameters.example.json runId=$RunId expiresOn=$ExpiresOn --result-format FullResourcePayloads --output json --only-show-errors | ConvertFrom-Json; if ($preview.changes | Where-Object changeType -ne 'Create') { throw 'What-if would modify, delete, or reuse a pre-existing resource.' }; if (($preview | ConvertTo-Json -Depth 50) -match '0\.0\.0\.0/0') { throw 'What-if exposes unrestricted network access.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB18-CP03 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB18-CP03-NEG' -Kind negative -Passed $negativePassed -Message 'Any destructive change, unbounded autoscale maximum, untagged resource, or unrelated scope must block execution.'

# LAB18-CP04: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $deployment = az deployment group show --resource-group $ResourceGroupName --name "lab18-$RunId" --output json --only-show-errors | ConvertFrom-Json; if ($deployment.properties.provisioningState -ne 'Succeeded') { throw 'The reference deployment did not succeed.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB18-CP04 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB18-CP04-POS' -Kind positive -Passed $positivePassed -Message 'The bounded reference footprint deploys only after execution and cost acknowledgements, and returned IDs are persisted immediately in run state.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $foreign = az resource list --resource-group $ResourceGroupName --query "[?tags.runId!='$RunId' || tags.labId!='LAB-18' || tags.purpose!='az305-lab']" --output json --only-show-errors | ConvertFrom-Json; if ($foreign.Count -gt 0) { throw 'The resource group contains an ownership mismatch.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB18-CP04 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB18-CP04-NEG' -Kind negative -Passed $negativePassed -Message 'Missing pre-mutation state, a failed ownership assertion, or an unrecorded returned resource ID makes the deployment unsafe.'

# LAB18-CP05: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $PoolResourceId = az deployment group show --resource-group $ResourceGroupName --name "lab18-$RunId" --query "properties.outputs.cleanupResourceIds.value[?contains(@, '/pools/')]|[0]" --output tsv --only-show-errors; $pool = az resource show --ids $PoolResourceId --api-version 2024-07-01 --output json --only-show-errors | ConvertFrom-Json; if (-not $pool -or $pool.properties.scaleSettings.fixedScale.targetDedicatedNodes -ne 0 -or $pool.properties.scaleSettings.fixedScale.targetLowPriorityNodes -ne 0) { throw 'The included Batch pool is absent or has nonzero target capacity.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB18-CP05 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB18-CP05-POS' -Kind positive -Passed $positivePassed -Message 'The exact pool emitted by the deployment remains at zero nodes, uses no public node IPs, and records the image, VM size, subnet, and later scale prerequisites without running a job.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $PoolResourceId = az deployment group show --resource-group $ResourceGroupName --name "lab18-$RunId" --query "properties.outputs.cleanupResourceIds.value[?contains(@, '/pools/')]|[0]" --output tsv --only-show-errors; $pool = az resource show --ids $PoolResourceId --api-version 2024-07-01 --output json --only-show-errors | ConvertFrom-Json; if ($pool.properties.networkConfiguration.publicIPAddressConfiguration.provision -ne 'NoPublicIPAddresses' -or $pool.properties.scaleSettings.autoScale) { throw 'The bounded pool permits public node IPs or unbounded autoscale.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB18-CP05 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB18-CP05-NEG' -Kind negative -Passed $negativePassed -Message 'A nonzero node target, public node IP, autoscale formula, unsupported image pair, or implicit outbound dependency must fail the bounded reference review.'

}
finally {
    Set-Location -LiteralPath $originalLocation
}

$passed = @($assertions | Where-Object { -not $_.passed }).Count -eq 0
Save-ValidationArtifact -Result $(if ($passed) { 'pass' } else { 'fail' })
if ($passed) { exit 0 }
exit 1
# END GENERATED AZ305 V1
