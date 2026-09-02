<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-08 solution rationale

The recommended architecture is **Azure SQL Database General Purpose serverless** with a weighted total of 91/100. Before the acquired dependency is known, serverless SQL Database best matches intermittent load and minimizes platform administration. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Azure SQL Managed Instance General Purpose:** Its initial cost is not justified until SQL Agent and instance-level dependencies become mandatory.
- **Azure Database for PostgreSQL Flexible Server General Purpose:** Engine migration risk is unnecessary for an application whose discovered dependencies remain SQL Server specific.
- **Larger Azure SQL Database tier without compatibility remediation:** The candidate is disqualified because scaling cannot repair a platform compatibility gap.

## Risks and mitigations

- **Compatibility tooling can miss runtime jobs or infrequently used cross-database paths.** — Reconcile assessment output with SQL Agent history, dependency telemetry, and an owner-signed feature inventory.
- **Managed Instance baseline cost may exceed the modernization budget during idle periods.** — Size from measured month-end and ordinary load, apply license benefits where eligible, and expose the fixed-cost delta.

## Initial Well-Architected consequences

- **reliability:** Managed database high availability and tested rollback protect transactions during platform and migration failure.
- **security:** Private access, managed identity where supported, encryption, and least-privilege database roles remain target requirements.
- **costOptimization:** Compute model follows measured utilization while compatibility prevents false savings that reappear as remediation work.
- **operationalExcellence:** Compatibility findings, cutover gates, and post-migration assertions make the target decision auditable.
- **performanceEfficiency:** Month-end benchmarks and workload-specific sizing replace an assumption that a larger tier fixes incompatibility.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: The acquired application reveals a hard dependency on SQL Agent, cross-database transactions, and instance-level collation; revise the platform choice without treating a larger SQL Database tier as compatibility.

The revised decision is **Azure SQL Managed Instance General Purpose**. LAB08-REQ-05 makes SQL Agent, cross-database transactions, and instance collation mandatory, so compatibility overrides the initial serverless score and selects Managed Instance. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Managed Instance retains managed high availability while avoiding unsupported job and transaction workarounds.
- **security:** The target still requires private networking and least-privilege database administration.
- **costOptimization:** Higher baseline compute is accepted and must be offset with measured sizing and eligible license benefits.
- **operationalExcellence:** Existing Agent jobs and instance behaviors move into a supported managed operating model.
- **performanceEfficiency:** Capacity is benchmarked for both ordinary and month-end demand after compatibility is established.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
