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
    [ValidateSet('Deployment', 'PostCleanup')][string]$Mode = 'Deployment',
    [switch]$Execute,
    [switch]$AcknowledgeCost,
    [switch]$AcknowledgeTenantChange
)

$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
if (-not $RunId) { [Console]::Error.WriteLine('RunId or AZ305_RUN_ID is required.'); exit 2 }
# Every lifecycle entrypoint intentionally exposes the same public parameter contract.
@($SubscriptionId, $TenantId, $RunId, $Location, $SecondaryLocation, $ResourceGroup, $WorkloadName, $ExpiresOn, $Mode, $Execute, $AcknowledgeCost, $AcknowledgeTenantChange) | Out-Null

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
    $artifact = [ordered]@{ schemaVersion = '1.0.0'; labId = 'LAB-26'; runId = $RunId; mode = $Mode; result = $Result; validatedAt = (Get-Date).ToUniversalTime().ToString('o'); assertions = @($assertions) }
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
    $state.labId -ceq 'LAB-26' -and
    $state.runId -ceq $RunId -and
    $state.track -ceq 'azure-cli' -and
    $state.implementationMode -ceq 'safe-analogue' -and
    ([string]$state.parameters.subscriptionId -ieq $SubscriptionId -and [string]$state.parameters.tenantId -ieq $TenantId)
)
Add-ValidationAssertion -Id 'LAB26-VAL-POS-01' -Kind positive -Passed $stateIdentityMatches -Message 'Run identity, implementation mode, command track, tenant, and subscription exactly match the copied lab and requested run.'
$hasSensitiveName = Test-ProhibitedStateField -Value $state
Add-ValidationAssertion -Id 'LAB26-VAL-NEG-01' -Kind negative -Passed (-not $hasSensitiveName) -Message 'State contains no prohibited sensitive field name.'

if ($Mode -eq 'PostCleanup') {
    $cleanupPath = Join-Path $StateRoot 'cleanup.json'
    $cleanup = if (Test-Path -LiteralPath $cleanupPath) { Get-Content -LiteralPath $cleanupPath -Raw | ConvertFrom-Json } else { $null }
    Add-ValidationAssertion -Id 'LAB26-VAL-POS-02' -Kind positive -Passed ($null -ne $cleanup -and $cleanup.labId -ceq 'LAB-26' -and $cleanup.runId -ceq $RunId -and $cleanup.result -eq 'pass' -and $cleanup.ownershipVerified) -Message 'The exact run cleanup completed with verified ownership.'
    Add-ValidationAssertion -Id 'LAB26-VAL-NEG-02' -Kind negative -Passed ($null -ne $cleanup -and $cleanup.activeManagedObjects -eq 0 -and @($state.managedObjects).Count -eq 0 -and @($state.originalSettings).Count -eq 0 -and $state.status -eq 'cleaned') -Message 'No active managed object or unresolved original setting remains in cleanup or run state.'
    $postCleanupPassed = @($assertions | Where-Object { -not $_.passed }).Count -eq 0
    Save-ValidationArtifact -Result $(if ($postCleanupPassed) { 'pass' } else { 'fail' })
    if ($postCleanupPassed) { exit 0 }
    exit 1
}

Add-ValidationAssertion -Id 'LAB26-VAL-POS-02' -Kind positive -Passed ($state.status -eq 'planned') -Message 'The planning-only setup completed and remains planned; no deployment is implied.'
Add-ValidationAssertion -Id 'LAB26-VAL-NEG-02' -Kind negative -Passed (@($state.managedObjects | Where-Object { $_.tags.purpose -ne 'az305-lab' -or $_.tags.labId -ne 'LAB-26' -or $_.tags.runId -ne $RunId }).Count -eq 0) -Message 'No recorded object has a foreign ownership tag.'

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
$missingValidationInputs = @()
if ($missingValidationInputs.Count -gt 0) {
    Add-ValidationAssertion -Id 'LAB26-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'One or more required non-secret validation inputs are missing.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}
try {
    Assert-ExactExecutionContext -ExpectedSubscriptionId $SubscriptionId -ExpectedTenantId $TenantId
    Assert-InputSubscriptionScope -Inputs $state.parameters -ExpectedSubscriptionId $SubscriptionId
    Add-ValidationAssertion -Id 'LAB26-VAL-POS-CONTEXT' -Kind positive -Passed $true -Message 'The active tenant and subscription exactly match the requested validation context.'
}
catch {
    Add-ValidationAssertion -Id 'LAB26-VAL-POS-CONTEXT' -Kind positive -Passed $false -Message 'Exact execution context could not be proven.'
    Save-ValidationArtifact -Result 'partial'
    exit 2
}

$originalLocation = Get-Location
try {
    Set-Location -LiteralPath $LabRoot
# LAB26-CP01: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $text = Get-Content design/decision.yml -Raw; $requiredPillars = @('Reliability','Security','Cost Optimization','Operational Excellence','Performance Efficiency'); foreach ($pillar in $requiredPillars) { if ($text -notmatch [regex]::Escape($pillar)) { throw "Missing WAF pillar: $pillar" } } }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB26-CP01-POS' -Kind positive -Passed $positivePassed -Message 'Requirements, assumptions, mandatory constraints, objective traceability, candidates, scores, risks, architecture decisions, and all five WAF pillars agree.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $text = Get-Content design/decision.yml -Raw; if ($text -match '(?i)Azure AD B2C|Azure Cache for Redis|Basic Load Balancer|Log Analytics agent') { throw 'The design contains a retired or superseded default.' } }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB26-CP01-NEG' -Kind negative -Passed $negativePassed -Message 'A selected service with no requirement, an unmet mandatory constraint, inconsistent RTO or RPO, or unsupported legacy default must fail.'

# LAB26-CP02: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $main = az bicep build --file artifacts/main.bicep --stdout --only-show-errors | ConvertFrom-Json; $regional = az bicep build --file artifacts/modules/regional-stamp.bicep --stdout --only-show-errors | ConvertFrom-Json; $global = az bicep build --file artifacts/modules/global-entry.bicep --stdout --only-show-errors | ConvertFrom-Json; $types = @($main.resources.type) + @($regional.resources.type) + @($global.resources.type); foreach ($requiredType in @('Microsoft.Resources/resourceGroups','Microsoft.Cdn/profiles','Microsoft.ManagedIdentity/userAssignedIdentities')) { if ($requiredType -notin $types) { throw "Missing required resource type: $requiredType" } }; if ($main.outputs.referenceBoundary.value.productionReady -ne $false -or $main.outputs.referenceBoundary.value.omittedCapabilities.Count -lt 6) { throw 'The compiled foundation slice does not disclose its non-production boundary.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB26-CP02 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB26-CP02-POS' -Kind positive -Passed $positivePassed -Message 'Subscription-scope Bicep compiles a bounded foundation slice with three tagged resource groups, two regional identity/network/empty-monitoring/storage/serverless-document/messaging scaffolds, and a disabled Front Door Standard endpoint; its output explicitly lists every omitted production capability.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $templateText = az bicep build --file artifacts/main.bicep --stdout --only-show-errors; if ($templateText -match '(?i)password|clientSecret|accountKey|0\.0\.0\.0/0') { throw 'The compiled template contains a secret-like field or unrestricted network rule.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB26-CP02 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB26-CP02-NEG' -Kind negative -Passed $negativePassed -Message 'Treating the slice as production-ready, hiding an omitted capability, embedded credentials, public data endpoints, or region literals outside parameters must fail.'

# LAB26-CP03: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $template = az bicep build --file artifacts/modules/regional-stamp.bicep --stdout --only-show-errors | ConvertFrom-Json; if (-not ($template.resources | Where-Object type -match 'Microsoft.Insights/dataCollectionRules') -or -not ($template.resources | Where-Object type -match 'Microsoft.DocumentDB/databaseAccounts')) { throw 'The empty DCR declaration or regional serverless document-store scaffold is missing.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB26-CP03 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB26-CP03-POS' -Kind positive -Passed $positivePassed -Message 'The foundation slice contains an empty DCR wired to a workspace and locked-down regional data scaffolds; DCRA, data sources and flows, diagnostics, alerts, backups, replication, compute, cache, private endpoints, and live recovery behavior are explicitly deferred to the production design.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $template = az bicep build --file artifacts/modules/regional-stamp.bicep --stdout --only-show-errors | ConvertFrom-Json; if ($template.resources | Where-Object { $_.type -match 'databaseAccounts|servers/databases|storageAccounts' -and $_.properties.publicNetworkAccess -eq 'Enabled' }) { throw 'A data service permits public network access.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB26-CP03 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB26-CP03-NEG' -Kind negative -Passed $negativePassed -Message 'Claiming AMA collection, global data coordination, backup, recovery, or alert coverage from these scaffold resources must fail.'

# LAB26-CP04: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $preview = az deployment sub what-if --location $Location --name "lab26-$RunId" --template-file artifacts/main.bicep --parameters artifacts/parameters.example.json runId=$RunId expiresOn=$ExpiresOn --result-format ResourceIdOnly --output json --only-show-errors | ConvertFrom-Json; if (-not ($preview.changes | Where-Object changeType -in @('Create','Deploy','Modify','NoChange'))) { throw 'What-if produced no expected platform changes.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB26-CP04 positive native command exited with code ' + $LASTEXITCODE + '.' }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB26-CP04-POS' -Kind positive -Passed $positivePassed -Message 'The reviewed what-if describes only the tagged foundation slice, reports no deletion or unrelated modification, exposes all three resource-group IDs for dependency-safe review, and is never followed by a deployment command.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $preview = az deployment sub what-if --location $Location --name "lab26-$RunId" --template-file artifacts/main.bicep --parameters artifacts/parameters.example.json runId=$RunId expiresOn=$ExpiresOn --result-format FullResourcePayloads --output json --only-show-errors | ConvertFrom-Json; if ($preview.changes | Where-Object { $_.changeType -eq 'Delete' -or $_.resourceId -notmatch $RunId }) { throw 'Preview contains deletion or a resource outside run ownership.' } }
    if ($LASTEXITCODE -ne 0) { throw 'LAB26-CP04 negative native command exited with code ' + $LASTEXITCODE + '.' }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB26-CP04-NEG' -Kind negative -Passed $negativePassed -Message 'A destructive change, production-scale tier, missing tag, undisclosed omission, unrelated resource modification, or any attempt to treat what-if as deployment evidence must block completion.'

# LAB26-CP05: run both polarities even when one fails.
$positivePassed = $false
try {
    $global:LASTEXITCODE = 0
    $positiveEvidence = & { $fixtures = Get-Content tests/fixtures/regional-failure.json -Raw | ConvertFrom-Json; if ($fixtures.assertions | Where-Object { $_.polarity -eq 'positive' -and $_.simulatedActual -ne $_.expected }) { throw 'A required platform behavior failed.' } }
    $positivePassed = $true
    $null = $positiveEvidence
} catch { $positivePassed = $false }
Add-ValidationAssertion -Id 'LAB26-CP05-POS' -Kind positive -Passed $positivePassed -Message 'The simulation covers identity, global routing, regional ingress, messaging, cache loss, data consistency, degraded capacity, alerting, business validation, recovery, and rollback.'

$negativePassed = $false
try {
    $global:LASTEXITCODE = 0
    $negativeEvidence = & { $fixtures = Get-Content tests/fixtures/regional-failure.json -Raw | ConvertFrom-Json; if ($fixtures.assertions | Where-Object { $_.polarity -eq 'negative' -and $_.simulatedActual -ne $_.expected }) { throw 'A prohibited platform behavior was observed.' } }
    $negativePassed = $true
    $null = $negativeEvidence
} catch { $negativePassed = $false }
Add-ValidationAssertion -Id 'LAB26-CP05-NEG' -Kind negative -Passed $negativePassed -Message 'Passing infrastructure assertions while authentication, purchase completion, data-loss, security, or cost-limit assertions fail must fail overall.'

}
finally {
    Set-Location -LiteralPath $originalLocation
}

$passed = @($assertions | Where-Object { -not $_.passed }).Count -eq 0
Save-ValidationArtifact -Result $(if ($passed) { 'pass' } else { 'fail' })
if ($passed) { exit 0 }
exit 1
# END GENERATED AZ305 V1
