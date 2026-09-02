# AZ-305 repository implementation charter

Build and maintain a command-first, offline-verifiable learning environment for the April 17, 2026 AZ-305 blueprint. The repository must remain local until a future owner deliberately configures a remote and publication policy.

The public contract is fixed: 28 portable labs, 49 measured objectives with exactly one instructional owner, five visible checkpoints per lab, 25 scored banks, and 1,250 original questions. Every lab connects business requirements to viable candidates, a weighted decision, an ADR, all five Well-Architected pillars, lane-correct commands, independent assertions, evidence, recovery state, and ownership-aware cleanup.

Author curriculum facts in `curriculum/blueprint.yml`, lab sequencing in `curriculum/lab-catalog.yml`, substantive scenarios in `curriculum/lab-content.yml`, citations in `curriculum/sources.yml`, and command support in `curriculum/commands.yml`. Generated regions use `BEGIN GENERATED AZ305 V1` and `END GENERATED AZ305 V1`; generators must preserve everything outside those boundaries and refuse malformed or nested markers.

Live work is opt-in and separate from release validation. Never authenticate automatically, switch tenant or subscription context, register a provider, perform a cloud mutation without `-Execute`, bypass cost or tenant acknowledgements, store sensitive state, infer ownership from names, automate purge, collect browser analytics, embed external active assets, publish Pages, or claim live verification from an offline fixture.

The definition of done is the successful container-local execution of `tools/Invoke-OfflineReleaseGate.ps1`, a clean local Git worktree, a release commit, and annotated tag `az305-2026-04-offline`.
