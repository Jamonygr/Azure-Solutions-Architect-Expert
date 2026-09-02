# Azure CLI cheat sheet

Labs assigned to the `azure-cli` track place lifecycle scripts under `scripts/azure-cli`. The commands below are study references; generating or building this site does not run them against Azure.

## Lifecycle entry points

```powershell
pwsh ./scripts/azure-cli/Preflight.ps1 -RunId synthetic-010001
pwsh ./scripts/azure-cli/Setup.ps1 -RunId synthetic-010001
pwsh ./scripts/azure-cli/Validate.ps1 -RunId synthetic-010001 -Mode Deployment
pwsh ./scripts/azure-cli/Cleanup.ps1 -RunId synthetic-010001
pwsh ./scripts/azure-cli/Validate.ps1 -RunId synthetic-010001 -Mode PostCleanup
```

These calls remain preview-only without `-Execute`. A future authorized execution must supply the lab inputs and applicable cost or tenant-change acknowledgements.

## Read-oriented patterns

| Intent | Pattern |
| --- | --- |
| Confirm CLI version | `az version` |
| Inspect selected context | `az account show --output json` |
| Inspect an exact resource | `az resource show --ids <exact-resource-id> --output json` |
| Query resources without changing them | `az graph query --graph-query <query> --output json` |
| Inspect a deployment | `az deployment group show --resource-group <group> --name <deployment>` |
| Validate Bicep at resource-group scope | `az deployment group validate --resource-group <group> --template-file ./artifacts/main.bicep --parameters @artifacts/parameters.example.json` |

Treat context output and resource IDs as sensitive operational data. Do not paste live output into tracked fixtures.

## Mutation boundary

The generated setup script validates inputs, creates `.state/<run-id>/run.json`, and only then reaches the first potential mutation. Returned IDs and original non-secret settings are recorded immediately. Never replace this sequence with a broad `az group delete` shortcut: cleanup must validate each exact ID and all ownership tags first.

## Reliable query habits

- Request JSON for machine interpretation and test each property explicitly.
- Use exact IDs after creation; names alone are insufficient cleanup identity.
- Keep a desired-state assertion separate from an absence assertion.
- Check command families against `curriculum/commands.yml` before adding a command.
- Use `--only-show-errors` only when it will not remove evidence required for diagnosis.
- Treat an empty result, authorization failure, throttling response, and transient transport failure as different outcomes.

For syntax and current behavior, use the [Azure CLI reference](https://learn.microsoft.com/en-us/cli/azure/).
