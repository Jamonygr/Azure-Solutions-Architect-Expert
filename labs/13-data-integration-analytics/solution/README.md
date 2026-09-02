<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-13 solution rationale

The recommended architecture is **Azure Data Factory with ADLS Gen2 and Azure Synapse serverless SQL** with a weighted total of 86/100. Data Factory handles governed batch and private connectivity while ADLS and serverless SQL minimize idle analytics capacity. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Microsoft Fabric Data Factory with OneLake and Fabric Warehouse:** The initial periodic workload does not yet justify moving every flow onto a Fabric capacity commitment.
- **Azure Databricks with Azure Data Factory orchestration and Delta Lake:** Its flexibility exceeds the transformation need and carries more platform ownership for this team.
- **Self-hosted scripts with embedded source passwords and no checkpoints:** It is ineligible because secretless access and recoverable lineage are mandatory.

## Risks and mitigations

- **Forcing hourly partner files through a streaming design can increase cost and duplicate late-arrival handling.** — Keep a batch contract for files and integrate its curated output into the shared semantic layer.
- **A Fabric preference can create capacity lock-in before private connectivity and throughput are proven.** — Benchmark the telemetry slice, record capacity utilization, and retain a reversible batch boundary for remaining flows.

## Initial Well-Architected consequences

- **reliability:** Watermarks, checkpoints, replay rules, and reconciliation distinguish recoverable batch and streaming failures.
- **security:** Managed identities and hardened private runtimes keep credentials out of pipeline definitions.
- **costOptimization:** Batch serverless processing and targeted Fabric capacity align spend with each flow's freshness requirement.
- **operationalExcellence:** Lineage, schema, watermark, and reconciliation evidence give operators a common failure model.
- **performanceEfficiency:** Near-real-time resources serve only the telemetry stream while hourly files retain efficient batch movement.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: Executives mandate near-real-time operational dashboards for one telemetry stream while partner files remain hourly and analysts prefer a unified Microsoft Fabric experience; revise the platform boundary without forcing every flow into streaming.

The revised decision is **Microsoft Fabric Data Factory with OneLake and Fabric Warehouse**. LAB13-REQ-01 requires integration patterns to follow cadence and source boundaries, so Fabric serves the near-real-time telemetry experience while partner files remain hourly batch. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Stream checkpoints and batch watermarks retain independent replay behavior.
- **security:** Private-source credentials remain protected even as curated output enters OneLake.
- **costOptimization:** Capacity is sized for the dashboard stream instead of converting every file flow to continuous processing.
- **operationalExcellence:** Shared lineage joins both cadences without erasing their distinct failure states.
- **performanceEfficiency:** Telemetry receives low-latency processing and partner files keep throughput-efficient hourly loads.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
