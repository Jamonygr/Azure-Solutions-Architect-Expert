<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-04 solution rationale

The recommended architecture is **Group-based Azure RBAC at stable scopes with Arc-aware local delegation** with a weighted total of 91/100. Stable groups decouple personnel churn from role definitions and Arc-aware local delegation avoids granting subscription networking rights. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Direct user assignments on individual resources and servers:** Assignment sprawl and person-by-person expiry weaken both auditability and operations.
- **Subscription-wide custom roles mirrored into local administrator groups:** The broad scope gives the provider capabilities beyond factory troubleshooting and complicates revocation.
- **Shared Owner account with permanent factory administrator membership:** The candidate is ineligible because standing shared privilege violates the provider boundary.

## Risks and mitigations

- **Azure role expiry may not remove a separately granted operating-system group membership.** — Reconcile cloud eligibility and Arc machine authorization as two explicit controls with the same end date.
- **An unavailable approver could delay urgent factory recovery.** — Assign a trained deputy, document emergency activation, and review every emergency use after the incident.

## Initial Well-Architected consequences

- **reliability:** Deputy approval and scoped emergency access preserve support during an identity-owner absence.
- **security:** Group eligibility, minimal scopes, and Arc-specific delegation remove standing subscription and local-admin privilege.
- **costOptimization:** Reusable groups reduce assignment administration while governance-license cost remains visible.
- **operationalExcellence:** Expiry, access reviews, and assignment exports provide one auditable provider offboarding sequence.
- **performanceEfficiency:** Stable group evaluation scales with personnel turnover without cloning role definitions per server.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: A managed-service provider must troubleshoot factory servers for ninety days but may not change subscription networking or receive permanent local administrator membership; revise delegation and expiry controls.

The revised decision is **Group-based Azure RBAC at stable scopes with Arc-aware local delegation**. LAB04-REQ-05 requires deterministic expiry and prohibited-network evidence, so the selected model adds ninety-day eligible group access plus independent Arc local-membership removal. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** A deputy activation route supports incidents without keeping access permanently active.
- **security:** Provider permissions end automatically and exclude subscription-network operations.
- **costOptimization:** Group-based renewal replaces repeated per-user assignment work.
- **operationalExcellence:** Cloud and server revocation assertions expose partial offboarding.
- **performanceEfficiency:** One stable role mapping supports the approved server fleet as technicians rotate.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
