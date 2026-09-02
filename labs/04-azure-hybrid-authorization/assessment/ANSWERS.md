<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-04 answer key

Use after completing the learner assessment. Every choice has a specific explanation.

## LAB04-Q01 — answer D

An assurance review of 'Model scopes and inherited access' includes internal audit. Approval requires a positive result plus this independent negative assertion: No individual user holds standing Owner at the reviewed production scope. Which response meets the need for the acceptance rule that makes LAB04-REQ-01 testable?

- ✗ **A. Select Direct user assignments on individual resources and servers before checking Model scopes and inherited access; next, take it as conclusive that a successful deployment will later prove the architecture constraint.** — The architecture evidence must show that no individual user holds standing Owner at the reviewed production scope. That evidence means a deployment result cannot prove LAB04-REQ-01, and Direct user assignments on individual resources and servers still has to meet the mandatory boundary.
- ✗ **B. Use the passing result from Delegate through groups rather than people to approve Model scopes and inherited access. In addition, treat it as established that one control establishes an unrelated acceptance boundary.** — The applicable design condition is that the operating team receives resource-group Contributor through an owned Microsoft Entra group. That evidence means that outcome belongs to Delegate through groups rather than people and leaves Model scopes and inherited access unverified.
- ✗ **C. Choose Subscription-wide custom roles mirrored into local administrator groups and skip the Model scopes and inherited access negative assertion; before approval, use as justification the claim that the candidate has the lowest implementation effort.** — The review is governed by this fact: reduce standing privilege and audit ambiguity without preventing platform and factory teams from meeting support obligations. That evidence means implementation effort cannot justify skipping the negative assertion or displace LAB04-REQ-01.
- ✓ **D. Require the documented positive state for Model scopes and inherited access. Also, verify that no individual user holds standing Owner at the reviewed production scope.** — The scenario makes clear that stable management scopes and group assignments explain both direct and inherited effective access. That evidence means the positive state and an independent negative assertion jointly make LAB04-REQ-01 testable.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q02 — answer D

Approval of 'Model scopes and inherited access' is questioned by cloud platform owner. The selected architecture is Group-based Azure RBAC at stable scopes with Arc-aware local delegation; object existence alone is not success. Which choice should be approved as the intended successful finding?

- ✗ **A. Use only the negative assertion 'No individual user holds standing Owner at the reviewed production scope' as the success result; before approval, treat as decisive the assertion that absence proves every required positive property.** — The decision tension comes from the fact that no individual user holds standing Owner at the reviewed production scope. That evidence means this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Constrain a custom control-plane role as the result for Model scopes and inherited access. Then, base approval on the claim that a property from the current checkpoint does not need to be inspected.** — The safe operating boundary says that the custom role contains only documented support actions and the minimum assignable scopes. That evidence means evidence for Constrain a custom control-plane role cannot substitute for the properties required at Model scopes and inherited access.
- ✗ **C. Record the failure condition 'A broad inherited assignment masks the intended resource-group delegation' as a successful state; afterward, use the premise that the command returned an object.** — The traceable checkpoint outcome is that a broad inherited assignment masks the intended resource-group delegation. That evidence means resource existence or command output does not convert the documented failure condition into success.
- ✓ **D. Record stable management scopes and group assignments explain both direct and inherited effective access. Afterward, classify it as success for LAB04-REQ-01.** — The retained result must be reconciled with the fact that stable management scopes and group assignments explain both direct and inherited effective access. That evidence means this is the authored target state for Model scopes and inherited access and directly supports LAB04-REQ-01.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q03 — answer B

The implementation review has reached 'Model scopes and inherited access'. Evidence must address this risk without retaining credentials: A broad inherited assignment masks the intended resource-group delegation. What should the team use as sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Separate control-plane and data-plane access for Model scopes and inherited access. Also, accept without proof that a related checkpoint proves the current expected state.** — The recovery guidance assumes that synthetic workload principal, data-plane role, exact vault scope, and denied management operations. That evidence means that evidence supports Separate control-plane and data-plane access, so it cannot demonstrate Stable management scopes and group assignments explain both direct and inherited effective access.
- ✓ **B. Retain synthetic principal labels, role names, assignment scopes, inheritance path, and business owner. Separately, exclude credentials and unrelated response fields.** — The failure model establishes that synthetic principal labels, role names, assignment scopes, inheritance path, and business owner. That evidence means it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **C. Store unredacted Model scopes and inherited access output with operator, tenant, token, and request context; in a separate step, rely on the claim that reproduction requires every captured field.** — The WAF consequence identifies that unredacted implementation output. That evidence means identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **D. Record only the Model scopes and inherited access positive inspection's exit status. As another control, rely on the belief that projected properties and assertion results can be reconstructed later.** — The command-level assertion is anchored in the fact that the positive inspection's exit status. That evidence means an exit code alone does not show whether stable management scopes and group assignments explain both direct and inherited effective access.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q04 — answer A

The approach to 'Model scopes and inherited access' is challenged by security assurance. The target is Stable management scopes and group assignments explain both direct and inherited effective access, but the latest evidence does not show it. Which option best establishes the most likely cause?

- ✓ **A. Investigate a broad inherited assignment masks the intended resource-group delegation; as a second control, isolate that cause before changing Group-based Azure RBAC at stable scopes with Arc-aware local delegation.** — a broad inherited assignment masks the intended resource-group delegation. The resulting architectural conclusion is that it is the checkpoint's causal failure model and should be isolated before retrying Model scopes and inherited access.
- ✗ **B. Treat 'Teams conflate Arc resource management with guest configuration or local sign-in rights' as grounds to reject Model scopes and inherited access; before approval, consider it sufficient that define the Azure Arc authorization boundary's failure model applies unchanged here.** — The controlling fact is that teams conflate Arc resource management with guest configuration or local sign-in rights. The resulting architectural conclusion is that that condition belongs to Define the Azure Arc authorization boundary and does not by itself invalidate Group-based Azure RBAC at stable scopes with Arc-aware local delegation.
- ✗ **C. Ignore the negative assertion 'No individual user holds standing Owner at the reviewed production scope'. Separately, take it as conclusive that a later material change will make it unnecessary.** — The authored acceptance boundary states that no individual user holds standing Owner at the reviewed production scope. The resulting architectural conclusion is that the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Delegate through groups rather than people instead of diagnosing Model scopes and inherited access; for this decision, treat it as established that a passing result at Delegate through groups rather than people identifies the current cause.** — The relevant observation is that the operating team receives resource-group Contributor through an owned Microsoft Entra group. The resulting architectural conclusion is that a passing result at Delegate through groups rather than people gives no causal evidence for the failure at Model scopes and inherited access.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q05 — answer C

A decision test for 'Model scopes and inherited access' includes internal audit. The run encountered this modeled failure: A broad inherited assignment masks the intended resource-group delegation. Which answer identifies the safest recovery action?

- ✗ **A. Perform cleanup immediately: Remove child assignments before groups only when exact run-owned IDs and tags are proven; afterward, proceed on the belief that the failed operation and its returned identifiers do not need reconciliation.** — The scenario makes clear that remove child assignments before groups only when exact run-owned IDs and tags are proven. The resulting architectural conclusion is that cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **B. Create a different run identity before diagnosing 'A broad inherited assignment masks the intended resource-group delegation'; then treat as decisive the assertion that the first state record and returned identifiers can be discarded.** — The architecture evidence must show that a broad inherited assignment masks the intended resource-group delegation. The resulting architectural conclusion is that discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✓ **C. Trace the assignment to its parent scope and redesign at the narrowest stable boundary. Independently, preserve the current run identity and evidence.** — The checkpoint specifically records that trace the assignment to its parent scope and redesign at the narrowest stable boundary. The resulting architectural conclusion is that it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **D. Change Delegate through groups rather than people instead. Independently, base approval on the claim that success at Delegate through groups rather than people will repair the failed state at Model scopes and inherited access.** — The applicable design condition is that the operating team receives resource-group Contributor through an owned Microsoft Entra group. The resulting architectural conclusion is that altering an already separate checkpoint does not repair the modeled failure at Model scopes and inherited access.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q06 — answer D

The architecture board reconsiders 'Model scopes and inherited access' with cloud platform owner. Without making a new change, the team must inspect the risk 'A broad inherited assignment masks the intended resource-group delegation' using the Azure CLI lane. What recommendation gives the reviewers the read-only, lane-correct inspection?

- ✗ **A. Rerun the Model scopes and inherited access implementation command and infer the expected state. As another control, use as justification the claim that absence of a shell error proves every property.** — The retained result must be reconciled with the fact that the implementation command. The resulting architectural conclusion is that it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Model scopes and inherited access: No individual user holds standing Owner at the reviewed production scope; as a separate check, accept without proof that an empty negative result reports every required positive property.** — The decision tension comes from the fact that the negative inspection. The resulting architectural conclusion is that absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **C. Run the positive inspection for Constrain a custom control-plane role and apply it to Model scopes and inherited access. Afterward, rely on the claim that any command from the same lane proves the current checkpoint.** — The safe operating boundary says that the positive inspection for Constrain a custom control-plane role. The resulting architectural conclusion is that it is lane-correct but proves Constrain a custom control-plane role, not Model scopes and inherited access.
- ✓ **D. Inspect the documented properties for Model scopes and inherited access; in a separate step, retain this evidence: synthetic principal labels, role names, assignment scopes, inheritance path, and business owner.** — The review is governed by this fact: stable management scopes and group assignments explain both direct and inherited effective access. The resulting architectural conclusion is that the read-only inspection directly tests the properties required at Model scopes and inherited access.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q07 — answer B

A review of 'Model scopes and inherited access' begins with input from factory operations. A passing positive check does not by itself prove this negative assertion: No individual user holds standing Owner at the reviewed production scope. Which action produces the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Model scopes and inherited access and report full compliance; for this decision, use the premise that every prohibited parallel state must therefore be absent.** — The failure model establishes that stable management scopes and group assignments explain both direct and inherited effective access. The resulting architectural conclusion is that the positive result alone does not test the explicit anti-condition 'No individual user holds standing Owner at the reviewed production scope'.
- ✓ **B. Verify the positive properties for Model scopes and inherited access; next, independently verify that no individual user holds standing Owner at the reviewed production scope.** — The traceable checkpoint outcome is that stable management scopes and group assignments explain both direct and inherited effective access; No individual user holds standing Owner at the reviewed production scope. The resulting architectural conclusion is that two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **C. Prove only that no individual user holds standing Owner at the reviewed production scope and report the intended configuration as present. Before sign-off, consider it sufficient that absence is equivalent to positive-state evidence.** — The recovery guidance assumes that no individual user holds standing Owner at the reviewed production scope. The resulting architectural conclusion is that absence evidence cannot demonstrate the required positive state 'Stable management scopes and group assignments explain both direct and inherited effective access'.
- ✗ **D. Use Separate control-plane and data-plane access's negative assertion for Model scopes and inherited access; as an independent condition, take it as conclusive that negative assertions are interchangeable between checkpoints.** — The WAF consequence identifies that the workload receives neither Owner nor Contributor at the vault or a parent scope. The resulting architectural conclusion is that the second assertion is valid for Separate control-plane and data-plane access but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q08 — answer B

'Model scopes and inherited access' awaits approval from security assurance. The board wants the Well-Architected consequence of mitigating this risk: A broad inherited assignment masks the intended resource-group delegation. What best demonstrates the consequence attributable to this checkpoint?

- ✗ **A. Use the Define the Azure Arc authorization boundary consequence as the result for Model scopes and inherited access. Independently, rely on the belief that a pillar statement remains valid when moved away from Define the Azure Arc authorization boundary.** — security: the hybrid boundary prevents Azure control-plane access from being mistaken for guest administrator privilege. Under the stated constraint, that tradeoff belongs to Define the Azure Arc authorization boundary and does not explain this checkpoint's decision.
- ✓ **B. Record this consequence: Operational Excellence: an explicit inheritance map makes effective access reviewable and supportable; for this decision, tie it to LAB04-REQ-01.** — The command-level assertion is anchored in the fact that operational Excellence: an explicit inheritance map makes effective access reviewable and supportable. The resulting architectural conclusion is that it states the authored pillar consequence of the control evaluated at Model scopes and inherited access.
- ✗ **C. Remove the control responsible for the Model scopes and inherited access outcome. Next, proceed on the belief that a low cost classification outweighs the mandatory architecture state.** — The controlling fact is that the required outcome at Model scopes and inherited access. Under the stated constraint, cost Optimization cannot remove the acceptance condition 'Stable management scopes and group assignments explain both direct and inherited effective access'.
- ✗ **D. Treat 'Operational Excellence: an explicit inheritance map makes effective access reviewable and supportable' as proof that all five pillars pass, and then treat as decisive the assertion that the checkpoint 'Model scopes and inherited access' no longer needs its separate negative check.** — The authored acceptance boundary states that no individual user holds standing Owner at the reviewed production scope. Under the stated constraint, one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q09 — answer B

'Model scopes and inherited access' is reopened at the request of internal audit. A material change now applies: A managed-service provider must troubleshoot factory servers for ninety days but may not change subscription networking or receive permanent local administrator membership; revise delegation and expiry controls. Which option is the correct revision to the decision record?

- ✗ **A. Retain Group-based Azure RBAC at stable scopes with Arc-aware local delegation at Model scopes and inherited access without recalculating criteria or eligibility. Afterward, treat it as established that the original weighted result is permanent.** — The checkpoint specifically records that group-based Azure RBAC at stable scopes with Arc-aware local delegation. Under the stated constraint, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✓ **B. Re-score Group-based Azure RBAC at stable scopes with Arc-aware local delegation and both alternatives for Model scopes and inherited access. Then, supersede the ADR using the changed evidence for LAB04-REQ-01.** — The relevant observation is that group-based Azure RBAC at stable scopes with Arc-aware local delegation at Model scopes and inherited access. Under the stated constraint, the material change 'A managed-service provider must troubleshoot factory servers for ninety days but may not change subscription networking or receive permanent local administrator membership; revise delegation and expiry controls.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **C. Select Direct user assignments on individual resources and servers for Model scopes and inherited access without rechecking its mandatory constraints; next, use as justification the claim that being different from the current design is an architecture criterion.** — The scenario makes clear that direct user assignments on individual resources and servers. Under the stated constraint, being different is not a criterion, and the candidate still must avoid the prohibited state at Model scopes and inherited access.
- ✗ **D. Keep Subscription-wide custom roles mirrored into local administrator groups eligible at Model scopes and inherited access by downgrading LAB04-REQ-01. In addition, accept without proof that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The architecture evidence must show that lAB04-REQ-01. Under the stated constraint, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q10 — answer D

A design review of 'Model scopes and inherited access' includes cloud platform owner. After a partial run, cleanup must follow this dependency: Remove child assignments before groups only when exact run-owned IDs and tags are proven. What should the architect select as the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Constrain a custom control-plane role before reconciling the current dependency; as an independent condition, base approval on the claim that removing a parent needed to identify Model scopes and inherited access is harmless.** — The review is governed by this fact: remove assignments that reference the custom role before deleting the definition. Under the stated constraint, a cleanup rule for Constrain a custom control-plane role cannot override the dependency declared for Model scopes and inherited access.
- ✗ **B. Delete candidates by display name before comparing the Model scopes and inherited access ownership tags; for the recorded decision, use the premise that the dependency rule 'Remove child assignments before groups only when exact run-owned IDs and tags are proven' is optional.** — The retained result must be reconciled with the fact that synthetic principal labels, role names, assignment scopes, inheritance path, and business owner. Under the stated constraint, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **C. Destroy recoverable copies before retaining the Model scopes and inherited access negative assertion 'No individual user holds standing Owner at the reviewed production scope'. Then, consider it sufficient that remaining command logs are sufficient recovery evidence.** — The decision tension comes from the fact that no individual user holds standing Owner at the reviewed production scope. Under the stated constraint, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.
- ✓ **D. Verify exact run-state IDs and ownership tags for Model scopes and inherited access. Next, follow this dependency rule without purge: Remove child assignments before groups only when exact run-owned IDs and tags are proven.** — The applicable design condition is that remove child assignments before groups only when exact run-owned IDs and tags are proven. Under the stated constraint, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q11 — answer A

The team asks cloud platform owner to assess 'Delegate through groups rather than people'. Approval requires a positive result plus this independent negative assertion: No equivalent direct-user assignment remains at the delegated scope. Which choice should be approved as the acceptance rule that makes LAB04-REQ-02 testable?

- ✓ **A. Require the documented positive state for Delegate through groups rather than people; as a separate check, verify that no equivalent direct-user assignment remains at the delegated scope.** — The safe operating boundary says that the operating team receives resource-group Contributor through an owned Microsoft Entra group. Under the stated constraint, the positive state and an independent negative assertion jointly make LAB04-REQ-02 testable.
- ✗ **B. Select Direct user assignments on individual resources and servers before checking Delegate through groups rather than people; before approval, treat as decisive the assertion that a successful deployment will later prove the architecture constraint.** — The traceable checkpoint outcome is that no equivalent direct-user assignment remains at the delegated scope. Under the stated constraint, a deployment result cannot prove LAB04-REQ-02, and Direct user assignments on individual resources and servers still has to meet the mandatory boundary.
- ✗ **C. Use the passing result from Model scopes and inherited access to approve Delegate through groups rather than people. Separately, base approval on the claim that one control establishes an unrelated acceptance boundary.** — The failure model establishes that stable management scopes and group assignments explain both direct and inherited effective access. Under the stated constraint, that outcome belongs to Model scopes and inherited access and leaves Delegate through groups rather than people unverified.
- ✗ **D. Choose Subscription-wide custom roles mirrored into local administrator groups and skip the Delegate through groups rather than people negative assertion; for this decision, use the premise that the candidate has the lowest implementation effort.** — The recovery guidance assumes that reduce standing privilege and audit ambiguity without preventing platform and factory teams from meeting support obligations. Under the stated constraint, implementation effort cannot justify skipping the negative assertion or displace LAB04-REQ-02.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q12 — answer B

A recommendation on 'Delegate through groups rather than people' is requested by factory operations. The selected architecture is Group-based Azure RBAC at stable scopes with Arc-aware local delegation; object existence alone is not success. What should the team use as the intended successful finding?

- ✗ **A. Use only the negative assertion 'No equivalent direct-user assignment remains at the delegated scope' as the success result; afterward, accept without proof that absence proves every required positive property.** — The command-level assertion is anchored in the fact that no equivalent direct-user assignment remains at the delegated scope. Under the stated constraint, this is the independent prohibited-state assertion, not a successful finding.
- ✓ **B. Record the operating team receives resource-group Contributor through an owned Microsoft Entra group; before approval, classify it as success for LAB04-REQ-02.** — The WAF consequence identifies that the operating team receives resource-group Contributor through an owned Microsoft Entra group. Under the stated constraint, this is the authored target state for Delegate through groups rather than people and directly supports LAB04-REQ-02.
- ✗ **C. Use the successful finding from Constrain a custom control-plane role as the result for Delegate through groups rather than people; then rely on the claim that a property from the current checkpoint does not need to be inspected.** — the custom role contains only documented support actions and the minimum assignable scopes. This matters because evidence for Constrain a custom control-plane role cannot substitute for the properties required at Delegate through groups rather than people.
- ✗ **D. Record the failure condition 'The caller cannot resolve the group or create assignments at the requested scope' as a successful state. Independently, rely on the belief that the command returned an object.** — The controlling fact is that the caller cannot resolve the group or create assignments at the requested scope. This matters because resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q13 — answer C

'Delegate through groups rather than people' is assigned to security assurance. Evidence must address this risk without retaining credentials: The caller cannot resolve the group or create assignments at the requested scope. Which option best establishes sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Separate control-plane and data-plane access for Delegate through groups rather than people. As another control, consider it sufficient that a related checkpoint proves the current expected state.** — The relevant observation is that synthetic workload principal, data-plane role, exact vault scope, and denied management operations. This matters because that evidence supports Separate control-plane and data-plane access, so it cannot demonstrate The operating team receives resource-group Contributor through an owned Microsoft Entra group.
- ✗ **B. Store unredacted Delegate through groups rather than people output with operator, tenant, token, and request context; as a separate check, take it as conclusive that reproduction requires every captured field.** — The checkpoint specifically records that unredacted implementation output. This matters because identity, tenant, or token material exceeds the non-secret evidence contract.
- ✓ **C. Retain synthetic group object ID, role definition, exact scope, owner, and access-review cadence; as an independent condition, exclude credentials and unrelated response fields.** — The authored acceptance boundary states that synthetic group object ID, role definition, exact scope, owner, and access-review cadence. This matters because it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **D. Record only the Delegate through groups rather than people positive inspection's exit status. Afterward, treat it as established that projected properties and assertion results can be reconstructed later.** — The scenario makes clear that the positive inspection's exit status. This matters because an exit code alone does not show whether the operating team receives resource-group Contributor through an owned Microsoft Entra group.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q14 — answer B

An assurance review of 'Delegate through groups rather than people' includes internal audit. The target is The operating team receives resource-group Contributor through an owned Microsoft Entra group, but the latest evidence does not show it. Which answer identifies the most likely cause?

- ✗ **A. Treat 'Teams conflate Arc resource management with guest configuration or local sign-in rights' as grounds to reject Delegate through groups rather than people; for this decision, proceed on the belief that define the Azure Arc authorization boundary's failure model applies unchanged here.** — The applicable design condition is that teams conflate Arc resource management with guest configuration or local sign-in rights. This matters because that condition belongs to Define the Azure Arc authorization boundary and does not by itself invalidate Group-based Azure RBAC at stable scopes with Arc-aware local delegation.
- ✓ **B. Investigate the caller cannot resolve the group or create assignments at the requested scope; then isolate that cause before changing Group-based Azure RBAC at stable scopes with Arc-aware local delegation.** — The architecture evidence must show that the caller cannot resolve the group or create assignments at the requested scope. This matters because it is the checkpoint's causal failure model and should be isolated before retrying Delegate through groups rather than people.
- ✗ **C. Ignore the negative assertion 'No equivalent direct-user assignment remains at the delegated scope'. Before sign-off, treat as decisive the assertion that a later material change will make it unnecessary.** — The review is governed by this fact: no equivalent direct-user assignment remains at the delegated scope. This matters because the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Model scopes and inherited access instead of diagnosing Delegate through groups rather than people; as an independent condition, base approval on the claim that a passing result at Model scopes and inherited access identifies the current cause.** — The retained result must be reconciled with the fact that stable management scopes and group assignments explain both direct and inherited effective access. This matters because a passing result at Model scopes and inherited access gives no causal evidence for the failure at Delegate through groups rather than people.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q15 — answer A

Approval of 'Delegate through groups rather than people' is questioned by cloud platform owner. The run encountered this modeled failure: The caller cannot resolve the group or create assignments at the requested scope. What recommendation gives the reviewers the safest recovery action?

- ✓ **A. Validate directory read access and role-assignment permissions without broadening the target scope. Also, preserve the current run identity and evidence.** — The decision tension comes from the fact that validate directory read access and role-assignment permissions without broadening the target scope. This matters because it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **B. Perform cleanup immediately: Delete the run-owned assignment before considering any group lifecycle action. Independently, use as justification the claim that the failed operation and its returned identifiers do not need reconciliation.** — The safe operating boundary says that delete the run-owned assignment before considering any group lifecycle action. This matters because cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **C. Create a different run identity before diagnosing 'The caller cannot resolve the group or create assignments at the requested scope'. Next, accept without proof that the first state record and returned identifiers can be discarded.** — The traceable checkpoint outcome is that the caller cannot resolve the group or create assignments at the requested scope. This matters because discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Model scopes and inherited access instead, and then rely on the claim that success at Model scopes and inherited access will repair the failed state at Delegate through groups rather than people.** — The failure model establishes that stable management scopes and group assignments explain both direct and inherited effective access. This matters because altering an already separate checkpoint does not repair the modeled failure at Delegate through groups rather than people.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q16 — answer C

The implementation review has reached 'Delegate through groups rather than people'. Without making a new change, the team must inspect the risk 'The caller cannot resolve the group or create assignments at the requested scope' using the Azure CLI lane. Which action produces the read-only, lane-correct inspection?

- ✗ **A. Rerun the Delegate through groups rather than people implementation command and infer the expected state. Afterward, use the premise that absence of a shell error proves every property.** — The WAF consequence identifies that the implementation command. This matters because it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Delegate through groups rather than people: No equivalent direct-user assignment remains at the delegated scope; next, consider it sufficient that an empty negative result reports every required positive property.** — The command-level assertion is anchored in the fact that the negative inspection. This matters because absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✓ **C. Inspect the documented properties for Delegate through groups rather than people. Afterward, retain this evidence: synthetic group object ID, role definition, exact scope, owner, and access-review cadence.** — The recovery guidance assumes that the operating team receives resource-group Contributor through an owned Microsoft Entra group. This matters because the read-only inspection directly tests the properties required at Delegate through groups rather than people.
- ✗ **D. Run the positive inspection for Constrain a custom control-plane role and apply it to Delegate through groups rather than people. In addition, take it as conclusive that any command from the same lane proves the current checkpoint.** — the positive inspection for Constrain a custom control-plane role. The checkpoint therefore requires that it is lane-correct but proves Constrain a custom control-plane role, not Delegate through groups rather than people.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q17 — answer D

The approach to 'Delegate through groups rather than people' is challenged by security assurance. A passing positive check does not by itself prove this negative assertion: No equivalent direct-user assignment remains at the delegated scope. What best demonstrates the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Delegate through groups rather than people and report full compliance; as an independent condition, rely on the belief that every prohibited parallel state must therefore be absent.** — The authored acceptance boundary states that the operating team receives resource-group Contributor through an owned Microsoft Entra group. The checkpoint therefore requires that the positive result alone does not test the explicit anti-condition 'No equivalent direct-user assignment remains at the delegated scope'.
- ✗ **B. Prove only that no equivalent direct-user assignment remains at the delegated scope and report the intended configuration as present; as another gate, proceed on the belief that absence is equivalent to positive-state evidence.** — The relevant observation is that no equivalent direct-user assignment remains at the delegated scope. The checkpoint therefore requires that absence evidence cannot demonstrate the required positive state 'The operating team receives resource-group Contributor through an owned Microsoft Entra group'.
- ✗ **C. Use Separate control-plane and data-plane access's negative assertion for Delegate through groups rather than people. Then, treat as decisive the assertion that negative assertions are interchangeable between checkpoints.** — The checkpoint specifically records that the workload receives neither Owner nor Contributor at the vault or a parent scope. The checkpoint therefore requires that the second assertion is valid for Separate control-plane and data-plane access but leaves this checkpoint's prohibited state untested.
- ✓ **D. Verify the positive properties for Delegate through groups rather than people. Separately, independently verify that no equivalent direct-user assignment remains at the delegated scope.** — The controlling fact is that the operating team receives resource-group Contributor through an owned Microsoft Entra group; No equivalent direct-user assignment remains at the delegated scope. The checkpoint therefore requires that two independent observations prevent a passing positive check from concealing an unsafe parallel state.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q18 — answer A

A decision test for 'Delegate through groups rather than people' includes internal audit. The board wants the Well-Architected consequence of mitigating this risk: The caller cannot resolve the group or create assignments at the requested scope. Which option is the consequence attributable to this checkpoint?

- ✓ **A. Record this consequence: Cost Optimization: group-based delegation reduces repetitive assignment and recertification effort; as another gate, tie it to LAB04-REQ-02.** — The scenario makes clear that cost Optimization: group-based delegation reduces repetitive assignment and recertification effort. The checkpoint therefore requires that it states the authored pillar consequence of the control evaluated at Delegate through groups rather than people.
- ✗ **B. Use the Define the Azure Arc authorization boundary consequence as the result for Delegate through groups rather than people, and then treat it as established that a pillar statement remains valid when moved away from Define the Azure Arc authorization boundary.** — The architecture evidence must show that security: the hybrid boundary prevents Azure control-plane access from being mistaken for guest administrator privilege. The checkpoint therefore requires that that tradeoff belongs to Define the Azure Arc authorization boundary and does not explain this checkpoint's decision.
- ✗ **C. Remove the control responsible for the Delegate through groups rather than people outcome. Also, use as justification the claim that a low cost classification outweighs the mandatory architecture state.** — The applicable design condition is that the required outcome at Delegate through groups rather than people. The checkpoint therefore requires that cost Optimization cannot remove the acceptance condition 'The operating team receives resource-group Contributor through an owned Microsoft Entra group'.
- ✗ **D. Treat 'Cost Optimization: group-based delegation reduces repetitive assignment and recertification effort' as proof that all five pillars pass; in a separate step, accept without proof that the checkpoint 'Delegate through groups rather than people' no longer needs its separate negative check.** — The review is governed by this fact: no equivalent direct-user assignment remains at the delegated scope. The checkpoint therefore requires that one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q19 — answer A

The architecture board reconsiders 'Delegate through groups rather than people' with cloud platform owner. A material change now applies: A managed-service provider must troubleshoot factory servers for ninety days but may not change subscription networking or receive permanent local administrator membership; revise delegation and expiry controls. What should the architect select as the correct revision to the decision record?

- ✓ **A. Re-score Group-based Azure RBAC at stable scopes with Arc-aware local delegation and both alternatives for Delegate through groups rather than people. Independently, supersede the ADR using the changed evidence for LAB04-REQ-02.** — The retained result must be reconciled with the fact that group-based Azure RBAC at stable scopes with Arc-aware local delegation at Delegate through groups rather than people. The checkpoint therefore requires that the material change 'A managed-service provider must troubleshoot factory servers for ninety days but may not change subscription networking or receive permanent local administrator membership; revise delegation and expiry controls.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **B. Retain Group-based Azure RBAC at stable scopes with Arc-aware local delegation at Delegate through groups rather than people without recalculating criteria or eligibility. In addition, base approval on the claim that the original weighted result is permanent.** — The decision tension comes from the fact that group-based Azure RBAC at stable scopes with Arc-aware local delegation. The checkpoint therefore requires that the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **C. Select Direct user assignments on individual resources and servers for Delegate through groups rather than people without rechecking its mandatory constraints; before approval, use the premise that being different from the current design is an architecture criterion.** — The safe operating boundary says that direct user assignments on individual resources and servers. The checkpoint therefore requires that being different is not a criterion, and the candidate still must avoid the prohibited state at Delegate through groups rather than people.
- ✗ **D. Keep Subscription-wide custom roles mirrored into local administrator groups eligible at Delegate through groups rather than people by downgrading LAB04-REQ-02. Separately, consider it sufficient that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The traceable checkpoint outcome is that lAB04-REQ-02. The checkpoint therefore requires that an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q20 — answer A

A review of 'Delegate through groups rather than people' begins with input from factory operations. After a partial run, cleanup must follow this dependency: Delete the run-owned assignment before considering any group lifecycle action. Select the dependency-safe cleanup plan.

- ✓ **A. Verify exact run-state IDs and ownership tags for Delegate through groups rather than people; in a separate step, follow this dependency rule without purge: Delete the run-owned assignment before considering any group lifecycle action.** — The failure model establishes that delete the run-owned assignment before considering any group lifecycle action. The checkpoint therefore requires that exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **B. Apply the cleanup rule for Constrain a custom control-plane role before reconciling the current dependency. Then, rely on the claim that removing a parent needed to identify Delegate through groups rather than people is harmless.** — The recovery guidance assumes that remove assignments that reference the custom role before deleting the definition. The checkpoint therefore requires that a cleanup rule for Constrain a custom control-plane role cannot override the dependency declared for Delegate through groups rather than people.
- ✗ **C. Delete candidates by display name before comparing the Delegate through groups rather than people ownership tags; afterward, rely on the belief that the dependency rule 'Delete the run-owned assignment before considering any group lifecycle action' is optional.** — The WAF consequence identifies that synthetic group object ID, role definition, exact scope, owner, and access-review cadence. The checkpoint therefore requires that names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Delegate through groups rather than people negative assertion 'No equivalent direct-user assignment remains at the delegated scope'; then proceed on the belief that remaining command logs are sufficient recovery evidence.** — The command-level assertion is anchored in the fact that no equivalent direct-user assignment remains at the delegated scope. The checkpoint therefore requires that irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q21 — answer C

'Constrain a custom control-plane role' awaits approval from factory operations. Approval requires a positive result plus this independent negative assertion: No wildcard action, role-assignment write, or destructive permission is granted. What should the team use as the acceptance rule that makes LAB04-REQ-03 testable?

- ✗ **A. Select Direct user assignments on individual resources and servers before checking Constrain a custom control-plane role; for this decision, accept without proof that a successful deployment will later prove the architecture constraint.** — The controlling fact is that no wildcard action, role-assignment write, or destructive permission is granted. In the decision record, a deployment result cannot prove LAB04-REQ-03, and Direct user assignments on individual resources and servers still has to meet the mandatory boundary.
- ✗ **B. Use the passing result from Model scopes and inherited access to approve Constrain a custom control-plane role. Before sign-off, rely on the claim that one control establishes an unrelated acceptance boundary.** — The authored acceptance boundary states that stable management scopes and group assignments explain both direct and inherited effective access. In the decision record, that outcome belongs to Model scopes and inherited access and leaves Constrain a custom control-plane role unverified.
- ✓ **C. Require the documented positive state for Constrain a custom control-plane role. In addition, verify that no wildcard action, role-assignment write, or destructive permission is granted.** — the custom role contains only documented support actions and the minimum assignable scopes. In the decision record, the positive state and an independent negative assertion jointly make LAB04-REQ-03 testable.
- ✗ **D. Choose Subscription-wide custom roles mirrored into local administrator groups and skip the Constrain a custom control-plane role negative assertion; as an independent condition, rely on the belief that the candidate has the lowest implementation effort.** — The relevant observation is that reduce standing privilege and audit ambiguity without preventing platform and factory teams from meeting support obligations. In the decision record, implementation effort cannot justify skipping the negative assertion or displace LAB04-REQ-03.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q22 — answer A

'Constrain a custom control-plane role' is reopened at the request of security assurance. The selected architecture is Group-based Azure RBAC at stable scopes with Arc-aware local delegation; object existence alone is not success. Which option best establishes the intended successful finding?

- ✓ **A. Record the custom role contains only documented support actions and the minimum assignable scopes. Before sign-off, classify it as success for LAB04-REQ-03.** — The checkpoint specifically records that the custom role contains only documented support actions and the minimum assignable scopes. In the decision record, this is the authored target state for Constrain a custom control-plane role and directly supports LAB04-REQ-03.
- ✗ **B. Use only the negative assertion 'No wildcard action, role-assignment write, or destructive permission is granted' as the success result. Independently, consider it sufficient that absence proves every required positive property.** — The scenario makes clear that no wildcard action, role-assignment write, or destructive permission is granted. In the decision record, this is the independent prohibited-state assertion, not a successful finding.
- ✗ **C. Use the successful finding from Delegate through groups rather than people as the result for Constrain a custom control-plane role. Next, take it as conclusive that a property from the current checkpoint does not need to be inspected.** — The architecture evidence must show that the operating team receives resource-group Contributor through an owned Microsoft Entra group. In the decision record, evidence for Delegate through groups rather than people cannot substitute for the properties required at Constrain a custom control-plane role.
- ✗ **D. Record the failure condition 'An operational task depends on a hidden action not represented in provider operations' as a successful state, and then treat it as established that the command returned an object.** — The applicable design condition is that an operational task depends on a hidden action not represented in provider operations. In the decision record, resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q23 — answer D

A design review of 'Constrain a custom control-plane role' includes internal audit. Evidence must address this risk without retaining credentials: An operational task depends on a hidden action not represented in provider operations. Which answer identifies sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Separate control-plane and data-plane access for Constrain a custom control-plane role. Afterward, proceed on the belief that a related checkpoint proves the current expected state.** — The retained result must be reconciled with the fact that synthetic workload principal, data-plane role, exact vault scope, and denied management operations. In the decision record, that evidence supports Separate control-plane and data-plane access, so it cannot demonstrate The custom role contains only documented support actions and the minimum assignable scopes.
- ✗ **B. Store unredacted Constrain a custom control-plane role output with operator, tenant, token, and request context; next, treat as decisive the assertion that reproduction requires every captured field.** — The decision tension comes from the fact that unredacted implementation output. In the decision record, identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **C. Record only the Constrain a custom control-plane role positive inspection's exit status. In addition, base approval on the claim that projected properties and assertion results can be reconstructed later.** — The safe operating boundary says that the positive inspection's exit status. In the decision record, an exit code alone does not show whether the custom role contains only documented support actions and the minimum assignable scopes.
- ✓ **D. Retain role definition hash, actions, notActions, dataActions, and assignable scopes; afterward, exclude credentials and unrelated response fields.** — The review is governed by this fact: role definition hash, actions, notActions, dataActions, and assignable scopes. In the decision record, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q24 — answer C

The team asks cloud platform owner to assess 'Constrain a custom control-plane role'. The target is The custom role contains only documented support actions and the minimum assignable scopes, but the latest evidence does not show it. What recommendation gives the reviewers the most likely cause?

- ✗ **A. Treat 'Teams conflate Arc resource management with guest configuration or local sign-in rights' as grounds to reject Constrain a custom control-plane role; as an independent condition, use as justification the claim that define the Azure Arc authorization boundary's failure model applies unchanged here.** — The failure model establishes that teams conflate Arc resource management with guest configuration or local sign-in rights. In the decision record, that condition belongs to Define the Azure Arc authorization boundary and does not by itself invalidate Group-based Azure RBAC at stable scopes with Arc-aware local delegation.
- ✗ **B. Ignore the negative assertion 'No wildcard action, role-assignment write, or destructive permission is granted'; without relying on inference, accept without proof that a later material change will make it unnecessary.** — The recovery guidance assumes that no wildcard action, role-assignment write, or destructive permission is granted. In the decision record, the negative assertion must be evaluated now, independent of a later business change.
- ✓ **C. Investigate an operational task depends on a hidden action not represented in provider operations, and then isolate that cause before changing Group-based Azure RBAC at stable scopes with Arc-aware local delegation.** — The traceable checkpoint outcome is that an operational task depends on a hidden action not represented in provider operations. In the decision record, it is the checkpoint's causal failure model and should be isolated before retrying Constrain a custom control-plane role.
- ✗ **D. Investigate Model scopes and inherited access instead of diagnosing Constrain a custom control-plane role. Then, rely on the claim that a passing result at Model scopes and inherited access identifies the current cause.** — The WAF consequence identifies that stable management scopes and group assignments explain both direct and inherited effective access. In the decision record, a passing result at Model scopes and inherited access gives no causal evidence for the failure at Constrain a custom control-plane role.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q25 — answer B

A recommendation on 'Constrain a custom control-plane role' is requested by factory operations. The run encountered this modeled failure: An operational task depends on a hidden action not represented in provider operations. Which action produces the safest recovery action?

- ✗ **A. Perform cleanup immediately: Remove assignments that reference the custom role before deleting the definition, and then use the premise that the failed operation and its returned identifiers do not need reconciliation.** — remove assignments that reference the custom role before deleting the definition. The independent assertion shows why cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✓ **B. Capture the denied operation, add only its documented action, and repeat the privilege review; as a separate check, preserve the current run identity and evidence.** — The command-level assertion is anchored in the fact that capture the denied operation, add only its documented action, and repeat the privilege review. In the decision record, it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **C. Create a different run identity before diagnosing 'An operational task depends on a hidden action not represented in provider operations'. Also, consider it sufficient that the first state record and returned identifiers can be discarded.** — The controlling fact is that an operational task depends on a hidden action not represented in provider operations. The independent assertion shows why discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Model scopes and inherited access instead; in a separate step, take it as conclusive that success at Model scopes and inherited access will repair the failed state at Constrain a custom control-plane role.** — The authored acceptance boundary states that stable management scopes and group assignments explain both direct and inherited effective access. The independent assertion shows why altering an already separate checkpoint does not repair the modeled failure at Constrain a custom control-plane role.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q26 — answer B

'Constrain a custom control-plane role' is assigned to security assurance. Without making a new change, the team must inspect the risk 'An operational task depends on a hidden action not represented in provider operations' using the Azure CLI lane. What best demonstrates the read-only, lane-correct inspection?

- ✗ **A. Rerun the Constrain a custom control-plane role implementation command and infer the expected state. In addition, rely on the belief that absence of a shell error proves every property.** — The checkpoint specifically records that the implementation command. The independent assertion shows why it can mutate state and shell success does not independently assert the expected properties.
- ✓ **B. Inspect the documented properties for Constrain a custom control-plane role; before approval, retain this evidence: role definition hash, actions, notActions, dataActions, and assignable scopes.** — The relevant observation is that the custom role contains only documented support actions and the minimum assignable scopes. The independent assertion shows why the read-only inspection directly tests the properties required at Constrain a custom control-plane role.
- ✗ **C. Run only this negative inspection for Constrain a custom control-plane role: No wildcard action, role-assignment write, or destructive permission is granted; before approval, proceed on the belief that an empty negative result reports every required positive property.** — The scenario makes clear that the negative inspection. The independent assertion shows why absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Delegate through groups rather than people and apply it to Constrain a custom control-plane role. Separately, treat as decisive the assertion that any command from the same lane proves the current checkpoint.** — The architecture evidence must show that the positive inspection for Delegate through groups rather than people. The independent assertion shows why it is lane-correct but proves Delegate through groups rather than people, not Constrain a custom control-plane role.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q27 — answer B

An assurance review of 'Constrain a custom control-plane role' includes internal audit. A passing positive check does not by itself prove this negative assertion: No wildcard action, role-assignment write, or destructive permission is granted. Which option is the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Constrain a custom control-plane role and report full compliance. Then, treat it as established that every prohibited parallel state must therefore be absent.** — The review is governed by this fact: the custom role contains only documented support actions and the minimum assignable scopes. The independent assertion shows why the positive result alone does not test the explicit anti-condition 'No wildcard action, role-assignment write, or destructive permission is granted'.
- ✓ **B. Verify the positive properties for Constrain a custom control-plane role; as an independent condition, independently verify that no wildcard action, role-assignment write, or destructive permission is granted.** — The applicable design condition is that the custom role contains only documented support actions and the minimum assignable scopes; No wildcard action, role-assignment write, or destructive permission is granted. The independent assertion shows why two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **C. Prove only that no wildcard action, role-assignment write, or destructive permission is granted and report the intended configuration as present; afterward, use as justification the claim that absence is equivalent to positive-state evidence.** — The retained result must be reconciled with the fact that no wildcard action, role-assignment write, or destructive permission is granted. The independent assertion shows why absence evidence cannot demonstrate the required positive state 'The custom role contains only documented support actions and the minimum assignable scopes'.
- ✗ **D. Use Separate control-plane and data-plane access's negative assertion for Constrain a custom control-plane role; then accept without proof that negative assertions are interchangeable between checkpoints.** — The decision tension comes from the fact that the workload receives neither Owner nor Contributor at the vault or a parent scope. The independent assertion shows why the second assertion is valid for Separate control-plane and data-plane access but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q28 — answer D

Approval of 'Constrain a custom control-plane role' is questioned by cloud platform owner. The board wants the Well-Architected consequence of mitigating this risk: An operational task depends on a hidden action not represented in provider operations. What should the architect select as the consequence attributable to this checkpoint?

- ✗ **A. Use the Define the Azure Arc authorization boundary consequence as the result for Constrain a custom control-plane role; in a separate step, base approval on the claim that a pillar statement remains valid when moved away from Define the Azure Arc authorization boundary.** — The traceable checkpoint outcome is that security: the hybrid boundary prevents Azure control-plane access from being mistaken for guest administrator privilege. The independent assertion shows why that tradeoff belongs to Define the Azure Arc authorization boundary and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Constrain a custom control-plane role outcome. As another control, use the premise that a low cost classification outweighs the mandatory architecture state.** — The failure model establishes that the required outcome at Constrain a custom control-plane role. The independent assertion shows why cost Optimization cannot remove the acceptance condition 'The custom role contains only documented support actions and the minimum assignable scopes'.
- ✗ **C. Treat 'Performance Efficiency: a task-focused role lets operators complete supported recovery work without broad authorization workflows' as proof that all five pillars pass; as a separate check, consider it sufficient that the checkpoint 'Constrain a custom control-plane role' no longer needs its separate negative check.** — The recovery guidance assumes that no wildcard action, role-assignment write, or destructive permission is granted. The independent assertion shows why one positive command cannot establish every pillar, especially while the negative state remains unchecked.
- ✓ **D. Record this consequence: Performance Efficiency: a task-focused role lets operators complete supported recovery work without broad authorization workflows; then tie it to LAB04-REQ-03.** — The safe operating boundary says that performance Efficiency: a task-focused role lets operators complete supported recovery work without broad authorization workflows. The independent assertion shows why it states the authored pillar consequence of the control evaluated at Constrain a custom control-plane role.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q29 — answer A

The implementation review has reached 'Constrain a custom control-plane role'. A material change now applies: A managed-service provider must troubleshoot factory servers for ninety days but may not change subscription networking or receive permanent local administrator membership; revise delegation and expiry controls. Select the correct revision to the decision record.

- ✓ **A. Re-score Group-based Azure RBAC at stable scopes with Arc-aware local delegation and both alternatives for Constrain a custom control-plane role. Also, supersede the ADR using the changed evidence for LAB04-REQ-03.** — The WAF consequence identifies that group-based Azure RBAC at stable scopes with Arc-aware local delegation at Constrain a custom control-plane role. The independent assertion shows why the material change 'A managed-service provider must troubleshoot factory servers for ninety days but may not change subscription networking or receive permanent local administrator membership; revise delegation and expiry controls.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **B. Retain Group-based Azure RBAC at stable scopes with Arc-aware local delegation at Constrain a custom control-plane role without recalculating criteria or eligibility. Separately, rely on the claim that the original weighted result is permanent.** — The command-level assertion is anchored in the fact that group-based Azure RBAC at stable scopes with Arc-aware local delegation. The independent assertion shows why the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **C. Select Direct user assignments on individual resources and servers for Constrain a custom control-plane role without rechecking its mandatory constraints; for this decision, rely on the belief that being different from the current design is an architecture criterion.** — direct user assignments on individual resources and servers. Operationally, being different is not a criterion, and the candidate still must avoid the prohibited state at Constrain a custom control-plane role.
- ✗ **D. Keep Subscription-wide custom roles mirrored into local administrator groups eligible at Constrain a custom control-plane role by downgrading LAB04-REQ-03. Before sign-off, proceed on the belief that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The controlling fact is that lAB04-REQ-03. Operationally, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q30 — answer A

The approach to 'Constrain a custom control-plane role' is challenged by security assurance. After a partial run, cleanup must follow this dependency: Remove assignments that reference the custom role before deleting the definition. Which response provides the dependency-safe cleanup plan?

- ✓ **A. Verify exact run-state IDs and ownership tags for Constrain a custom control-plane role. Afterward, follow this dependency rule without purge: Remove assignments that reference the custom role before deleting the definition.** — The authored acceptance boundary states that remove assignments that reference the custom role before deleting the definition. Operationally, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **B. Apply the cleanup rule for Delegate through groups rather than people before reconciling the current dependency; then take it as conclusive that removing a parent needed to identify Constrain a custom control-plane role is harmless.** — The relevant observation is that delete the run-owned assignment before considering any group lifecycle action. Operationally, a cleanup rule for Delegate through groups rather than people cannot override the dependency declared for Constrain a custom control-plane role.
- ✗ **C. Delete candidates by display name before comparing the Constrain a custom control-plane role ownership tags. Independently, treat it as established that the dependency rule 'Remove assignments that reference the custom role before deleting the definition' is optional.** — The checkpoint specifically records that role definition hash, actions, notActions, dataActions, and assignable scopes. Operationally, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Constrain a custom control-plane role negative assertion 'No wildcard action, role-assignment write, or destructive permission is granted'. Next, use as justification the claim that remaining command logs are sufficient recovery evidence.** — The scenario makes clear that no wildcard action, role-assignment write, or destructive permission is granted. Operationally, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q31 — answer D

A decision test for 'Separate control-plane and data-plane access' includes security assurance. Approval requires a positive result plus this independent negative assertion: The workload receives neither Owner nor Contributor at the vault or a parent scope. Which option best establishes the acceptance rule that makes LAB04-REQ-04 testable?

- ✗ **A. Select Direct user assignments on individual resources and servers before checking Separate control-plane and data-plane access; as an independent condition, consider it sufficient that a successful deployment will later prove the architecture constraint.** — The applicable design condition is that the workload receives neither Owner nor Contributor at the vault or a parent scope. Operationally, a deployment result cannot prove LAB04-REQ-04, and Direct user assignments on individual resources and servers still has to meet the mandatory boundary.
- ✗ **B. Use the passing result from Model scopes and inherited access to approve Separate control-plane and data-plane access; before closing the checkpoint, take it as conclusive that one control establishes an unrelated acceptance boundary.** — The review is governed by this fact: stable management scopes and group assignments explain both direct and inherited effective access. Operationally, that outcome belongs to Model scopes and inherited access and leaves Separate control-plane and data-plane access unverified.
- ✗ **C. Choose Subscription-wide custom roles mirrored into local administrator groups and skip the Separate control-plane and data-plane access negative assertion. Then, treat it as established that the candidate has the lowest implementation effort.** — The retained result must be reconciled with the fact that reduce standing privilege and audit ambiguity without preventing platform and factory teams from meeting support obligations. Operationally, implementation effort cannot justify skipping the negative assertion or displace LAB04-REQ-04.
- ✓ **D. Require the documented positive state for Separate control-plane and data-plane access; for this decision, verify that the workload receives neither Owner nor Contributor at the vault or a parent scope.** — The architecture evidence must show that the workload identity can read secret values through a data-plane role without managing the vault. Operationally, the positive state and an independent negative assertion jointly make LAB04-REQ-04 testable.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q32 — answer C

The architecture board reconsiders 'Separate control-plane and data-plane access' with internal audit. The selected architecture is Group-based Azure RBAC at stable scopes with Arc-aware local delegation; object existence alone is not success. Which answer identifies the intended successful finding?

- ✗ **A. Use only the negative assertion 'The workload receives neither Owner nor Contributor at the vault or a parent scope' as the success result, and then proceed on the belief that absence proves every required positive property.** — The safe operating boundary says that the workload receives neither Owner nor Contributor at the vault or a parent scope. Operationally, this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Delegate through groups rather than people as the result for Separate control-plane and data-plane access. Also, treat as decisive the assertion that a property from the current checkpoint does not need to be inspected.** — The traceable checkpoint outcome is that the operating team receives resource-group Contributor through an owned Microsoft Entra group. Operationally, evidence for Delegate through groups rather than people cannot substitute for the properties required at Separate control-plane and data-plane access.
- ✓ **C. Record the workload identity can read secret values through a data-plane role without managing the vault. Then, classify it as success for LAB04-REQ-04.** — The decision tension comes from the fact that the workload identity can read secret values through a data-plane role without managing the vault. Operationally, this is the authored target state for Separate control-plane and data-plane access and directly supports LAB04-REQ-04.
- ✗ **D. Record the failure condition 'The vault still uses access policies or an inherited management role supplies unintended power' as a successful state; in a separate step, base approval on the claim that the command returned an object.** — The failure model establishes that the vault still uses access policies or an inherited management role supplies unintended power. Operationally, resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q33 — answer C

A review of 'Separate control-plane and data-plane access' begins with input from cloud platform owner. Evidence must address this risk without retaining credentials: The vault still uses access policies or an inherited management role supplies unintended power. What recommendation gives the reviewers sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Constrain a custom control-plane role for Separate control-plane and data-plane access. In addition, use as justification the claim that a related checkpoint proves the current expected state.** — The WAF consequence identifies that role definition hash, actions, notActions, dataActions, and assignable scopes. Operationally, that evidence supports Constrain a custom control-plane role, so it cannot demonstrate The workload identity can read secret values through a data-plane role without managing the vault.
- ✗ **B. Store unredacted Separate control-plane and data-plane access output with operator, tenant, token, and request context; before approval, accept without proof that reproduction requires every captured field.** — The command-level assertion is anchored in the fact that unredacted implementation output. Operationally, identity, tenant, or token material exceeds the non-secret evidence contract.
- ✓ **C. Retain synthetic workload principal, data-plane role, exact vault scope, and denied management operations. Next, exclude credentials and unrelated response fields.** — The recovery guidance assumes that synthetic workload principal, data-plane role, exact vault scope, and denied management operations. Operationally, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **D. Record only the Separate control-plane and data-plane access positive inspection's exit status. Separately, rely on the claim that projected properties and assertion results can be reconstructed later.** — the positive inspection's exit status. The requirement-to-evidence link establishes that an exit code alone does not show whether the workload identity can read secret values through a data-plane role without managing the vault.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q34 — answer D

'Separate control-plane and data-plane access' awaits approval from factory operations. The target is The workload identity can read secret values through a data-plane role without managing the vault, but the latest evidence does not show it. Which action produces the most likely cause?

- ✗ **A. Treat 'Teams conflate Arc resource management with guest configuration or local sign-in rights' as grounds to reject Separate control-plane and data-plane access. Then, use the premise that define the Azure Arc authorization boundary's failure model applies unchanged here.** — The authored acceptance boundary states that teams conflate Arc resource management with guest configuration or local sign-in rights. The requirement-to-evidence link establishes that that condition belongs to Define the Azure Arc authorization boundary and does not by itself invalidate Group-based Azure RBAC at stable scopes with Arc-aware local delegation.
- ✗ **B. Ignore the negative assertion 'The workload receives neither Owner nor Contributor at the vault or a parent scope'; afterward, consider it sufficient that a later material change will make it unnecessary.** — The relevant observation is that the workload receives neither Owner nor Contributor at the vault or a parent scope. The requirement-to-evidence link establishes that the negative assertion must be evaluated now, independent of a later business change.
- ✗ **C. Investigate Model scopes and inherited access instead of diagnosing Separate control-plane and data-plane access; then take it as conclusive that a passing result at Model scopes and inherited access identifies the current cause.** — The checkpoint specifically records that stable management scopes and group assignments explain both direct and inherited effective access. The requirement-to-evidence link establishes that a passing result at Model scopes and inherited access gives no causal evidence for the failure at Separate control-plane and data-plane access.
- ✓ **D. Investigate the vault still uses access policies or an inherited management role supplies unintended power. As another control, isolate that cause before changing Group-based Azure RBAC at stable scopes with Arc-aware local delegation.** — The controlling fact is that the vault still uses access policies or an inherited management role supplies unintended power. The requirement-to-evidence link establishes that it is the checkpoint's causal failure model and should be isolated before retrying Separate control-plane and data-plane access.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q35 — answer A

'Separate control-plane and data-plane access' is reopened at the request of security assurance. The run encountered this modeled failure: The vault still uses access policies or an inherited management role supplies unintended power. What best demonstrates the safest recovery action?

- ✓ **A. Document the authorization model, remove overlap in a controlled change, and validate both planes independently. In addition, preserve the current run identity and evidence.** — The scenario makes clear that document the authorization model, remove overlap in a controlled change, and validate both planes independently. The requirement-to-evidence link establishes that it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **B. Perform cleanup immediately: Remove the exact run-owned role assignment; do not alter unrelated vault access; in a separate step, rely on the belief that the failed operation and its returned identifiers do not need reconciliation.** — The architecture evidence must show that remove the exact run-owned role assignment; do not alter unrelated vault access. The requirement-to-evidence link establishes that cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **C. Create a different run identity before diagnosing 'The vault still uses access policies or an inherited management role supplies unintended power'. As another control, proceed on the belief that the first state record and returned identifiers can be discarded.** — The applicable design condition is that the vault still uses access policies or an inherited management role supplies unintended power. The requirement-to-evidence link establishes that discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Model scopes and inherited access instead; as a separate check, treat as decisive the assertion that success at Model scopes and inherited access will repair the failed state at Separate control-plane and data-plane access.** — The review is governed by this fact: stable management scopes and group assignments explain both direct and inherited effective access. The requirement-to-evidence link establishes that altering an already separate checkpoint does not repair the modeled failure at Separate control-plane and data-plane access.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q36 — answer C

A design review of 'Separate control-plane and data-plane access' includes internal audit. Without making a new change, the team must inspect the risk 'The vault still uses access policies or an inherited management role supplies unintended power' using the Azure CLI lane. Which option is the read-only, lane-correct inspection?

- ✗ **A. Rerun the Separate control-plane and data-plane access implementation command and infer the expected state. Separately, treat it as established that absence of a shell error proves every property.** — The decision tension comes from the fact that the implementation command. The requirement-to-evidence link establishes that it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Separate control-plane and data-plane access: The workload receives neither Owner nor Contributor at the vault or a parent scope; for this decision, use as justification the claim that an empty negative result reports every required positive property.** — The safe operating boundary says that the negative inspection. The requirement-to-evidence link establishes that absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✓ **C. Inspect the documented properties for Separate control-plane and data-plane access. Before sign-off, retain this evidence: synthetic workload principal, data-plane role, exact vault scope, and denied management operations.** — The retained result must be reconciled with the fact that the workload identity can read secret values through a data-plane role without managing the vault. The requirement-to-evidence link establishes that the read-only inspection directly tests the properties required at Separate control-plane and data-plane access.
- ✗ **D. Run the positive inspection for Delegate through groups rather than people and apply it to Separate control-plane and data-plane access. Before sign-off, accept without proof that any command from the same lane proves the current checkpoint.** — The traceable checkpoint outcome is that the positive inspection for Delegate through groups rather than people. The requirement-to-evidence link establishes that it is lane-correct but proves Delegate through groups rather than people, not Separate control-plane and data-plane access.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q37 — answer A

The team asks cloud platform owner to assess 'Separate control-plane and data-plane access'. A passing positive check does not by itself prove this negative assertion: The workload receives neither Owner nor Contributor at the vault or a parent scope. What should the architect select as the assertion pair that proves both conditions independently?

- ✓ **A. Verify the positive properties for Separate control-plane and data-plane access; afterward, independently verify that the workload receives neither Owner nor Contributor at the vault or a parent scope.** — The failure model establishes that the workload identity can read secret values through a data-plane role without managing the vault; The workload receives neither Owner nor Contributor at the vault or a parent scope. The requirement-to-evidence link establishes that two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **B. Verify only the positive result for Separate control-plane and data-plane access and report full compliance; then base approval on the claim that every prohibited parallel state must therefore be absent.** — The recovery guidance assumes that the workload identity can read secret values through a data-plane role without managing the vault. The requirement-to-evidence link establishes that the positive result alone does not test the explicit anti-condition 'The workload receives neither Owner nor Contributor at the vault or a parent scope'.
- ✗ **C. Prove only that the workload receives neither Owner nor Contributor at the vault or a parent scope and report the intended configuration as present. Independently, use the premise that absence is equivalent to positive-state evidence.** — The WAF consequence identifies that the workload receives neither Owner nor Contributor at the vault or a parent scope. The requirement-to-evidence link establishes that absence evidence cannot demonstrate the required positive state 'The workload identity can read secret values through a data-plane role without managing the vault'.
- ✗ **D. Use Constrain a custom control-plane role's negative assertion for Separate control-plane and data-plane access. Next, consider it sufficient that negative assertions are interchangeable between checkpoints.** — The command-level assertion is anchored in the fact that no wildcard action, role-assignment write, or destructive permission is granted. The requirement-to-evidence link establishes that the second assertion is valid for Constrain a custom control-plane role but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q38 — answer C

A recommendation on 'Separate control-plane and data-plane access' is requested by factory operations. The board wants the Well-Architected consequence of mitigating this risk: The vault still uses access policies or an inherited management role supplies unintended power. Select the consequence attributable to this checkpoint.

- ✗ **A. Use the Define the Azure Arc authorization boundary consequence as the result for Separate control-plane and data-plane access; as a separate check, rely on the claim that a pillar statement remains valid when moved away from Define the Azure Arc authorization boundary.** — The controlling fact is that security: the hybrid boundary prevents Azure control-plane access from being mistaken for guest administrator privilege. Consequently, that tradeoff belongs to Define the Azure Arc authorization boundary and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Separate control-plane and data-plane access outcome. Afterward, rely on the belief that a low cost classification outweighs the mandatory architecture state.** — The authored acceptance boundary states that the required outcome at Separate control-plane and data-plane access. Consequently, cost Optimization cannot remove the acceptance condition 'The workload identity can read secret values through a data-plane role without managing the vault'.
- ✓ **C. Record this consequence: Reliability: data-plane roles let workloads consume dependencies without coupling service availability to vault administration, and then tie it to LAB04-REQ-04.** — reliability: data-plane roles let workloads consume dependencies without coupling service availability to vault administration. Consequently, it states the authored pillar consequence of the control evaluated at Separate control-plane and data-plane access.
- ✗ **D. Treat 'Reliability: data-plane roles let workloads consume dependencies without coupling service availability to vault administration' as proof that all five pillars pass; next, proceed on the belief that the checkpoint 'Separate control-plane and data-plane access' no longer needs its separate negative check.** — The relevant observation is that the workload receives neither Owner nor Contributor at the vault or a parent scope. Consequently, one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q39 — answer D

'Separate control-plane and data-plane access' is assigned to security assurance. A material change now applies: A managed-service provider must troubleshoot factory servers for ninety days but may not change subscription networking or receive permanent local administrator membership; revise delegation and expiry controls. Which response provides the correct revision to the decision record?

- ✗ **A. Retain Group-based Azure RBAC at stable scopes with Arc-aware local delegation at Separate control-plane and data-plane access without recalculating criteria or eligibility. Before sign-off, take it as conclusive that the original weighted result is permanent.** — The scenario makes clear that group-based Azure RBAC at stable scopes with Arc-aware local delegation. Consequently, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Direct user assignments on individual resources and servers for Separate control-plane and data-plane access without rechecking its mandatory constraints; as an independent condition, treat it as established that being different from the current design is an architecture criterion.** — The architecture evidence must show that direct user assignments on individual resources and servers. Consequently, being different is not a criterion, and the candidate still must avoid the prohibited state at Separate control-plane and data-plane access.
- ✗ **C. Keep Subscription-wide custom roles mirrored into local administrator groups eligible at Separate control-plane and data-plane access by downgrading LAB04-REQ-04; independently, use as justification the claim that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The applicable design condition is that lAB04-REQ-04. Consequently, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.
- ✓ **D. Re-score Group-based Azure RBAC at stable scopes with Arc-aware local delegation and both alternatives for Separate control-plane and data-plane access; as a separate check, supersede the ADR using the changed evidence for LAB04-REQ-04.** — The checkpoint specifically records that group-based Azure RBAC at stable scopes with Arc-aware local delegation at Separate control-plane and data-plane access. Consequently, the material change 'A managed-service provider must troubleshoot factory servers for ninety days but may not change subscription networking or receive permanent local administrator membership; revise delegation and expiry controls.' requires fresh eligibility, weighted analysis, and a superseding decision.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q40 — answer C

An assurance review of 'Separate control-plane and data-plane access' includes internal audit. After a partial run, cleanup must follow this dependency: Remove the exact run-owned role assignment; do not alter unrelated vault access. Which choice gives the team the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Delegate through groups rather than people before reconciling the current dependency. Next, treat as decisive the assertion that removing a parent needed to identify Separate control-plane and data-plane access is harmless.** — The retained result must be reconciled with the fact that delete the run-owned assignment before considering any group lifecycle action. Consequently, a cleanup rule for Delegate through groups rather than people cannot override the dependency declared for Separate control-plane and data-plane access.
- ✗ **B. Delete candidates by display name before comparing the Separate control-plane and data-plane access ownership tags, and then base approval on the claim that the dependency rule 'Remove the exact run-owned role assignment; do not alter unrelated vault access' is optional.** — The decision tension comes from the fact that synthetic workload principal, data-plane role, exact vault scope, and denied management operations. Consequently, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✓ **C. Verify exact run-state IDs and ownership tags for Separate control-plane and data-plane access; before approval, follow this dependency rule without purge: Remove the exact run-owned role assignment; do not alter unrelated vault access.** — The review is governed by this fact: remove the exact run-owned role assignment; do not alter unrelated vault access. Consequently, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **D. Destroy recoverable copies before retaining the Separate control-plane and data-plane access negative assertion 'The workload receives neither Owner nor Contributor at the vault or a parent scope'. Also, use the premise that remaining command logs are sufficient recovery evidence.** — The safe operating boundary says that the workload receives neither Owner nor Contributor at the vault or a parent scope. Consequently, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q41 — answer B

Approval of 'Define the Azure Arc authorization boundary' is questioned by internal audit. Approval requires a positive result plus this independent negative assertion: An Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted. Which answer identifies the acceptance rule that makes LAB04-REQ-05 testable?

- ✗ **A. Select Direct user assignments on individual resources and servers before checking Define the Azure Arc authorization boundary. Then, proceed on the belief that a successful deployment will later prove the architecture constraint.** — The failure model establishes that an Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted. Consequently, a deployment result cannot prove LAB04-REQ-05, and Direct user assignments on individual resources and servers still has to meet the mandatory boundary.
- ✓ **B. Require the documented positive state for Define the Azure Arc authorization boundary; independently, verify that an Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted.** — The traceable checkpoint outcome is that azure resource actions and guest operating-system privileges have separate accountable delegation paths. Consequently, the positive state and an independent negative assertion jointly make LAB04-REQ-05 testable.
- ✗ **C. Use the passing result from Model scopes and inherited access to approve Define the Azure Arc authorization boundary; afterward, treat as decisive the assertion that one control establishes an unrelated acceptance boundary.** — The recovery guidance assumes that stable management scopes and group assignments explain both direct and inherited effective access. Consequently, that outcome belongs to Model scopes and inherited access and leaves Define the Azure Arc authorization boundary unverified.
- ✗ **D. Choose Subscription-wide custom roles mirrored into local administrator groups and skip the Define the Azure Arc authorization boundary negative assertion; then base approval on the claim that the candidate has the lowest implementation effort.** — The WAF consequence identifies that reduce standing privilege and audit ambiguity without preventing platform and factory teams from meeting support obligations. Consequently, implementation effort cannot justify skipping the negative assertion or displace LAB04-REQ-05.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q42 — answer B

The implementation review has reached 'Define the Azure Arc authorization boundary'. The selected architecture is Group-based Azure RBAC at stable scopes with Arc-aware local delegation; object existence alone is not success. What recommendation gives the reviewers the intended successful finding?

- ✗ **A. Use only the negative assertion 'An Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted' as the success result; in a separate step, use as justification the claim that absence proves every required positive property.** — an Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted. For this case, this is the independent prohibited-state assertion, not a successful finding.
- ✓ **B. Record azure resource actions and guest operating-system privileges have separate accountable delegation paths. Independently, classify it as success for LAB04-REQ-05.** — The command-level assertion is anchored in the fact that azure resource actions and guest operating-system privileges have separate accountable delegation paths. Consequently, this is the authored target state for Define the Azure Arc authorization boundary and directly supports LAB04-REQ-05.
- ✗ **C. Use the successful finding from Delegate through groups rather than people as the result for Define the Azure Arc authorization boundary. As another control, accept without proof that a property from the current checkpoint does not need to be inspected.** — The controlling fact is that the operating team receives resource-group Contributor through an owned Microsoft Entra group. For this case, evidence for Delegate through groups rather than people cannot substitute for the properties required at Define the Azure Arc authorization boundary.
- ✗ **D. Record the failure condition 'Teams conflate Arc resource management with guest configuration or local sign-in rights' as a successful state; as a separate check, rely on the claim that the command returned an object.** — The authored acceptance boundary states that teams conflate Arc resource management with guest configuration or local sign-in rights. For this case, resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q43 — answer C

The approach to 'Define the Azure Arc authorization boundary' is challenged by factory operations. Evidence must address this risk without retaining credentials: Teams conflate Arc resource management with guest configuration or local sign-in rights. Which action produces sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Constrain a custom control-plane role for Define the Azure Arc authorization boundary. Separately, use the premise that a related checkpoint proves the current expected state.** — The checkpoint specifically records that role definition hash, actions, notActions, dataActions, and assignable scopes. For this case, that evidence supports Constrain a custom control-plane role, so it cannot demonstrate Azure resource actions and guest operating-system privileges have separate accountable delegation paths.
- ✗ **B. Store unredacted Define the Azure Arc authorization boundary output with operator, tenant, token, and request context; for this decision, consider it sufficient that reproduction requires every captured field.** — The scenario makes clear that unredacted implementation output. For this case, identity, tenant, or token material exceeds the non-secret evidence contract.
- ✓ **C. Retain synthetic Arc resource ID, Azure role path, local-role owner, elevation mechanism, and review cadence; in a separate step, exclude credentials and unrelated response fields.** — The relevant observation is that synthetic Arc resource ID, Azure role path, local-role owner, elevation mechanism, and review cadence. For this case, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **D. Record only the Define the Azure Arc authorization boundary positive inspection's exit status. Before sign-off, take it as conclusive that projected properties and assertion results can be reconstructed later.** — The architecture evidence must show that the positive inspection's exit status. For this case, an exit code alone does not show whether azure resource actions and guest operating-system privileges have separate accountable delegation paths.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q44 — answer B

A decision test for 'Define the Azure Arc authorization boundary' includes security assurance. The target is Azure resource actions and guest operating-system privileges have separate accountable delegation paths, but the latest evidence does not show it. What best demonstrates the most likely cause?

- ✗ **A. Treat 'The vault still uses access policies or an inherited management role supplies unintended power' as grounds to reject Define the Azure Arc authorization boundary; then rely on the belief that separate control-plane and data-plane access's failure model applies unchanged here.** — The review is governed by this fact: the vault still uses access policies or an inherited management role supplies unintended power. For this case, that condition belongs to Separate control-plane and data-plane access and does not by itself invalidate Group-based Azure RBAC at stable scopes with Arc-aware local delegation.
- ✓ **B. Investigate teams conflate Arc resource management with guest configuration or local sign-in rights; next, isolate that cause before changing Group-based Azure RBAC at stable scopes with Arc-aware local delegation.** — The applicable design condition is that teams conflate Arc resource management with guest configuration or local sign-in rights. For this case, it is the checkpoint's causal failure model and should be isolated before retrying Define the Azure Arc authorization boundary.
- ✗ **C. Ignore the negative assertion 'An Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted'. Independently, proceed on the belief that a later material change will make it unnecessary.** — The retained result must be reconciled with the fact that an Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted. For this case, the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Model scopes and inherited access instead of diagnosing Define the Azure Arc authorization boundary. Next, treat as decisive the assertion that a passing result at Model scopes and inherited access identifies the current cause.** — The decision tension comes from the fact that stable management scopes and group assignments explain both direct and inherited effective access. For this case, a passing result at Model scopes and inherited access gives no causal evidence for the failure at Define the Azure Arc authorization boundary.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q45 — answer A

The architecture board reconsiders 'Define the Azure Arc authorization boundary' with internal audit. The run encountered this modeled failure: Teams conflate Arc resource management with guest configuration or local sign-in rights. Which option is the safest recovery action?

- ✓ **A. Split the permission matrix by control plane, Arc extension action, and guest operating-system action; for this decision, preserve the current run identity and evidence.** — The safe operating boundary says that split the permission matrix by control plane, Arc extension action, and guest operating-system action. For this case, it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **B. Perform cleanup immediately: Remove only tagged run-owned Azure assignments; never alter a connected server or local group automatically; as a separate check, treat it as established that the failed operation and its returned identifiers do not need reconciliation.** — The traceable checkpoint outcome is that remove only tagged run-owned Azure assignments; never alter a connected server or local group automatically. For this case, cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **C. Create a different run identity before diagnosing 'Teams conflate Arc resource management with guest configuration or local sign-in rights'. Afterward, use as justification the claim that the first state record and returned identifiers can be discarded.** — The failure model establishes that teams conflate Arc resource management with guest configuration or local sign-in rights. For this case, discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Model scopes and inherited access instead; next, accept without proof that success at Model scopes and inherited access will repair the failed state at Define the Azure Arc authorization boundary.** — The recovery guidance assumes that stable management scopes and group assignments explain both direct and inherited effective access. For this case, altering an already separate checkpoint does not repair the modeled failure at Define the Azure Arc authorization boundary.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q46 — answer A

A review of 'Define the Azure Arc authorization boundary' begins with input from cloud platform owner. Without making a new change, the team must inspect the risk 'Teams conflate Arc resource management with guest configuration or local sign-in rights' using the Azure CLI lane. What should the architect select as the read-only, lane-correct inspection?

- ✓ **A. Inspect the documented properties for Define the Azure Arc authorization boundary. Then, retain this evidence: synthetic Arc resource ID, Azure role path, local-role owner, elevation mechanism, and review cadence.** — The WAF consequence identifies that azure resource actions and guest operating-system privileges have separate accountable delegation paths. For this case, the read-only inspection directly tests the properties required at Define the Azure Arc authorization boundary.
- ✗ **B. Rerun the Define the Azure Arc authorization boundary implementation command and infer the expected state. Before sign-off, base approval on the claim that absence of a shell error proves every property.** — The command-level assertion is anchored in the fact that the implementation command. For this case, it can mutate state and shell success does not independently assert the expected properties.
- ✗ **C. Run only this negative inspection for Define the Azure Arc authorization boundary: An Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted; as an independent condition, use the premise that an empty negative result reports every required positive property.** — the negative inspection. That evidence means absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Delegate through groups rather than people and apply it to Define the Azure Arc authorization boundary; before approval, consider it sufficient that any command from the same lane proves the current checkpoint.** — The controlling fact is that the positive inspection for Delegate through groups rather than people. That evidence means it is lane-correct but proves Delegate through groups rather than people, not Define the Azure Arc authorization boundary.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q47 — answer C

'Define the Azure Arc authorization boundary' awaits approval from factory operations. A passing positive check does not by itself prove this negative assertion: An Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted. Select the assertion pair that proves both conditions independently.

- ✗ **A. Verify only the positive result for Define the Azure Arc authorization boundary and report full compliance. Next, rely on the claim that every prohibited parallel state must therefore be absent.** — The relevant observation is that azure resource actions and guest operating-system privileges have separate accountable delegation paths. That evidence means the positive result alone does not test the explicit anti-condition 'An Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted'.
- ✗ **B. Prove only that an Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted and report the intended configuration as present, and then rely on the belief that absence is equivalent to positive-state evidence.** — The checkpoint specifically records that an Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted. That evidence means absence evidence cannot demonstrate the required positive state 'Azure resource actions and guest operating-system privileges have separate accountable delegation paths'.
- ✓ **C. Verify the positive properties for Define the Azure Arc authorization boundary. Next, independently verify that an Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted.** — The authored acceptance boundary states that azure resource actions and guest operating-system privileges have separate accountable delegation paths; An Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted. That evidence means two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **D. Use Constrain a custom control-plane role's negative assertion for Define the Azure Arc authorization boundary. Also, proceed on the belief that negative assertions are interchangeable between checkpoints.** — The scenario makes clear that no wildcard action, role-assignment write, or destructive permission is granted. That evidence means the second assertion is valid for Constrain a custom control-plane role but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q48 — answer B

'Define the Azure Arc authorization boundary' is reopened at the request of security assurance. The board wants the Well-Architected consequence of mitigating this risk: Teams conflate Arc resource management with guest configuration or local sign-in rights. Which response provides the consequence attributable to this checkpoint?

- ✗ **A. Use the Separate control-plane and data-plane access consequence as the result for Define the Azure Arc authorization boundary; next, take it as conclusive that a pillar statement remains valid when moved away from Separate control-plane and data-plane access.** — The applicable design condition is that reliability: data-plane roles let workloads consume dependencies without coupling service availability to vault administration. That evidence means that tradeoff belongs to Separate control-plane and data-plane access and does not explain this checkpoint's decision.
- ✓ **B. Record this consequence: Security: the hybrid boundary prevents Azure control-plane access from being mistaken for guest administrator privilege. As another control, tie it to LAB04-REQ-05.** — The architecture evidence must show that security: the hybrid boundary prevents Azure control-plane access from being mistaken for guest administrator privilege. That evidence means it states the authored pillar consequence of the control evaluated at Define the Azure Arc authorization boundary.
- ✗ **C. Remove the control responsible for the Define the Azure Arc authorization boundary outcome. In addition, treat it as established that a low cost classification outweighs the mandatory architecture state.** — The review is governed by this fact: the required outcome at Define the Azure Arc authorization boundary. That evidence means cost Optimization cannot remove the acceptance condition 'Azure resource actions and guest operating-system privileges have separate accountable delegation paths'.
- ✗ **D. Treat 'Security: the hybrid boundary prevents Azure control-plane access from being mistaken for guest administrator privilege' as proof that all five pillars pass; before approval, use as justification the claim that the checkpoint 'Define the Azure Arc authorization boundary' no longer needs its separate negative check.** — The retained result must be reconciled with the fact that an Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted. That evidence means one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q49 — answer D

A design review of 'Define the Azure Arc authorization boundary' includes internal audit. A material change now applies: A managed-service provider must troubleshoot factory servers for ninety days but may not change subscription networking or receive permanent local administrator membership; revise delegation and expiry controls. Which choice gives the team the correct revision to the decision record?

- ✗ **A. Retain Group-based Azure RBAC at stable scopes with Arc-aware local delegation at Define the Azure Arc authorization boundary without recalculating criteria or eligibility; as a second control, treat as decisive the assertion that the original weighted result is permanent.** — The safe operating boundary says that group-based Azure RBAC at stable scopes with Arc-aware local delegation. That evidence means the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Direct user assignments on individual resources and servers for Define the Azure Arc authorization boundary without rechecking its mandatory constraints. Then, base approval on the claim that being different from the current design is an architecture criterion.** — The traceable checkpoint outcome is that direct user assignments on individual resources and servers. That evidence means being different is not a criterion, and the candidate still must avoid the prohibited state at Define the Azure Arc authorization boundary.
- ✗ **C. Keep Subscription-wide custom roles mirrored into local administrator groups eligible at Define the Azure Arc authorization boundary by downgrading LAB04-REQ-05; afterward, use the premise that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The failure model establishes that lAB04-REQ-05. That evidence means an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.
- ✓ **D. Re-score Group-based Azure RBAC at stable scopes with Arc-aware local delegation and both alternatives for Define the Azure Arc authorization boundary. In addition, supersede the ADR using the changed evidence for LAB04-REQ-05.** — The decision tension comes from the fact that group-based Azure RBAC at stable scopes with Arc-aware local delegation at Define the Azure Arc authorization boundary. That evidence means the material change 'A managed-service provider must troubleshoot factory servers for ninety days but may not change subscription networking or receive permanent local administrator membership; revise delegation and expiry controls.' requires fresh eligibility, weighted analysis, and a superseding decision.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)

## LAB04-Q50 — answer D

The team asks cloud platform owner to assess 'Define the Azure Arc authorization boundary'. After a partial run, cleanup must follow this dependency: Remove only tagged run-owned Azure assignments; never alter a connected server or local group automatically. What is the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Delegate through groups rather than people before reconciling the current dependency. Also, accept without proof that removing a parent needed to identify Define the Azure Arc authorization boundary is harmless.** — The WAF consequence identifies that delete the run-owned assignment before considering any group lifecycle action. That evidence means a cleanup rule for Delegate through groups rather than people cannot override the dependency declared for Define the Azure Arc authorization boundary.
- ✗ **B. Delete candidates by display name before comparing the Define the Azure Arc authorization boundary ownership tags; in a separate step, rely on the claim that the dependency rule 'Remove only tagged run-owned Azure assignments; never alter a connected server or local group automatically' is optional.** — The command-level assertion is anchored in the fact that synthetic Arc resource ID, Azure role path, local-role owner, elevation mechanism, and review cadence. That evidence means names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **C. Destroy recoverable copies before retaining the Define the Azure Arc authorization boundary negative assertion 'An Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted'. As another control, rely on the belief that remaining command logs are sufficient recovery evidence.** — an Azure assignment is not assumed to grant local administrator access, and no direct-user exception is accepted. The resulting architectural conclusion is that irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.
- ✓ **D. Verify exact run-state IDs and ownership tags for Define the Azure Arc authorization boundary. Before sign-off, follow this dependency rule without purge: Remove only tagged run-owned Azure assignments; never alter a connected server or local group automatically.** — The recovery guidance assumes that remove only tagged run-owned Azure assignments; never alter a connected server or local group automatically. That evidence means exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/role-based-access-control/best-practices (verified 2026-09-02)
<!-- END GENERATED AZ305 V1 -->
