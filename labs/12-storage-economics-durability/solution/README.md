<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-12 solution rationale

The recommended architecture is **StorageV2 with GZRS and class-specific lifecycle policies** with a weighted total of 90/100. StorageV2 combines regional durability with data-class lifecycle rules and supports a dedicated immutable evidence boundary. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **StorageV2 with LRS and application-managed secondary copies:** The custom secondary lacks the managed regional durability and auditable behavior required by evidence classes.
- **Premium block blob accounts with uniform online retention:** Uniform premium retention ignores different retrieval and deletion requirements and produces the weakest cost fit.
- **One mutable hot-tier container with manual seven-year deletion reminders:** The candidate is disqualified because procedural intent is not an immutable storage control.

## Risks and mitigations

- **An incorrect data-class tag can archive active media or leave audit evidence mutable.** — Validate classification at ingestion and run policy simulations against representative objects before activation.
- **Locked immutability can preserve erroneous or sensitive content for seven years.** — Establish legal approval, narrow the immutable container, and test content validation before final locking.

## Initial Well-Architected consequences

- **reliability:** GZRS and per-class recovery tests protect durability without confusing immutability with availability.
- **security:** Locked audit containers, least-privilege data roles, and private access preserve evidence integrity.
- **costOptimization:** Lifecycle timing follows actual retention and retrieval behavior for media and audit classes.
- **operationalExcellence:** Classification, policy simulation, lock approval, and exception evidence form a controlled lifecycle process.
- **performanceEfficiency:** Hot access remains available for active media while cold evidence uses capacity-efficient tiers.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: Audit packages become subject to a seven-year immutable retention mandate while media can be deleted after eighteen months; revise account, container, lifecycle, and cost boundaries.

The revised decision is **StorageV2 with GZRS and class-specific lifecycle policies**. LAB12-REQ-05 requires enforceable seven-year immutability and eighteen-month media deletion, so class-specific GZRS boundaries are retained with a separately locked audit container. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Regional redundancy remains independent from the immutable evidence control.
- **security:** Audit objects cannot be altered or deleted by ordinary storage administrators.
- **costOptimization:** Media exits storage at eighteen months while long-lived evidence uses an intentional tier.
- **operationalExcellence:** Lock approval and lifecycle simulation become required release evidence.
- **performanceEfficiency:** Active media avoids archive delay and rarely read audit packages avoid premium capacity.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
