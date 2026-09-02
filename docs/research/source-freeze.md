# Source and environment freeze

This record fixes the research boundary used to author and validate the offline learning environment.

## Blueprint check

- Checked: 2026-09-02
- Primary source: [Microsoft AZ-305 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-305)
- Published blueprint effective date: 2026-04-17
- Study-guide page last updated: 2026-03-19
- Result: four domains and 49 measured objectives, transcribed verbatim into `curriculum/blueprint.yml`
- Foundation IDs `FD-*` are repository prerequisites and are not exam objectives.

The complete frozen Microsoft source set, including service-specific pages and per-lab mappings, is in `curriculum/sources.yml`. The release gate consumes that registry without requesting the web.

## Toolchain check

- Checked: 2026-09-02
- Runtime line: Ubuntu 24.04, Python 3.12, and Node.js 22
- Exact pins: PowerShell 7.6.5, Azure CLI 2.90.0, Az 16.3.0, Bicep 0.46.1, AzCopy 10.32.8, Python 3.12.14, Node.js 22.23.2, Pester 5.7.1, and PSScriptAnalyzer 1.25.0
- Microsoft Graph: only the eight GA modules declared in `curriculum/tool-versions.yml`, each at 2.39.0; no Beta module
- Container base: `mcr.microsoft.com/devcontainers/base:ubuntu-24.04@sha256:d94c97dd9cacf183d0a6fd12a8e87b526e9e928307674ae9c94139139c0c6eae`

Artifact hashes and package integrity data are frozen in `tools/container-lock.json`, `tools/quality-tools-lock.json`, `requirements-container.lock.txt`, and `package-lock.json`.

## Reference provenance

The adaptation reference was read at Git commit `a532eb73711f7b8eb02ba95baa06a3a69376a1c3`. Its worktree was clean before adaptation and was rechecked clean at the same commit after adaptation. No Git metadata, cache, state, built site, learner data, or runtime dependency was copied.

## Operational boundary

Research used public documentation and dependency acquisition only. Implementation performed no Azure or Microsoft Graph sign-in or query, tenant or subscription mutation, Portal interaction, screenshot processing, remote push, Pages deployment, or external-setting change. All completed lab status is `offline-validated`; every `lastLiveVerified` value is `null`.
