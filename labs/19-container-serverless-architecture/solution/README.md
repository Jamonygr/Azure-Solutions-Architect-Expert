<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-19 solution rationale

The recommended architecture is **Azure Container Apps for APIs and workers with Azure Functions for event handlers** with a weighted total of 84/100. Container Apps and Functions provide event-driven independent scaling, managed identity, revision controls, and low idle consumption. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Azure Kubernetes Service for every application component:** Universal AKS keeps an operational and cost baseline that conflicts with simple overnight scale-to-zero goals.
- **Azure App Service containers with WebJobs for all background processing:** Coupled plan capacity makes the short GPU burst and zero-idle API less efficient.
- **Public webhook functions with embedded registry and queue credentials:** It is ineligible because secretless durable intake is mandatory.

## Risks and mitigations

- **GPU capacity may be unavailable when a catastrophe causes the burst.** — Validate quota and regions, define a CPU degraded mode, and queue work without rejecting accepted claims.
- **Independent scaling can overwhelm a downstream claims database.** — Limit concurrency from observed database capacity and monitor queue age rather than scaling only on item count.

## Initial Well-Architected consequences

- **reliability:** Durable queues and independent component revisions keep intake available while scorers recover or scale.
- **security:** Managed identities, private registry access, and secret-free images reduce credential exposure.
- **costOptimization:** Intake and handlers scale to zero while GPU capacity exists only for the bounded risk-scoring interval.
- **operationalExcellence:** Revision, queue-age, retry, model, and dead-letter evidence separate deployment from workload failure.
- **performanceEfficiency:** Each component scales on its own demand signal and specialized GPU workers do not dictate API capacity.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: The risk-scoring worker now needs GPU acceleration for two hours after a catastrophe, but the intake API must still scale to zero overnight.

The revised decision is **Azure Container Apps for APIs and workers with Azure Functions for event handlers**. LAB19-REQ-05 requires both two-hour GPU scoring and overnight zero scale, so the selected design adds an approved GPU workload profile only for the scorer while intake remains event-driven. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Claims remain queued if GPU quota or model execution is temporarily unavailable.
- **security:** The GPU worker uses managed identity and the same private artifact boundary.
- **costOptimization:** Expensive accelerators are active only for the measured catastrophe backlog.
- **operationalExcellence:** GPU availability and CPU degraded mode are explicit runbook decisions.
- **performanceEfficiency:** Queue age and model throughput independently control the specialized worker profile.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
