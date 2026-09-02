<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-01 solution rationale

The recommended architecture is **Regional workspaces with cross-workspace queries and policy-driven routing** with a weighted total of 93/100. Region-bound workspaces satisfy residency and isolate collection failure while DCR routing and cross-workspace views preserve a common operating experience. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Central Log Analytics workspace with DCR-based collection and archive export:** Its simpler operations do not compensate for weaker residency fit and a larger regional failure domain.
- **Dedicated workspace per workload with independent retention and access:** Workspace proliferation raises management and ingestion cost without improving the mandated regional boundary.
- **One global workspace retaining every stream interactively for seven years:** The candidate is disqualified by the regional security-record mandate.

## Risks and mitigations

- **A DCR association omission can create a silent telemetry gap for one workload or region.** — Reconcile source inventory to DCR and DCRA resource IDs and fail the coverage assertion for any unmatched source.
- **Cross-workspace permissions can expose regulated records to regional operators who need only application telemetry.** — Separate table access and workbook scopes, then test both an allowed query and a denied cross-boundary query.

## Initial Well-Architected consequences

- **reliability:** Independent regional ingestion limits correlated collection loss and makes partial query behavior explicit.
- **security:** Workspace and table boundaries enforce residency and least-privilege access for security evidence.
- **costOptimization:** Thirty-day trace search and archived audit retention align price with access frequency instead of duplicating streams.
- **operationalExcellence:** Policy-assigned DCRs and shared workbooks make coverage drift and incident handoffs observable.
- **performanceEfficiency:** Regional ingestion reduces collection paths, while scoped cross-workspace queries avoid scanning unrelated tables.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: A new regulator requires security control-plane records to remain in-region for seven years while application traces must stay searchable for only thirty days; revise routing and retention without duplicating every stream.

The revised decision is **Regional workspaces with cross-workspace queries and policy-driven routing**. LAB01-REQ-05 makes the seven-year in-region evidence boundary mandatory, so the regional-workspace decision is retained with archive retention for security tables and thirty-day trace search. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Each region keeps collecting its own control-plane stream during a remote workspace outage.
- **security:** Long-lived records never traverse the mandated regional boundary.
- **costOptimization:** Only the regulated stream receives seven-year retention and application traces remain thirty-day searchable.
- **operationalExcellence:** DCR and table-policy evidence reveals exactly which stream follows each rule.
- **performanceEfficiency:** Routine trace queries scan short-lived regional tables instead of the seven-year archive.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
