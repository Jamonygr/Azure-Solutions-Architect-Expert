<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-11 solution rationale

The recommended architecture is **ADLS Gen2 on a hierarchical-namespace StorageV2 account** with a weighted total of 92/100. ADLS Gen2 provides object-scale analytics, directory-aware ACLs, and integration with the governed data pipeline. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Flat Azure Blob Storage containers with prefix conventions:** It weakens analytics namespace governance without solving the legal SMB requirement.
- **Azure Files shares mounted by analytics and document clients:** A universal share imposes the wrong access pattern and cost model on the analytics estate.
- **One unmanaged file server for lake ingestion and legal collaboration:** It is ineligible because the analytics access and scale requirements cannot be met.

## Risks and mitigations

- **Users can copy regulated legal documents into the analytics lake and bypass share controls.** — Classify ingress, deny unapproved paths, and reconcile file manifests across the two ownership boundaries.
- **Private endpoint or DNS configuration can work for Blob while failing for File.** — Validate each service subresource and protocol independently from every authorized network zone.

## Initial Well-Architected consequences

- **reliability:** Independent redundancy, snapshots, and replay paths match the failure behavior of lake objects and collaborative files.
- **security:** ACLs, service-specific private endpoints, and classified ingress keep legal and analytics data in distinct trust boundaries.
- **costOptimization:** SMB-priced capacity is reserved for collaboration and lower-cost object tiers serve analytics retention.
- **operationalExcellence:** Separate owners, inventories, lifecycle rules, and restore assertions prevent protocol ambiguity.
- **performanceEfficiency:** Object-native parallelism serves analytics while Azure Files supplies locking and metadata behavior for users.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: The legal department introduces collaborative document shares that require native SMB locking and Windows ACL behavior, but analytics ingestion must remain object-native; revise the service boundaries.

The revised decision is **ADLS Gen2 on a hierarchical-namespace StorageV2 account**. LAB11-REQ-01 requires service semantics to match access patterns, so ADLS remains the object-analytics decision and Azure Files is added only for native SMB legal collaboration. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Each service uses recovery controls suited to its protocol and business owner.
- **security:** Transfers between legal shares and the lake become explicit classified operations.
- **costOptimization:** File-service charges apply only to documents that need SMB semantics.
- **operationalExcellence:** Separate inventories and restore tests remove ambiguity about ownership and recovery.
- **performanceEfficiency:** Analytics avoids SMB overhead and legal users retain native locking behavior.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
