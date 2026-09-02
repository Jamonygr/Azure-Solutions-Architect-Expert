<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-26 solution rationale

The recommended architecture is **Active-active regional PaaS stamps behind Front Door Premium with globally coordinated data services** with a weighted total of 96/100. PaaS stamps and Premium edge controls support independent regional release and routing while data services can be split by residency class. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Active-passive AKS clusters with database failover and a warm secondary region:** The platform does not need Kubernetes-specific control enough to justify its operational burden and slower passive activation.
- **Single-region modular PaaS platform with cross-region backups and rebuild automation:** Its recovery behavior misses the anonymous-catalog continuity outcome despite attractive economics.
- **One global customer-profile store replicated to every launch region:** It is ineligible because profile availability cannot override residency.

## Risks and mitigations

- **Anonymous responses can accidentally include profile-derived fields and enter the global cache or logs.** — Enforce separate contracts, classify fields, and assert that global responses and telemetry contain no profile attributes.
- **Active-active stamps can drift in policy, secret references, or feature configuration.** — Promote immutable Bicep and configuration versions and block release when regional evidence hashes differ.

## Initial Well-Architected consequences

- **reliability:** Independent stamps and global routing keep catalog service available through regional loss while honoring profile boundaries.
- **security:** Premium edge controls, private origins, managed identities, policy, and geography-scoped data reduce exposure.
- **costOptimization:** Shared global catalog capacity and market-specific profile stacks make continuity and residency spend attributable.
- **operationalExcellence:** Declarative releases, regional assertions, failover exercises, governance evidence, and rollback support fast controlled delivery.
- **performanceEfficiency:** Edge caching and regional PaaS autoscale serve anonymous demand while profile calls remain geography-local.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: A launch-market regulator now requires all customer profiles to remain in one geography, while anonymous catalog traffic must continue globally through a complete regional outage.

The revised decision is **Active-active regional PaaS stamps behind Front Door Premium with globally coordinated data services**. LAB26-REQ-01 requires mandatory constraints to drive the architecture decision, so active-active stamps split into geography-specific profile planes and a separate global anonymous catalog plane. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Anonymous catalog survives a regional loss without failing over restricted profile data unlawfully.
- **security:** Profile routes, stores, caches, and logs are constrained to the assigned geography.
- **costOptimization:** Global replication is purchased for catalog data, while profile capacity is funded per regulated market.
- **operationalExcellence:** Contract and routing assertions detect profile leakage before regional release.
- **performanceEfficiency:** Catalog requests use edge and nearest healthy stamp; profile calls remain within geography.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
