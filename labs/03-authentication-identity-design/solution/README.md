<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-03 solution rationale

The recommended architecture is **Workforce tenant plus a dedicated External ID external tenant and managed identities** with a weighted total of 90/100. Separate workforce and external directories establish clear policy boundaries while managed identities remove application secrets from service access. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Single workforce tenant for employees partners and customers:** Its weak trust-boundary score outweighs the operational convenience of one directory.
- **Separate workforce tenants with custom application-managed customer credentials:** Custom customer credentials create avoidable security and lifecycle ownership that managed External ID provides.
- **New Azure AD B2C tenant storing patient profile attributes:** It is disqualified by both the current-service and data-boundary requirements.

## Risks and mitigations

- **Subject-to-profile mapping could expose health attributes in tokens or directory extension fields.** — Use an opaque subject key and assert that issued claims and external user objects contain no regulated fields.
- **Social identity-provider failure can prevent a customer cohort from signing in.** — Define provider-specific monitoring, recovery communication, and an approved alternate authentication journey.

## Initial Well-Architected consequences

- **reliability:** Separate populations and provider-aware journeys contain authentication failure to the affected trust path.
- **security:** External ID, minimal claims, managed identities, and isolated health profiles reduce credential and data exposure.
- **costOptimization:** Monthly-active-user billing and managed federation avoid funding custom password infrastructure.
- **operationalExcellence:** Lifecycle owners and journey-specific evidence make failed federation and provisioning easier to diagnose.
- **performanceEfficiency:** Tokens carry only authorization context and defer regulated profile retrieval to the workload data tier.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: A mobile patient application now requires native authentication and social federation while a regulator forbids health attributes from being stored in the customer directory; revise the journey and profile-data boundary.

The revised decision is **Workforce tenant plus a dedicated External ID external tenant and managed identities**. LAB03-REQ-03 makes the native and social authentication journey mandatory, so External ID is retained with opaque subject claims that never write health attributes to the directory. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Provider-specific fallback and monitoring isolate a social federation disruption.
- **security:** Opaque subject claims keep regulated data outside the external directory and tokens.
- **costOptimization:** Managed native authentication avoids developing and auditing a password service.
- **operationalExcellence:** Journey tests separately verify federation, token claims, and profile lookup.
- **performanceEfficiency:** Minimal tokens reduce sign-in payload and leave profile queries to the regional application store.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
