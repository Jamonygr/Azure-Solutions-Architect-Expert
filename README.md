# AZ-305 Complete Learning Environment

![AZ-305 Complete Learning Environment cover showing connected identity, data, continuity, and infrastructure architecture](docs/site-assets/visuals/home-hero.png)

A visual, architecture-first learning environment for the Microsoft AZ-305 blueprint effective April 17, 2026.

This repository provides a guided path from architecture requirements to defensible Azure design decisions. It contains 28 portable labs, maps all 49 measured skills to one primary lab, and includes 1,250 original questions across Labs 01–25.

All learner operations use Azure CLI, Azure PowerShell, Microsoft Graph PowerShell, Bicep, AzCopy, or KQL from PowerShell 7. Lab instructions do not require Azure Portal procedures, screenshots, or screenshot evidence. The visual layer uses repository-local illustrations, accessible architecture diagrams, decision matrices, timelines, and infographics.

> [!IMPORTANT]
> This independent project is not an official Microsoft course. Azure resources can incur charges. Use an approved disposable subscription, review every lab's permission and cost gates, and complete its ownership-aware residual-resource audit.

## Choose a pathway

| Pathway | Best for | Route |
| --- | --- | --- |
| [Quick start](docs/site/paths/quick-start.md) | Learners who want a safe six-session architecture tour | Lab 00 → Labs 03, 12, 16, and 24 → Capstone 26 |
| [Full exam preparation](docs/site/paths/full-exam.md) | Learners covering every official objective | Labs 00–25 in order → all 1,250 questions → Capstones 26–27 |
| [Job ready](docs/site/paths/job-ready.md) | Learners practising requirements, trade-offs, ADRs, and operational ownership | Labs 00–25 → portfolio reviews and material changes → both capstones |

The searchable documentation site adds visual domain navigation, architecture guidance, field guides, assessment dashboards, and private browser-local progress. From the pinned development container, stage and preview it with:

```powershell
python tools/build_docs_site.py
python -m mkdocs serve --strict
```

The documentation workflow runs the complete quality gate on pull requests and pushes to `main`. Publishing remains disabled unless a future repository owner explicitly sets `AZ305_ENABLE_PAGES` to `true`; the workflow does not change that repository setting.

## Start safely

1. Open the repository in its pinned development container.
2. Run `pwsh ./tools/Invoke-OfflineReleaseGate.ps1` to verify the frozen toolchain and generated content.
3. Read [Lab 00: Safe Bootstrap and Dual-Command Lab Contract](labs/00-safe-architect-bootstrap/README.md).
4. Review the [permissions](docs/site/guides/permissions.md), [cost](docs/site/guides/cost.md), and [evidence](docs/site/guidance/evidence.md) guidance.
5. Choose a pathway above or continue through the [complete lab catalog](labs/README.md).

Lifecycle scripts preview by default. A potential mutation requires `-Execute`; cost-bearing work also requires `-AcknowledgeCost`, and tenant-scoped work requires `-AcknowledgeTenantChange`. Scripts do not sign in for you, transmit learner data, or silently install dependencies. Cleanup refuses resources whose exact identity and ownership tags cannot be proven.

## What every lab provides

Each standalone lab folder includes:

- a realistic architecture scenario, learner role, stakeholders, business outcome, constraints, assumptions, and acceptance criteria;
- authored requirements and decision records with objective-to-checkpoint traceability;
- a domain-colored summary, service-specific topology, and decision-matrix visualization;
- exactly five checkpoints with lane-correct commands, expected evidence, and independent positive and negative assertions;
- explicit inputs, permissions, cost gates, implementation mode, safe analogue, retry guidance, and WAF consequences;
- weighted candidate analysis, disqualifiers, selected and rejected alternatives, risks, mitigations, and an ADR;
- a deterministic material change that requires the learner to revisit the recommendation;
- synchronized `Preflight.ps1`, `Setup.ps1`, `Validate.ps1`, and `Cleanup.ps1` lifecycle scripts;
- dependency-aware, idempotent cleanup with ownership refusal and post-cleanup validation; and
- 50 original assessment questions in Labs 01–25, each mapped to one objective and checkpoint.

Lab 00 establishes the operating contract. Labs 26 and 27 are integrative capstones without question banks. Browser and CLI progress do not synchronize silently; JSON import and export are always explicit.

## Coverage

| Official AZ-305 domain | Weight | Labs | Questions |
| --- | ---: | --- | ---: |
| Design identity, governance, and monitoring solutions | 25–30% | 01–07 | 350 |
| Design data storage solutions | 20–25% | 08–13 | 300 |
| Design business continuity solutions | 15–20% | 14–17 | 200 |
| Design infrastructure solutions | 30–35% | 18–25 | 400 |
| Foundation and capstones | Not exam-weighted | 00, 26–27 | Hands-on only |

All 49 official measured skills are covered. Every assessment-enabled lab contains exactly 50 questions with a 15 foundational / 25 applied / 10 advanced difficulty mix, for 1,250 questions total.

## Learning and safety model

A complete architecture pass follows this loop:

1. Translate the scenario into functional and nonfunctional requirements, constraints, assumptions, and acceptance criteria.
2. Confirm scale, latency, availability, RTO, RPO, budget, permissions, regions, and service limitations.
3. Compare at least three eligible candidates where possible, apply disqualifiers, and calculate weighted scores.
4. Select a design, document rejected alternatives, and test it against all five Well-Architected Framework pillars.
5. Preview the assigned Azure CLI or Azure PowerShell lane before any acknowledged execution.
6. Prove each checkpoint with separate positive and negative assertions and retain only redacted evidence.
7. Apply the deterministic material change and revise the decision when a mandatory requirement demands it.
8. Preview cleanup, remove only proven owned resources in dependency order, and verify that no active managed object remains.
9. Use assessment remediation links to repeat weak objectives and checkpoints.

A deployment is not a pass merely because a command returned successfully. Every required checkpoint must satisfy its independent assertions. Cleanup passes only after the post-cleanup validation proves zero active managed resources; soft-deleted or deliberately retained items must remain explicitly recorded.

## Repository interfaces

- [Visual learning home](docs/site/index.md)
- [Lab catalog](labs/README.md)
- [Searchable visual catalog](docs/site/catalog.md)
- [Objective map and status](docs/site/objective-map.md)
- [Study plan](docs/site/study-plan.md)
- [Architecture decisions and ADRs](docs/site/guidance/architecture-decisions.md)
- [Well-Architected review](docs/site/guidance/well-architected.md)
- [Permissions guide](docs/site/guides/permissions.md)
- [Cost guidance](docs/site/guides/cost.md)
- [Continuity guide](docs/site/guides/continuity.md)
- [Migration guide](docs/site/guides/migration.md)
- [Troubleshooting guide](docs/site/guides/troubleshooting.md)
- [Evidence handling](docs/site/guidance/evidence.md)
- [Assessment dashboard](docs/site/assessment-dashboard.md)

Repository authoring and automated validation are performed without Azure or Microsoft Graph access. No lab is labelled live-verified until a separately approved disposable-environment run completes its implementation path, validation, cleanup, and residual audit. See [SECURITY.md](SECURITY.md) and the [implementation report](IMPLEMENTATION-REPORT.md).

## License

Code and documentation are available under the [MIT License](LICENSE). Microsoft Azure and Entra icons remain subject to the separate terms recorded in [THIRD-PARTY-NOTICES.md](THIRD-PARTY-NOTICES.md).
