<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-22 solution rationale

The recommended architecture is **Cloud Adoption Framework outcome-led assessment and dependency-based waves** with a weighted total of 93/100. Outcome-led assessment joins readiness, value, dependency, governance, and measurable success before workloads enter waves. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Datacenter-by-datacenter rehost schedule based only on server age:** Server age is not a sufficient readiness or value measure and produces unsafe dependency cuts.
- **Application-team modernization projects without a shared portfolio assessment:** Uncoordinated projects cannot reliably satisfy the fixed lease exit or portfolio risk controls.
- **Move classified applications before encryption approval to preserve the lease schedule:** It is disqualified because lease pressure cannot override mandatory encryption approval.

## Risks and mitigations

- **The accelerated facility wave can strand an application whose dependency is blocked by classification review.** — Model temporary coexistence, dependency proxies, or an approved alternate hosting location before wave approval.
- **Outcome measures may be replaced by completion counts once schedule pressure rises.** — Keep value, reliability, cost, and risk measures in the wave exit gate alongside migrated-server count.

## Initial Well-Architected consequences

- **reliability:** Dependency-based waves, coexistence, and rollback protect service during portfolio transition.
- **security:** Classification and encryption evidence are hard gates rather than schedule-adjustable preferences.
- **costOptimization:** Lease avoidance, dual running, remediation, and target run cost are evaluated in one wave business case.
- **operationalExcellence:** Owners, decisions, readiness evidence, and outcome measures make wave approval reviewable.
- **performanceEfficiency:** Migration-factory capacity is allocated to ready waves instead of blocked or low-value server batches.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: The first datacenter lease now ends six months earlier, but the regulator prohibits moving two classified applications until encryption evidence is approved.

The revised decision is **Cloud Adoption Framework outcome-led assessment and dependency-based waves**. LAB22-REQ-04 requires dependency-safe waves and explicit readiness gates, so ready workloads advance for the lease exit while classified systems remain behind encryption approval. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Coexistence prevents an accelerated wave from severing blocked dependencies.
- **security:** Classified applications remain behind the encryption-evidence gate.
- **costOptimization:** Six months of facility cost is compared transparently with temporary hosting and acceleration expense.
- **operationalExcellence:** Revised wave decisions record owner, blocker, exit evidence, and outcome measure.
- **performanceEfficiency:** Migration teams focus on ready dependency groups instead of spending capacity on compliance-blocked systems.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
