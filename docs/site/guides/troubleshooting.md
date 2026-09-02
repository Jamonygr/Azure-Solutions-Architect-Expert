# Troubleshooting guide

Troubleshoot from contracts and evidence. Do not widen scope, delete broadly, or rerun a partial mutation until state and ownership are understood.

## First classification

| Symptom | Check first | Safe response |
| --- | --- | --- |
| Exit code `1` | Which independent assertion failed? | Preserve result, diagnose that assertion, and retry only its dependency |
| Exit code `2` | Which acknowledgement, uncertainty, or partial operation gated completion? | Review state and require a human decision |
| No `.state/<run-id>` in preview | Whether `-Execute` was absent | Expected behavior; preview must not create state |
| Missing state during cleanup | Exact run ID and lab root | Refuse cleanup; do not reconstruct ownership from names |
| Ownership mismatch | ID plus `purpose`, `labId`, `runId`, `expiresOn` | Refuse the object and investigate provenance |
| Partial setup | Last recorded managed ID and failed operation | Keep state, correct the cause, and resume or clean exact recorded objects |
| Post-cleanup residual | Dependency order and action result | Retry the exact residual after verifying ownership |
| Authentication or authorization error | Current context, scope, deny assignment, data plane | Stop; do not solve by granting broad permanent rights |
| Region, quota, or SKU error | Current availability and requested capacity | Revisit the requirement and candidate decision |

## Diagnose in layers

1. **Input contract** — required parameters, environment fallbacks, run ID, location pair, and acknowledgements.
2. **Local toolchain** — pinned command presence and versions.
3. **Context** — intended tenant and subscription, established explicitly outside the lab.
4. **Authorization** — management plane, data plane, Graph, policy, locks, and deny assignments.
5. **Service constraints** — region, quota, provider registration, SKU, naming, and dependency state.
6. **Assertion logic** — distinguish absent, empty, denied, throttled, transient, and malformed results.
7. **Cleanup graph** — remove dependents before parents and keep failed items in state.

## Preserve recoverability

Do not edit a run record to make validation pass. Append or replace only fields the lifecycle contract owns, keep returned identifiers, and record a failure before exiting. Never automate purge of soft-deleted material. If ownership is uncertain, the correct outcome is refusal and escalation.

## Documentation build failures

Run `python tools/build_docs_site.py --check` to list staging drift. If a lab page or learner question bank is missing, regenerate the authoritative artifacts before staging. A detected `ANSWERS.md`, external script, or external stylesheet in the staging tree is a release failure, not a warning to suppress.
