<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-09 solution rationale

The recommended architecture is **Azure SQL Database Hyperscale with named read-scale replicas** with a weighted total of 89/100. Hyperscale decouples storage growth from named read replicas and supports intentional routing of tenant reporting load. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Azure SQL Database elastic pool partitioned by tenant:** Pool partitioning does not match the shared ledger model as cleanly and increases operational fragmentation.
- **Azure SQL Managed Instance Business Critical:** The design pays for broad instance capability that the ledger does not require and weakens tenant-specific attribution.
- **One vertically scaled database with no read routing or tenant telemetry:** It is ineligible because it cannot isolate the burst or prove tenant cost attribution.

## Risks and mitigations

- **A named replica can lag and return stale ledger projections during a burst.** — Route only approved read workloads, measure replica delay, and fall back to the primary when freshness exceeds the contract.
- **Tenant labels in telemetry may be inconsistent and produce disputed chargeback.** — Validate the tenant dimension at ingress and reconcile replica/query usage against the authoritative tenant registry.

## Initial Well-Architected consequences

- **reliability:** Primary writes, read routing, backup recovery, and regional continuity are validated as distinct mechanisms.
- **security:** Encryption, auditing, and tenant-aware access remain mandatory across primary and replica endpoints.
- **costOptimization:** Named burst capacity and query telemetry make the exceptional tenant's demand attributable.
- **operationalExcellence:** Replica lag, routing, protection, and audit evidence share one tenant-labeled operating view.
- **performanceEfficiency:** Read replicas absorb unpredictable reporting load without scaling the transactional primary for every burst.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: A new tenant produces unpredictable read bursts but contributes little write load and requires strict cost attribution; revise replica and tenancy decisions without weakening encryption or audit controls.

The revised decision is **Azure SQL Database Hyperscale with named read-scale replicas**. LAB09-REQ-02 makes read-workload isolation mandatory, so Hyperscale is retained with a named replica and routing policy dedicated to the bursty tenant's attributable reads. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Freshness checks keep stale replica results from silently entering ledger workflows.
- **security:** The tenant replica preserves encryption, audit, and authorization controls from the primary design.
- **costOptimization:** Dedicated replica hours and queries can be assigned to the tenant that creates them.
- **operationalExcellence:** Tenant-tagged lag and routing telemetry expose when fallback to the primary occurs.
- **performanceEfficiency:** Bursty reads scale independently while write capacity remains sized for actual ledger traffic.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
