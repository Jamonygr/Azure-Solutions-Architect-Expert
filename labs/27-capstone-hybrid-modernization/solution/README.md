<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-27 solution rationale

The recommended architecture is **Dependency-wave modernization using Azure Arc, Azure Migrate patterns, managed PaaS targets, and staged coexistence** with a weighted total of 95/100. Dependency waves preserve rollback and evidence while Arc inventory, migration patterns, and PaaS targets support deliberate modernization by workload. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Parallel cloud rebuild followed by one enterprise-wide big-bang cutover:** The combined cutover cannot expose or contain failures by wave and leaves little credible rollback time.
- **Indefinite hybrid retention with lifecycle-only virtual machine rehosting:** It does not deliver the modernization outcome or transparent retirement economics.
- **Single-tenant big-bang migration with WAN-dependent branch order entry:** It is ineligible because it cannot preserve regulated separation or branch continuity.

## Risks and mitigations

- **Offline branches can generate conflicting order updates when centralized service continues processing.** — Use globally unique order identifiers, versioned commands, deterministic conflict policy, and an exception queue with business ownership.
- **Cross-tenant administration can create hidden shared identities or copy regulated evidence between geographies.** — Maintain separate identity and logging boundaries, broker only approved business messages, and test prohibited cross-tenant paths.

## Initial Well-Architected consequences

- **reliability:** Edge persistence, staged coexistence, dependency waves, and rollback contain WAN, workload, and migration failure.
- **security:** Tenant and geography boundaries, Arc governance, classified message contracts, and least privilege preserve regulatory separation.
- **costOptimization:** Wave business cases include coexistence and edge cost alongside eliminated facilities and managed-service value.
- **operationalExcellence:** Portfolio, dependency, sync, conflict, evidence, cutover, and residual-risk records make modernization governable.
- **performanceEfficiency:** Local branch writes avoid WAN latency and managed targets scale independently after each approved wave.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: A merger adds a second tenant, a separately regulated geography, and a hard requirement to keep branch order capture working for eight hours without WAN connectivity.

The revised decision is **Dependency-wave modernization using Azure Arc, Azure Migrate patterns, managed PaaS targets, and staged coexistence**. LAB27-REQ-04 requires deterministic continuity and security injects, so dependency waves add an eight-hour branch outbox plus distinct tenant and geography landing-zone boundaries. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Branch orders remain durable for eight hours and synchronize after WAN recovery.
- **security:** Tenant and geography planes exchange only classified, authorized business messages.
- **costOptimization:** Edge and dual-governance costs are visible against avoided branch outage and datacenter expense.
- **operationalExcellence:** Conflict queues, wave gates, rollback, and residual risk have named owners.
- **performanceEfficiency:** Local capture avoids WAN delay and post-recovery synchronization is paced to central capacity.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
