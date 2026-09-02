<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-02 solution rationale

The recommended architecture is **Service-centric alerts with shared action groups and curated workbooks** with a weighted total of 89/100. SLO-oriented multi-signal alerts correlate customer impact, dependency state, and deployment context while reusable action groups control routing. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Resource-by-resource static thresholds with team-specific receivers:** It scores poorly on operability because duplicated thresholds and receiver lists drift independently.
- **External monitoring only with Azure telemetry exported downstream:** Export-only detection adds latency and makes Azure-native dependency and deployment context harder to preserve.
- **One fixed latency threshold copied to every resource:** It is ineligible because it cannot meet the independent alert-quality acceptance criteria.

## Risks and mitigations

- **Dynamic thresholds may learn a promotion spike and suppress a genuine payment-path failure.** — Combine demand-aware baselines with an invariant failed-transaction or availability SLO signal.
- **A shared action group can become a single notification dependency.** — Configure and exercise independent receiver types, then retain delivery-status evidence for each route.

## Initial Well-Architected consequences

- **reliability:** Multi-signal service alerts detect degraded customer outcomes even when individual resources report healthy.
- **security:** Least-privilege action-group maintenance and sanitized alert payloads limit exposure through notification channels.
- **costOptimization:** Curated rules reduce duplicate evaluations and the labor cost of unactionable pages.
- **operationalExcellence:** Workbooks join SLO, dependency, deployment, and alert evidence into one triage sequence.
- **performanceEfficiency:** Demand-relative thresholds absorb planned bursts while invariant failure signals protect sensitivity.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: The payment API adopts a bursty promotion model that triples legitimate traffic for fifteen minutes, so static latency and error-rate thresholds must be revised without masking genuine customer impact.

The revised decision is **Service-centric alerts with shared action groups and curated workbooks**. LAB02-REQ-03 requires an auditable customer-impact query, so the promotion case uses demand-relative latency evaluation plus an invariant failure-rate signal rather than a static resource threshold. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Two independent signals prevent a benign traffic surge from hiding a true outage.
- **security:** Receiver scopes and payload fields remain unchanged while alert logic evolves.
- **costOptimization:** Noise suppression avoids a threefold burst producing redundant pages and log queries.
- **operationalExcellence:** Promotion annotations give responders an auditable reason for changed baselines.
- **performanceEfficiency:** Multi-window evaluation reflects short bursts without permanently raising the latency threshold.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
