# Implementation report

## Scope

This repository implements the AZ-305 learning environment against the Microsoft study guide effective April 17, 2026. The official wording and 49-objective count were rechecked on September 2, 2026 before repository creation.

## Delivered contract

- 28 substantive, standalone labs: LAB-00 through LAB-27.
- 49 measured objectives, each with exactly one primary lab; five `FD-*` items remain explicitly non-exam foundations.
- 25 assessment banks and 1,250 questions, with 50 questions and the required 15/25/10 difficulty mix in each instructional lab.
- Exactly five checkpoints in every lab, for 140 checkpoints total.
- Four `design-simulation`, ten `reference-deployable`, and fourteen `safe-analogue` labs.
- 28 Mermaid sources with deterministic accessible SVG counterparts and seven self-contained Bicep source files across Labs 18, 21, 26, and 27.
- Browser-local progress under `az305LearnerProgress.v1`, with explicit JSON import/export and no silent browser/CLI synchronization.

## Validation classification

All labs are `offline-validated`; every `lastLiveVerified` value is `null`. Offline validation covers schemas, generation drift, traceability, assessment quality, PowerShell safety behavior with throwing shims, Bicep compilation, diagrams, links, documentation, and secret-pattern scans. It does not assert that any Azure or Microsoft Graph operation succeeded in a tenant.

The definitive gate ran inside the pinned container with Docker networking disabled. All 18 steps passed, including 29,382 repository checks, 36 Python tests, 309 isolated Pester tests, 19 Node tests, seven Bicep builds, zero PSScriptAnalyzer warnings or errors, assessment originality checks for all 1,250 questions, Markdown and spelling checks, action lint, secret scanning, and strict staging/build inspection of 104 answer-free documentation files.

## Live verification

No Azure or Microsoft Graph sign-in, query, mutation, Portal action, screenshot capture, remote push, GitHub Pages deployment, or external setting change was performed during implementation. The included live paths require explicit execution and acknowledgement switches and must be run only by an authorized future owner.

## Reproducibility

The development container pins Ubuntu 24.04 by digest and records all required package and feature hashes. The verified local image ID is `sha256:40c6ed78aab23201c0df793c5c4017088eec87c7888190dc36420868d17c925c`. The gate verified PowerShell 7.6.5, Azure CLI 2.90.0, Az 16.3.0, Bicep 0.46.1, AzCopy 10.32.8, Python 3.12.14, Node.js 22.23.2, Pester 5.7.1, PSScriptAnalyzer 1.25.0, and only the eight approved Microsoft Graph 2.39.0 modules. The offline release gate consumes only repository registries and local artifacts and performs no web, Azure, or Graph requests.

## Repository provenance

The read-only structural reference repository was clean before adaptation at Git HEAD `a532eb73711f7b8eb02ba95baa06a3a69376a1c3` and was rechecked clean at the same HEAD after adaptation. The target used `main` with no remote when the definitive gate passed and the annotated local release tag `az305-2026-04-offline` was created. After release completion, the user explicitly authorized creation of the private GitHub repository `Jamonygr/Azure-Solutions-Architect-Expert` and the push of `main` plus that tag. GitHub Pages remains disabled and was not deployed. No host component was upgraded; dependency acquisition and all verification occurred in the development container.
