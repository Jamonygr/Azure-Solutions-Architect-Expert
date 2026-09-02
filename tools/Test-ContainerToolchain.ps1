#requires -Version 7.4
[CmdletBinding()]
param(
    [string]$LockFile = (Join-Path $PSScriptRoot 'container-lock.json'),
    [string]$QualityLockFile = (Join-Path $PSScriptRoot 'quality-tools-lock.json'),
    [string]$AzureCliExtensionLockFile = (Join-Path $PSScriptRoot 'azure-cli-extensions.lock.json'),
    [switch]$Strict
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$PSNativeCommandUseErrorActionPreference = $true

if (-not (Test-Path -LiteralPath $LockFile -PathType Leaf)) {
    throw "Container lock file not found: $LockFile"
}
if (-not (Test-Path -LiteralPath $QualityLockFile -PathType Leaf)) {
    throw "Quality-tool lock file not found: $QualityLockFile"
}
if (-not (Test-Path -LiteralPath $AzureCliExtensionLockFile -PathType Leaf)) {
    throw "Azure CLI extension lock file not found: $AzureCliExtensionLockFile"
}

$lock = Get-Content -Raw -LiteralPath $LockFile | ConvertFrom-Json -Depth 20
$qualityLock = Get-Content -Raw -LiteralPath $QualityLockFile | ConvertFrom-Json -Depth 20
$azureCliExtensionLock = Get-Content -Raw -LiteralPath $AzureCliExtensionLockFile | ConvertFrom-Json -Depth 20
$failures = [System.Collections.Generic.List[string]]::new()

function Add-CheckResult {
    param(
        [Parameter(Mandatory)][string]$Name,
        [Parameter(Mandatory)][string]$Expected,
        [Parameter(Mandatory)][scriptblock]$Probe
    )

    try {
        $actual = (& $Probe | Out-String).Trim()
        $passed = $actual -eq $Expected
        if (-not $passed) {
            $failures.Add("$Name expected '$Expected' but reported '$actual'.")
        }
        [pscustomobject]@{ Check = $Name; Expected = $Expected; Actual = $actual; Passed = $passed }
    } catch {
        $failures.Add("$Name could not be inspected: $($_.Exception.Message)")
        [pscustomobject]@{ Check = $Name; Expected = $Expected; Actual = '<unavailable>'; Passed = $false }
    }
}

function Test-AzCommandGroup {
    param([Parameter(Mandatory)][string]$CommandGroup)

    $tokens = @($CommandGroup.Split(' ', [System.StringSplitOptions]::RemoveEmptyEntries))
    if ($tokens.Count -lt 2 -or $tokens[0] -ne 'az') {
        throw "Azure CLI command group must start with 'az ': $CommandGroup"
    }

    $arguments = @($tokens[1..($tokens.Count - 1)]) + '--help'
    & az @arguments *> $null
    if ($LASTEXITCODE -ne 0) {
        return "exit-$LASTEXITCODE"
    }
    return 'available'
}

$results = @(
    Add-CheckResult -Name 'PowerShell' -Expected $lock.artifacts.powershell.version -Probe { $PSVersionTable.PSVersion.ToString() }
    Add-CheckResult -Name 'Azure CLI' -Expected $lock.artifacts.azureCli.version -Probe { (az version --output json | ConvertFrom-Json).'azure-cli' }
    Add-CheckResult -Name 'Bicep' -Expected $lock.artifacts.bicep.version -Probe { if ((bicep --version) -match '(?<version>\d+\.\d+\.\d+)') { $Matches.version } }
    Add-CheckResult -Name 'AzCopy' -Expected $lock.artifacts.azcopy.version -Probe { if ((azcopy --version) -match '(?<version>\d+\.\d+\.\d+)') { $Matches.version } }
    Add-CheckResult -Name 'Python' -Expected $lock.artifacts.python.version -Probe { if ((python --version) -match '(?<version>\d+\.\d+\.\d+)') { $Matches.version } }
    Add-CheckResult -Name 'Node.js' -Expected $lock.artifacts.node.version -Probe { (node --version).TrimStart('v') }
    Add-CheckResult -Name 'markdownlint-cli2' -Expected $qualityLock.qualityTools.markdownlintCli2.version -Probe {
        $match = [regex]::Match((markdownlint-cli2 --version | Out-String), '\d+\.\d+\.\d+')
        if ($match.Success) { $match.Value }
    }
    Add-CheckResult -Name 'cspell' -Expected $qualityLock.qualityTools.cspell.version -Probe { (cspell --version).Trim() }
    Add-CheckResult -Name 'actionlint' -Expected $qualityLock.qualityTools.actionlint.version -Probe {
        $match = [regex]::Match((actionlint -version | Out-String), '\d+\.\d+\.\d+')
        if ($match.Success) { $match.Value }
    }
    Add-CheckResult -Name 'gitleaks' -Expected $qualityLock.qualityTools.gitleaks.version -Probe { if ((gitleaks version) -match '(?<version>\d+\.\d+\.\d+)') { $Matches.version } }
)

foreach ($extension in $azureCliExtensionLock.extensions) {
    $extensionName = $extension.name
    $expectedVersion = $extension.version
    $results += Add-CheckResult -Name "Azure CLI extension $extensionName" -Expected $expectedVersion -Probe {
        $installed = az extension show --name $extensionName --output json | ConvertFrom-Json
        $previewProperty = $installed.metadata.PSObject.Properties['azext.isPreview']
        if ($previewProperty -and $previewProperty.Value -eq $true) {
            throw "Azure CLI extension $extensionName is marked preview."
        }
        $installed.version
    }
    foreach ($commandGroup in $extension.commandGroups) {
        $results += Add-CheckResult -Name "Azure CLI command group $commandGroup" -Expected 'available' -Probe {
            Test-AzCommandGroup -CommandGroup $commandGroup
        }
    }
}

foreach ($commandGroup in $azureCliExtensionLock.coreCommandGroups) {
    $results += Add-CheckResult -Name "Azure CLI core command group $commandGroup" -Expected 'available' -Probe {
        Test-AzCommandGroup -CommandGroup $commandGroup
    }
}

foreach ($property in $lock.powershellModules.PSObject.Properties) {
    $moduleName = $property.Name
    $expectedVersion = $property.Value.version
    $results += Add-CheckResult -Name "PowerShell module $moduleName" -Expected $expectedVersion -Probe {
        Import-Module -Name $moduleName -RequiredVersion $expectedVersion -Force -ErrorAction Stop
        $module = Get-Module -Name $moduleName |
            Sort-Object Version -Descending |
            Select-Object -First 1
        if ($module) { $module.Version.ToString() }
    }
}

$betaModules = @(Get-Module -ListAvailable -Name 'Microsoft.Graph.Beta*')
$betaPassed = $betaModules.Count -eq 0
if (-not $betaPassed) {
    $failures.Add("Graph Beta modules are installed: $($betaModules.Name -join ', ').")
}
$results += [pscustomobject]@{
    Check = 'No Microsoft.Graph.Beta modules'
    Expected = '0'
    Actual = $betaModules.Count.ToString()
    Passed = $betaPassed
}

$results | Format-Table -AutoSize

if ($failures.Count -gt 0) {
    $failures | ForEach-Object { Write-Error $_ }
    if ($Strict) { exit 1 }
}

exit 0
