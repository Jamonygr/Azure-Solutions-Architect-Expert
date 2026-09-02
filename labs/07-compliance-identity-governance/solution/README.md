<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-07 solution rationale

The recommended architecture is **Azure Policy initiatives plus Microsoft Entra ID Governance lifecycle controls** with a weighted total of 93/100. Policy evaluates resource state while access packages, reviews, and workflows assign accountable identity lifecycle decisions. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Azure Policy for resources with manual identity recertification:** Manual identity evidence cannot reliably prove quarterly owner action and timely revocation at scale.
- **Third-party GRC attestations with standing directory and Azure assignments:** The evidence system remains detached from enforcement and permits reviewed findings to stay active.
- **Permanent partner access with nonexpiring policy exemptions:** The approach is ineligible because neither partner access nor exemptions end deterministically.

## Risks and mitigations

- **A resource owner can ignore a review campaign until access is implicitly retained.** — Configure explicit denial or escalation behavior, named deputies, and an assertion for overdue decisions.
- **Policy exemptions can be recreated with a new identifier to evade the ninety-day limit.** — Query all effective exemptions by scope and owner, then flag overlapping replacements in the evidence ledger.

## Initial Well-Architected consequences

- **reliability:** Deputy reviewers and deterministic campaign outcomes prevent governance from stalling on one unavailable owner.
- **security:** Expiring access packages and exemptions reduce standing privilege and policy bypass duration.
- **costOptimization:** Automated recurring evidence replaces manual quarterly reconciliation while license scope remains explicit.
- **operationalExcellence:** One trace joins policy state, review decisions, revocation, owners, and escalation timestamps.
- **performanceEfficiency:** Campaign scoping and incremental compliance queries avoid reevaluating unrelated identities and resources.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: A regulator now requires quarterly evidence that external partner access was reviewed by the resource owner and that every exemption expired within ninety days; revise evidence flow and escalation.

The revised decision is **Azure Policy initiatives plus Microsoft Entra ID Governance lifecycle controls**. LAB07-REQ-04 requires recurring owner-attributed access review, so linked Policy and Entra governance evidence adds quarterly partner decisions alongside independently bounded ninety-day exemptions. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Deputy review and escalation prevent a campaign from failing because one owner is absent.
- **security:** Access and exemptions terminate automatically when their approved period ends.
- **costOptimization:** Targeted licensed governance replaces broad manual evidence collection.
- **operationalExcellence:** Correlated timestamps demonstrate review, expiry, revocation, and escalation outcomes.
- **performanceEfficiency:** Owner-scoped campaigns limit review volume and focus compliance queries on exceptions.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
