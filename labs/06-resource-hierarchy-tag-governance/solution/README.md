<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-06 solution rationale

The recommended architecture is **Archetype-based management groups with workload subscriptions and governed tags** with a weighted total of 92/100. Archetypes provide stable inheritance for platform, sandbox, and regulated workloads while subscription ownership preserves billing separation. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Management groups that mirror the corporate reporting hierarchy:** Organizational churn weakens policy stability and creates avoidable migration work.
- **One shared subscription with resource groups per application:** The model cannot preserve the subsidiary's required billing and administrator boundary at useful scope.
- **Resource-group-only tagging with no inherited policy boundary:** It is disqualified because metadata alone cannot enforce the mandatory hierarchy controls.

## Risks and mitigations

- **Existing assignments at lower scopes can conflict with or dilute new inherited policies.** — Export effective policy state, resolve conflicts in a canary subscription, and move subscriptions only after both assertions pass.
- **Tag inheritance can overwrite a valid workload-specific financial owner.** — Define precedence per tag key and test append, inherit, and deny behavior against representative resources.

## Initial Well-Architected consequences

- **reliability:** Stable archetypes keep critical guardrails attached through organizational change and subscription growth.
- **security:** Inherited security and European-location policies establish a consistent subsidiary boundary.
- **costOptimization:** Separate billing plus governed allocation tags makes shared and workload cost attributable.
- **operationalExcellence:** Versioned hierarchy, policy, and exemption records expose drift and simplify onboarding.
- **performanceEfficiency:** Management-group evaluation scales across subscriptions without duplicating assignments at every resource group.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: A regulated subsidiary must retain its own administrators and billing while inheriting enterprise security guardrails and keeping resources exclusively in approved European regions; revise hierarchy and tagging decisions.

The revised decision is **Archetype-based management groups with workload subscriptions and governed tags**. LAB06-REQ-01 requires the hierarchy to follow durable governance archetypes, so the subsidiary receives its own regulated branch beneath inherited European controls without mirroring reporting lines. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** The subsidiary keeps the same guardrails when its corporate reporting line changes.
- **security:** Approved-region and security initiatives inherit above the subsidiary subscription boundary.
- **costOptimization:** Billing remains directly attributable while shared services use governed allocation tags.
- **operationalExcellence:** A dedicated archetype documents onboarding, exemption, and administrator responsibilities.
- **performanceEfficiency:** One inherited policy set replaces repeated assignments across subsidiary workloads.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
