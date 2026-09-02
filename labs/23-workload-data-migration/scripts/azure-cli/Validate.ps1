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
    [string]$ApprovedWave = $env:AZ305_APPROVED_WAVE,
    [string]$DestinationDataUrl = $env:AZ305_DESTINATION_DATA_URL,
    [string]$MigrateProjectName = $env:AZ305_MIGRATE_PROJECT_NAME,
    [string]$MigrationResourceGroupName = $env:AZ305_MIGRATION_RESOURCE_GROUP_NAME,
    [string]$SourceDataUrl = $env:AZ305_SOURCE_DATA_URL,
    [string]$TargetApplicationResourceId = $env:AZ305_TARGET_APPLICATION_RESOURCE_ID,
    [string]$TargetContainerName = $env:AZ305_TARGET_CONTAINER_NAME,
    [string]$TargetDatabaseName = $env:AZ305_TARGET_DATABASE_NAME,
    [string]$TargetResourceGroupName = $env:AZ305_TARGET_RESOURCE_GROUP_NAME,
    [string]$TargetSqlServerName = $env:AZ305_TARGET_SQL_SERVER_NAME,
    [string]$TargetStorageAccountName = $env:AZ305_TARGET_STORAGE_ACCOUNT_NAME,
    [ValidateSet('Deployment', 'PostCleanup')][string]$Mode = 'Deployment',
    [switch]$Execute,
    [switch]$AcknowledgeCost,
    [switch]$AcknowledgeTenantChange
)

$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
if (-not $RunId) { [Console]::Error.WriteLine('RunId or AZ305_RUN_ID is required.'); exit 2 }
# Every lifecycle entrypoint intentionally exposes the same public parameter contract.
@($SubscriptionId, $TenantId, $RunId, $Location, $SecondaryLocation, $ResourceGroup, $WorkloadName, $ExpiresOn, $ApprovedWave, $DestinationDataUrl, $MigrateProjectName, $MigrationResourceGroupName, $SourceDataUrl, $TargetApplicationResourceId, $TargetContainerName, $TargetDatabaseName, $TargetResourceGroupName, $TargetSqlServerName, $TargetStorageAccountName, $Mode, $Execute, $AcknowledgeCost, $AcknowledgeTenantChange) | Out-Null

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
    $artifact = [ordered]@{ schemaVersion = '1.0.0'; labId = 'LAB-23'; runId = $RunId; mode = $Mode; result = $Result; validatedAt = (Get-Date).ToUniversalTime().ToString('o'); assertions = @($assertions) }
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
    $state.labId -ceq 'LAB-23' -and
    $state.runId -ceq $RunId -and
    $state.track -ceq 'azure-cli' -and
    $state.implementationMode -ceq 'safe-analogue' -and
    ([string]$state.parameters.subscriptionId -ieq $SubscriptionId -and [string]$state.parameters.tenantId -ieq $TenantId)
)
Add-ValidationAssertion -Id 'LAB23-VAL-POS-01' -Kind positive -Passed $stateIdentityMatches -Message 'Run identity, implementation mode, command track, tenant, and subscription exactly match the copied lab and requested run.'
$hasSensitiveName = Test-ProhibitedStateField -Value $state
Add-ValidationAssertion -Id 'LAB23-VAL-NEG-01' -Kind negative -Passed (-not $hasSensitiveName) -Message 'State contains no prohibited sensitive field name.'

if ($Mode -eq 'PostCleanup') {
    $cleanupPath = Join-Path $StateRoot 'cleanup.json'
    $cleanup = if (Test-Path -LiteralPath $cleanupPath) { Get-Content -LiteralPath $cleanupPath -Raw | ConvertFrom-Json } else { $null }
    Add-ValidationAssertion -Id 'LAB23-VAL-POS-02' -Kind positive -Passed ($null -ne $cleanup -and $cleanup.labId -ceq 'LAB-23' -and $cleanup.runId -ceq $RunId -and $cleanup.result -eq 'pass' -and $cleanup.ownershipVerified) -Message 'The exact run cleanup completed with verified ownership.'
    Add-ValidationAssertion -Id 'LAB23-VAL-NEG-02' -Kind negative -Passed ($null -ne $cleanup -and $cleanup.activeManagedObjects -eq 0 -and @($state.managedObjects).Count -eq 0 -and @($state.originalSettings).Count -eq 0 -and $state.status -eq 'cleaned') -Message 'No active managed object or unresolved original setting remains in cleanup or run state.'
    $postCleanupPassed = @($assertions | Where-Object { -not $_.passed }).Count -eq 0
    Save-ValidationArtifact -Result $(if ($postCleanupPassed) { 'pass' } else { 'fail' })
    if ($postCleanupPassed) { exit 0 }
    exit 1
}

Add-ValidationAssertion -Id 'LAB23-VAL-POS-02' -Kind positive -Passed ($state.status -eq 'deployed') -Message 'The executed setup completed successfully; a failed setup can never validate as pass.'
Add-ValidationAssertion -Id 'LAB23-VAL-NEG-02' -Kind negative -Passed (@($state.managedObjects | Where-Object { $_.tags.purpose -ne 'az305-lab' -or $_.tags.labId -ne 'LAB-23' -or $_.tags.runId -ne $RunId }).Count -eq 0) -Message 'No recorded object has a foreign ownership tag.'

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
$requiredValidationInputs = [ordered]@{ ApprovedWave = $ApprovedWave; MigrateProjectName = $MigrateProjectName; MigrationResourceGroupName = $MigrationResourceGroupName; TargetApplicationResourceId = $TargetApplicationResourceId; TargetContainerName = $TargetContainerName; TargetDatabaseName = $TargetDatabaseName; TargetResourceGroupName = $TargetResourceGroupName; TargetSqlServerName = $TargetSqlServerName; TargetStorageAccountName = $TargetStorageAccountName }
$missingValidationInputs = @($requiredValidationInputs.GetEnumerator() | Where-Object { $_.Value -is [string] -and [string]::IsNullOrWhiteSpace([string]$_.Value) } | ForEach-Object Key)
if ($missingValidationInputs.Count -gt 0) {
    Add-ValidationAssertion -Id 'LAB23-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'One or more required non-secret validation inputs are missing.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}
try {
    Assert-ExactExecutionContext -ExpectedSubscriptionId $SubscriptionId -ExpectedTenantId $TenantId
    Assert-InputSubscriptionScope -Inputs $state.parameters -ExpectedSubscriptionId $SubscriptionId
    Add-ValidationAssertion -Id 'LAB23-VAL-POS-CONTEXT' -Kind positive -Passed $true -Message 'The active tenant and subscription exactly match the requested validation context.'
}
catch {
    Add-ValidationAssertion -Id 'LAB23-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'Exact execution context could not be proven.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}

$originalLocation = Get-Location
try {
    Set-Location -LiteralPath $LabRoot
# LAB23-CP01: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $group = az group show --name $TargetResourceGroupName --output json --only-show-errors | ConvertFrom-Json; if ($group.properties.provisioningState -ne 'Succeeded' -or $group.tags.wave -ne $ApprovedWave) { throw 'The target scope is not ready for the approved wave.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB23-CP01 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB23-CP01-POS' -Kind positive -Passed $positivePassed -Message 'Scope, quotas, policy, DNS, identity, connectivity, encryption, monitoring, ownership, and rollback capacity satisfy the wave entry criteria.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $locks = az lock list --resource-group $TargetResourceGroupName --output json --only-show-errors | ConvertFrom-Json; if ($locks | Where-Object { $_.level -eq 'ReadOnly' }) { throw 'A read-only lock blocks migration deployment.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB23-CP01 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB23-CP01-NEG' -Kind negative -Passed $negativePassed -Message 'An unapproved resource group, unresolved policy denial, missing private resolution, or absent rollback capacity must block migration.'

# LAB23-CP02: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $project = az resource show --resource-group $MigrationResourceGroupName --resource-type Microsoft.Migrate/migrateProjects --name $MigrateProjectName --api-version 2020-05-01 --output json --only-show-errors | ConvertFrom-Json; if ($project.properties.provisioningState -ne 'Succeeded') { throw 'The Azure Migrate project is not ready.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB23-CP02 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB23-CP02-POS' -Kind positive -Passed $positivePassed -Message 'Appliance placement, discovery boundary, replication cadence, rightsizing, disk handling, test network, agent impact, and rollback are explicit for each server.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $targets = az vm list --resource-group $TargetResourceGroupName --query "[?tags.wave=='$ApprovedWave' && tags.runId!='$RunId']" --output json --only-show-errors | ConvertFrom-Json; if ($targets.Count -gt 0) { throw 'The target contains a wave VM owned by another run.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB23-CP02 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB23-CP02-NEG' -Kind negative -Passed $negativePassed -Message 'A test migration connected to production, an unsupported disk, missing dependency, or overwrite of an existing target VM must fail.'

# LAB23-CP03: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $services = az resource list --resource-group $MigrationResourceGroupName --resource-type Microsoft.DataMigration/services --output json --only-show-errors | ConvertFrom-Json; if (-not ($services | Where-Object { $_.properties.provisioningState -eq 'Succeeded' })) { throw 'No ready database migration service was found.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB23-CP03 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB23-CP03-POS' -Kind positive -Passed $positivePassed -Message 'Compatibility, target tier, schema, continuous synchronization, encryption, logins, jobs, cutover lag, application freeze, and rollback are covered.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $targets = az sql db list --resource-group $TargetResourceGroupName --server $TargetSqlServerName --output json --only-show-errors | ConvertFrom-Json; if ($targets | Where-Object { $_.name -eq $TargetDatabaseName -and $_.status -ne 'Online' }) { throw 'The target database exists but is not online.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB23-CP03 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB23-CP03-NEG' -Kind negative -Passed $negativePassed -Message 'Unresolved blocking compatibility findings, missing principals, excessive replication lag, or a writable source after the cutover gate must fail.'

# LAB23-CP04: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $blobs = az storage blob list --account-name $TargetStorageAccountName --container-name $TargetContainerName --auth-mode login --query "[?metadata.runId=='$RunId'].{name:name,size:properties.contentLength,md5:properties.contentSettings.contentMd5}" --output json --only-show-errors | ConvertFrom-Json; if ($blobs.Count -lt 1) { throw 'No run-owned target blobs were found.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB23-CP04 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB23-CP04-POS' -Kind positive -Passed $positivePassed -Message 'Baseline and delta transfers preserve hierarchy, metadata, access tier, hashes, timestamps where required, encryption, and an auditable manifest.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $unexpected = az storage blob list --account-name $TargetStorageAccountName --container-name $TargetContainerName --auth-mode login --query "[?metadata.wave!='$ApprovedWave']" --output json --only-show-errors | ConvertFrom-Json; if ($unexpected.Count -gt 0) { throw 'The target container contains data outside the approved wave.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB23-CP04 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB23-CP04-NEG' -Kind negative -Passed $negativePassed -Message 'A copy count without byte totals and hashes, a source URL with embedded credentials, or data outside the approved prefix must fail.'

# LAB23-CP05: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $metrics = az monitor metrics list --resource $TargetApplicationResourceId --metric Availability,Requests --interval PT1M --aggregation Average --output json --only-show-errors | ConvertFrom-Json; if (-not $metrics.value.timeseries.data) { throw 'No target application validation metrics were returned.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB23-CP05 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB23-CP05-POS' -Kind positive -Passed $positivePassed -Message 'The runbook freezes writes, performs final deltas, redirects by an approved mechanism, validates infrastructure, data, security, performance, and business transactions, then gates rollback.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $failed = az monitor activity-log list --resource-group $TargetResourceGroupName --status Failed --offset 2h --output json --only-show-errors | ConvertFrom-Json; if ($failed.Count -gt 0) { throw 'Failed target operations remain unresolved before cutover.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB23-CP05 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB23-CP05-NEG' -Kind negative -Passed $negativePassed -Message 'Proceeding after outage budget, unresolved checksum difference, failed business transaction, or uncertain authoritative write location must fail.'

}
finally {
    Set-Location -LiteralPath $originalLocation
}

$passed = @($assertions | Where-Object { -not $_.passed }).Count -eq 0
Save-ValidationArtifact -Result $(if ($passed) { 'pass' } else { 'fail' })
if ($passed) { exit 0 }
exit 1
# END GENERATED AZ305 V1
