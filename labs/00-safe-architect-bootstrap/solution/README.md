<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-00 solution rationale

The recommended architecture is **Shared bootstrap contract with immutable run state and explicit execution gates** with a weighted total of 95/100. A state-first contract gives every copied lab the same recoverable boundary while explicit execution and acknowledgement gates remain locally testable. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Manual operator checklist without persisted state:** Its low recovery and operating scores leave no machine-verifiable record of returned identifiers.
- **Central automation account that executes every lab on behalf of learners:** The shared privilege boundary conflicts with isolated self-paced operation and adds an unnecessary control plane.
- **Untracked shell snippets with implicit cached credentials:** The candidate is ineligible because it violates the state-first mandatory boundary.

## Risks and mitigations

- **A malformed or reused RunId could merge evidence from unrelated exercises.** — Validate the RunId pattern and isolate every artifact beneath the exact run directory before command evaluation.
- **A future author could add a cloud command to a simulation checkpoint.** — Parse command surfaces in CI and force design-simulation lifecycle scripts to exit before context discovery.

## Initial Well-Architected consequences

- **reliability:** Atomic state replacement and resumable status values preserve an intelligible recovery point after interruption.
- **security:** Explicit tenant and subscription inputs eliminate reliance on cached identity context and sensitive fields are recursively rejected.
- **costOptimization:** An offline simulation produces the required evidence without standing cloud resources or idle automation accounts.
- **operationalExcellence:** One lifecycle contract, fixed exit codes, and schema-validated artifacts make faults reproducible across copied labs.
- **performanceEfficiency:** Local registry lookups and bounded JSON files avoid network latency and scale work only with the current run.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: Security now requires all labs to run from an isolated build worker. Revise the decision toward the shared bootstrap contract because its offline registries, state-first sequence, and explicit gates can be reproduced without tenant access.

The revised decision is **Shared bootstrap contract with immutable run state and explicit execution gates**. LAB00-REQ-01 now requires isolated-worker reproducibility, which the local registries, persisted state, and pre-context simulation gate satisfy without tenant access. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** The isolated worker can resume from the same run artifact after process loss.
- **security:** Removing cached-context discovery narrows the trust boundary to explicit inputs and local files.
- **costOptimization:** No central worker service or cloud resource must remain allocated between exercises.
- **operationalExcellence:** The frozen container becomes the single repeatable execution surface for release validation.
- **performanceEfficiency:** Dependency checks execute locally and avoid remote discovery round trips.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
