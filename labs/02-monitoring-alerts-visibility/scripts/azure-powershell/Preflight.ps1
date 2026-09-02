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
    [string]$ActionGroupName = $env:AZ305_ACTION_GROUP_NAME,
    [string]$ActionGroupResourceId = $env:AZ305_ACTION_GROUP_RESOURCE_ID,
    [string]$DeprecatedMetricName = $env:AZ305_DEPRECATED_METRIC_NAME,
    [string]$HealthAlertName = $env:AZ305_HEALTH_ALERT_NAME,
    [string]$RequiredMetricName = $env:AZ305_REQUIRED_METRIC_NAME,
    [string]$ScheduledQueryRuleName = $env:AZ305_SCHEDULED_QUERY_RULE_NAME,
    [string]$TargetResourceId = $env:AZ305_TARGET_RESOURCE_ID,
    [string]$WorkbookDisplayName = $env:AZ305_WORKBOOK_DISPLAY_NAME,
    [string]$WorkbookJson = $env:AZ305_WORKBOOK_JSON,
    [string]$WorkbookResourceName = $env:AZ305_WORKBOOK_RESOURCE_NAME,
    [switch]$Execute,
    [switch]$AcknowledgeCost,
    [switch]$AcknowledgeTenantChange
)

$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
if (-not $RunId) { [Console]::Error.WriteLine('RunId or AZ305_RUN_ID is required.'); exit 2 }
# Every lifecycle entrypoint intentionally exposes the same public parameter contract.
@($SubscriptionId, $TenantId, $RunId, $Location, $SecondaryLocation, $ResourceGroup, $WorkloadName, $ExpiresOn, $ActionGroupName, $ActionGroupResourceId, $DeprecatedMetricName, $HealthAlertName, $RequiredMetricName, $ScheduledQueryRuleName, $TargetResourceId, $WorkbookDisplayName, $WorkbookJson, $WorkbookResourceName, $Execute, $AcknowledgeCost, $AcknowledgeTenantChange) | Out-Null

$requiredCommands = @('pwsh')
$missing = @($requiredCommands | Where-Object { -not (Get-Command $_ -ErrorAction SilentlyContinue) })
if ($missing.Count -gt 0) {
    Write-Error "Missing local commands: $($missing -join ', ')"
    exit 1
}
$requiredCmdlets = @('Get-AzActionGroup', 'Get-AzActivityLogAlert', 'Get-AzApplicationInsightsWorkbook', 'Get-AzMetricDefinition', 'Get-AzScheduledQueryRule', 'New-AzActivityLogAlert', 'New-AzActivityLogAlertActionGroupObject', 'New-AzActivityLogAlertAlertRuleAnyOfOrLeafConditionObject', 'New-AzApplicationInsightsWorkbook')
$missingCmdlets = @($requiredCmdlets | Where-Object { -not (Get-Command $_ -ErrorAction SilentlyContinue) })
if ($missingCmdlets.Count -gt 0) {
    Write-Error "Missing local cmdlets: $($missingCmdlets -join ', ')"
    exit 1
}

[pscustomobject]@{
    labId = 'LAB-02'
    track = 'azure-powershell'
    implementationMode = 'reference-deployable'
    result = 'pass'
    note = 'Local tool discovery only; no Azure or Microsoft Graph request was made.'
} | ConvertTo-Json
exit 0
# END GENERATED AZ305 V1
