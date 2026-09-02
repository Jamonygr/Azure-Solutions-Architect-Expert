# Azure PowerShell cheat sheet

Labs assigned to the `azure-powershell` track place lifecycle scripts under `scripts/azure-powershell`. Labs 03 and 07 may also use the pinned GA Microsoft Graph PowerShell v1.0 submodules. No Beta module is part of this environment.

## Lifecycle entry points

```powershell
pwsh ./scripts/azure-powershell/Preflight.ps1 -RunId synthetic-030001
pwsh ./scripts/azure-powershell/Setup.ps1 -RunId synthetic-030001
pwsh ./scripts/azure-powershell/Validate.ps1 -RunId synthetic-030001 -Mode Deployment
pwsh ./scripts/azure-powershell/Cleanup.ps1 -RunId synthetic-030001
pwsh ./scripts/azure-powershell/Validate.ps1 -RunId synthetic-030001 -Mode PostCleanup
```

Without `-Execute`, setup and cleanup show the intended work and make no cloud request or state directory. A future live run must begin from an explicitly authenticated context established outside the scripts.

## Read-oriented patterns

| Intent | Pattern |
| --- | --- |
| Inspect installed versions | `Get-Module -ListAvailable Az, Microsoft.Graph.Authentication` |
| Inspect selected Azure context | `Get-AzContext` |
| Inspect an exact ARM object | `Get-AzResource -ResourceId <exact-resource-id>` |
| Invoke a read-only ARM request | `Invoke-AzRestMethod -Method GET -Path <arm-path>` |
| Inspect Graph context | `Get-MgContext` |
| Invoke a Graph v1.0 read | `Invoke-MgGraphRequest -Method GET -Uri <v1.0-uri>` |
| Compile Bicep offline | `bicep build ./artifacts/main.bicep --stdout` |

## Graph boundary

Graph commands are confined to Authentication, Users, Groups, Applications, Identity.DirectoryManagement, Identity.SignIns, Identity.Governance, and Reports at the pinned version. Request the least delegated scope needed for an authorized future exercise, make tenant-wide consequences explicit, and require `-AcknowledgeTenantChange` before a mutation. Disconnecting does not undo a directory change, so state and cleanup ownership still matter.

## PowerShell habits

- Use `-LiteralPath` for state and evidence paths.
- Set `$ErrorActionPreference = 'Stop'` inside lifecycle scripts.
- Convert structured results with sufficient JSON depth and UTF-8 without a byte-order mark.
- Capture returned IDs before proceeding to dependent operations.
- Distinguish `$null`, an empty collection, and a caught command failure.
- Mock Azure, Graph, REST, AzCopy, and migration entry points so an offline test fails on an unexpected call.

Use the [Azure PowerShell reference](https://learn.microsoft.com/en-us/powershell/azure/) and [Microsoft Graph PowerShell overview](https://learn.microsoft.com/en-us/powershell/microsoftgraph/overview) for current syntax.
