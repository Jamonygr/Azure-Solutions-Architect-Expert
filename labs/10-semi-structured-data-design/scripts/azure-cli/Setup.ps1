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
    [string]$ContainerName = $env:AZ305_CONTAINER_NAME,
    [string]$CosmosAccountName = $env:AZ305_COSMOS_ACCOUNT_NAME,
    [string]$CosmosAccountResourceId = $env:AZ305_COSMOS_ACCOUNT_RESOURCE_ID,
    [string]$CosmosDatabaseName = $env:AZ305_COSMOS_DATABASE_NAME,
    [string]$PrivateConnectionName = $env:AZ305_PRIVATE_CONNECTION_NAME,
    [string]$PrivateEndpointName = $env:AZ305_PRIVATE_ENDPOINT_NAME,
    [string]$SubnetId = $env:AZ305_SUBNET_ID,
    [switch]$Execute,
    [switch]$AcknowledgeCost,
    [switch]$AcknowledgeTenantChange
)

$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true
if (-not $RunId) { [Console]::Error.WriteLine('RunId or AZ305_RUN_ID is required.'); exit 2 }
# Every lifecycle entrypoint intentionally exposes the same public parameter contract.
@($SubscriptionId, $TenantId, $RunId, $Location, $SecondaryLocation, $ResourceGroup, $WorkloadName, $ExpiresOn, $ContainerName, $CosmosAccountName, $CosmosAccountResourceId, $CosmosDatabaseName, $PrivateConnectionName, $PrivateEndpointName, $SubnetId, $Execute, $AcknowledgeCost, $AcknowledgeTenantChange) | Out-Null

$LabRoot = Split-Path (Split-Path $PSScriptRoot -Parent) -Parent
$StateRoot = Join-Path $LabRoot ".state/$RunId"
$StatePath = Join-Path $StateRoot 'run.json'

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

function Save-RunState {
    [CmdletBinding()]
    param([Parameter(Mandatory)]$State)
    $temporaryPath = "$StatePath.tmp"
    $State | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $temporaryPath -Encoding utf8NoBOM
    Move-Item -LiteralPath $temporaryPath -Destination $StatePath -Force
}

function Assert-SafeStateValue {
    [CmdletBinding()]
    param($Value)
    $serialized = $Value | ConvertTo-Json -Depth 12 -Compress
    if ($serialized -match '(?i)"(?:token|password|secret|certificate|connectionString|sas|clientSecret|accessToken|refreshToken|accountKey|privateKey)"\s*:') {
        throw 'A prohibited sensitive field name was returned; state capture is refused.'
    }
}

function Convert-CheckpointOutput {
    [CmdletBinding()]
    param($Value)
    if ($Value -is [string]) { $raw = [string]$Value }
    elseif ($Value -is [System.Collections.IEnumerable] -and @($Value | Where-Object { $_ -isnot [string] }).Count -eq 0) { $raw = @($Value) -join "`n" }
    else { return $Value }
    if ([string]::IsNullOrWhiteSpace($raw)) { return $null }
    try { return ($raw | ConvertFrom-Json -Depth 100) } catch { return $Value }
}

function Get-ReturnedResourceId {
    [CmdletBinding()]
    param($Value)
    $seen = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    $results = [System.Collections.Generic.List[string]]::new()
    function Add-ArmId {
        param($Candidate)
        if ($Candidate -is [string] -and $Candidate -match '^/subscriptions/[0-9a-f-]+/(?:resourceGroups/[^/]+(?:/providers/.+)?|providers/.+)$' -and $Candidate -notmatch '/providers/Microsoft\.Resources/deployments/') {
            if ($seen.Add($Candidate)) { $results.Add($Candidate) }
        }
    }
    function Find-DeploymentOutputId {
        param($Item, [int]$Depth)
        if ($null -eq $Item -or $Depth -gt 12) { return }
        if ($Item -is [string]) { Add-ArmId -Candidate $Item; return }
        if ($Item -is [System.Collections.IDictionary]) { foreach ($key in $Item.Keys) { Find-DeploymentOutputId -Item $Item[$key] -Depth ($Depth + 1) }; return }
        if ($Item -is [System.Collections.IEnumerable]) { foreach ($entry in $Item) { Find-DeploymentOutputId -Item $entry -Depth ($Depth + 1) }; return }
        foreach ($property in @($Item.PSObject.Properties | Where-Object { $_.MemberType -in @('NoteProperty', 'Property') })) { Find-DeploymentOutputId -Item $property.Value -Depth ($Depth + 1) }
    }
    foreach ($rootItem in @($Value)) {
        if ($rootItem -is [System.Collections.IDictionary]) {
            foreach ($name in @('id', 'resourceId')) { if ($rootItem.Contains($name)) { Add-ArmId -Candidate $rootItem[$name] } }
            if ($rootItem.Contains('properties') -and $rootItem.properties -and $rootItem.properties.outputs) { Find-DeploymentOutputId -Item $rootItem.properties.outputs -Depth 0 }
            continue
        }
        foreach ($name in @('Id', 'ResourceId')) {
            $property = $rootItem.PSObject.Properties[$name]
            if ($property) { Add-ArmId -Candidate $property.Value }
        }
        if ($rootItem.PSObject.Properties['Properties'] -and $rootItem.Properties -and $rootItem.Properties.outputs) {
            Find-DeploymentOutputId -Item $rootItem.Properties.outputs -Depth 0
        }
    }
    return @($results)
}

function Get-PlannedDeploymentResourceId {
    [CmdletBinding()]
    param($Value)
    $seen = [System.Collections.Generic.HashSet[string]]::new([System.StringComparer]::OrdinalIgnoreCase)
    $results = [System.Collections.Generic.List[string]]::new()
    foreach ($change in @($Value.changes)) {
        $candidate = [string]$change.resourceId
        if ($candidate -match '^/subscriptions/[0-9a-f-]+/(?:resourceGroups/[^/]+(?:/providers/.+)?|providers/.+)$' -and $candidate -notmatch '/providers/Microsoft\.Resources/deployments/' -and $seen.Add($candidate)) {
            $results.Add($candidate)
        }
    }
    return @($results)
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
        if ($entry.Value -is [string] -and [string]$entry.Value -match '^/subscriptions/([^/]+)/') {
            if ($Matches[1] -ine $ExpectedSubscriptionId) { throw "Input $($entry.Key) belongs to a different subscription." }
        }
    }
}

function Assert-ManagedMutation {
    [CmdletBinding()]
    param($State, [string]$CheckpointId, [bool]$CarriesOwnership, [object[]]$TargetResourceIds)
    if ($CarriesOwnership) { return }
    $targets = @($TargetResourceIds | Where-Object { $_ -is [string] -and $_ -match '^/subscriptions/' })
    if ($targets.Count -eq 0) { throw "$CheckpointId refuses an untagged mutation because no exact ARM target ID was supplied." }
    $knownIds = @($State.managedObjects | ForEach-Object { [string]$_.id })
    if ($knownIds.Count -eq 0) { throw "$CheckpointId refuses to modify a pre-existing object because no run-owned parent has been recorded." }
    foreach ($target in $targets) {
        $related = @($knownIds | Where-Object { $target -ieq $_ -or $target.StartsWith("$_/", [System.StringComparison]::OrdinalIgnoreCase) -or $_.StartsWith("$target/", [System.StringComparison]::OrdinalIgnoreCase) }).Count -gt 0
        if (-not $related) { throw "$CheckpointId refuses a mutation outside the exact run-owned resource boundary." }
    }
}

$executionInputs = [ordered]@{ subscriptionId = $SubscriptionId; tenantId = $TenantId; location = $Location; secondaryLocation = $SecondaryLocation; resourceGroup = $ResourceGroup; workloadName = $WorkloadName; expiresOn = $ExpiresOn; ContainerName = $ContainerName; CosmosAccountName = $CosmosAccountName; CosmosAccountResourceId = $CosmosAccountResourceId; CosmosDatabaseName = $CosmosDatabaseName; PrivateConnectionName = $PrivateConnectionName; PrivateEndpointName = $PrivateEndpointName; SubnetId = $SubnetId }

if (-not $Execute) {
    Write-Output '[preview] No cloud command was called and no state was created.'
    Write-Output '[preview] Re-run with -Execute only in an authorized disposable environment.'
    exit 0
}
# This setup is compatible with the lab implementation mode.
if (-not $AcknowledgeCost) { [Console]::Error.WriteLine('Cost acknowledgement is required.'); exit 2 }
# This lab does not perform a tenant-scoped change by default.
$requiredLabInputs = [ordered]@{ ContainerName = $ContainerName; CosmosAccountName = $CosmosAccountName; CosmosAccountResourceId = $CosmosAccountResourceId; CosmosDatabaseName = $CosmosDatabaseName; PrivateConnectionName = $PrivateConnectionName; PrivateEndpointName = $PrivateEndpointName; SubnetId = $SubnetId }
$missingLabInputs = @($requiredLabInputs.GetEnumerator() | Where-Object { $_.Value -is [string] -and [string]::IsNullOrWhiteSpace([string]$_.Value) } | ForEach-Object Key)
if ($missingLabInputs.Count -gt 0) { [Console]::Error.WriteLine("Execution is gated; supply: $($missingLabInputs -join ', ')."); exit 2 }

try {
    Assert-ExactExecutionContext -ExpectedSubscriptionId $SubscriptionId -ExpectedTenantId $TenantId
    Assert-InputSubscriptionScope -Inputs $executionInputs -ExpectedSubscriptionId $SubscriptionId
    Assert-SafeStateValue -Value $executionInputs
}
catch {
    [Console]::Error.WriteLine("Execution is gated by context or input validation: $($_.Exception.Message)")
    exit 2
}

# Recovery state is persisted before the first possible mutation below.
if (Test-Path -LiteralPath $StatePath) {
    [Console]::Error.WriteLine('Run state already exists. Choose a new RunId or complete the recorded cleanup; existing recovery state will not be overwritten.')
    exit 2
}
New-Item -ItemType Directory -Path $StateRoot -Force | Out-Null
$state = [ordered]@{
    schemaVersion = '1.0.0'; labId = 'LAB-10'; runId = $RunId; track = 'azure-cli'
    implementationMode = 'reference-deployable'; status = 'initialized'
    createdAt = (Get-Date).ToUniversalTime().ToString('o'); execute = $true
    parameters = $executionInputs
    managedObjects = @(); originalSettings = @()
}
Save-RunState -State $state
$state.status = 'deploying'
Save-RunState -State $state

$originalLocation = Get-Location
try {
    Set-Location -LiteralPath $LabRoot
    # 10-CP01: Choose API and consistency deliberately
    Assert-ManagedMutation -State $state -CheckpointId 'LAB10-CP01' -CarriesOwnership:$true -TargetResourceIds @()
    $stepResult = & { az cosmosdb create --name $CosmosAccountName --resource-group $ResourceGroup --locations regionName=$Location failoverPriority=0 isZoneRedundant=false --default-consistency-level Session --enable-free-tier false --tags purpose=az305-lab labId=LAB-10 runId=$RunId expiresOn=$ExpiresOn }
    if ($LASTEXITCODE -ne 0) { throw 'LAB10-CP01 native command exited with code ' + $LASTEXITCODE + '.' }
    $candidate = Convert-CheckpointOutput -Value $stepResult
    $returnedIds = @(Get-ReturnedResourceId -Value $candidate)
    if ($returnedIds.Count -eq 0) { throw 'LAB10-CP01 created an owned resource but returned no recoverable ARM resource ID.' }
    foreach ($returnedId in $returnedIds) {
        if ($returnedId -notmatch '^/subscriptions/([^/]+)/' -or $Matches[1] -ine $SubscriptionId) { throw 'A returned recovery ID belongs to a different subscription.' }
        if (@($state.managedObjects | Where-Object { $_.id -ieq $returnedId }).Count -eq 0) {
            $state.managedObjects += [pscustomobject]@{
                id = $returnedId
                type = 'azure-resource'
                tags = [ordered]@{ purpose = 'az305-lab'; labId = 'LAB-10'; runId = $RunId; expiresOn = $ExpiresOn }
            }
            Save-RunState -State $state
        }
    }
    $null = $stepResult

    # 10-CP02: Design a high-cardinality partition key
    Assert-ManagedMutation -State $state -CheckpointId 'LAB10-CP02' -CarriesOwnership:$false -TargetResourceIds @($CosmosAccountResourceId)
    $stepResult = & { $ownedCosmosId = az cosmosdb show --name $CosmosAccountName --resource-group $ResourceGroup --query id -o tsv --only-show-errors; if ($ownedCosmosId -ine $CosmosAccountResourceId) { throw 'The supplied Cosmos DB ID is not the exact run-owned account.' }; az cosmosdb sql database create --account-name $CosmosAccountName --resource-group $ResourceGroup --name $CosmosDatabaseName --only-show-errors | Out-Null; az cosmosdb sql container create --account-name $CosmosAccountName --resource-group $ResourceGroup --database-name $CosmosDatabaseName --name $ContainerName --partition-key-path /tenantId --max-throughput 4000 --only-show-errors }
    if ($LASTEXITCODE -ne 0) { throw 'LAB10-CP02 native command exited with code ' + $LASTEXITCODE + '.' }
    $null = $stepResult

    # 10-CP03: Minimize indexing write amplification
    Assert-ManagedMutation -State $state -CheckpointId 'LAB10-CP03' -CarriesOwnership:$false -TargetResourceIds @($CosmosAccountResourceId)
    # Capture the original non-secret projection before changing an exact run-owned object.
    $originalProjection = & { az cosmosdb sql container show --account-name $CosmosAccountName --resource-group $ResourceGroup --database-name $CosmosDatabaseName --name $ContainerName --query "resource.indexingPolicy.{mode:indexingMode,included:includedPaths,excluded:excludedPaths}" -o json }
    if ($LASTEXITCODE -ne 0) { throw 'LAB10-CP03 original-state native command exited with code ' + $LASTEXITCODE + '.' }
    Assert-SafeStateValue -Value $originalProjection
    foreach ($originalTargetId in @($CosmosAccountResourceId)) {
        $state.originalSettings += [pscustomobject]@{ id = $originalTargetId; setting = 'LAB10-CP03: Minimize indexing write amplification'; value = $originalProjection }
    }
    Save-RunState -State $state
    $stepResult = & { $ownedCosmosId = az cosmosdb show --name $CosmosAccountName --resource-group $ResourceGroup --query id -o tsv --only-show-errors; if ($ownedCosmosId -ine $CosmosAccountResourceId) { throw 'The supplied Cosmos DB ID is not the exact run-owned account.' }; az cosmosdb sql container update --account-name $CosmosAccountName --resource-group $ResourceGroup --database-name $CosmosDatabaseName --name $ContainerName --idx @artifacts/indexing-policy.json --only-show-errors }
    if ($LASTEXITCODE -ne 0) { throw 'LAB10-CP03 native command exited with code ' + $LASTEXITCODE + '.' }
    $null = $stepResult

    # 10-CP04: Bound autoscale throughput
    Assert-ManagedMutation -State $state -CheckpointId 'LAB10-CP04' -CarriesOwnership:$false -TargetResourceIds @($CosmosAccountResourceId)
    # Capture the original non-secret projection before changing an exact run-owned object.
    $originalProjection = & { az cosmosdb sql container throughput show --account-name $CosmosAccountName --resource-group $ResourceGroup --database-name $CosmosDatabaseName --name $ContainerName --query "resource.autoscaleSettings.maxThroughput" -o tsv }
    if ($LASTEXITCODE -ne 0) { throw 'LAB10-CP04 original-state native command exited with code ' + $LASTEXITCODE + '.' }
    Assert-SafeStateValue -Value $originalProjection
    foreach ($originalTargetId in @($CosmosAccountResourceId)) {
        $state.originalSettings += [pscustomobject]@{ id = $originalTargetId; setting = 'LAB10-CP04: Bound autoscale throughput'; value = $originalProjection }
    }
    Save-RunState -State $state
    $stepResult = & { $ownedCosmosId = az cosmosdb show --name $CosmosAccountName --resource-group $ResourceGroup --query id -o tsv --only-show-errors; if ($ownedCosmosId -ine $CosmosAccountResourceId) { throw 'The supplied Cosmos DB ID is not the exact run-owned account.' }; az cosmosdb sql container throughput migrate --account-name $CosmosAccountName --resource-group $ResourceGroup --database-name $CosmosDatabaseName --name $ContainerName --throughput-type autoscale --only-show-errors }
    if ($LASTEXITCODE -ne 0) { throw 'LAB10-CP04 native command exited with code ' + $LASTEXITCODE + '.' }
    $null = $stepResult

    # 10-CP05: Restrict the account network boundary
    Assert-ManagedMutation -State $state -CheckpointId 'LAB10-CP05' -CarriesOwnership:$true -TargetResourceIds @($CosmosAccountResourceId)
    $stepResult = & { az network private-endpoint create --name $PrivateEndpointName --resource-group $ResourceGroup --location $Location --subnet $SubnetId --private-connection-resource-id $CosmosAccountResourceId --group-id Sql --connection-name $PrivateConnectionName --tags purpose=az305-lab labId=LAB-10 runId=$RunId expiresOn=$ExpiresOn }
    if ($LASTEXITCODE -ne 0) { throw 'LAB10-CP05 native command exited with code ' + $LASTEXITCODE + '.' }
    $candidate = Convert-CheckpointOutput -Value $stepResult
    $returnedIds = @(Get-ReturnedResourceId -Value $candidate)
    if ($returnedIds.Count -eq 0) { throw 'LAB10-CP05 created an owned resource but returned no recoverable ARM resource ID.' }
    foreach ($returnedId in $returnedIds) {
        if ($returnedId -notmatch '^/subscriptions/([^/]+)/' -or $Matches[1] -ine $SubscriptionId) { throw 'A returned recovery ID belongs to a different subscription.' }
        if (@($state.managedObjects | Where-Object { $_.id -ieq $returnedId }).Count -eq 0) {
            $state.managedObjects += [pscustomobject]@{
                id = $returnedId
                type = 'azure-resource'
                tags = [ordered]@{ purpose = 'az305-lab'; labId = 'LAB-10'; runId = $RunId; expiresOn = $ExpiresOn }
            }
            Save-RunState -State $state
        }
    }
    $null = $stepResult

    $state.status = 'deployed'
    Save-RunState -State $state
} catch {
    $state.status = 'failed'
    Save-RunState -State $state
    Write-Error $_
    exit 1
} finally {
    Set-Location -LiteralPath $originalLocation
}
exit 0
# END GENERATED AZ305 V1
