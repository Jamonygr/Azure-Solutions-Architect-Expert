<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-15 solution rationale

The recommended architecture is **Zone-spread virtual machine scale sets with Azure Backup and isolated restore** with a weighted total of 93/100. Zone-spread compute covers datacenter loss and Azure Backup supplies protected recovery points for a controlled quarantined restore. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Availability sets with locally redundant vault protection:** It does not meet the datacenter-failure requirement as directly as zone-spread placement.
- **Azure Site Recovery warm replicas in a secondary region for every virtual machine:** Uniform replication exceeds the lab budget and does not replace immutable clean recovery points.
- **In-place production restore over the suspected virtual machines:** It is disqualified because a trusted isolated-restore boundary is mandatory.

## Risks and mitigations

- **Excluding three recovery points may leave no point inside the two-hour transfer and validation window.** — Increase protected-point frequency or pre-stage isolated restore capacity after measuring older-point restore duration.
- **A zone-spread VM set can still depend on a single-zone database or ingress component.** — Map and assert every upstream dependency's failure domain before accepting the compute availability result.

## Initial Well-Architected consequences

- **reliability:** Zone placement, backup coverage, clean-point selection, and dependency-aware startup address distinct failure modes.
- **security:** Immutable recovery points and quarantined validation prevent compromised machines from rejoining automatically.
- **costOptimization:** Permanent capacity covers zonal availability while secondary-region and restore resources remain risk-based.
- **operationalExcellence:** Timed restore, forensic approval, transaction checks, and rollback form one rehearsable recovery record.
- **performanceEfficiency:** SKU and degraded-capacity evidence ensure surviving zones and restore hosts can process the clinical load.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: Security now requires a known-clean restore to be available within two hours even when the latest three recovery points are considered suspect.

The revised decision is **Zone-spread virtual machine scale sets with Azure Backup and isolated restore**. LAB15-REQ-04 makes isolated trusted recovery mandatory, so the selected design adds enough immutable points and prevalidated quarantine capacity to reject three suspect copies and finish within two hours. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** A deeper point set and measured restore throughput protect the two-hour target.
- **security:** Forensic rejection and quarantine remain gates before any production reconnection.
- **costOptimization:** Temporary restore capacity is funded instead of a full permanent secondary estate.
- **operationalExcellence:** Exercises record selection, transfer, validation, approval, and rollback timestamps.
- **performanceEfficiency:** Prevalidated restore sizing avoids discovering disk-throughput limits during a cyber event.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
