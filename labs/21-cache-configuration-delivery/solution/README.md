<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-21 solution rationale

The recommended architecture is **Azure Managed Redis with Azure App Configuration and Bicep deployment stacks** with a weighted total of 95/100. Managed Redis accelerates catalog reads, App Configuration versions settings, and Bicep deployment stacks make regional release state declarative. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Per-instance memory caches with image-baked configuration and imperative scripts:** Inconsistent caches and baked settings undermine regional release consistency and degraded-mode proof.
- **Cosmos DB integrated cache with Key Vault references and Terraform delivery:** Coupling cache choice to a new database platform and delivery tool expands the decision without a requirement.
- **New Azure Cache for Redis deployment with mutable portal configuration:** It is disqualified by the current-service and declarative-delivery requirements.

## Risks and mitigations

- **A stale cache can serve a recalled or legally invalid catalog item for the full thirty-minute window.** — Define noncacheable emergency flags and a signed invalidation path independent of the source database.
- **Configuration refresh failure can leave regions on different feature versions.** — Pin a last-known-safe snapshot identifier and assert regional version convergence during every release.

## Initial Well-Architected consequences

- **reliability:** Versioned safe snapshots and cache fallback maintain catalog reads through configuration or source failure.
- **security:** Managed identities, private paths, and external secret references keep credentials out of images and templates.
- **costOptimization:** Cache capacity is tied to the measured working set and avoids scaling the source for repeated reads.
- **operationalExcellence:** Declarative stacks, configuration labels, snapshot versions, and rollback evidence control regional drift.
- **performanceEfficiency:** Managed Redis handles the read working set while refresh and invalidation protect data freshness.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: A regulatory review requires the storefront to keep serving last-known-safe catalog data for thirty minutes during configuration-store or source-database unavailability.

The revised decision is **Azure Managed Redis with Azure App Configuration and Bicep deployment stacks**. LAB21-REQ-01 requires explicit cache failure behavior, so the selected design retains a versioned thirty-minute last-known-safe snapshot plus a source-independent invalidation control. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Catalog reads continue through temporary configuration or database loss.
- **security:** Emergency invalidation is narrowly authorized and does not expose configuration secrets.
- **costOptimization:** Existing cache capacity supplies continuity without a duplicate active database.
- **operationalExcellence:** Snapshot version, activation, expiry, and recovery are recorded in the release runbook.
- **performanceEfficiency:** Bounded stale reads prevent dependency retry storms and protect storefront latency.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
