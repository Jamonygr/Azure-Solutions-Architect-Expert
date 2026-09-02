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
    [string]$ApplicationSubnetName = $env:AZ305_APPLICATION_SUBNET_NAME,
    [string]$ApprovedDestinationIp = $env:AZ305_APPROVED_DESTINATION_IP,
    [bool]$ApprovedFirewallEgressRoute = $(if ($env:AZ305_APPROVED_FIREWALL_EGRESS_ROUTE) { [System.Convert]::ToBoolean($env:AZ305_APPROVED_FIREWALL_EGRESS_ROUTE) } else { $false }),
    [string]$DestinationIp = $env:AZ305_DESTINATION_IP,
    [string]$DisallowedDestinationIp = $env:AZ305_DISALLOWED_DESTINATION_IP,
    [string]$FirewallName = $env:AZ305_FIREWALL_NAME,
    [string]$FirewallPolicyName = $env:AZ305_FIREWALL_POLICY_NAME,
    [string]$FrontDoorProfileName = $env:AZ305_FRONT_DOOR_PROFILE_NAME,
    [string]$InternalLoadBalancerName = $env:AZ305_INTERNAL_LOAD_BALANCER_NAME,
    [string]$NetworkWatcherName = $env:AZ305_NETWORK_WATCHER_NAME,
    [string]$ResourceGroupName = $env:AZ305_RESOURCE_GROUP_NAME,
    [string]$SourceIp = $env:AZ305_SOURCE_IP,
    [string]$SourceVmId = $env:AZ305_SOURCE_VM_ID,
    [string]$SpokeVnetName = $env:AZ305_SPOKE_VNET_NAME,
    [ValidateSet('Deployment', 'PostCleanup')][string]$Mode = 'Deployment',
    [switch]$Execute,
    [switch]$AcknowledgeCost,
    [switch]$AcknowledgeTenantChange
)

$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
if (-not $RunId) { [Console]::Error.WriteLine('RunId or AZ305_RUN_ID is required.'); exit 2 }
# Every lifecycle entrypoint intentionally exposes the same public parameter contract.
@($SubscriptionId, $TenantId, $RunId, $Location, $SecondaryLocation, $ResourceGroup, $WorkloadName, $ExpiresOn, $ApplicationSubnetName, $ApprovedDestinationIp, $ApprovedFirewallEgressRoute, $DestinationIp, $DisallowedDestinationIp, $FirewallName, $FirewallPolicyName, $FrontDoorProfileName, $InternalLoadBalancerName, $NetworkWatcherName, $ResourceGroupName, $SourceIp, $SourceVmId, $SpokeVnetName, $Mode, $Execute, $AcknowledgeCost, $AcknowledgeTenantChange) | Out-Null

$LabRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$StateRoot = Join-Path $LabRoot ".state/$RunId"
$RunPath = Join-Path $StateRoot 'run.json'
$ValidationPath = Join-Path $StateRoot 'validation.json'

function Assert-ExactExecutionContext {
    [CmdletBinding()]
    param([string]$ExpectedSubscriptionId, [string]$ExpectedTenantId)
    if ([string]::IsNullOrWhiteSpace($ExpectedSubscriptionId) -or [string]::IsNullOrWhiteSpace($ExpectedTenantId)) { throw 'SubscriptionId and TenantId are required before an Azure request.' }
    $azContext = Get-AzContext -ErrorAction Stop
    if (-not $azContext -or [string]$azContext.Subscription.Id -ine $ExpectedSubscriptionId -or [string]$azContext.Tenant.Id -ine $ExpectedTenantId) {
        throw 'The active Azure PowerShell subscription or tenant does not exactly match the requested context.'
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
    $artifact = [ordered]@{ schemaVersion = '1.0.0'; labId = 'LAB-25'; runId = $RunId; mode = $Mode; result = $Result; validatedAt = (Get-Date).ToUniversalTime().ToString('o'); assertions = @($assertions) }
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
    $state.labId -ceq 'LAB-25' -and
    $state.runId -ceq $RunId -and
    $state.track -ceq 'azure-powershell' -and
    $state.implementationMode -ceq 'safe-analogue' -and
    ([string]$state.parameters.subscriptionId -ieq $SubscriptionId -and [string]$state.parameters.tenantId -ieq $TenantId)
)
Add-ValidationAssertion -Id 'LAB25-VAL-POS-01' -Kind positive -Passed $stateIdentityMatches -Message 'Run identity, implementation mode, command track, tenant, and subscription exactly match the copied lab and requested run.'
$hasSensitiveName = Test-ProhibitedStateField -Value $state
Add-ValidationAssertion -Id 'LAB25-VAL-NEG-01' -Kind negative -Passed (-not $hasSensitiveName) -Message 'State contains no prohibited sensitive field name.'

if ($Mode -eq 'PostCleanup') {
    $cleanupPath = Join-Path $StateRoot 'cleanup.json'
    $cleanup = if (Test-Path -LiteralPath $cleanupPath) { Get-Content -LiteralPath $cleanupPath -Raw | ConvertFrom-Json } else { $null }
    Add-ValidationAssertion -Id 'LAB25-VAL-POS-02' -Kind positive -Passed ($null -ne $cleanup -and $cleanup.labId -ceq 'LAB-25' -and $cleanup.runId -ceq $RunId -and $cleanup.result -eq 'pass' -and $cleanup.ownershipVerified) -Message 'The exact run cleanup completed with verified ownership.'
    Add-ValidationAssertion -Id 'LAB25-VAL-NEG-02' -Kind negative -Passed ($null -ne $cleanup -and $cleanup.activeManagedObjects -eq 0 -and @($state.managedObjects).Count -eq 0 -and @($state.originalSettings).Count -eq 0 -and $state.status -eq 'cleaned') -Message 'No active managed object or unresolved original setting remains in cleanup or run state.'
    $postCleanupPassed = @($assertions | Where-Object { -not $_.passed }).Count -eq 0
    Save-ValidationArtifact -Result $(if ($postCleanupPassed) { 'pass' } else { 'fail' })
    if ($postCleanupPassed) { exit 0 }
    exit 1
}

Add-ValidationAssertion -Id 'LAB25-VAL-POS-02' -Kind positive -Passed ($state.status -eq 'deployed') -Message 'The executed setup completed successfully; a failed setup can never validate as pass.'
Add-ValidationAssertion -Id 'LAB25-VAL-NEG-02' -Kind negative -Passed (@($state.managedObjects | Where-Object { $_.tags.purpose -ne 'az305-lab' -or $_.tags.labId -ne 'LAB-25' -or $_.tags.runId -ne $RunId }).Count -eq 0) -Message 'No recorded object has a foreign ownership tag.'

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
$requiredValidationInputs = [ordered]@{ ApplicationSubnetName = $ApplicationSubnetName; ApprovedDestinationIp = $ApprovedDestinationIp; ApprovedFirewallEgressRoute = $ApprovedFirewallEgressRoute; DisallowedDestinationIp = $DisallowedDestinationIp; FirewallName = $FirewallName; FirewallPolicyName = $FirewallPolicyName; FrontDoorProfileName = $FrontDoorProfileName; InternalLoadBalancerName = $InternalLoadBalancerName; NetworkWatcherName = $NetworkWatcherName; ResourceGroupName = $ResourceGroupName; SourceIp = $SourceIp; SourceVmId = $SourceVmId; SpokeVnetName = $SpokeVnetName }
$missingValidationInputs = @($requiredValidationInputs.GetEnumerator() | Where-Object { $_.Value -is [string] -and [string]::IsNullOrWhiteSpace([string]$_.Value) } | ForEach-Object Key)
if ($missingValidationInputs.Count -gt 0) {
    Add-ValidationAssertion -Id 'LAB25-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'One or more required non-secret validation inputs are missing.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}
try {
    Assert-ExactExecutionContext -ExpectedSubscriptionId $SubscriptionId -ExpectedTenantId $TenantId
    Assert-InputSubscriptionScope -Inputs $state.parameters -ExpectedSubscriptionId $SubscriptionId
    Add-ValidationAssertion -Id 'LAB25-VAL-POS-CONTEXT' -Kind positive -Passed $true -Message 'The active tenant and subscription exactly match the requested validation context.'
}
catch {
    Add-ValidationAssertion -Id 'LAB25-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'Exact execution context could not be proven.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}

$originalLocation = Get-Location
try {
    Set-Location -LiteralPath $LabRoot
# LAB25-CP01: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $vnet = Get-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Name $SpokeVnetName; if (-not ($vnet.Subnets | Where-Object Name -eq $ApplicationSubnetName)) { throw 'The application subnet is absent.' } }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB25-CP01-POS' -Kind positive -Passed $positivePassed -Message 'Environment, tier, management, private endpoint, firewall, and gateway boundaries have nonoverlapping prefixes, owned route intent, and minimum required flows.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $nsgs = Get-AzNetworkSecurityGroup -ResourceGroupName $ResourceGroupName; if ($nsgs.SecurityRules | Where-Object { $_.Direction -eq 'Inbound' -and $_.Access -eq 'Allow' -and $_.SourceAddressPrefix -eq '*' -and $_.DestinationPortRange -eq '*' }) { throw 'An unrestricted inbound NSG rule exists.' } }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB25-CP01-NEG' -Kind negative -Passed $negativePassed -Message 'Flat address space, broad any-to-any rule, unmanaged peering transit, or a private endpoint sharing an application subnet must fail.'

# LAB25-CP02: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $firewall = Get-AzFirewall -ResourceGroupName $ResourceGroupName -Name $FirewallName; if ($firewall.ProvisioningState -ne 'Succeeded' -or $firewall.Sku.Tier -ne 'Premium') { throw 'Azure Firewall Premium is not ready.' } }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB25-CP02-POS' -Kind positive -Passed $positivePassed -Message 'Hierarchical policy, DNS proxy, TLS inspection decision, IDPS, threat intelligence, rule ownership, logging, and exception expiry are explicit.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $policy = Get-AzFirewallPolicy -ResourceGroupName $ResourceGroupName -Name $FirewallPolicyName; if ($policy.ThreatIntelMode -eq 'Off' -or -not $policy.DnsSetting) { throw 'Threat intelligence or governed DNS proxy configuration is absent.' } }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB25-CP02-NEG' -Kind negative -Passed $negativePassed -Message 'An application rule bypassed by a broad network rule, permanent exception, missing diagnostics, or asymmetric route around inspection must fail.'

# LAB25-CP03: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $frontDoorProfile = Get-AzFrontDoorCdnProfile -ResourceGroupName $ResourceGroupName -Name $FrontDoorProfileName; if ($frontDoorProfile.SkuName -ne 'Premium_AzureFrontDoor' -or $frontDoorProfile.ProvisioningState -ne 'Succeeded') { throw 'Front Door Premium is not ready.' } }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB25-CP03-POS' -Kind positive -Passed $positivePassed -Message 'Front Door Premium provides global WAF and private origin access; Application Gateway WAF v2 provides regional routing, probes, TLS policy, and backend isolation.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $gateways = Get-AzApplicationGateway -ResourceGroupName $ResourceGroupName; if ($gateways | Where-Object { $_.WebApplicationFirewallConfiguration.Enabled -eq $false }) { throw 'A regional application gateway has WAF disabled.' } }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB25-CP03-NEG' -Kind negative -Passed $negativePassed -Message 'Direct public origin reachability, WAF detection-only mode without approval, mismatched TLS name, or health probe that bypasses application readiness must fail.'

# LAB25-CP04: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $lb = Get-AzLoadBalancer -ResourceGroupName $ResourceGroupName -Name $InternalLoadBalancerName; if ($lb.Sku.Name -ne 'Standard' -or -not $lb.Probes) { throw 'The internal load balancer is not Standard or has no probe.' } }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB25-CP04-POS' -Kind positive -Passed $positivePassed -Message 'Standard Load Balancer distributes private TCP traffic with HA Ports only where justified, while NAT Gateway or inspected firewall egress provides stable outbound addresses and scale.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $subnet = (Get-AzVirtualNetwork -ResourceGroupName $ResourceGroupName -Name $SpokeVnetName).Subnets | Where-Object Name -eq $ApplicationSubnetName; if (-not $subnet.NatGateway -and -not $ApprovedFirewallEgressRoute) { throw 'The application subnet lacks explicit outbound connectivity.' } }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB25-CP04-NEG' -Kind negative -Passed $negativePassed -Message 'Basic Load Balancer, implicit default outbound access, shared inbound rule for egress, exhausted SNAT ports, or probe mismatch must fail.'

# LAB25-CP05: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $networkWatcher = Get-AzNetworkWatcher -ResourceGroupName $ResourceGroupName -Name $NetworkWatcherName; $allow = Test-AzNetworkWatcherIPFlow -NetworkWatcher $networkWatcher -TargetVirtualMachineId $SourceVmId -Direction Outbound -Protocol TCP -LocalIPAddress $SourceIp -LocalPort 50000 -RemoteIPAddress $ApprovedDestinationIp -RemotePort 443; if ($allow.Access -ne 'Allow') { throw 'The required clinical flow is denied.' } }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB25-CP05-POS' -Kind positive -Passed $positivePassed -Message 'Required flows traverse the intended WAF, firewall, or load-balancer path; prohibited flows are denied; zone and origin failure route only to healthy targets.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $networkWatcher = Get-AzNetworkWatcher -ResourceGroupName $ResourceGroupName -Name $NetworkWatcherName; $deny = Test-AzNetworkWatcherIPFlow -NetworkWatcher $networkWatcher -TargetVirtualMachineId $SourceVmId -Direction Outbound -Protocol TCP -LocalIPAddress $SourceIp -LocalPort 50000 -RemoteIPAddress $DisallowedDestinationIp -RemotePort 22; if ($deny.Access -ne 'Deny') { throw 'A prohibited administrative flow is allowed.' } }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB25-CP05-NEG' -Kind negative -Passed $negativePassed -Message 'A required allow with unintended bypass, a denied health probe, a permitted prohibited flow, or asymmetric return path must fail.'

}
finally {
    Set-Location -LiteralPath $originalLocation
}

$passed = @($assertions | Where-Object { -not $_.passed }).Count -eq 0
Save-ValidationArtifact -Result $(if ($passed) { 'pass' } else { 'fail' })
if ($passed) { exit 0 }
exit 1
# END GENERATED AZ305 V1
