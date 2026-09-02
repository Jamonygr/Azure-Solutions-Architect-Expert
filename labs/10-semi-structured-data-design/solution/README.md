<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-10 solution rationale

The recommended architecture is **Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning** with a weighted total of 88/100. Hierarchical partition keys distribute tenant and catalog access while preserving native document evolution and global service capabilities. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Azure Table Storage with denormalized entities and account-level scale:** Lower unit cost does not offset weaker global behavior and limited isolation for the dominant tenant.
- **Azure SQL Database with JSON columns and relational indexes:** It couples variable catalog structure to relational capacity and provides a less direct global partition model.
- **One fixed partition containing the entire catalog:** The proposal is disqualified because it cannot satisfy scale or tenant-isolation acceptance criteria.

## Risks and mitigations

- **A hierarchical key can still concentrate traffic if the leading tenant segment dominates requests.** — Measure normalized RU consumption and move the exceptional tenant to a dedicated container when the threshold is crossed.
- **Splitting a tenant can create inconsistent indexing or consistency policies across containers.** — Version a common container baseline and compare policy hashes before routing production traffic.

## Initial Well-Architected consequences

- **reliability:** Explicit region, consistency, and failover behavior protects accepted catalog changes beyond simple data distribution.
- **security:** Tenant-aware data roles and an optional dedicated container provide enforceable isolation boundaries.
- **costOptimization:** RU attribution and selective tenant separation avoid overprovisioning every catalog partition.
- **operationalExcellence:** Hot-partition, throttling, policy, and tenant-routing evidence supports repeatable scale decisions.
- **performanceEfficiency:** Hierarchical partitioning aligns common reads with physical distribution and isolates exceptional demand.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: One enterprise tenant grows to forty percent of all traffic and requires per-tenant cost attribution and data isolation; revise partition and container strategy without breaking other tenants.

The revised decision is **Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning**. LAB10-REQ-02 requires a partition strategy that mitigates an exceptionally large tenant, so Cosmos DB adds a dedicated container with independently attributable throughput. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Tenant separation contains throttling and partition pressure to the exceptional workload.
- **security:** A dedicated data-plane role and container scope strengthen enterprise-tenant isolation.
- **costOptimization:** Its provisioned or autoscale RU consumption is measured and charged independently.
- **operationalExcellence:** Versioned routing and policy checks prevent shared and dedicated containers from drifting.
- **performanceEfficiency:** The shared hierarchy stays balanced while the dominant tenant scales on its own ceiling.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
