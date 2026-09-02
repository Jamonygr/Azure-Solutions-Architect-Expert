<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-23 solution rationale

The recommended architecture is **Azure Migrate plus Azure Database Migration Service and staged AzCopy transfer** with a weighted total of 91/100. Specialized migration paths preseed each workload type, preserve assessment and integrity evidence, and constrain final deltas. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Manual virtual machine rebuild plus database backup restore and one-time file copy:** The shortened window cannot absorb full database and engineering-file copies plus manual validation.
- **Partner replication appliance for all servers, databases, and files as one opaque unit:** Opaque replication weakens independent database, file, and VM acceptance even if transfer completes.
- **Unstaged live copy with no source rollback point:** It is ineligible because neither the ninety-minute window nor reversibility can be proven.

## Risks and mitigations

- **Engineering-file churn in the final fifteen minutes can exceed available transfer throughput.** — Measure change rate, journal final deltas, set a go/no-go threshold, and preserve source write logs for reconciliation.
- **A successful infrastructure cutover can hide database or file inconsistency.** — Run workload-specific row, checksum, and manufacturing transaction assertions before redirecting users.

## Initial Well-Architected consequences

- **reliability:** Preseeding, independent consistency checks, and preserved source rollback reduce cutover failure impact.
- **security:** Managed identities, private transfer paths, sanitized evidence, and least-privilege migration roles protect source data.
- **costOptimization:** Temporary replication and dual running are bounded to the period that buys a shorter controlled outage.
- **operationalExcellence:** Timed gates, owners, integrity results, redirection, and rollback criteria create an executable cutover record.
- **performanceEfficiency:** Only measured final deltas and validation remain inside the ninety-minute critical path.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: Plant leadership reduces the outage window from four hours to ninety minutes and requires engineering-file writes to continue until fifteen minutes before redirection.

The revised decision is **Azure Migrate plus Azure Database Migration Service and staged AzCopy transfer**. LAB23-REQ-05 requires a ninety-minute outage with writes continuing to minute fifteen, so staged services remain selected and only recorded deltas plus acceptance enter the critical path. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** A preserved source and explicit abort threshold keep the shortened event reversible.
- **security:** Final deltas travel through the same approved protected transfer boundary.
- **costOptimization:** Temporary staging cost avoids emergency bandwidth and extended factory downtime.
- **operationalExcellence:** Minute-by-minute gates expose when to continue, abort, or roll back.
- **performanceEfficiency:** Preseeded bulk data leaves a measured fifteen-minute write delta for final transfer.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
