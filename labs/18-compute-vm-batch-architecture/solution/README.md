<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-18 solution rationale

The recommended architecture is **Zonal control virtual machines with an autoscaled Azure Batch pool** with a weighted total of 87/100. Batch supplies queue, pool, task, and retry primitives while zonal control VMs protect orchestration and autoscale bounds worker spend. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Flexible Virtual Machine Scale Sets running custom queue workers:** Custom batch orchestration adds operating risk without a workload feature that requires it.
- **Dedicated zonal virtual machines scheduled for the nightly processing window:** Fixed nightly hosts respond less efficiently to queue variation and require more orchestration work.
- **Analyst desktops running jobs with local result files:** It is ineligible because local unmanaged execution violates the workload control boundary.

## Risks and mitigations

- **Dedicated node allocation may not ramp quickly enough to meet the shorter window.** — Measure allocation lead time, maintain approved quota headroom, and begin pool scale before the job release gate.
- **Export-controlled packages can leak through general-purpose storage or logs.** — Use run-owned private storage, minimal sanitized telemetry, approved images, and an explicit data-placement assertion.

## Initial Well-Architected consequences

- **reliability:** Zonal orchestration, durable task state, retry, and worker replacement keep the batch recoverable.
- **security:** Dedicated approved nodes, private data paths, and classified package handling enforce export controls.
- **costOptimization:** Autoscale removes dedicated workers after the five-hour batch while preserving justified control capacity.
- **operationalExcellence:** Queue depth, allocation, task failure, result integrity, and cleanup evidence provide one run ledger.
- **performanceEfficiency:** Measured task throughput and parallelism size dedicated capacity for the shortened completion window.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: Export-controlled simulations can no longer use low-priority capacity, and the processing window is shortened from eight hours to five.

The revised decision is **Zonal control virtual machines with an autoscaled Azure Batch pool**. LAB18-REQ-05 requires a five-hour export-controlled completion window, so Batch remains selected with dedicated-only nodes, quota headroom, and earlier scale-out. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Dedicated quota and pre-scaling reduce allocation uncertainty inside the batch window.
- **security:** No export-controlled task can land on low-priority or unapproved worker capacity.
- **costOptimization:** Dedicated nodes still scale to zero after results and ownership-checked cleanup complete.
- **operationalExcellence:** Allocation and queue timing become explicit go/no-go evidence before job submission.
- **performanceEfficiency:** Pool size derives from observed task throughput needed to compress eight hours into five.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
