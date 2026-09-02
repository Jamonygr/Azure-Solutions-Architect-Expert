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
    [switch]$Execute,
    [switch]$AcknowledgeCost,
    [switch]$AcknowledgeTenantChange
)

$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
if (-not $RunId) { [Console]::Error.WriteLine('RunId or AZ305_RUN_ID is required.'); exit 2 }
# Every lifecycle entrypoint intentionally exposes the same public parameter contract.
@($SubscriptionId, $TenantId, $RunId, $Location, $SecondaryLocation, $ResourceGroup, $WorkloadName, $ExpiresOn, $ApplicationSubnetName, $ApprovedDestinationIp, $ApprovedFirewallEgressRoute, $DestinationIp, $DisallowedDestinationIp, $FirewallName, $FirewallPolicyName, $FrontDoorProfileName, $InternalLoadBalancerName, $NetworkWatcherName, $ResourceGroupName, $SourceIp, $SourceVmId, $SpokeVnetName, $Execute, $AcknowledgeCost, $AcknowledgeTenantChange) | Out-Null

$requiredCommands = @('pwsh')
$missing = @($requiredCommands | Where-Object { -not (Get-Command $_ -ErrorAction SilentlyContinue) })
if ($missing.Count -gt 0) {
    Write-Error "Missing local commands: $($missing -join ', ')"
    exit 1
}
$requiredCmdlets = @('Get-AzApplicationGateway', 'Get-AzFirewall', 'Get-AzFirewallPolicy', 'Get-AzFrontDoorCdnProfile', 'Get-AzLoadBalancer', 'Get-AzNetworkSecurityGroup', 'Get-AzNetworkWatcher', 'Get-AzVirtualNetwork', 'Test-AzNetworkWatcherIPFlow')
$missingCmdlets = @($requiredCmdlets | Where-Object { -not (Get-Command $_ -ErrorAction SilentlyContinue) })
if ($missingCmdlets.Count -gt 0) {
    Write-Error "Missing local cmdlets: $($missingCmdlets -join ', ')"
    exit 1
}

[pscustomobject]@{
    labId = 'LAB-25'
    track = 'azure-powershell'
    implementationMode = 'safe-analogue'
    result = 'pass'
    note = 'Local tool discovery only; no Azure or Microsoft Graph request was made.'
} | ConvertTo-Json
exit 0
# END GENERATED AZ305 V1
