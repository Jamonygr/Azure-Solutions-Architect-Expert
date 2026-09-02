[CmdletBinding()]
param(
    [switch]$AllowMissingTools
)

Set-StrictMode -Version Latest
$ErrorActionPreference = 'Stop'
$ProgressPreference = 'SilentlyContinue'

$RepositoryRoot = [System.IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..'))
$TemporaryBase = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath())
$TemporaryRoot = [System.IO.Path]::GetFullPath((Join-Path $TemporaryBase ("az305-release-{0}" -f [guid]::NewGuid().ToString('N'))))
$Failures = [System.Collections.Generic.List[string]]::new()
$Passed = 0
$BypassMissingTools = [bool]$AllowMissingTools

function Add-GateFailure {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)][string]$Name,
        [Parameter(Mandatory)][string]$Message
    )
    $script:Failures.Add("$Name`: $Message")
    Write-Information "[FAIL] $Name - $Message" -InformationAction Continue
}

function Invoke-NativeChecked {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)][string]$FilePath,
        [string[]]$ArgumentList = @()
    )
    & $FilePath @ArgumentList
    if ($LASTEXITCODE -ne 0) {
        throw "process exited with code $LASTEXITCODE"
    }
}

function Invoke-GateStep {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)][string]$Name,
        [Parameter(Mandatory)][scriptblock]$Action
    )
    Write-Information "`n== $Name ==" -InformationAction Continue
    try {
        & $Action
        $script:Passed += 1
        Write-Information "[PASS] $Name" -InformationAction Continue
    }
    catch {
        Add-GateFailure -Name $Name -Message $_.Exception.Message
    }
}

function Find-RequiredCommand {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)][string]$Name,
        [Parameter(Mandatory)][string]$Purpose
    )
    $command = Get-Command -Name $Name -ErrorAction SilentlyContinue
    if ($command) {
        return $command.Source
    }
    if ($script:BypassMissingTools) {
        Write-Warning "$Name is unavailable; $Purpose was explicitly bypassed by -AllowMissingTools."
        return $null
    }
    throw "$Name is required for $Purpose in the frozen release container"
}

function Invoke-PythonTool {
    [CmdletBinding()]
    param(
        [Parameter(Mandatory)][string]$Python,
        [Parameter(Mandatory)][string]$RelativePath,
        [string[]]$Arguments = @()
    )
    $path = Join-Path $RepositoryRoot $RelativePath
    if (-not (Test-Path -LiteralPath $path -PathType Leaf)) {
        throw "required tool is missing: $RelativePath"
    }
    Invoke-NativeChecked -FilePath $Python -ArgumentList (@($path) + $Arguments)
}

New-Item -ItemType Directory -Path $TemporaryRoot -Force | Out-Null
$OriginalLocation = Get-Location

try {
    Set-Location -LiteralPath $RepositoryRoot
    try { $Python = Find-RequiredCommand -Name 'python' -Purpose 'Python validation and generators' }
    catch { Add-GateFailure -Name 'Python availability' -Message $_.Exception.Message; $Python = $null }
    try { $Node = Find-RequiredCommand -Name 'node' -Purpose 'browser progress tests' }
    catch { Add-GateFailure -Name 'Node availability' -Message $_.Exception.Message; $Node = $null }

    Invoke-GateStep -Name 'Frozen toolchain contract' -Action {
        & (Join-Path $PSScriptRoot 'Test-ContainerToolchain.ps1') -Strict
        if (-not $?) { throw 'toolchain verification returned failure' }
        if ($Python) {
            Invoke-PythonTool -Python $Python -RelativePath 'tools/validate_container_lock.py'
        }
    }

    Invoke-GateStep -Name 'Authored content aggregation drift' -Action {
        if ($Python) { Invoke-PythonTool -Python $Python -RelativePath 'tools/merge_lab_content.py' -Arguments @('--check') }
    }

    Invoke-GateStep -Name 'Generated lab drift' -Action {
        if ($Python) { Invoke-PythonTool -Python $Python -RelativePath 'tools/generate_labs.py' -Arguments @('--check') }
    }

    Invoke-GateStep -Name 'Assessment source drift' -Action {
        if ($Python) { Invoke-PythonTool -Python $Python -RelativePath 'tools/generate_assessment_banks.py' -Arguments @('--check') }
    }

    Invoke-GateStep -Name 'Rendered assessment drift' -Action {
        if ($Python) { Invoke-PythonTool -Python $Python -RelativePath 'tools/expand_assessments.py' -Arguments @('--check') }
    }

    Invoke-GateStep -Name 'Diagram and accessible SVG drift' -Action {
        if ($Python) { Invoke-PythonTool -Python $Python -RelativePath 'tools/render_diagrams.py' -Arguments @('--check') }
    }

    Invoke-GateStep -Name 'Repository schemas, traceability, safety, and portability' -Action {
        if ($Python) { Invoke-PythonTool -Python $Python -RelativePath 'tools/validate_repository.py' }
    }

    Invoke-GateStep -Name 'Python unit tests' -Action {
        if ($Python) {
            Invoke-NativeChecked -FilePath $Python -ArgumentList @('-m', 'unittest', 'discover', '-s', 'tools/tests', '-p', 'test_*.py', '-v')
        }
    }

    Invoke-GateStep -Name 'Assessment quality and originality' -Action {
        if ($Python) { Invoke-PythonTool -Python $Python -RelativePath 'tools/validate_assessments.py' -Arguments @('--verbose') }
    }

    Invoke-GateStep -Name 'Isolated Pester lab safety suites' -Action {
        $pester = Get-Module -ListAvailable -Name Pester | Sort-Object Version -Descending | Select-Object -First 1
        if (-not $pester) {
            if ($script:BypassMissingTools) { Write-Warning 'Pester is unavailable; isolated lab tests were bypassed.'; return }
            throw 'Pester is required in the frozen release container'
        }
        Import-Module Pester -RequiredVersion '5.7.1' -Force
        $copyRoot = Join-Path $TemporaryRoot 'isolated-labs'
        New-Item -ItemType Directory -Path $copyRoot -Force | Out-Null
        Get-ChildItem -LiteralPath (Join-Path $RepositoryRoot 'labs') -Directory | ForEach-Object {
            Copy-Item -LiteralPath $_.FullName -Destination (Join-Path $copyRoot $_.Name) -Recurse
        }
        $testPaths = @(Get-ChildItem -LiteralPath $copyRoot -Recurse -Filter 'Contract.Tests.ps1' | Sort-Object FullName | ForEach-Object FullName)
        if ($testPaths.Count -ne 28) { throw "expected 28 isolated Pester files, found $($testPaths.Count)" }
        $configuration = New-PesterConfiguration
        $configuration.Run.Path = $testPaths
        $configuration.Run.PassThru = $true
        $configuration.Output.Verbosity = 'Detailed'
        $result = Invoke-Pester -Configuration $configuration
        if ($result.FailedCount -ne 0 -or $result.Result -ne 'Passed') {
            throw "Pester result $($result.Result) with $($result.FailedCount) failed test(s)"
        }
        if ($result.PassedCount -lt 224) { throw "expected at least 224 passing safety cases, found $($result.PassedCount)" }
    }

    Invoke-GateStep -Name 'PSScriptAnalyzer zero-warning policy' -Action {
        $analyzer = Get-Module -ListAvailable -Name PSScriptAnalyzer | Sort-Object Version -Descending | Select-Object -First 1
        if (-not $analyzer) {
            if ($script:BypassMissingTools) { Write-Warning 'PSScriptAnalyzer is unavailable; script analysis was bypassed.'; return }
            throw 'PSScriptAnalyzer is required in the frozen release container'
        }
        Import-Module PSScriptAnalyzer -RequiredVersion '1.25.0' -Force
        $findings = @(Invoke-ScriptAnalyzer -Path $RepositoryRoot -Recurse -Severity @('Warning', 'Error'))
        if ($findings.Count -gt 0) {
            $details = $findings | Select-Object RuleName, Severity, ScriptName, Line, Message | Format-Table -AutoSize | Out-String
            Write-Output $details
            throw "PSScriptAnalyzer returned $($findings.Count) warning/error finding(s)"
        }
    }

    Invoke-GateStep -Name 'Bicep compilation' -Action {
        $bicep = Find-RequiredCommand -Name 'bicep' -Purpose 'Bicep compilation'
        if (-not $bicep) { return }
        $sources = @(Get-ChildItem -LiteralPath (Join-Path $RepositoryRoot 'labs') -Recurse -Filter '*.bicep' | Sort-Object FullName)
        if ($sources.Count -lt 4) { throw "expected at least four Bicep sources, found $($sources.Count)" }
        $index = 0
        foreach ($source in $sources) {
            $index += 1
            $output = Join-Path $TemporaryRoot ("bicep-{0:D3}.json" -f $index)
            Invoke-NativeChecked -FilePath $bicep -ArgumentList @('build', $source.FullName, '--outfile', $output)
            if (-not (Test-Path -LiteralPath $output -PathType Leaf)) { throw "Bicep did not create expected output for $($source.FullName)" }
        }
    }

    Invoke-GateStep -Name 'Node progress tests' -Action {
        if (-not $Node) { return }
        $tests = @(
            Get-ChildItem -LiteralPath (Join-Path $RepositoryRoot 'tools/tests') -File |
                Where-Object { $_.Name -match '\.test\.(?:mjs|cjs)$' } |
                Sort-Object FullName |
                ForEach-Object FullName
        )
        if ($tests.Count -lt 1) { throw 'at least one Node test file is required' }
        Invoke-NativeChecked -FilePath $Node -ArgumentList (@('--test') + $tests)
    }

    Invoke-GateStep -Name 'Markdown lint' -Action {
        $markdownlint = Get-Command -Name 'markdownlint-cli2' -ErrorAction SilentlyContinue
        if (-not $markdownlint) { $markdownlint = Get-Command -Name 'markdownlint' -ErrorAction SilentlyContinue }
        if (-not $markdownlint) {
            if ($script:BypassMissingTools) { Write-Warning 'Markdown lint is unavailable and was bypassed.'; return }
            throw 'markdownlint-cli2 or markdownlint is required in the frozen release container'
        }
        if ($markdownlint.Name -eq 'markdownlint-cli2') {
            Invoke-NativeChecked -FilePath $markdownlint.Source -ArgumentList @('**/*.md', '#.site-docs/**', '#site/**')
        }
        else {
            $markdownFiles = @(Get-ChildItem -LiteralPath $RepositoryRoot -Recurse -Filter '*.md' | Where-Object { $_.FullName -notmatch '[\\/](?:\.site-docs|site)[\\/]' } | ForEach-Object FullName)
            Invoke-NativeChecked -FilePath $markdownlint.Source -ArgumentList $markdownFiles
        }
    }

    Invoke-GateStep -Name 'Spelling validation' -Action {
        $cspell = Find-RequiredCommand -Name 'cspell' -Purpose 'spelling validation'
        if (-not $cspell) { return }
        Invoke-NativeChecked -FilePath $cspell -ArgumentList @('lint', '--no-progress', '--no-summary', '**/*.{md,yml,yaml,ps1,py,js,json,bicep}', '--exclude', '.site-docs/**', '--exclude', 'site/**')
    }

    Invoke-GateStep -Name 'GitHub Actions lint' -Action {
        $actionlint = Find-RequiredCommand -Name 'actionlint' -Purpose 'GitHub Actions validation'
        if ($actionlint) { Invoke-NativeChecked -FilePath $actionlint }
    }

    Invoke-GateStep -Name 'Secret scan' -Action {
        $gitleaks = Find-RequiredCommand -Name 'gitleaks' -Purpose 'tracked and untracked secret scanning'
        if (-not $gitleaks) { return }
        & $gitleaks 'dir' '--help' *> $null
        if ($LASTEXITCODE -eq 0) {
            Invoke-NativeChecked -FilePath $gitleaks -ArgumentList @('dir', $RepositoryRoot, '--no-banner', '--redact', '--exit-code', '1')
        }
        else {
            Invoke-NativeChecked -FilePath $gitleaks -ArgumentList @('detect', '--source', $RepositoryRoot, '--no-banner', '--redact', '--exit-code', '1')
        }
    }

    Invoke-GateStep -Name 'Strict MkDocs staging and build' -Action {
        if (-not $Python) { return }
        Invoke-PythonTool -Python $Python -RelativePath 'tools/build_docs_site.py'
        Invoke-PythonTool -Python $Python -RelativePath 'tools/build_docs_site.py' -Arguments @('--check')
        $siteOutput = Join-Path $TemporaryRoot 'site'
        Invoke-NativeChecked -FilePath $Python -ArgumentList @('-m', 'mkdocs', 'build', '--strict', '--clean', '--site-dir', $siteOutput)
        Invoke-PythonTool -Python $Python -RelativePath 'tools/validate_repository.py' -Arguments @('--skip-portability', '--site', $siteOutput)
    }
}
finally {
    Set-Location -LiteralPath $OriginalLocation.Path
    $resolvedTemporary = [System.IO.Path]::GetFullPath($TemporaryRoot)
    $safePrefix = $TemporaryBase.TrimEnd([System.IO.Path]::DirectorySeparatorChar, [System.IO.Path]::AltDirectorySeparatorChar) + [System.IO.Path]::DirectorySeparatorChar
    if ($resolvedTemporary.StartsWith($safePrefix, [System.StringComparison]::OrdinalIgnoreCase) -and (Split-Path $resolvedTemporary -Leaf) -like 'az305-release-*') {
        Remove-Item -LiteralPath $resolvedTemporary -Recurse -Force -ErrorAction SilentlyContinue
    }
    else {
        Add-GateFailure -Name 'Temporary cleanup' -Message "refused unsafe temporary path $resolvedTemporary"
    }
}

Write-Information "`nOffline release gate: $Passed step(s) passed; $($Failures.Count) failed." -InformationAction Continue
if ($Failures.Count) {
    foreach ($failure in $Failures) { Write-Output "- $failure" }
    exit 1
}
exit 0
