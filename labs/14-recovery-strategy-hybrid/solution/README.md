<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-14 solution rationale

The recommended architecture is **Tiered recovery using Azure Backup, Azure Site Recovery, and application-native replication** with a weighted total of 91/100. Tiering maps recovery technology and retained capacity to business targets while keeping residency and dependency decisions explicit. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Uniform paired-region warm standby for every business service:** It spends continuously on workloads that tolerate slower recovery and weakens residency fit.
- **Active-active deployment across two Azure regions with independent factory edges:** Its cost and operational complexity exceed most tiers and do not inherently solve residency constraints.
- **Untested backup-only plan with no dependency or business validation:** It is disqualified because restore media alone cannot satisfy end-to-end recovery evidence.

## Risks and mitigations

- **Shared identity or network dependencies can consume most of the forty-five-minute Tier 1 window.** — Place prerequisites in recovery wave zero, assign decision timestamps, and measure their degraded-mode startup independently.
- **Warm in-boundary capacity can sit idle and be removed during cost optimization.** — Tag the capacity to the Tier 1 objective, include it in exercises, and report its cost as an explicit resilience control.

## Initial Well-Architected consequences

- **reliability:** Dependency waves and tier-specific mechanisms align recovery behavior with validated business targets.
- **security:** Residency, privileged recovery identities, and isolated evidence remain explicit in every recovery pattern.
- **costOptimization:** Warm capacity is limited to Tier 1 while slower tiers use lower-cost protection that meets their objectives.
- **operationalExcellence:** Timed authority, technical, communication, and business gates expose where recovery actually spends time.
- **performanceEfficiency:** Degraded-mode sizing reserves enough in-boundary capacity for Tier 1 without duplicating peak capacity everywhere.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: The board reduces the Tier 1 RTO from four hours to forty-five minutes while prohibiting any additional cross-border data replication.

The revised decision is **Tiered recovery using Azure Backup, Azure Site Recovery, and application-native replication**. LAB14-REQ-05 now requires a forty-five-minute Tier 1 recovery without cross-border replication, so tiering is retained with warm capacity inside the approved geography and faster orchestration gates. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Warm Tier 1 capacity removes provisioning from the critical recovery path.
- **security:** Data remains within the approved geography and emergency identities stay time-bound.
- **costOptimization:** Only Tier 1 carries the new standby premium.
- **operationalExcellence:** Shorter authority and dependency gates require more frequent timed exercises.
- **performanceEfficiency:** Degraded-mode capacity is sized to the recovery load rather than ordinary peak demand.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
