<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-01 answer key

Use after completing the learner assessment. Every choice has a specific explanation.

## LAB01-Q01 — answer A

A review of 'Establish regional workspace boundaries' begins with input from security operations. Approval requires a positive result plus this independent negative assertion: No unapproved workspace is selected as a destination for this run. Which option is the acceptance rule that makes LAB01-REQ-01 testable?

- ✓ **A. Require the documented positive state for Establish regional workspace boundaries; separately, verify that no unapproved workspace is selected as a destination for this run.** — the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. Consequently, the positive state and an independent negative assertion jointly make LAB01-REQ-01 testable.
- ✗ **B. Select Central Log Analytics workspace with DCR-based collection and archive export before checking Establish regional workspace boundaries. Then, rely on the belief that a successful deployment will later prove the architecture constraint.** — The controlling fact is that no unapproved workspace is selected as a destination for this run. Consequently, a deployment result cannot prove LAB01-REQ-01, and Central Log Analytics workspace with DCR-based collection and archive export still has to meet the mandatory boundary.
- ✗ **C. Use the passing result from Define an Azure Monitor Agent data collection rule to approve Establish regional workspace boundaries; afterward, proceed on the belief that one control establishes an unrelated acceptance boundary.** — The authored acceptance boundary states that the DCR maps only the required streams to a named Log Analytics destination. Consequently, that outcome belongs to Define an Azure Monitor Agent data collection rule and leaves Establish regional workspace boundaries unverified.
- ✗ **D. Choose Dedicated workspace per workload with independent retention and access and skip the Establish regional workspace boundaries negative assertion; then treat as decisive the assertion that the candidate has the lowest implementation effort.** — The relevant observation is that reduce incident investigation time while giving security and regional operators governed access to complete, correctly routed telemetry. Consequently, implementation effort cannot justify skipping the negative assertion or displace LAB01-REQ-01.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q02 — answer C

'Establish regional workspace boundaries' awaits approval from regional platform teams. The selected architecture is Regional workspaces with cross-workspace queries and policy-driven routing; object existence alone is not success. What should the architect select as the intended successful finding?

- ✗ **A. Use only the negative assertion 'No unapproved workspace is selected as a destination for this run' as the success result; in a separate step, treat it as established that absence proves every required positive property.** — The scenario makes clear that no unapproved workspace is selected as a destination for this run. Consequently, this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Associate the rule with an explicit resource scope as the result for Establish regional workspace boundaries. As another control, use as justification the claim that a property from the current checkpoint does not need to be inspected.** — The architecture evidence must show that the target has one intentional association to the approved DCR. Consequently, evidence for Associate the rule with an explicit resource scope cannot substitute for the properties required at Establish regional workspace boundaries.
- ✓ **C. Record the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. Independently, classify it as success for LAB01-REQ-01.** — The checkpoint specifically records that the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. Consequently, this is the authored target state for Establish regional workspace boundaries and directly supports LAB01-REQ-01.
- ✗ **D. Record the failure condition 'A conflicting regional residency rule or unavailable workspace SKU blocks the chosen topology' as a successful state; as a separate check, accept without proof that the command returned an object.** — The applicable design condition is that a conflicting regional residency rule or unavailable workspace SKU blocks the chosen topology. Consequently, resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q03 — answer B

'Establish regional workspace boundaries' is reopened at the request of data protection officer. Evidence must address this risk without retaining credentials: A conflicting regional residency rule or unavailable workspace SKU blocks the chosen topology. Select sufficient, properly scoped evidence.

- ✗ **A. Substitute the evidence from Route resource logs with diagnostic settings for Establish regional workspace boundaries. Separately, base approval on the claim that a related checkpoint proves the current expected state.** — The retained result must be reconciled with the fact that diagnostic-setting name, enabled categories, destination IDs, and export mode. Consequently, that evidence supports Route resource logs with diagnostic settings, so it cannot demonstrate The workspace is in the approved data boundary with thirty-day interactive retention and ownership tags.
- ✓ **B. Retain sanitized workspace name, region, retention, and resource ID; in a separate step, exclude credentials and unrelated response fields.** — The review is governed by this fact: sanitized workspace name, region, retention, and resource ID. Consequently, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **C. Store unredacted Establish regional workspace boundaries output with operator, tenant, token, and request context; for this decision, use the premise that reproduction requires every captured field.** — The decision tension comes from the fact that unredacted implementation output. Consequently, identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **D. Record only the Establish regional workspace boundaries positive inspection's exit status. Before sign-off, consider it sufficient that projected properties and assertion results can be reconstructed later.** — The safe operating boundary says that the positive inspection's exit status. Consequently, an exit code alone does not show whether the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q04 — answer A

A design review of 'Establish regional workspace boundaries' includes finOps. The target is The workspace is in the approved data boundary with thirty-day interactive retention and ownership tags, but the latest evidence does not show it. Which response provides the most likely cause?

- ✓ **A. Investigate a conflicting regional residency rule or unavailable workspace SKU blocks the chosen topology; next, isolate that cause before changing Regional workspaces with cross-workspace queries and policy-driven routing.** — The traceable checkpoint outcome is that a conflicting regional residency rule or unavailable workspace SKU blocks the chosen topology. Consequently, it is the checkpoint's causal failure model and should be isolated before retrying Establish regional workspace boundaries.
- ✗ **B. Treat 'Workspace defaults obscure a table-specific compliance or cost requirement' as grounds to reject Establish regional workspace boundaries; then rely on the claim that validate retention and archive economics's failure model applies unchanged here.** — The failure model establishes that workspace defaults obscure a table-specific compliance or cost requirement. Consequently, that condition belongs to Validate retention and archive economics and does not by itself invalidate Regional workspaces with cross-workspace queries and policy-driven routing.
- ✗ **C. Ignore the negative assertion 'No unapproved workspace is selected as a destination for this run'. Independently, rely on the belief that a later material change will make it unnecessary.** — The recovery guidance assumes that no unapproved workspace is selected as a destination for this run. Consequently, the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Define an Azure Monitor Agent data collection rule instead of diagnosing Establish regional workspace boundaries. Next, proceed on the belief that a passing result at Define an Azure Monitor Agent data collection rule identifies the current cause.** — The WAF consequence identifies that the DCR maps only the required streams to a named Log Analytics destination. Consequently, a passing result at Define an Azure Monitor Agent data collection rule gives no causal evidence for the failure at Establish regional workspace boundaries.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q05 — answer D

The team asks security operations to assess 'Establish regional workspace boundaries'. The run encountered this modeled failure: A conflicting regional residency rule or unavailable workspace SKU blocks the chosen topology. Which choice gives the team the safest recovery action?

- ✗ **A. Perform cleanup immediately: Remove diagnostic settings and DCR associations before deleting the workspace; as a separate check, take it as conclusive that the failed operation and its returned identifiers do not need reconciliation.** — remove diagnostic settings and DCR associations before deleting the workspace. For this case, cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **B. Create a different run identity before diagnosing 'A conflicting regional residency rule or unavailable workspace SKU blocks the chosen topology'. Afterward, treat it as established that the first state record and returned identifiers can be discarded.** — The controlling fact is that a conflicting regional residency rule or unavailable workspace SKU blocks the chosen topology. For this case, discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **C. Change Define an Azure Monitor Agent data collection rule instead; next, use as justification the claim that success at Define an Azure Monitor Agent data collection rule will repair the failed state at Establish regional workspace boundaries.** — The authored acceptance boundary states that the DCR maps only the required streams to a named Log Analytics destination. For this case, altering an already separate checkpoint does not repair the modeled failure at Establish regional workspace boundaries.
- ✓ **D. Re-evaluate the approved region and pricing tier, retain the same RunId, and preview before execution; for this decision, preserve the current run identity and evidence.** — The command-level assertion is anchored in the fact that re-evaluate the approved region and pricing tier, retain the same RunId, and preview before execution. Consequently, it corrects the narrow cause while retaining the same recovery trail and decision scope.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q06 — answer B

A recommendation on 'Establish regional workspace boundaries' is requested by regional platform teams. Without making a new change, the team must inspect the risk 'A conflicting regional residency rule or unavailable workspace SKU blocks the chosen topology' using the Azure CLI lane. What is the read-only, lane-correct inspection?

- ✗ **A. Rerun the Establish regional workspace boundaries implementation command and infer the expected state. Before sign-off, treat as decisive the assertion that absence of a shell error proves every property.** — The checkpoint specifically records that the implementation command. For this case, it can mutate state and shell success does not independently assert the expected properties.
- ✓ **B. Inspect the documented properties for Establish regional workspace boundaries. Then, retain this evidence: sanitized workspace name, region, retention, and resource ID.** — The relevant observation is that the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. For this case, the read-only inspection directly tests the properties required at Establish regional workspace boundaries.
- ✗ **C. Run only this negative inspection for Establish regional workspace boundaries: No unapproved workspace is selected as a destination for this run; as an independent condition, base approval on the claim that an empty negative result reports every required positive property.** — The scenario makes clear that the negative inspection. For this case, absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Associate the rule with an explicit resource scope and apply it to Establish regional workspace boundaries; before approval, use the premise that any command from the same lane proves the current checkpoint.** — The architecture evidence must show that the positive inspection for Associate the rule with an explicit resource scope. For this case, it is lane-correct but proves Associate the rule with an explicit resource scope, not Establish regional workspace boundaries.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q07 — answer C

'Establish regional workspace boundaries' is assigned to data protection officer. A passing positive check does not by itself prove this negative assertion: No unapproved workspace is selected as a destination for this run. Which recommendation supplies the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Establish regional workspace boundaries and report full compliance. Next, accept without proof that every prohibited parallel state must therefore be absent.** — The review is governed by this fact: the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. For this case, the positive result alone does not test the explicit anti-condition 'No unapproved workspace is selected as a destination for this run'.
- ✗ **B. Prove only that no unapproved workspace is selected as a destination for this run and report the intended configuration as present, and then rely on the claim that absence is equivalent to positive-state evidence.** — The retained result must be reconciled with the fact that no unapproved workspace is selected as a destination for this run. For this case, absence evidence cannot demonstrate the required positive state 'The workspace is in the approved data boundary with thirty-day interactive retention and ownership tags'.
- ✓ **C. Verify the positive properties for Establish regional workspace boundaries. Next, independently verify that no unapproved workspace is selected as a destination for this run.** — The applicable design condition is that the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags; No unapproved workspace is selected as a destination for this run. For this case, two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **D. Use Route resource logs with diagnostic settings's negative assertion for Establish regional workspace boundaries. Also, rely on the belief that negative assertions are interchangeable between checkpoints.** — The decision tension comes from the fact that event Hubs or storage are not silently configured as extra destinations. For this case, the second assertion is valid for Route resource logs with diagnostic settings but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q08 — answer B

An assurance review of 'Establish regional workspace boundaries' includes finOps. The board wants the Well-Architected consequence of mitigating this risk: A conflicting regional residency rule or unavailable workspace SKU blocks the chosen topology. Choose the consequence attributable to this checkpoint.

- ✗ **A. Use the Validate retention and archive economics consequence as the result for Establish regional workspace boundaries; next, consider it sufficient that a pillar statement remains valid when moved away from Validate retention and archive economics.** — The traceable checkpoint outcome is that cost Optimization: table-level retention aligns searchable and archived data with its continuing value. For this case, that tradeoff belongs to Validate retention and archive economics and does not explain this checkpoint's decision.
- ✓ **B. Record this consequence: Reliability: regional telemetry boundaries remain available and supportable during an incident. As another control, tie it to LAB01-REQ-01.** — The safe operating boundary says that reliability: regional telemetry boundaries remain available and supportable during an incident. For this case, it states the authored pillar consequence of the control evaluated at Establish regional workspace boundaries.
- ✗ **C. Remove the control responsible for the Establish regional workspace boundaries outcome. In addition, take it as conclusive that a moderate cost classification outweighs the mandatory architecture state.** — The failure model establishes that the required outcome at Establish regional workspace boundaries. For this case, cost Optimization cannot remove the acceptance condition 'The workspace is in the approved data boundary with thirty-day interactive retention and ownership tags'.
- ✗ **D. Treat 'Reliability: regional telemetry boundaries remain available and supportable during an incident' as proof that all five pillars pass; before approval, treat it as established that the checkpoint 'Establish regional workspace boundaries' no longer needs its separate negative check.** — The recovery guidance assumes that no unapproved workspace is selected as a destination for this run. For this case, one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q09 — answer C

Approval of 'Establish regional workspace boundaries' is questioned by security operations. A material change now applies: A new regulator requires security control-plane records to remain in-region for seven years while application traces must stay searchable for only thirty days; revise routing and retention without duplicating every stream. Which answer describes the correct revision to the decision record?

- ✗ **A. Retain Regional workspaces with cross-workspace queries and policy-driven routing at Establish regional workspace boundaries without recalculating criteria or eligibility; as a second control, proceed on the belief that the original weighted result is permanent.** — The command-level assertion is anchored in the fact that regional workspaces with cross-workspace queries and policy-driven routing. For this case, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Central Log Analytics workspace with DCR-based collection and archive export for Establish regional workspace boundaries without rechecking its mandatory constraints. Then, treat as decisive the assertion that being different from the current design is an architecture criterion.** — central Log Analytics workspace with DCR-based collection and archive export. That evidence means being different is not a criterion, and the candidate still must avoid the prohibited state at Establish regional workspace boundaries.
- ✓ **C. Re-score Regional workspaces with cross-workspace queries and policy-driven routing and both alternatives for Establish regional workspace boundaries. In addition, supersede the ADR using the changed evidence for LAB01-REQ-01.** — The WAF consequence identifies that regional workspaces with cross-workspace queries and policy-driven routing at Establish regional workspace boundaries. For this case, the material change 'A new regulator requires security control-plane records to remain in-region for seven years while application traces must stay searchable for only thirty days; revise routing and retention without duplicating every stream.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **D. Keep Dedicated workspace per workload with independent retention and access eligible at Establish regional workspace boundaries by downgrading LAB01-REQ-01; afterward, base approval on the claim that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The controlling fact is that lAB01-REQ-01. That evidence means an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q10 — answer D

The implementation review has reached 'Establish regional workspace boundaries'. After a partial run, cleanup must follow this dependency: Remove diagnostic settings and DCR associations before deleting the workspace. What should be recorded as the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Associate the rule with an explicit resource scope before reconciling the current dependency. Also, use as justification the claim that removing a parent needed to identify Establish regional workspace boundaries is harmless.** — The relevant observation is that delete the association before its DCR or target resource. That evidence means a cleanup rule for Associate the rule with an explicit resource scope cannot override the dependency declared for Establish regional workspace boundaries.
- ✗ **B. Delete candidates by display name before comparing the Establish regional workspace boundaries ownership tags; in a separate step, accept without proof that the dependency rule 'Remove diagnostic settings and DCR associations before deleting the workspace' is optional.** — The checkpoint specifically records that sanitized workspace name, region, retention, and resource ID. That evidence means names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **C. Destroy recoverable copies before retaining the Establish regional workspace boundaries negative assertion 'No unapproved workspace is selected as a destination for this run'. As another control, rely on the claim that remaining command logs are sufficient recovery evidence.** — The scenario makes clear that no unapproved workspace is selected as a destination for this run. That evidence means irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.
- ✓ **D. Verify exact run-state IDs and ownership tags for Establish regional workspace boundaries. Before sign-off, follow this dependency rule without purge: Remove diagnostic settings and DCR associations before deleting the workspace.** — The authored acceptance boundary states that remove diagnostic settings and DCR associations before deleting the workspace. That evidence means exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q11 — answer A

The approach to 'Define an Azure Monitor Agent data collection rule' is challenged by regional platform teams. Approval requires a positive result plus this independent negative assertion: No legacy Log Analytics agent or unapproved stream is represented in the rule. What should the architect select as the acceptance rule that makes LAB01-REQ-02 testable?

- ✓ **A. Require the documented positive state for Define an Azure Monitor Agent data collection rule; then verify that no legacy Log Analytics agent or unapproved stream is represented in the rule.** — The architecture evidence must show that the DCR maps only the required streams to a named Log Analytics destination. That evidence means the positive state and an independent negative assertion jointly make LAB01-REQ-02 testable.
- ✗ **B. Select Central Log Analytics workspace with DCR-based collection and archive export before checking Define an Azure Monitor Agent data collection rule; then treat it as established that a successful deployment will later prove the architecture constraint.** — The applicable design condition is that no legacy Log Analytics agent or unapproved stream is represented in the rule. That evidence means a deployment result cannot prove LAB01-REQ-02, and Central Log Analytics workspace with DCR-based collection and archive export still has to meet the mandatory boundary.
- ✗ **C. Use the passing result from Establish regional workspace boundaries to approve Define an Azure Monitor Agent data collection rule. Independently, use as justification the claim that one control establishes an unrelated acceptance boundary.** — The review is governed by this fact: the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. That evidence means that outcome belongs to Establish regional workspace boundaries and leaves Define an Azure Monitor Agent data collection rule unverified.
- ✗ **D. Choose Dedicated workspace per workload with independent retention and access and skip the Define an Azure Monitor Agent data collection rule negative assertion. Next, accept without proof that the candidate has the lowest implementation effort.** — The retained result must be reconciled with the fact that reduce incident investigation time while giving security and regional operators governed access to complete, correctly routed telemetry. That evidence means implementation effort cannot justify skipping the negative assertion or displace LAB01-REQ-02.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q12 — answer C

A decision test for 'Define an Azure Monitor Agent data collection rule' includes data protection officer. The selected architecture is Regional workspaces with cross-workspace queries and policy-driven routing; object existence alone is not success. Select the intended successful finding.

- ✗ **A. Use only the negative assertion 'No legacy Log Analytics agent or unapproved stream is represented in the rule' as the success result; as a separate check, base approval on the claim that absence proves every required positive property.** — The safe operating boundary says that no legacy Log Analytics agent or unapproved stream is represented in the rule. That evidence means this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Associate the rule with an explicit resource scope as the result for Define an Azure Monitor Agent data collection rule. Afterward, use the premise that a property from the current checkpoint does not need to be inspected.** — The traceable checkpoint outcome is that the target has one intentional association to the approved DCR. That evidence means evidence for Associate the rule with an explicit resource scope cannot substitute for the properties required at Define an Azure Monitor Agent data collection rule.
- ✓ **C. Record the DCR maps only the required streams to a named Log Analytics destination. Also, classify it as success for LAB01-REQ-02.** — The decision tension comes from the fact that the DCR maps only the required streams to a named Log Analytics destination. That evidence means this is the authored target state for Define an Azure Monitor Agent data collection rule and directly supports LAB01-REQ-02.
- ✗ **D. Record the failure condition 'A stream name is incompatible with the selected data source or destination' as a successful state; next, consider it sufficient that the command returned an object.** — The failure model establishes that a stream name is incompatible with the selected data source or destination. That evidence means resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q13 — answer B

The architecture board reconsiders 'Define an Azure Monitor Agent data collection rule' with finOps. Evidence must address this risk without retaining credentials: A stream name is incompatible with the selected data source or destination. Which response provides sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Route resource logs with diagnostic settings for Define an Azure Monitor Agent data collection rule. Before sign-off, rely on the claim that a related checkpoint proves the current expected state.** — The WAF consequence identifies that diagnostic-setting name, enabled categories, destination IDs, and export mode. That evidence means that evidence supports Route resource logs with diagnostic settings, so it cannot demonstrate The DCR maps only the required streams to a named Log Analytics destination.
- ✓ **B. Retain dCR resource ID, stream names, destinations, and source file hash. Afterward, exclude credentials and unrelated response fields.** — The recovery guidance assumes that dCR resource ID, stream names, destinations, and source file hash. That evidence means it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **C. Store unredacted Define an Azure Monitor Agent data collection rule output with operator, tenant, token, and request context; as an independent condition, rely on the belief that reproduction requires every captured field.** — The command-level assertion is anchored in the fact that unredacted implementation output. That evidence means identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **D. Record only the Define an Azure Monitor Agent data collection rule positive inspection's exit status; as a second control, proceed on the belief that projected properties and assertion results can be reconstructed later.** — the positive inspection's exit status. The resulting architectural conclusion is that an exit code alone does not show whether the DCR maps only the required streams to a named Log Analytics destination.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q14 — answer A

A review of 'Define an Azure Monitor Agent data collection rule' begins with input from security operations. The target is The DCR maps only the required streams to a named Log Analytics destination, but the latest evidence does not show it. Which choice gives the team the most likely cause?

- ✓ **A. Investigate a stream name is incompatible with the selected data source or destination. Separately, isolate that cause before changing Regional workspaces with cross-workspace queries and policy-driven routing.** — The controlling fact is that a stream name is incompatible with the selected data source or destination. The resulting architectural conclusion is that it is the checkpoint's causal failure model and should be isolated before retrying Define an Azure Monitor Agent data collection rule.
- ✗ **B. Treat 'Workspace defaults obscure a table-specific compliance or cost requirement' as grounds to reject Define an Azure Monitor Agent data collection rule. Next, take it as conclusive that validate retention and archive economics's failure model applies unchanged here.** — The authored acceptance boundary states that workspace defaults obscure a table-specific compliance or cost requirement. The resulting architectural conclusion is that that condition belongs to Validate retention and archive economics and does not by itself invalidate Regional workspaces with cross-workspace queries and policy-driven routing.
- ✗ **C. Ignore the negative assertion 'No legacy Log Analytics agent or unapproved stream is represented in the rule', and then treat it as established that a later material change will make it unnecessary.** — The relevant observation is that no legacy Log Analytics agent or unapproved stream is represented in the rule. The resulting architectural conclusion is that the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Establish regional workspace boundaries instead of diagnosing Define an Azure Monitor Agent data collection rule. Also, use as justification the claim that a passing result at Establish regional workspace boundaries identifies the current cause.** — The checkpoint specifically records that the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. The resulting architectural conclusion is that a passing result at Establish regional workspace boundaries gives no causal evidence for the failure at Define an Azure Monitor Agent data collection rule.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q15 — answer A

'Define an Azure Monitor Agent data collection rule' awaits approval from regional platform teams. The run encountered this modeled failure: A stream name is incompatible with the selected data source or destination. What is the safest recovery action?

- ✓ **A. Correct artifacts/dcr.json against the current DCR schema and rerun the preview; as a second control, preserve the current run identity and evidence.** — The scenario makes clear that correct artifacts/dcr.json against the current DCR schema and rerun the preview. The resulting architectural conclusion is that it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **B. Perform cleanup immediately: Delete all DCR associations before deleting the DCR; next, treat as decisive the assertion that the failed operation and its returned identifiers do not need reconciliation.** — The architecture evidence must show that delete all DCR associations before deleting the DCR. The resulting architectural conclusion is that cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **C. Create a different run identity before diagnosing 'A stream name is incompatible with the selected data source or destination'. In addition, base approval on the claim that the first state record and returned identifiers can be discarded.** — The applicable design condition is that a stream name is incompatible with the selected data source or destination. The resulting architectural conclusion is that discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Establish regional workspace boundaries instead; before approval, use the premise that success at Establish regional workspace boundaries will repair the failed state at Define an Azure Monitor Agent data collection rule.** — The review is governed by this fact: the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. The resulting architectural conclusion is that altering an already separate checkpoint does not repair the modeled failure at Define an Azure Monitor Agent data collection rule.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q16 — answer A

'Define an Azure Monitor Agent data collection rule' is reopened at the request of data protection officer. Without making a new change, the team must inspect the risk 'A stream name is incompatible with the selected data source or destination' using the Azure CLI lane. Which recommendation supplies the read-only, lane-correct inspection?

- ✓ **A. Inspect the documented properties for Define an Azure Monitor Agent data collection rule. Independently, retain this evidence: dCR resource ID, stream names, destinations, and source file hash.** — The retained result must be reconciled with the fact that the DCR maps only the required streams to a named Log Analytics destination. The resulting architectural conclusion is that the read-only inspection directly tests the properties required at Define an Azure Monitor Agent data collection rule.
- ✗ **B. Rerun the Define an Azure Monitor Agent data collection rule implementation command and infer the expected state; during the same review, accept without proof that absence of a shell error proves every property.** — The decision tension comes from the fact that the implementation command. The resulting architectural conclusion is that it can mutate state and shell success does not independently assert the expected properties.
- ✗ **C. Run only this negative inspection for Define an Azure Monitor Agent data collection rule: No legacy Log Analytics agent or unapproved stream is represented in the rule. Then, rely on the claim that an empty negative result reports every required positive property.** — The safe operating boundary says that the negative inspection. The resulting architectural conclusion is that absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Associate the rule with an explicit resource scope and apply it to Define an Azure Monitor Agent data collection rule; afterward, rely on the belief that any command from the same lane proves the current checkpoint.** — The traceable checkpoint outcome is that the positive inspection for Associate the rule with an explicit resource scope. The resulting architectural conclusion is that it is lane-correct but proves Associate the rule with an explicit resource scope, not Define an Azure Monitor Agent data collection rule.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q17 — answer B

A design review of 'Define an Azure Monitor Agent data collection rule' includes finOps. A passing positive check does not by itself prove this negative assertion: No legacy Log Analytics agent or unapproved stream is represented in the rule. Choose the assertion pair that proves both conditions independently.

- ✗ **A. Verify only the positive result for Define an Azure Monitor Agent data collection rule and report full compliance. Also, consider it sufficient that every prohibited parallel state must therefore be absent.** — The recovery guidance assumes that the DCR maps only the required streams to a named Log Analytics destination. The resulting architectural conclusion is that the positive result alone does not test the explicit anti-condition 'No legacy Log Analytics agent or unapproved stream is represented in the rule'.
- ✓ **B. Verify the positive properties for Define an Azure Monitor Agent data collection rule; in a separate step, independently verify that no legacy Log Analytics agent or unapproved stream is represented in the rule.** — The failure model establishes that the DCR maps only the required streams to a named Log Analytics destination; No legacy Log Analytics agent or unapproved stream is represented in the rule. The resulting architectural conclusion is that two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **C. Prove only that no legacy Log Analytics agent or unapproved stream is represented in the rule and report the intended configuration as present; in a separate step, take it as conclusive that absence is equivalent to positive-state evidence.** — The WAF consequence identifies that no legacy Log Analytics agent or unapproved stream is represented in the rule. The resulting architectural conclusion is that absence evidence cannot demonstrate the required positive state 'The DCR maps only the required streams to a named Log Analytics destination'.
- ✗ **D. Use Route resource logs with diagnostic settings's negative assertion for Define an Azure Monitor Agent data collection rule. As another control, treat it as established that negative assertions are interchangeable between checkpoints.** — The command-level assertion is anchored in the fact that event Hubs or storage are not silently configured as extra destinations. The resulting architectural conclusion is that the second assertion is valid for Route resource logs with diagnostic settings but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q18 — answer D

The team asks security operations to assess 'Define an Azure Monitor Agent data collection rule'. The board wants the Well-Architected consequence of mitigating this risk: A stream name is incompatible with the selected data source or destination. Which answer describes the consequence attributable to this checkpoint?

- ✗ **A. Use the Validate retention and archive economics consequence as the result for Define an Azure Monitor Agent data collection rule; before approval, proceed on the belief that a pillar statement remains valid when moved away from Validate retention and archive economics.** — The controlling fact is that cost Optimization: table-level retention aligns searchable and archived data with its continuing value. Under the stated constraint, that tradeoff belongs to Validate retention and archive economics and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Define an Azure Monitor Agent data collection rule outcome. Separately, treat as decisive the assertion that a moderate cost classification outweighs the mandatory architecture state.** — The authored acceptance boundary states that the required outcome at Define an Azure Monitor Agent data collection rule. Under the stated constraint, cost Optimization cannot remove the acceptance condition 'The DCR maps only the required streams to a named Log Analytics destination'.
- ✗ **C. Treat 'Performance Efficiency: filtering noisy streams near the source protects ingestion and query capacity' as proof that all five pillars pass; for this decision, base approval on the claim that the checkpoint 'Define an Azure Monitor Agent data collection rule' no longer needs its separate negative check.** — The relevant observation is that no legacy Log Analytics agent or unapproved stream is represented in the rule. Under the stated constraint, one positive command cannot establish every pillar, especially while the negative state remains unchecked.
- ✓ **D. Record this consequence: Performance Efficiency: filtering noisy streams near the source protects ingestion and query capacity; next, tie it to LAB01-REQ-02.** — performance Efficiency: filtering noisy streams near the source protects ingestion and query capacity. Under the stated constraint, it states the authored pillar consequence of the control evaluated at Define an Azure Monitor Agent data collection rule.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q19 — answer D

A recommendation on 'Define an Azure Monitor Agent data collection rule' is requested by regional platform teams. A material change now applies: A new regulator requires security control-plane records to remain in-region for seven years while application traces must stay searchable for only thirty days; revise routing and retention without duplicating every stream. What should be recorded as the correct revision to the decision record?

- ✗ **A. Retain Regional workspaces with cross-workspace queries and policy-driven routing at Define an Azure Monitor Agent data collection rule without recalculating criteria or eligibility; afterward, use as justification the claim that the original weighted result is permanent.** — The scenario makes clear that regional workspaces with cross-workspace queries and policy-driven routing. Under the stated constraint, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Central Log Analytics workspace with DCR-based collection and archive export for Define an Azure Monitor Agent data collection rule without rechecking its mandatory constraints; then accept without proof that being different from the current design is an architecture criterion.** — The architecture evidence must show that central Log Analytics workspace with DCR-based collection and archive export. Under the stated constraint, being different is not a criterion, and the candidate still must avoid the prohibited state at Define an Azure Monitor Agent data collection rule.
- ✗ **C. Keep Dedicated workspace per workload with independent retention and access eligible at Define an Azure Monitor Agent data collection rule by downgrading LAB01-REQ-02. Independently, rely on the claim that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The applicable design condition is that lAB01-REQ-02. Under the stated constraint, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.
- ✓ **D. Re-score Regional workspaces with cross-workspace queries and policy-driven routing and both alternatives for Define an Azure Monitor Agent data collection rule; for this decision, supersede the ADR using the changed evidence for LAB01-REQ-02.** — The checkpoint specifically records that regional workspaces with cross-workspace queries and policy-driven routing at Define an Azure Monitor Agent data collection rule. Under the stated constraint, the material change 'A new regulator requires security control-plane records to remain in-region for seven years while application traces must stay searchable for only thirty days; revise routing and retention without duplicating every stream.' requires fresh eligibility, weighted analysis, and a superseding decision.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q20 — answer A

'Define an Azure Monitor Agent data collection rule' is assigned to data protection officer. After a partial run, cleanup must follow this dependency: Delete all DCR associations before deleting the DCR. Which proposal supplies the dependency-safe cleanup plan?

- ✓ **A. Verify exact run-state IDs and ownership tags for Define an Azure Monitor Agent data collection rule. Then, follow this dependency rule without purge: Delete all DCR associations before deleting the DCR.** — The review is governed by this fact: delete all DCR associations before deleting the DCR. Under the stated constraint, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **B. Apply the cleanup rule for Associate the rule with an explicit resource scope before reconciling the current dependency. As another control, use the premise that removing a parent needed to identify Define an Azure Monitor Agent data collection rule is harmless.** — The retained result must be reconciled with the fact that delete the association before its DCR or target resource. Under the stated constraint, a cleanup rule for Associate the rule with an explicit resource scope cannot override the dependency declared for Define an Azure Monitor Agent data collection rule.
- ✗ **C. Delete candidates by display name before comparing the Define an Azure Monitor Agent data collection rule ownership tags; as a separate check, consider it sufficient that the dependency rule 'Delete all DCR associations before deleting the DCR' is optional.** — The decision tension comes from the fact that dCR resource ID, stream names, destinations, and source file hash. Under the stated constraint, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Define an Azure Monitor Agent data collection rule negative assertion 'No legacy Log Analytics agent or unapproved stream is represented in the rule'. Afterward, take it as conclusive that remaining command logs are sufficient recovery evidence.** — The safe operating boundary says that no legacy Log Analytics agent or unapproved stream is represented in the rule. Under the stated constraint, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q21 — answer B

An assurance review of 'Associate the rule with an explicit resource scope' includes data protection officer. Approval requires a positive result plus this independent negative assertion: The target is not simultaneously associated with a competing lab DCR. Select the acceptance rule that makes LAB01-REQ-03 testable.

- ✗ **A. Select Central Log Analytics workspace with DCR-based collection and archive export before checking Associate the rule with an explicit resource scope. Next, base approval on the claim that a successful deployment will later prove the architecture constraint.** — The failure model establishes that the target is not simultaneously associated with a competing lab DCR. Under the stated constraint, a deployment result cannot prove LAB01-REQ-03, and Central Log Analytics workspace with DCR-based collection and archive export still has to meet the mandatory boundary.
- ✓ **B. Require the documented positive state for Associate the rule with an explicit resource scope, and then verify that the target is not simultaneously associated with a competing lab DCR.** — The traceable checkpoint outcome is that the target has one intentional association to the approved DCR. Under the stated constraint, the positive state and an independent negative assertion jointly make LAB01-REQ-03 testable.
- ✗ **C. Use the passing result from Establish regional workspace boundaries to approve Associate the rule with an explicit resource scope, and then use the premise that one control establishes an unrelated acceptance boundary.** — The recovery guidance assumes that the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. Under the stated constraint, that outcome belongs to Establish regional workspace boundaries and leaves Associate the rule with an explicit resource scope unverified.
- ✗ **D. Choose Dedicated workspace per workload with independent retention and access and skip the Associate the rule with an explicit resource scope negative assertion. Also, consider it sufficient that the candidate has the lowest implementation effort.** — The WAF consequence identifies that reduce incident investigation time while giving security and regional operators governed access to complete, correctly routed telemetry. Under the stated constraint, implementation effort cannot justify skipping the negative assertion or displace LAB01-REQ-03.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q22 — answer D

Approval of 'Associate the rule with an explicit resource scope' is questioned by finOps. The selected architecture is Regional workspaces with cross-workspace queries and policy-driven routing; object existence alone is not success. Which response provides the intended successful finding?

- ✗ **A. Use only the negative assertion 'The target is not simultaneously associated with a competing lab DCR' as the success result; next, rely on the claim that absence proves every required positive property.** — the target is not simultaneously associated with a competing lab DCR. This matters because this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Define an Azure Monitor Agent data collection rule as the result for Associate the rule with an explicit resource scope. In addition, rely on the belief that a property from the current checkpoint does not need to be inspected.** — The controlling fact is that the DCR maps only the required streams to a named Log Analytics destination. This matters because evidence for Define an Azure Monitor Agent data collection rule cannot substitute for the properties required at Associate the rule with an explicit resource scope.
- ✗ **C. Record the failure condition 'The target resource type, region, or authorization scope does not support the association' as a successful state; before approval, proceed on the belief that the command returned an object.** — The authored acceptance boundary states that the target resource type, region, or authorization scope does not support the association. This matters because resource existence or command output does not convert the documented failure condition into success.
- ✓ **D. Record the target has one intentional association to the approved DCR; as a separate check, classify it as success for LAB01-REQ-03.** — The command-level assertion is anchored in the fact that the target has one intentional association to the approved DCR. Under the stated constraint, this is the authored target state for Associate the rule with an explicit resource scope and directly supports LAB01-REQ-03.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q23 — answer A

The implementation review has reached 'Associate the rule with an explicit resource scope'. Evidence must address this risk without retaining credentials: The target resource type, region, or authorization scope does not support the association. Which choice gives the team sufficient, properly scoped evidence?

- ✓ **A. Retain target resource ID, association name, and DCR ID without host or user data; before approval, exclude credentials and unrelated response fields.** — The relevant observation is that target resource ID, association name, and DCR ID without host or user data. This matters because it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **B. Substitute the evidence from Route resource logs with diagnostic settings for Associate the rule with an explicit resource scope; for the recorded decision, take it as conclusive that a related checkpoint proves the current expected state.** — The checkpoint specifically records that diagnostic-setting name, enabled categories, destination IDs, and export mode. This matters because that evidence supports Route resource logs with diagnostic settings, so it cannot demonstrate The target has one intentional association to the approved DCR.
- ✗ **C. Store unredacted Associate the rule with an explicit resource scope output with operator, tenant, token, and request context. Then, treat it as established that reproduction requires every captured field.** — The scenario makes clear that unredacted implementation output. This matters because identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **D. Record only the Associate the rule with an explicit resource scope positive inspection's exit status; afterward, use as justification the claim that projected properties and assertion results can be reconstructed later.** — The architecture evidence must show that the positive inspection's exit status. This matters because an exit code alone does not show whether the target has one intentional association to the approved DCR.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q24 — answer D

The approach to 'Associate the rule with an explicit resource scope' is challenged by regional platform teams. The target is The target has one intentional association to the approved DCR, but the latest evidence does not show it. What is the most likely cause?

- ✗ **A. Treat 'Workspace defaults obscure a table-specific compliance or cost requirement' as grounds to reject Associate the rule with an explicit resource scope. Also, treat as decisive the assertion that validate retention and archive economics's failure model applies unchanged here.** — The review is governed by this fact: workspace defaults obscure a table-specific compliance or cost requirement. This matters because that condition belongs to Validate retention and archive economics and does not by itself invalidate Regional workspaces with cross-workspace queries and policy-driven routing.
- ✗ **B. Ignore the negative assertion 'The target is not simultaneously associated with a competing lab DCR'; in a separate step, base approval on the claim that a later material change will make it unnecessary.** — The retained result must be reconciled with the fact that the target is not simultaneously associated with a competing lab DCR. This matters because the negative assertion must be evaluated now, independent of a later business change.
- ✗ **C. Investigate Establish regional workspace boundaries instead of diagnosing Associate the rule with an explicit resource scope. As another control, use the premise that a passing result at Establish regional workspace boundaries identifies the current cause.** — The decision tension comes from the fact that the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. This matters because a passing result at Establish regional workspace boundaries gives no causal evidence for the failure at Associate the rule with an explicit resource scope.
- ✓ **D. Investigate the target resource type, region, or authorization scope does not support the association; as an independent condition, isolate that cause before changing Regional workspaces with cross-workspace queries and policy-driven routing.** — The applicable design condition is that the target resource type, region, or authorization scope does not support the association. This matters because it is the checkpoint's causal failure model and should be isolated before retrying Associate the rule with an explicit resource scope.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q25 — answer B

A decision test for 'Associate the rule with an explicit resource scope' includes data protection officer. The run encountered this modeled failure: The target resource type, region, or authorization scope does not support the association. Which recommendation supplies the safest recovery action?

- ✗ **A. Perform cleanup immediately: Delete the association before its DCR or target resource; before approval, accept without proof that the failed operation and its returned identifiers do not need reconciliation.** — The traceable checkpoint outcome is that delete the association before its DCR or target resource. This matters because cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✓ **B. Confirm the exact target ID and regional compatibility, then recreate only the missing association; then preserve the current run identity and evidence.** — The safe operating boundary says that confirm the exact target ID and regional compatibility, then recreate only the missing association. This matters because it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **C. Create a different run identity before diagnosing 'The target resource type, region, or authorization scope does not support the association'. Separately, rely on the claim that the first state record and returned identifiers can be discarded.** — The failure model establishes that the target resource type, region, or authorization scope does not support the association. This matters because discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Establish regional workspace boundaries instead; for this decision, rely on the belief that success at Establish regional workspace boundaries will repair the failed state at Associate the rule with an explicit resource scope.** — The recovery guidance assumes that the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. This matters because altering an already separate checkpoint does not repair the modeled failure at Associate the rule with an explicit resource scope.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q26 — answer B

The architecture board reconsiders 'Associate the rule with an explicit resource scope' with finOps. Without making a new change, the team must inspect the risk 'The target resource type, region, or authorization scope does not support the association' using the Azure CLI lane. Choose the read-only, lane-correct inspection.

- ✗ **A. Rerun the Associate the rule with an explicit resource scope implementation command and infer the expected state; afterward, consider it sufficient that absence of a shell error proves every property.** — The command-level assertion is anchored in the fact that the implementation command. This matters because it can mutate state and shell success does not independently assert the expected properties.
- ✓ **B. Inspect the documented properties for Associate the rule with an explicit resource scope. Also, retain this evidence: target resource ID, association name, and DCR ID without host or user data.** — The WAF consequence identifies that the target has one intentional association to the approved DCR. This matters because the read-only inspection directly tests the properties required at Associate the rule with an explicit resource scope.
- ✗ **C. Run only this negative inspection for Associate the rule with an explicit resource scope: The target is not simultaneously associated with a competing lab DCR; then take it as conclusive that an empty negative result reports every required positive property.** — the negative inspection. The checkpoint therefore requires that absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Define an Azure Monitor Agent data collection rule and apply it to Associate the rule with an explicit resource scope. Independently, treat it as established that any command from the same lane proves the current checkpoint.** — The controlling fact is that the positive inspection for Define an Azure Monitor Agent data collection rule. The checkpoint therefore requires that it is lane-correct but proves Define an Azure Monitor Agent data collection rule, not Associate the rule with an explicit resource scope.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q27 — answer B

A review of 'Associate the rule with an explicit resource scope' begins with input from security operations. A passing positive check does not by itself prove this negative assertion: The target is not simultaneously associated with a competing lab DCR. Which answer describes the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Associate the rule with an explicit resource scope and report full compliance. As another control, proceed on the belief that every prohibited parallel state must therefore be absent.** — The relevant observation is that the target has one intentional association to the approved DCR. The checkpoint therefore requires that the positive result alone does not test the explicit anti-condition 'The target is not simultaneously associated with a competing lab DCR'.
- ✓ **B. Verify the positive properties for Associate the rule with an explicit resource scope. Afterward, independently verify that the target is not simultaneously associated with a competing lab DCR.** — The authored acceptance boundary states that the target has one intentional association to the approved DCR; The target is not simultaneously associated with a competing lab DCR. The checkpoint therefore requires that two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **C. Prove only that the target is not simultaneously associated with a competing lab DCR and report the intended configuration as present; as a separate check, treat as decisive the assertion that absence is equivalent to positive-state evidence.** — The checkpoint specifically records that the target is not simultaneously associated with a competing lab DCR. The checkpoint therefore requires that absence evidence cannot demonstrate the required positive state 'The target has one intentional association to the approved DCR'.
- ✗ **D. Use Route resource logs with diagnostic settings's negative assertion for Associate the rule with an explicit resource scope. Afterward, base approval on the claim that negative assertions are interchangeable between checkpoints.** — The scenario makes clear that event Hubs or storage are not silently configured as extra destinations. The checkpoint therefore requires that the second assertion is valid for Route resource logs with diagnostic settings but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q28 — answer A

'Associate the rule with an explicit resource scope' awaits approval from regional platform teams. The board wants the Well-Architected consequence of mitigating this risk: The target resource type, region, or authorization scope does not support the association. What should be recorded as the consequence attributable to this checkpoint?

- ✓ **A. Record this consequence: Security: explicit DCR associations limit collection to approved assets and destinations. Separately, tie it to LAB01-REQ-03.** — The architecture evidence must show that security: explicit DCR associations limit collection to approved assets and destinations. The checkpoint therefore requires that it states the authored pillar consequence of the control evaluated at Associate the rule with an explicit resource scope.
- ✗ **B. Use the Validate retention and archive economics consequence as the result for Associate the rule with an explicit resource scope; for this decision, use as justification the claim that a pillar statement remains valid when moved away from Validate retention and archive economics.** — The applicable design condition is that cost Optimization: table-level retention aligns searchable and archived data with its continuing value. The checkpoint therefore requires that that tradeoff belongs to Validate retention and archive economics and does not explain this checkpoint's decision.
- ✗ **C. Remove the control responsible for the Associate the rule with an explicit resource scope outcome. Before sign-off, accept without proof that a moderate cost classification outweighs the mandatory architecture state.** — The review is governed by this fact: the required outcome at Associate the rule with an explicit resource scope. The checkpoint therefore requires that cost Optimization cannot remove the acceptance condition 'The target has one intentional association to the approved DCR'.
- ✗ **D. Treat 'Security: explicit DCR associations limit collection to approved assets and destinations' as proof that all five pillars pass; as an independent condition, rely on the claim that the checkpoint 'Associate the rule with an explicit resource scope' no longer needs its separate negative check.** — The retained result must be reconciled with the fact that the target is not simultaneously associated with a competing lab DCR. The checkpoint therefore requires that one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q29 — answer D

'Associate the rule with an explicit resource scope' is reopened at the request of data protection officer. A material change now applies: A new regulator requires security control-plane records to remain in-region for seven years while application traces must stay searchable for only thirty days; revise routing and retention without duplicating every stream. Which proposal supplies the correct revision to the decision record?

- ✗ **A. Retain Regional workspaces with cross-workspace queries and policy-driven routing at Associate the rule with an explicit resource scope without recalculating criteria or eligibility. Independently, use the premise that the original weighted result is permanent.** — The safe operating boundary says that regional workspaces with cross-workspace queries and policy-driven routing. The checkpoint therefore requires that the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Central Log Analytics workspace with DCR-based collection and archive export for Associate the rule with an explicit resource scope without rechecking its mandatory constraints. Next, consider it sufficient that being different from the current design is an architecture criterion.** — The traceable checkpoint outcome is that central Log Analytics workspace with DCR-based collection and archive export. The checkpoint therefore requires that being different is not a criterion, and the candidate still must avoid the prohibited state at Associate the rule with an explicit resource scope.
- ✗ **C. Keep Dedicated workspace per workload with independent retention and access eligible at Associate the rule with an explicit resource scope by downgrading LAB01-REQ-03, and then take it as conclusive that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The failure model establishes that lAB01-REQ-03. The checkpoint therefore requires that an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.
- ✓ **D. Re-score Regional workspaces with cross-workspace queries and policy-driven routing and both alternatives for Associate the rule with an explicit resource scope; as another gate, supersede the ADR using the changed evidence for LAB01-REQ-03.** — The decision tension comes from the fact that regional workspaces with cross-workspace queries and policy-driven routing at Associate the rule with an explicit resource scope. The checkpoint therefore requires that the material change 'A new regulator requires security control-plane records to remain in-region for seven years while application traces must stay searchable for only thirty days; revise routing and retention without duplicating every stream.' requires fresh eligibility, weighted analysis, and a superseding decision.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q30 — answer C

A design review of 'Associate the rule with an explicit resource scope' includes finOps. After a partial run, cleanup must follow this dependency: Delete the association before its DCR or target resource. Which option best represents the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Define an Azure Monitor Agent data collection rule before reconciling the current dependency. Afterward, rely on the belief that removing a parent needed to identify Associate the rule with an explicit resource scope is harmless.** — The WAF consequence identifies that delete all DCR associations before deleting the DCR. The checkpoint therefore requires that a cleanup rule for Define an Azure Monitor Agent data collection rule cannot override the dependency declared for Associate the rule with an explicit resource scope.
- ✗ **B. Delete candidates by display name before comparing the Associate the rule with an explicit resource scope ownership tags; next, proceed on the belief that the dependency rule 'Delete the association before its DCR or target resource' is optional.** — The command-level assertion is anchored in the fact that target resource ID, association name, and DCR ID without host or user data. The checkpoint therefore requires that names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✓ **C. Verify exact run-state IDs and ownership tags for Associate the rule with an explicit resource scope. Independently, follow this dependency rule without purge: Delete the association before its DCR or target resource.** — The recovery guidance assumes that delete the association before its DCR or target resource. The checkpoint therefore requires that exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **D. Destroy recoverable copies before retaining the Associate the rule with an explicit resource scope negative assertion 'The target is not simultaneously associated with a competing lab DCR'. In addition, treat as decisive the assertion that remaining command logs are sufficient recovery evidence.** — the target is not simultaneously associated with a competing lab DCR. In the decision record, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q31 — answer A

The team asks finOps to assess 'Route resource logs with diagnostic settings'. Approval requires a positive result plus this independent negative assertion: Event Hubs or storage are not silently configured as extra destinations. Which response provides the acceptance rule that makes LAB01-REQ-04 testable?

- ✓ **A. Require the documented positive state for Route resource logs with diagnostic settings. As another control, verify that event Hubs or storage are not silently configured as extra destinations.** — The controlling fact is that supported log categories and metrics route to the intended regional workspace. In the decision record, the positive state and an independent negative assertion jointly make LAB01-REQ-04 testable.
- ✗ **B. Select Central Log Analytics workspace with DCR-based collection and archive export before checking Route resource logs with diagnostic settings. Also, rely on the claim that a successful deployment will later prove the architecture constraint.** — The authored acceptance boundary states that event Hubs or storage are not silently configured as extra destinations. In the decision record, a deployment result cannot prove LAB01-REQ-04, and Central Log Analytics workspace with DCR-based collection and archive export still has to meet the mandatory boundary.
- ✗ **C. Use the passing result from Establish regional workspace boundaries to approve Route resource logs with diagnostic settings; in a separate step, rely on the belief that one control establishes an unrelated acceptance boundary.** — The relevant observation is that the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. In the decision record, that outcome belongs to Establish regional workspace boundaries and leaves Route resource logs with diagnostic settings unverified.
- ✗ **D. Choose Dedicated workspace per workload with independent retention and access and skip the Route resource logs with diagnostic settings negative assertion. As another control, proceed on the belief that the candidate has the lowest implementation effort.** — The checkpoint specifically records that reduce incident investigation time while giving security and regional operators governed access to complete, correctly routed telemetry. In the decision record, implementation effort cannot justify skipping the negative assertion or displace LAB01-REQ-04.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q32 — answer D

A recommendation on 'Route resource logs with diagnostic settings' is requested by security operations. The selected architecture is Regional workspaces with cross-workspace queries and policy-driven routing; object existence alone is not success. Which choice gives the team the intended successful finding?

- ✗ **A. Use only the negative assertion 'Event Hubs or storage are not silently configured as extra destinations' as the success result; before approval, take it as conclusive that absence proves every required positive property.** — The architecture evidence must show that event Hubs or storage are not silently configured as extra destinations. In the decision record, this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Define an Azure Monitor Agent data collection rule as the result for Route resource logs with diagnostic settings. Separately, treat it as established that a property from the current checkpoint does not need to be inspected.** — The applicable design condition is that the DCR maps only the required streams to a named Log Analytics destination. In the decision record, evidence for Define an Azure Monitor Agent data collection rule cannot substitute for the properties required at Route resource logs with diagnostic settings.
- ✗ **C. Record the failure condition 'The chosen category group is unsupported by the resource provider' as a successful state; for this decision, use as justification the claim that the command returned an object.** — The review is governed by this fact: the chosen category group is unsupported by the resource provider. In the decision record, resource existence or command output does not convert the documented failure condition into success.
- ✓ **D. Record supported log categories and metrics route to the intended regional workspace. In addition, classify it as success for LAB01-REQ-04.** — The scenario makes clear that supported log categories and metrics route to the intended regional workspace. In the decision record, this is the authored target state for Route resource logs with diagnostic settings and directly supports LAB01-REQ-04.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q33 — answer B

'Route resource logs with diagnostic settings' is assigned to regional platform teams. Evidence must address this risk without retaining credentials: The chosen category group is unsupported by the resource provider. What is sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Associate the rule with an explicit resource scope for Route resource logs with diagnostic settings; afterward, treat as decisive the assertion that a related checkpoint proves the current expected state.** — The decision tension comes from the fact that target resource ID, association name, and DCR ID without host or user data. In the decision record, that evidence supports Associate the rule with an explicit resource scope, so it cannot demonstrate Supported log categories and metrics route to the intended regional workspace.
- ✓ **B. Retain diagnostic-setting name, enabled categories, destination IDs, and export mode. Before sign-off, exclude credentials and unrelated response fields.** — The retained result must be reconciled with the fact that diagnostic-setting name, enabled categories, destination IDs, and export mode. In the decision record, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **C. Store unredacted Route resource logs with diagnostic settings output with operator, tenant, token, and request context; then base approval on the claim that reproduction requires every captured field.** — The safe operating boundary says that unredacted implementation output. In the decision record, identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **D. Record only the Route resource logs with diagnostic settings positive inspection's exit status. Independently, use the premise that projected properties and assertion results can be reconstructed later.** — The traceable checkpoint outcome is that the positive inspection's exit status. In the decision record, an exit code alone does not show whether supported log categories and metrics route to the intended regional workspace.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q34 — answer B

An assurance review of 'Route resource logs with diagnostic settings' includes data protection officer. The target is Supported log categories and metrics route to the intended regional workspace, but the latest evidence does not show it. Which recommendation supplies the most likely cause?

- ✗ **A. Treat 'Workspace defaults obscure a table-specific compliance or cost requirement' as grounds to reject Route resource logs with diagnostic settings. As another control, accept without proof that validate retention and archive economics's failure model applies unchanged here.** — The recovery guidance assumes that workspace defaults obscure a table-specific compliance or cost requirement. In the decision record, that condition belongs to Validate retention and archive economics and does not by itself invalidate Regional workspaces with cross-workspace queries and policy-driven routing.
- ✓ **B. Investigate the chosen category group is unsupported by the resource provider; afterward, isolate that cause before changing Regional workspaces with cross-workspace queries and policy-driven routing.** — The failure model establishes that the chosen category group is unsupported by the resource provider. In the decision record, it is the checkpoint's causal failure model and should be isolated before retrying Route resource logs with diagnostic settings.
- ✗ **C. Ignore the negative assertion 'Event Hubs or storage are not silently configured as extra destinations'; as a separate check, rely on the claim that a later material change will make it unnecessary.** — The WAF consequence identifies that event Hubs or storage are not silently configured as extra destinations. In the decision record, the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Establish regional workspace boundaries instead of diagnosing Route resource logs with diagnostic settings. Afterward, rely on the belief that a passing result at Establish regional workspace boundaries identifies the current cause.** — The command-level assertion is anchored in the fact that the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. In the decision record, a passing result at Establish regional workspace boundaries gives no causal evidence for the failure at Route resource logs with diagnostic settings.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q35 — answer D

Approval of 'Route resource logs with diagnostic settings' is questioned by finOps. The run encountered this modeled failure: The chosen category group is unsupported by the resource provider. Choose the safest recovery action.

- ✗ **A. Perform cleanup immediately: Delete the diagnostic setting before deleting either source or destination; for this decision, consider it sufficient that the failed operation and its returned identifiers do not need reconciliation.** — The controlling fact is that delete the diagnostic setting before deleting either source or destination. The independent assertion shows why cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **B. Create a different run identity before diagnosing 'The chosen category group is unsupported by the resource provider'. Before sign-off, take it as conclusive that the first state record and returned identifiers can be discarded.** — The authored acceptance boundary states that the chosen category group is unsupported by the resource provider. The independent assertion shows why discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **C. Change Establish regional workspace boundaries instead; as an independent condition, treat it as established that success at Establish regional workspace boundaries will repair the failed state at Route resource logs with diagnostic settings.** — The relevant observation is that the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. The independent assertion shows why altering an already separate checkpoint does not repair the modeled failure at Route resource logs with diagnostic settings.
- ✓ **D. Query diagnostic categories, update the design artifact, and apply the smallest corrected setting, and then preserve the current run identity and evidence.** — query diagnostic categories, update the design artifact, and apply the smallest corrected setting. The independent assertion shows why it corrects the narrow cause while retaining the same recovery trail and decision scope.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q36 — answer C

The implementation review has reached 'Route resource logs with diagnostic settings'. Without making a new change, the team must inspect the risk 'The chosen category group is unsupported by the resource provider' using the Azure CLI lane. Which answer describes the read-only, lane-correct inspection?

- ✗ **A. Rerun the Route resource logs with diagnostic settings implementation command and infer the expected state. Independently, proceed on the belief that absence of a shell error proves every property.** — The scenario makes clear that the implementation command. The independent assertion shows why it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Route resource logs with diagnostic settings: Event Hubs or storage are not silently configured as extra destinations. Next, treat as decisive the assertion that an empty negative result reports every required positive property.** — The architecture evidence must show that the negative inspection. The independent assertion shows why absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✓ **C. Inspect the documented properties for Route resource logs with diagnostic settings; as a separate check, retain this evidence: diagnostic-setting name, enabled categories, destination IDs, and export mode.** — The checkpoint specifically records that supported log categories and metrics route to the intended regional workspace. The independent assertion shows why the read-only inspection directly tests the properties required at Route resource logs with diagnostic settings.
- ✗ **D. Run the positive inspection for Define an Azure Monitor Agent data collection rule and apply it to Route resource logs with diagnostic settings, and then base approval on the claim that any command from the same lane proves the current checkpoint.** — The applicable design condition is that the positive inspection for Define an Azure Monitor Agent data collection rule. The independent assertion shows why it is lane-correct but proves Define an Azure Monitor Agent data collection rule, not Route resource logs with diagnostic settings.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q37 — answer A

The approach to 'Route resource logs with diagnostic settings' is challenged by regional platform teams. A passing positive check does not by itself prove this negative assertion: Event Hubs or storage are not silently configured as extra destinations. What should be recorded as the assertion pair that proves both conditions independently?

- ✓ **A. Verify the positive properties for Route resource logs with diagnostic settings; before approval, independently verify that event Hubs or storage are not silently configured as extra destinations.** — The review is governed by this fact: supported log categories and metrics route to the intended regional workspace; Event Hubs or storage are not silently configured as extra destinations. The independent assertion shows why two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **B. Verify only the positive result for Route resource logs with diagnostic settings and report full compliance. Afterward, use as justification the claim that every prohibited parallel state must therefore be absent.** — The retained result must be reconciled with the fact that supported log categories and metrics route to the intended regional workspace. The independent assertion shows why the positive result alone does not test the explicit anti-condition 'Event Hubs or storage are not silently configured as extra destinations'.
- ✗ **C. Prove only that event Hubs or storage are not silently configured as extra destinations and report the intended configuration as present; next, accept without proof that absence is equivalent to positive-state evidence.** — The decision tension comes from the fact that event Hubs or storage are not silently configured as extra destinations. The independent assertion shows why absence evidence cannot demonstrate the required positive state 'Supported log categories and metrics route to the intended regional workspace'.
- ✗ **D. Use Associate the rule with an explicit resource scope's negative assertion for Route resource logs with diagnostic settings. In addition, rely on the claim that negative assertions are interchangeable between checkpoints.** — The safe operating boundary says that the target is not simultaneously associated with a competing lab DCR. The independent assertion shows why the second assertion is valid for Associate the rule with an explicit resource scope but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q38 — answer C

A decision test for 'Route resource logs with diagnostic settings' includes data protection officer. The board wants the Well-Architected consequence of mitigating this risk: The chosen category group is unsupported by the resource provider. Which proposal supplies the consequence attributable to this checkpoint?

- ✗ **A. Use the Validate retention and archive economics consequence as the result for Route resource logs with diagnostic settings; as an independent condition, use the premise that a pillar statement remains valid when moved away from Validate retention and archive economics.** — The failure model establishes that cost Optimization: table-level retention aligns searchable and archived data with its continuing value. The independent assertion shows why that tradeoff belongs to Validate retention and archive economics and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Route resource logs with diagnostic settings outcome; for the final assessment, consider it sufficient that a moderate cost classification outweighs the mandatory architecture state.** — The recovery guidance assumes that the required outcome at Route resource logs with diagnostic settings. The independent assertion shows why cost Optimization cannot remove the acceptance condition 'Supported log categories and metrics route to the intended regional workspace'.
- ✓ **C. Record this consequence: Operational Excellence: diagnostic settings create a repeatable routing contract that teams can inspect; as an independent condition, tie it to LAB01-REQ-04.** — The traceable checkpoint outcome is that operational Excellence: diagnostic settings create a repeatable routing contract that teams can inspect. The independent assertion shows why it states the authored pillar consequence of the control evaluated at Route resource logs with diagnostic settings.
- ✗ **D. Treat 'Operational Excellence: diagnostic settings create a repeatable routing contract that teams can inspect' as proof that all five pillars pass. Then, take it as conclusive that the checkpoint 'Route resource logs with diagnostic settings' no longer needs its separate negative check.** — The WAF consequence identifies that event Hubs or storage are not silently configured as extra destinations. The independent assertion shows why one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q39 — answer B

The architecture board reconsiders 'Route resource logs with diagnostic settings' with finOps. A material change now applies: A new regulator requires security control-plane records to remain in-region for seven years while application traces must stay searchable for only thirty days; revise routing and retention without duplicating every stream. Which option best represents the correct revision to the decision record?

- ✗ **A. Retain Regional workspaces with cross-workspace queries and policy-driven routing at Route resource logs with diagnostic settings without recalculating criteria or eligibility, and then rely on the belief that the original weighted result is permanent.** — regional workspaces with cross-workspace queries and policy-driven routing. Operationally, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✓ **B. Re-score Regional workspaces with cross-workspace queries and policy-driven routing and both alternatives for Route resource logs with diagnostic settings; then supersede the ADR using the changed evidence for LAB01-REQ-04.** — The command-level assertion is anchored in the fact that regional workspaces with cross-workspace queries and policy-driven routing at Route resource logs with diagnostic settings. The independent assertion shows why the material change 'A new regulator requires security control-plane records to remain in-region for seven years while application traces must stay searchable for only thirty days; revise routing and retention without duplicating every stream.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **C. Select Central Log Analytics workspace with DCR-based collection and archive export for Route resource logs with diagnostic settings without rechecking its mandatory constraints. Also, proceed on the belief that being different from the current design is an architecture criterion.** — The controlling fact is that central Log Analytics workspace with DCR-based collection and archive export. Operationally, being different is not a criterion, and the candidate still must avoid the prohibited state at Route resource logs with diagnostic settings.
- ✗ **D. Keep Dedicated workspace per workload with independent retention and access eligible at Route resource logs with diagnostic settings by downgrading LAB01-REQ-04; in a separate step, treat as decisive the assertion that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The authored acceptance boundary states that lAB01-REQ-04. Operationally, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q40 — answer A

A review of 'Route resource logs with diagnostic settings' begins with input from security operations. After a partial run, cleanup must follow this dependency: Delete the diagnostic setting before deleting either source or destination. Which course of action provides the dependency-safe cleanup plan?

- ✓ **A. Verify exact run-state IDs and ownership tags for Route resource logs with diagnostic settings. Also, follow this dependency rule without purge: Delete the diagnostic setting before deleting either source or destination.** — The relevant observation is that delete the diagnostic setting before deleting either source or destination. Operationally, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **B. Apply the cleanup rule for Define an Azure Monitor Agent data collection rule before reconciling the current dependency. In addition, treat it as established that removing a parent needed to identify Route resource logs with diagnostic settings is harmless.** — The checkpoint specifically records that delete all DCR associations before deleting the DCR. Operationally, a cleanup rule for Define an Azure Monitor Agent data collection rule cannot override the dependency declared for Route resource logs with diagnostic settings.
- ✗ **C. Delete candidates by display name before comparing the Route resource logs with diagnostic settings ownership tags; before approval, use as justification the claim that the dependency rule 'Delete the diagnostic setting before deleting either source or destination' is optional.** — The scenario makes clear that diagnostic-setting name, enabled categories, destination IDs, and export mode. Operationally, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Route resource logs with diagnostic settings negative assertion 'Event Hubs or storage are not silently configured as extra destinations'. Separately, accept without proof that remaining command logs are sufficient recovery evidence.** — The architecture evidence must show that event Hubs or storage are not silently configured as extra destinations. Operationally, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q41 — answer D

'Validate retention and archive economics' awaits approval from security operations. Approval requires a positive result plus this independent negative assertion: High-volume tables do not inherit unjustified extended interactive retention. Which choice gives the team the acceptance rule that makes LAB01-REQ-05 testable?

- ✗ **A. Select Central Log Analytics workspace with DCR-based collection and archive export before checking Validate retention and archive economics. As another control, take it as conclusive that a successful deployment will later prove the architecture constraint.** — The review is governed by this fact: high-volume tables do not inherit unjustified extended interactive retention. Operationally, a deployment result cannot prove LAB01-REQ-05, and Central Log Analytics workspace with DCR-based collection and archive export still has to meet the mandatory boundary.
- ✗ **B. Use the passing result from Establish regional workspace boundaries to approve Validate retention and archive economics; as a separate check, treat it as established that one control establishes an unrelated acceptance boundary.** — The retained result must be reconciled with the fact that the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. Operationally, that outcome belongs to Establish regional workspace boundaries and leaves Validate retention and archive economics unverified.
- ✗ **C. Choose Dedicated workspace per workload with independent retention and access and skip the Validate retention and archive economics negative assertion. Afterward, use as justification the claim that the candidate has the lowest implementation effort.** — The decision tension comes from the fact that reduce incident investigation time while giving security and regional operators governed access to complete, correctly routed telemetry. Operationally, implementation effort cannot justify skipping the negative assertion or displace LAB01-REQ-05.
- ✓ **D. Require the documented positive state for Validate retention and archive economics; next, verify that high-volume tables do not inherit unjustified extended interactive retention.** — The applicable design condition is that interactive and total retention match the documented use case for each reviewed table. Operationally, the positive state and an independent negative assertion jointly make LAB01-REQ-05 testable.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q42 — answer C

'Validate retention and archive economics' is reopened at the request of regional platform teams. The selected architecture is Regional workspaces with cross-workspace queries and policy-driven routing; object existence alone is not success. What is the intended successful finding?

- ✗ **A. Use only the negative assertion 'High-volume tables do not inherit unjustified extended interactive retention' as the success result; for this decision, treat as decisive the assertion that absence proves every required positive property.** — The traceable checkpoint outcome is that high-volume tables do not inherit unjustified extended interactive retention. Operationally, this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Define an Azure Monitor Agent data collection rule as the result for Validate retention and archive economics. Before sign-off, base approval on the claim that a property from the current checkpoint does not need to be inspected.** — The failure model establishes that the DCR maps only the required streams to a named Log Analytics destination. Operationally, evidence for Define an Azure Monitor Agent data collection rule cannot substitute for the properties required at Validate retention and archive economics.
- ✓ **C. Record interactive and total retention match the documented use case for each reviewed table; for this decision, classify it as success for LAB01-REQ-05.** — The safe operating boundary says that interactive and total retention match the documented use case for each reviewed table. Operationally, this is the authored target state for Validate retention and archive economics and directly supports LAB01-REQ-05.
- ✗ **D. Record the failure condition 'Workspace defaults obscure a table-specific compliance or cost requirement' as a successful state; as an independent condition, use the premise that the command returned an object.** — The recovery guidance assumes that workspace defaults obscure a table-specific compliance or cost requirement. Operationally, resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q43 — answer C

A design review of 'Validate retention and archive economics' includes data protection officer. Evidence must address this risk without retaining credentials: Workspace defaults obscure a table-specific compliance or cost requirement. Which recommendation supplies sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Associate the rule with an explicit resource scope for Validate retention and archive economics. Independently, accept without proof that a related checkpoint proves the current expected state.** — The command-level assertion is anchored in the fact that target resource ID, association name, and DCR ID without host or user data. Operationally, that evidence supports Associate the rule with an explicit resource scope, so it cannot demonstrate Interactive and total retention match the documented use case for each reviewed table.
- ✗ **B. Store unredacted Validate retention and archive economics output with operator, tenant, token, and request context. Next, rely on the claim that reproduction requires every captured field.** — unredacted implementation output. The requirement-to-evidence link establishes that identity, tenant, or token material exceeds the non-secret evidence contract.
- ✓ **C. Retain table-level retention summary and a synthetic monthly-ingestion estimate. Then, exclude credentials and unrelated response fields.** — The WAF consequence identifies that table-level retention summary and a synthetic monthly-ingestion estimate. Operationally, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **D. Record only the Validate retention and archive economics positive inspection's exit status, and then rely on the belief that projected properties and assertion results can be reconstructed later.** — The controlling fact is that the positive inspection's exit status. The requirement-to-evidence link establishes that an exit code alone does not show whether interactive and total retention match the documented use case for each reviewed table.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q44 — answer D

The team asks finOps to assess 'Validate retention and archive economics'. The target is Interactive and total retention match the documented use case for each reviewed table, but the latest evidence does not show it. Choose the most likely cause.

- ✗ **A. Treat 'The chosen category group is unsupported by the resource provider' as grounds to reject Validate retention and archive economics. Afterward, consider it sufficient that route resource logs with diagnostic settings's failure model applies unchanged here.** — The relevant observation is that the chosen category group is unsupported by the resource provider. The requirement-to-evidence link establishes that that condition belongs to Route resource logs with diagnostic settings and does not by itself invalidate Regional workspaces with cross-workspace queries and policy-driven routing.
- ✗ **B. Ignore the negative assertion 'High-volume tables do not inherit unjustified extended interactive retention'; next, take it as conclusive that a later material change will make it unnecessary.** — The checkpoint specifically records that high-volume tables do not inherit unjustified extended interactive retention. The requirement-to-evidence link establishes that the negative assertion must be evaluated now, independent of a later business change.
- ✗ **C. Investigate Establish regional workspace boundaries instead of diagnosing Validate retention and archive economics. In addition, treat it as established that a passing result at Establish regional workspace boundaries identifies the current cause.** — The scenario makes clear that the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. The requirement-to-evidence link establishes that a passing result at Establish regional workspace boundaries gives no causal evidence for the failure at Validate retention and archive economics.
- ✓ **D. Investigate workspace defaults obscure a table-specific compliance or cost requirement. Next, isolate that cause before changing Regional workspaces with cross-workspace queries and policy-driven routing.** — The authored acceptance boundary states that workspace defaults obscure a table-specific compliance or cost requirement. The requirement-to-evidence link establishes that it is the checkpoint's causal failure model and should be isolated before retrying Validate retention and archive economics.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q45 — answer C

A recommendation on 'Validate retention and archive economics' is requested by security operations. The run encountered this modeled failure: Workspace defaults obscure a table-specific compliance or cost requirement. Which answer describes the safest recovery action?

- ✗ **A. Perform cleanup immediately: Export required sanitized evidence before removing the workspace; never retain customer log data; as an independent condition, proceed on the belief that the failed operation and its returned identifiers do not need reconciliation.** — The applicable design condition is that export required sanitized evidence before removing the workspace; never retain customer log data. The requirement-to-evidence link establishes that cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **B. Create a different run identity before diagnosing 'Workspace defaults obscure a table-specific compliance or cost requirement'; separately, treat as decisive the assertion that the first state record and returned identifiers can be discarded.** — The review is governed by this fact: workspace defaults obscure a table-specific compliance or cost requirement. The requirement-to-evidence link establishes that discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✓ **C. Recalculate retention by evidence class and update only the affected table plan. As another control, preserve the current run identity and evidence.** — The architecture evidence must show that recalculate retention by evidence class and update only the affected table plan. The requirement-to-evidence link establishes that it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **D. Change Establish regional workspace boundaries instead. Then, base approval on the claim that success at Establish regional workspace boundaries will repair the failed state at Validate retention and archive economics.** — The retained result must be reconciled with the fact that the workspace is in the approved data boundary with thirty-day interactive retention and ownership tags. The requirement-to-evidence link establishes that altering an already separate checkpoint does not repair the modeled failure at Validate retention and archive economics.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q46 — answer B

'Validate retention and archive economics' is assigned to regional platform teams. Without making a new change, the team must inspect the risk 'Workspace defaults obscure a table-specific compliance or cost requirement' using the Azure CLI lane. What should be recorded as the read-only, lane-correct inspection?

- ✗ **A. Rerun the Validate retention and archive economics implementation command and infer the expected state, and then use as justification the claim that absence of a shell error proves every property.** — The safe operating boundary says that the implementation command. The requirement-to-evidence link establishes that it can mutate state and shell success does not independently assert the expected properties.
- ✓ **B. Inspect the documented properties for Validate retention and archive economics. In addition, retain this evidence: table-level retention summary and a synthetic monthly-ingestion estimate.** — The decision tension comes from the fact that interactive and total retention match the documented use case for each reviewed table. The requirement-to-evidence link establishes that the read-only inspection directly tests the properties required at Validate retention and archive economics.
- ✗ **C. Run only this negative inspection for Validate retention and archive economics: High-volume tables do not inherit unjustified extended interactive retention. Also, accept without proof that an empty negative result reports every required positive property.** — The traceable checkpoint outcome is that the negative inspection. The requirement-to-evidence link establishes that absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Define an Azure Monitor Agent data collection rule and apply it to Validate retention and archive economics; in a separate step, rely on the claim that any command from the same lane proves the current checkpoint.** — The failure model establishes that the positive inspection for Define an Azure Monitor Agent data collection rule. The requirement-to-evidence link establishes that it is lane-correct but proves Define an Azure Monitor Agent data collection rule, not Validate retention and archive economics.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q47 — answer D

An assurance review of 'Validate retention and archive economics' includes data protection officer. A passing positive check does not by itself prove this negative assertion: High-volume tables do not inherit unjustified extended interactive retention. Which proposal supplies the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Validate retention and archive economics and report full compliance. In addition, use the premise that every prohibited parallel state must therefore be absent.** — The WAF consequence identifies that interactive and total retention match the documented use case for each reviewed table. The requirement-to-evidence link establishes that the positive result alone does not test the explicit anti-condition 'High-volume tables do not inherit unjustified extended interactive retention'.
- ✗ **B. Prove only that high-volume tables do not inherit unjustified extended interactive retention and report the intended configuration as present; before approval, consider it sufficient that absence is equivalent to positive-state evidence.** — The command-level assertion is anchored in the fact that high-volume tables do not inherit unjustified extended interactive retention. The requirement-to-evidence link establishes that absence evidence cannot demonstrate the required positive state 'Interactive and total retention match the documented use case for each reviewed table'.
- ✗ **C. Use Associate the rule with an explicit resource scope's negative assertion for Validate retention and archive economics. Separately, take it as conclusive that negative assertions are interchangeable between checkpoints.** — the target is not simultaneously associated with a competing lab DCR. Consequently, the second assertion is valid for Associate the rule with an explicit resource scope but leaves this checkpoint's prohibited state untested.
- ✓ **D. Verify the positive properties for Validate retention and archive economics. Before sign-off, independently verify that high-volume tables do not inherit unjustified extended interactive retention.** — The recovery guidance assumes that interactive and total retention match the documented use case for each reviewed table; High-volume tables do not inherit unjustified extended interactive retention. The requirement-to-evidence link establishes that two independent observations prevent a passing positive check from concealing an unsafe parallel state.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q48 — answer C

Approval of 'Validate retention and archive economics' is questioned by finOps. The board wants the Well-Architected consequence of mitigating this risk: Workspace defaults obscure a table-specific compliance or cost requirement. Which option best represents the consequence attributable to this checkpoint?

- ✗ **A. Use the Route resource logs with diagnostic settings consequence as the result for Validate retention and archive economics. Then, rely on the belief that a pillar statement remains valid when moved away from Route resource logs with diagnostic settings.** — The authored acceptance boundary states that operational Excellence: diagnostic settings create a repeatable routing contract that teams can inspect. Consequently, that tradeoff belongs to Route resource logs with diagnostic settings and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Validate retention and archive economics outcome; afterward, proceed on the belief that a moderate cost classification outweighs the mandatory architecture state.** — The relevant observation is that the required outcome at Validate retention and archive economics. Consequently, cost Optimization cannot remove the acceptance condition 'Interactive and total retention match the documented use case for each reviewed table'.
- ✓ **C. Record this consequence: Cost Optimization: table-level retention aligns searchable and archived data with its continuing value; afterward, tie it to LAB01-REQ-05.** — The controlling fact is that cost Optimization: table-level retention aligns searchable and archived data with its continuing value. Consequently, it states the authored pillar consequence of the control evaluated at Validate retention and archive economics.
- ✗ **D. Treat 'Cost Optimization: table-level retention aligns searchable and archived data with its continuing value' as proof that all five pillars pass; then treat as decisive the assertion that the checkpoint 'Validate retention and archive economics' no longer needs its separate negative check.** — The checkpoint specifically records that high-volume tables do not inherit unjustified extended interactive retention. Consequently, one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q49 — answer A

The implementation review has reached 'Validate retention and archive economics'. A material change now applies: A new regulator requires security control-plane records to remain in-region for seven years while application traces must stay searchable for only thirty days; revise routing and retention without duplicating every stream. Which course of action provides the correct revision to the decision record?

- ✓ **A. Re-score Regional workspaces with cross-workspace queries and policy-driven routing and both alternatives for Validate retention and archive economics, and then supersede the ADR using the changed evidence for LAB01-REQ-05.** — The scenario makes clear that regional workspaces with cross-workspace queries and policy-driven routing at Validate retention and archive economics. Consequently, the material change 'A new regulator requires security control-plane records to remain in-region for seven years while application traces must stay searchable for only thirty days; revise routing and retention without duplicating every stream.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **B. Retain Regional workspaces with cross-workspace queries and policy-driven routing at Validate retention and archive economics without recalculating criteria or eligibility; in a separate step, treat it as established that the original weighted result is permanent.** — The architecture evidence must show that regional workspaces with cross-workspace queries and policy-driven routing. Consequently, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **C. Select Central Log Analytics workspace with DCR-based collection and archive export for Validate retention and archive economics without rechecking its mandatory constraints. As another control, use as justification the claim that being different from the current design is an architecture criterion.** — The applicable design condition is that central Log Analytics workspace with DCR-based collection and archive export. Consequently, being different is not a criterion, and the candidate still must avoid the prohibited state at Validate retention and archive economics.
- ✗ **D. Keep Dedicated workspace per workload with independent retention and access eligible at Validate retention and archive economics by downgrading LAB01-REQ-05; as a separate check, accept without proof that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The review is governed by this fact: lAB01-REQ-05. Consequently, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)

## LAB01-Q50 — answer C

The approach to 'Validate retention and archive economics' is challenged by regional platform teams. After a partial run, cleanup must follow this dependency: Export required sanitized evidence before removing the workspace; never retain customer log data. Which finding constitutes the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Define an Azure Monitor Agent data collection rule before reconciling the current dependency. Separately, base approval on the claim that removing a parent needed to identify Validate retention and archive economics is harmless.** — The decision tension comes from the fact that delete all DCR associations before deleting the DCR. Consequently, a cleanup rule for Define an Azure Monitor Agent data collection rule cannot override the dependency declared for Validate retention and archive economics.
- ✗ **B. Delete candidates by display name before comparing the Validate retention and archive economics ownership tags; for this decision, use the premise that the dependency rule 'Export required sanitized evidence before removing the workspace; never retain customer log data' is optional.** — The safe operating boundary says that table-level retention summary and a synthetic monthly-ingestion estimate. Consequently, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✓ **C. Verify exact run-state IDs and ownership tags for Validate retention and archive economics; as a separate check, follow this dependency rule without purge: Export required sanitized evidence before removing the workspace; never retain customer log data.** — The retained result must be reconciled with the fact that export required sanitized evidence before removing the workspace; never retain customer log data. Consequently, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **D. Destroy recoverable copies before retaining the Validate retention and archive economics negative assertion 'High-volume tables do not inherit unjustified extended interactive retention'. Before sign-off, consider it sufficient that remaining command logs are sufficient recovery evidence.** — The traceable checkpoint outcome is that high-volume tables do not inherit unjustified extended interactive retention. Consequently, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/platform/diagnostic-settings (verified 2026-09-02)
<!-- END GENERATED AZ305 V1 -->
