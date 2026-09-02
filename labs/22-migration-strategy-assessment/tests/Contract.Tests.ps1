# BEGIN GENERATED AZ305 V1
[Diagnostics.CodeAnalysis.SuppressMessageAttribute('PSUseDeclaredVarsMoreThanAssignments', '', Justification = 'Pester lifecycle variables cross BeforeAll, BeforeEach, helper, and It scopes.')]
param()

BeforeAll {
    $SourceLabRoot = Split-Path $PSScriptRoot -Parent
    $Track = 'azure-powershell'
    $IsDesignSimulation = $true
    $IsFoundationPreview = $false
    $SetupHasDesignCloudGate = $true
    $ValidationHasDesignCloudGate = $true
    $IsCliTrack = $false
    $SubscriptionId = '00000000-0000-4000-8000-000000000305'
    $TenantId = '00000000-0000-4000-8000-000000000306'
    $BaseParameters = [ordered]@{
        SubscriptionId = $SubscriptionId
        TenantId = $TenantId
        Location = 'westeurope'
        SecondaryLocation = 'northeurope'
        ResourceGroup = 'rg-az305-contract'
        WorkloadName = 'az305-contract'
        ExpiresOn = '2099-12-31'

    }

    $ShimPreamble = @'
function global:Record-Az305TestCall {
    param([string]$Name)
    if ($env:AZ305_TEST_CALL_LOG) {
        $stateExists = Test-Path -LiteralPath $env:AZ305_TEST_STATE_PATH
        Add-Content -LiteralPath $env:AZ305_TEST_CALL_LOG -Value "$Name|state=$stateExists"
    }
}
function global:Invoke-AzRestMethod { Record-Az305TestCall -Name 'Invoke-AzRestMethod'; throw 'Unexpected Azure REST request.' }
function global:Connect-MgGraph { Record-Az305TestCall -Name 'Connect-MgGraph'; throw 'Lifecycle scripts must never sign in.' }
function global:Invoke-MgGraphRequest { Record-Az305TestCall -Name 'Invoke-MgGraphRequest'; throw 'Unexpected Microsoft Graph request.' }
function global:Start-AzDataMigration { Record-Az305TestCall -Name 'Start-AzDataMigration'; throw 'Unexpected migration request.' }
'@
    $MatchingFailureShim = $ShimPreamble + @'
function global:az {
    if ($args.Count -ge 2 -and $args[0] -eq 'account' -and $args[1] -eq 'show') {
        $global:LASTEXITCODE = 0
        return '{"id":"00000000-0000-4000-8000-000000000305","tenantId":"00000000-0000-4000-8000-000000000306"}'
    }
    Record-Az305TestCall -Name ('az ' + ($args -join ' '))
    $global:LASTEXITCODE = 17
    return '{}'
}
function global:Get-AzContext {
    return [pscustomobject]@{ Subscription = [pscustomobject]@{ Id = '00000000-0000-4000-8000-000000000305' }; Tenant = [pscustomobject]@{ Id = '00000000-0000-4000-8000-000000000306' } }
}
function global:Get-MgContext { return [pscustomobject]@{ TenantId = '00000000-0000-4000-8000-000000000306' } }
function global:Get-AzPolicyAssignment { Record-Az305TestCall -Name 'Get-AzPolicyAssignment'; throw 'Injected checkpoint failure.' }
function global:Get-AzResourceGroup { Record-Az305TestCall -Name 'Get-AzResourceGroup'; throw 'Injected checkpoint failure.' }
function global:Get-AzSubscription { Record-Az305TestCall -Name 'Get-AzSubscription'; throw 'Injected checkpoint failure.' }
function global:azcopy { Record-Az305TestCall -Name 'azcopy'; $global:LASTEXITCODE = 17; return '{}' }
function global:bicep { Record-Az305TestCall -Name 'bicep'; $global:LASTEXITCODE = 17; return '{}' }
'@
    $ContextMismatchShim = $ShimPreamble + @'
function global:az {
    if ($args.Count -ge 2 -and $args[0] -eq 'account' -and $args[1] -eq 'show') {
        $global:LASTEXITCODE = 0
        return '{"id":"00000000-0000-4000-8000-000000009999","tenantId":"00000000-0000-4000-8000-000000009998"}'
    }
    Record-Az305TestCall -Name 'unexpected-az'
    throw 'A checkpoint command ran after context mismatch.'
}
function global:Get-AzContext { return [pscustomobject]@{ Subscription = [pscustomobject]@{ Id = '00000000-0000-4000-8000-000000009999' }; Tenant = [pscustomobject]@{ Id = '00000000-0000-4000-8000-000000009998' } } }
function global:Get-MgContext { return [pscustomobject]@{ TenantId = '00000000-0000-4000-8000-000000009998' } }
'@
    $OfflineRefusalShim = $ShimPreamble + @'
function global:az { Record-Az305TestCall -Name 'forbidden-az'; throw 'Design simulation issued an Azure CLI request.' }
function global:Get-AzContext { Record-Az305TestCall -Name 'forbidden-Get-AzContext'; throw 'Design simulation issued an Az request.' }
function global:Get-MgContext { Record-Az305TestCall -Name 'forbidden-Get-MgContext'; throw 'Design simulation issued a Graph request.' }
function global:Get-AzPolicyAssignment { Record-Az305TestCall -Name 'Get-AzPolicyAssignment'; throw 'Injected checkpoint failure.' }
function global:Get-AzResourceGroup { Record-Az305TestCall -Name 'Get-AzResourceGroup'; throw 'Injected checkpoint failure.' }
function global:Get-AzSubscription { Record-Az305TestCall -Name 'Get-AzSubscription'; throw 'Injected checkpoint failure.' }
function global:azcopy { Record-Az305TestCall -Name 'forbidden-azcopy'; throw 'Design simulation issued an AzCopy request.' }
'@
}

Describe 'LAB-22 portable lifecycle behavior' {
    BeforeEach {
        $IsolatedLab = Join-Path $TestDrive ("lab-" + [guid]::NewGuid().ToString('N'))
        Copy-Item -LiteralPath $SourceLabRoot -Destination $IsolatedLab -Recurse
        $ScriptRoot = Join-Path $IsolatedLab "scripts/$Track"
        $CallLog = Join-Path $IsolatedLab 'cloud-calls.log'
        $env:AZ305_TEST_CALL_LOG = $CallLog
    }

    AfterEach {
        Remove-Item Env:AZ305_TEST_CALL_LOG -ErrorAction SilentlyContinue
        Remove-Item Env:AZ305_TEST_STATE_PATH -ErrorAction SilentlyContinue
        Remove-Item Env:AZ305_TEST_RUN_ID -ErrorAction SilentlyContinue
    }

    BeforeAll {
    function Get-TestParameterSet {
        param([string]$RunId, [switch]$Execute, [string]$Mode)
        $parameters = @{}
        foreach ($entry in $BaseParameters.GetEnumerator()) { $parameters[$entry.Key] = $entry.Value }
        $parameters.RunId = $RunId
        if ($Execute) {
            $parameters.Execute = $true
            $parameters.AcknowledgeCost = $true
            $parameters.AcknowledgeTenantChange = $true
        }
        if ($Mode) { $parameters.Mode = $Mode }
        return $parameters
    }

    function Invoke-LifecycleProcess {
        param([string]$ScriptName, [hashtable]$Parameters, [string]$ShimBody = '')
        $invocationId = [guid]::NewGuid().ToString('N')
        $parametersPath = Join-Path $IsolatedLab "$invocationId.parameters.json"
        $harnessPath = Join-Path $IsolatedLab "$invocationId.harness.ps1"
        $Parameters | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $parametersPath -Encoding utf8NoBOM
        $harness = @'
param([string]$TargetScript, [string]$ParametersPath)
'@ + "`n" + $ShimBody + @'
$invokeParameters = Get-Content -LiteralPath $ParametersPath -Raw | ConvertFrom-Json -AsHashtable
& $TargetScript @invokeParameters
exit $LASTEXITCODE
'@
        $harness | Set-Content -LiteralPath $harnessPath -Encoding utf8NoBOM
        $env:AZ305_TEST_RUN_ID = [string]$Parameters.RunId
        $env:AZ305_TEST_STATE_PATH = Join-Path $IsolatedLab ".state/$($Parameters.RunId)/run.json"
        $savedNativePreference = $PSNativeCommandUseErrorActionPreference
        try {
            $PSNativeCommandUseErrorActionPreference = $false
            $output = @(& pwsh -NoLogo -NoProfile -File $harnessPath -TargetScript (Join-Path $ScriptRoot $ScriptName) -ParametersPath $parametersPath 2>&1)
            $exitCode = $LASTEXITCODE
        }
        finally { $PSNativeCommandUseErrorActionPreference = $savedNativePreference }
        return [pscustomobject]@{ ExitCode = $exitCode; Output = @($output) }
    }

    function Write-TestRunState {
        param([string]$RunId, [string]$Status = 'planned', [object[]]$ManagedObjects = @(), [object[]]$OriginalSettings = @())
        $stateRoot = Join-Path $IsolatedLab ".state/$RunId"
        New-Item -ItemType Directory -Path $stateRoot -Force | Out-Null
        $state = [ordered]@{
            schemaVersion = '1.0.0'; labId = 'LAB-22'; runId = $RunId; track = 'azure-powershell'
            implementationMode = 'design-simulation'; status = $Status
            createdAt = '2026-09-02T00:00:00Z'; execute = $true
            parameters = [ordered]@{ subscriptionId = $SubscriptionId; tenantId = $TenantId; expiresOn = '2099-12-31' }
            managedObjects = @($ManagedObjects); originalSettings = @($OriginalSettings)
        }
        $path = Join-Path $stateRoot 'run.json'
        $state | ConvertTo-Json -Depth 20 | Set-Content -LiteralPath $path -Encoding utf8NoBOM
        return $path
    }

    function Get-ManagedObjectFixture {
        param([string]$Id, [string]$RunId, [string]$RecordedRunId = $RunId)
        return [pscustomobject]@{
            id = $Id; type = 'azure-resource'
            tags = [ordered]@{ purpose = 'az305-lab'; labId = 'LAB-22'; runId = $RecordedRunId; expiresOn = '2099-12-31' }
        }
    }

    function Get-CleanupSuccessShim {
        if ($IsCliTrack) {
            return $ShimPreamble + @'
function global:az {
    if ($args[0] -eq 'account' -and $args[1] -eq 'show') { $global:LASTEXITCODE = 0; return '{"id":"00000000-0000-4000-8000-000000000305","tenantId":"00000000-0000-4000-8000-000000000306"}' }
    $idIndex = [Array]::IndexOf([object[]]$args, '--ids')
    $id = [string]$args[$idIndex + 1]
    if ($args[0] -eq 'resource' -and $args[1] -eq 'show') {
        $global:LASTEXITCODE = 0
        return ([ordered]@{ id = $id; tags = [ordered]@{ purpose = 'az305-lab'; labId = '__LAB_ID__'; runId = $env:AZ305_TEST_RUN_ID; expiresOn = '2099-12-31' } } | ConvertTo-Json -Compress)
    }
    if ($args[0] -eq 'resource' -and $args[1] -eq 'delete') { Add-Content -LiteralPath $env:AZ305_TEST_CALL_LOG -Value $id; $global:LASTEXITCODE = 0; return }
    throw 'Unexpected Azure CLI cleanup command.'
}
'@.Replace('__LAB_ID__', 'LAB-22')
        }
        return $ShimPreamble + @'
function global:Get-AzContext { return [pscustomobject]@{ Subscription = [pscustomobject]@{ Id = '00000000-0000-4000-8000-000000000305' }; Tenant = [pscustomobject]@{ Id = '00000000-0000-4000-8000-000000000306' } } }
function global:Get-AzResource { [CmdletBinding()] param([string]$ResourceId) return [pscustomobject]@{ ResourceId = $ResourceId; Tags = [ordered]@{ purpose = 'az305-lab'; labId = '__LAB_ID__'; runId = $env:AZ305_TEST_RUN_ID; expiresOn = '2099-12-31' } } }
function global:Remove-AzResource { [CmdletBinding()] param([string]$ResourceId, [switch]$Force) Add-Content -LiteralPath $env:AZ305_TEST_CALL_LOG -Value $ResourceId; return $true }
'@.Replace('__LAB_ID__', 'LAB-22')
    }

    function Get-CleanupFailureShim {
        if ($IsCliTrack) {
            return $ShimPreamble + @'
function global:az {
    if ($args[0] -eq 'account' -and $args[1] -eq 'show') { $global:LASTEXITCODE = 0; return '{"id":"00000000-0000-4000-8000-000000000305","tenantId":"00000000-0000-4000-8000-000000000306"}' }
    $idIndex = [Array]::IndexOf([object[]]$args, '--ids')
    $id = [string]$args[$idIndex + 1]
    if ($args[0] -eq 'resource' -and $args[1] -eq 'show') { $global:LASTEXITCODE = 0; return ([ordered]@{ id = $id; tags = [ordered]@{ purpose = 'az305-lab'; labId = '__LAB_ID__'; runId = $env:AZ305_TEST_RUN_ID; expiresOn = '2099-12-31' } } | ConvertTo-Json -Compress) }
    if ($args[0] -eq 'resource' -and $args[1] -eq 'delete') { Record-Az305TestCall -Name 'delete-failure'; $global:LASTEXITCODE = 17; return }
    throw 'Unexpected Azure CLI cleanup command.'
}
'@.Replace('__LAB_ID__', 'LAB-22')
        }
        return $ShimPreamble + @'
function global:Get-AzContext { return [pscustomobject]@{ Subscription = [pscustomobject]@{ Id = '00000000-0000-4000-8000-000000000305' }; Tenant = [pscustomobject]@{ Id = '00000000-0000-4000-8000-000000000306' } } }
function global:Get-AzResource { [CmdletBinding()] param([string]$ResourceId) return [pscustomobject]@{ ResourceId = $ResourceId; Tags = [ordered]@{ purpose = 'az305-lab'; labId = '__LAB_ID__'; runId = $env:AZ305_TEST_RUN_ID; expiresOn = '2099-12-31' } } }
function global:Remove-AzResource { [CmdletBinding()] param([string]$ResourceId, [switch]$Force) Record-Az305TestCall -Name 'Remove-AzResource-failure'; throw 'Injected delete failure.' }
'@.Replace('__LAB_ID__', 'LAB-22')
    }
    }

    It 'uses exactly one generated region in every lifecycle script' {
        Get-ChildItem $ScriptRoot -Filter '*.ps1' | ForEach-Object {
            $marker = 'BEGIN GENERATED ' + 'AZ305 V1'
            (Get-Content $_.FullName -Raw).Split($marker).Count | Should -Be 2
        }
    }

    It 'executes setup preview without cloud access and uses only the Golden Lab intent record' {
        $run = 'preview-000001'
        $result = Invoke-LifecycleProcess -ScriptName 'Setup.ps1' -Parameters (Get-TestParameterSet -RunId $run) -ShimBody $OfflineRefusalShim
        $result.ExitCode | Should -Be 0
        $statePath = Join-Path $IsolatedLab ".state/$run/run.json"
        if ($IsFoundationPreview) {
            $state = Get-Content -LiteralPath $statePath -Raw | ConvertFrom-Json
            $state.status | Should -Be 'planned'
            $state.execute | Should -BeFalse
        } else { Test-Path $statePath | Should -BeFalse }
        Test-Path $CallLog | Should -BeFalse
    }

    It 'refuses a mismatched context and keeps every design simulation offline' {
        $run = 'context-000001'
        $shim = if ($IsDesignSimulation) { $OfflineRefusalShim } else { $ContextMismatchShim }
        $result = Invoke-LifecycleProcess -ScriptName 'Setup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $shim
        if ($IsDesignSimulation) {
            $result.ExitCode | Should -BeIn @(0, 1, 2)
            Test-Path $CallLog | Should -BeFalse
            if ($SetupHasDesignCloudGate) {
                $result.ExitCode | Should -Be 2
                Test-Path (Join-Path $IsolatedLab ".state/$run") | Should -BeFalse
            }
        } else {
            $result.ExitCode | Should -Be 2
            Test-Path (Join-Path $IsolatedLab ".state/$run") | Should -BeFalse
            Test-Path $CallLog | Should -BeFalse
        }
    }

    It 'writes recovery state before an injected checkpoint failure and preserves failed status' {
        if ($IsDesignSimulation) {
            (Get-Content (Join-Path $ScriptRoot 'Setup.ps1') -Raw).IndexOf('Save-RunState -State $state') | Should -BeLessThan (Get-Content (Join-Path $ScriptRoot 'Setup.ps1') -Raw).IndexOf('# 22-CP01:')
            return
        }
        $run = 'failure-000001'
        $result = Invoke-LifecycleProcess -ScriptName 'Setup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $MatchingFailureShim
        $result.ExitCode | Should -Be 1
        $calls = @(Get-Content -LiteralPath $CallLog)
        $calls.Count | Should -BeGreaterThan 0
        $calls[0] | Should -Match 'state=True'
        $state = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/run.json") -Raw | ConvertFrom-Json
        $state.status | Should -Be 'failed'
    }

    It 'never overwrites an existing recovery record' {
        $run = 'existing-000001'
        $statePath = Write-TestRunState -RunId $run -Status deployed
        $before = Get-Content -LiteralPath $statePath -Raw
        $shim = if ($IsDesignSimulation) { $OfflineRefusalShim } else { $MatchingFailureShim }
        $result = Invoke-LifecycleProcess -ScriptName 'Setup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $shim
        $result.ExitCode | Should -Be 2
        (Get-Content -LiteralPath $statePath -Raw) | Should -BeExactly $before
        Test-Path $CallLog | Should -BeFalse
    }

    It 'fails deployment validation for a failed setup state without cloud access' {
        $run = 'validate-failed-000001'
        Write-TestRunState -RunId $run -Status failed | Out-Null
        $result = Invoke-LifecycleProcess -ScriptName 'Validate.ps1' -Parameters (Get-TestParameterSet -RunId $run -Mode Deployment) -ShimBody $OfflineRefusalShim
        $result.ExitCode | Should -Be 1
        $artifact = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/validation.json") -Raw | ConvertFrom-Json
        $artifact.result | Should -Be 'fail'
        Test-Path $CallLog | Should -BeFalse
    }

    It 'executes every positive and negative checkpoint independently or gates design cloud validation' {
        $run = 'validate-live-000001'
        Write-TestRunState -RunId $run | Out-Null
        $shim = if ($IsDesignSimulation) { $OfflineRefusalShim } else { $MatchingFailureShim }
        $result = Invoke-LifecycleProcess -ScriptName 'Validate.ps1' -Parameters (Get-TestParameterSet -RunId $run -Mode Deployment -Execute) -ShimBody $shim
        $artifact = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/validation.json") -Raw | ConvertFrom-Json
        if ($ValidationHasDesignCloudGate) {
            $result.ExitCode | Should -Be 2
            $artifact.result | Should -Be 'partial'
            Test-Path $CallLog | Should -BeFalse
        } else {
            $result.ExitCode | Should -BeIn @(0, 1)
            @($artifact.assertions | Where-Object id -Match '^LAB22-CP0[1-5]-(POS|NEG)$').Count | Should -Be 10
        }
    }

    It 'refuses a recorded ownership mismatch before any live inspection or deletion' {
        $run = 'ownership-000001'
        $id = "/subscriptions/$SubscriptionId/resourceGroups/rg-az305-contract/providers/Microsoft.Test/parents/one"
        Write-TestRunState -RunId $run -ManagedObjects @((Get-ManagedObjectFixture -Id $id -RunId $run -RecordedRunId 'foreign-run')) | Out-Null
        $result = Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $OfflineRefusalShim
        $result.ExitCode | Should -Be 1
        Test-Path $CallLog | Should -BeFalse
        $artifact = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/cleanup.json") -Raw | ConvertFrom-Json
        $artifact.ownershipVerified | Should -BeFalse
        $artifact.actions[0].result | Should -Be 'refused'
    }

    It 'keeps a failed deletion recoverable and prevents design-simulation cloud cleanup' {
        $run = 'delete-failed-000001'
        $id = "/subscriptions/$SubscriptionId/resourceGroups/rg-az305-contract/providers/Microsoft.Test/parents/one"
        Write-TestRunState -RunId $run -ManagedObjects @((Get-ManagedObjectFixture -Id $id -RunId $run)) | Out-Null
        $shim = if ($IsDesignSimulation) { $OfflineRefusalShim } else { Get-CleanupFailureShim }
        $result = Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $shim
        $result.ExitCode | Should -Be 1
        $state = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/run.json") -Raw | ConvertFrom-Json
        @($state.managedObjects).Count | Should -Be 1
        if ($IsDesignSimulation) { Test-Path $CallLog | Should -BeFalse } else { $state.status | Should -Be 'failed' }
    }

    It 'cleans in reverse dependency order and is idempotent' {
        $run = 'cleanup-order-000001'
        if ($IsDesignSimulation) {
            Write-TestRunState -RunId $run | Out-Null
            $first = Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $OfflineRefusalShim
            $second = Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $OfflineRefusalShim
            $first.ExitCode | Should -Be 0
            $second.ExitCode | Should -Be 0
            Test-Path $CallLog | Should -BeFalse
            return
        }
        $parentId = "/subscriptions/$SubscriptionId/resourceGroups/rg-az305-contract/providers/Microsoft.Test/parents/one"
        $childId = "$parentId/children/two"
        $objects = @((Get-ManagedObjectFixture -Id $parentId -RunId $run), (Get-ManagedObjectFixture -Id $childId -RunId $run))
        $originals = @([pscustomobject]@{ id = $childId; setting = 'synthetic-original'; value = 'before' })
        Write-TestRunState -RunId $run -ManagedObjects $objects -OriginalSettings $originals | Out-Null
        $first = Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody (Get-CleanupSuccessShim)
        $first.ExitCode | Should -Be 0
        @(Get-Content -LiteralPath $CallLog) | Should -Be @($childId, $parentId)
        $state = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/run.json") -Raw | ConvertFrom-Json
        $state.status | Should -Be 'cleaned'
        @($state.managedObjects).Count | Should -Be 0
        @($state.originalSettings).Count | Should -Be 0
        $second = Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $OfflineRefusalShim
        $second.ExitCode | Should -Be 0
        @(Get-Content -LiteralPath $CallLog).Count | Should -Be 2
    }

    It 'passes post-cleanup validation only after actual zero-residual cleanup' {
        $run = 'post-cleanup-000001'
        Write-TestRunState -RunId $run | Out-Null
        (Invoke-LifecycleProcess -ScriptName 'Cleanup.ps1' -Parameters (Get-TestParameterSet -RunId $run -Execute) -ShimBody $OfflineRefusalShim).ExitCode | Should -Be 0
        $result = Invoke-LifecycleProcess -ScriptName 'Validate.ps1' -Parameters (Get-TestParameterSet -RunId $run -Mode PostCleanup) -ShimBody $OfflineRefusalShim
        $result.ExitCode | Should -Be 0
        $artifact = Get-Content -LiteralPath (Join-Path $IsolatedLab ".state/$run/validation.json") -Raw | ConvertFrom-Json
        $artifact.result | Should -Be 'pass'
    }

}
# END GENERATED AZ305 V1
