<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-02 answer key

Use after completing the learner assessment. Every choice has a specific explanation.

## LAB02-Q01 — answer D

A decision test for 'Build a layered signal inventory' includes application owners. Approval requires a positive result plus this independent negative assertion: No unsupported or deprecated metric is used as a release gate. What is the acceptance rule that makes LAB02-REQ-01 testable?

- ✗ **A. Select Resource-by-resource static thresholds with team-specific receivers before checking Build a layered signal inventory. Afterward, treat as decisive the assertion that a successful deployment will later prove the architecture constraint.** — The recovery guidance assumes that no unsupported or deprecated metric is used as a release gate. Consequently, a deployment result cannot prove LAB02-REQ-01, and Resource-by-resource static thresholds with team-specific receivers still has to meet the mandatory boundary.
- ✗ **B. Use the passing result from Design platform and resource-health alerts to approve Build a layered signal inventory; next, base approval on the claim that one control establishes an unrelated acceptance boundary.** — The WAF consequence identifies that resource Health and Service Health alerts are separated from routine administrative events and have owned severities. Consequently, that outcome belongs to Design platform and resource-health alerts and leaves Build a layered signal inventory unverified.
- ✗ **C. Choose External monitoring only with Azure telemetry exported downstream and skip the Build a layered signal inventory negative assertion. In addition, use the premise that the candidate has the lowest implementation effort.** — The command-level assertion is anchored in the fact that detect and triage material service degradation before customers report it while reducing unactionable alerts. Consequently, implementation effort cannot justify skipping the negative assertion or displace LAB02-REQ-01.
- ✓ **D. Require the documented positive state for Build a layered signal inventory. Separately, verify that no unsupported or deprecated metric is used as a release gate.** — The failure model establishes that the design identifies platform, application, dependency, and business signals with explicit owners. Consequently, the positive state and an independent negative assertion jointly make LAB02-REQ-01 testable.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q02 — answer B

The architecture board reconsiders 'Build a layered signal inventory' with security operations. The selected architecture is Service-centric alerts with shared action groups and curated workbooks; object existence alone is not success. Which recommendation supplies the intended successful finding?

- ✗ **A. Use only the negative assertion 'No unsupported or deprecated metric is used as a release gate' as the success result; as an independent condition, accept without proof that absence proves every required positive property.** — The controlling fact is that no unsupported or deprecated metric is used as a release gate. For this case, this is the independent prohibited-state assertion, not a successful finding.
- ✓ **B. Record the design identifies platform, application, dependency, and business signals with explicit owners; independently, classify it as success for LAB02-REQ-01.** — the design identifies platform, application, dependency, and business signals with explicit owners. For this case, this is the authored target state for Build a layered signal inventory and directly supports LAB02-REQ-01.
- ✗ **C. Use the successful finding from Define a query-based service-level alert as the result for Build a layered signal inventory; independently, rely on the claim that a property from the current checkpoint does not need to be inspected.** — The authored acceptance boundary states that the selected log alert evaluates an auditable customer-impact query over a suitable window and frequency. For this case, evidence for Define a query-based service-level alert cannot substitute for the properties required at Build a layered signal inventory.
- ✗ **D. Record the failure condition 'A desired metric is unavailable at the resource SKU or namespace' as a successful state. Then, rely on the belief that the command returned an object.** — The relevant observation is that a desired metric is unavailable at the resource SKU or namespace. For this case, resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q03 — answer C

A review of 'Build a layered signal inventory' begins with input from service desk. Evidence must address this risk without retaining credentials: A desired metric is unavailable at the resource SKU or namespace. Choose sufficient, properly scoped evidence.

- ✗ **A. Substitute the evidence from Curate an operator workbook for Build a layered signal inventory, and then consider it sufficient that a related checkpoint proves the current expected state.** — The scenario makes clear that workbook resource ID, display name, query-purpose inventory, and accessibility review. For this case, that evidence supports Curate an operator workbook, so it cannot demonstrate The design identifies platform, application, dependency, and business signals with explicit owners.
- ✗ **B. Store unredacted Build a layered signal inventory output with operator, tenant, token, and request context. Also, take it as conclusive that reproduction requires every captured field.** — The architecture evidence must show that unredacted implementation output. For this case, identity, tenant, or token material exceeds the non-secret evidence contract.
- ✓ **C. Retain metric namespace, aggregation, grain, owner, and business symptom mapping. Independently, exclude credentials and unrelated response fields.** — The checkpoint specifically records that metric namespace, aggregation, grain, owner, and business symptom mapping. For this case, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **D. Record only the Build a layered signal inventory positive inspection's exit status; in a separate step, treat it as established that projected properties and assertion results can be reconstructed later.** — The applicable design condition is that the positive inspection's exit status. For this case, an exit code alone does not show whether the design identifies platform, application, dependency, and business signals with explicit owners.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q04 — answer D

'Build a layered signal inventory' awaits approval from site reliability engineering. The target is The design identifies platform, application, dependency, and business signals with explicit owners, but the latest evidence does not show it. Which answer describes the most likely cause?

- ✗ **A. Treat 'An action group exists but a receiver is disabled, unverified, or unsupported in the region' as grounds to reject Build a layered signal inventory. In addition, proceed on the belief that verify action routing and noise controls's failure model applies unchanged here.** — The retained result must be reconciled with the fact that an action group exists but a receiver is disabled, unverified, or unsupported in the region. For this case, that condition belongs to Verify action routing and noise controls and does not by itself invalidate Service-centric alerts with shared action groups and curated workbooks.
- ✗ **B. Ignore the negative assertion 'No unsupported or deprecated metric is used as a release gate'; before approval, treat as decisive the assertion that a later material change will make it unnecessary.** — The decision tension comes from the fact that no unsupported or deprecated metric is used as a release gate. For this case, the negative assertion must be evaluated now, independent of a later business change.
- ✗ **C. Investigate Design platform and resource-health alerts instead of diagnosing Build a layered signal inventory. Separately, base approval on the claim that a passing result at Design platform and resource-health alerts identifies the current cause.** — The safe operating boundary says that resource Health and Service Health alerts are separated from routine administrative events and have owned severities. For this case, a passing result at Design platform and resource-health alerts gives no causal evidence for the failure at Build a layered signal inventory.
- ✓ **D. Investigate a desired metric is unavailable at the resource SKU or namespace; in a separate step, isolate that cause before changing Service-centric alerts with shared action groups and curated workbooks.** — The review is governed by this fact: a desired metric is unavailable at the resource SKU or namespace. For this case, it is the checkpoint's causal failure model and should be isolated before retrying Build a layered signal inventory.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q05 — answer B

'Build a layered signal inventory' is reopened at the request of application owners. The run encountered this modeled failure: A desired metric is unavailable at the resource SKU or namespace. What should be recorded as the safest recovery action?

- ✗ **A. Perform cleanup immediately: No resource cleanup is required for this read-only inventory checkpoint. Then, use as justification the claim that the failed operation and its returned identifiers do not need reconciliation.** — The failure model establishes that no resource cleanup is required for this read-only inventory checkpoint. For this case, cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✓ **B. Select a supported proxy signal and record the detection trade-off before continuing; next, preserve the current run identity and evidence.** — The traceable checkpoint outcome is that select a supported proxy signal and record the detection trade-off before continuing. For this case, it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **C. Create a different run identity before diagnosing 'A desired metric is unavailable at the resource SKU or namespace'; afterward, accept without proof that the first state record and returned identifiers can be discarded.** — The recovery guidance assumes that a desired metric is unavailable at the resource SKU or namespace. For this case, discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Design platform and resource-health alerts instead; then rely on the claim that success at Design platform and resource-health alerts will repair the failed state at Build a layered signal inventory.** — The WAF consequence identifies that resource Health and Service Health alerts are separated from routine administrative events and have owned severities. For this case, altering an already separate checkpoint does not repair the modeled failure at Build a layered signal inventory.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q06 — answer D

A design review of 'Build a layered signal inventory' includes security operations. Without making a new change, the team must inspect the risk 'A desired metric is unavailable at the resource SKU or namespace' using the Azure PowerShell lane. Which proposal supplies the read-only, lane-correct inspection?

- ✗ **A. Rerun the Build a layered signal inventory implementation command and infer the expected state; in a separate step, use the premise that absence of a shell error proves every property.** — the implementation command. That evidence means it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Build a layered signal inventory: No unsupported or deprecated metric is used as a release gate. As another control, consider it sufficient that an empty negative result reports every required positive property.** — The controlling fact is that the negative inspection. That evidence means absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **C. Run the positive inspection for Define a query-based service-level alert and apply it to Build a layered signal inventory; as a separate check, take it as conclusive that any command from the same lane proves the current checkpoint.** — The authored acceptance boundary states that the positive inspection for Define a query-based service-level alert. That evidence means it is lane-correct but proves Define a query-based service-level alert, not Build a layered signal inventory.
- ✓ **D. Inspect the documented properties for Build a layered signal inventory; for this decision, retain this evidence: metric namespace, aggregation, grain, owner, and business symptom mapping.** — The command-level assertion is anchored in the fact that the design identifies platform, application, dependency, and business signals with explicit owners. For this case, the read-only inspection directly tests the properties required at Build a layered signal inventory.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q07 — answer D

The team asks service desk to assess 'Build a layered signal inventory'. A passing positive check does not by itself prove this negative assertion: No unsupported or deprecated metric is used as a release gate. Which option best represents the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Build a layered signal inventory and report full compliance. Separately, rely on the belief that every prohibited parallel state must therefore be absent.** — The checkpoint specifically records that the design identifies platform, application, dependency, and business signals with explicit owners. That evidence means the positive result alone does not test the explicit anti-condition 'No unsupported or deprecated metric is used as a release gate'.
- ✗ **B. Prove only that no unsupported or deprecated metric is used as a release gate and report the intended configuration as present; for this decision, proceed on the belief that absence is equivalent to positive-state evidence.** — The scenario makes clear that no unsupported or deprecated metric is used as a release gate. That evidence means absence evidence cannot demonstrate the required positive state 'The design identifies platform, application, dependency, and business signals with explicit owners'.
- ✗ **C. Use Curate an operator workbook's negative assertion for Build a layered signal inventory. Before sign-off, treat as decisive the assertion that negative assertions are interchangeable between checkpoints.** — The architecture evidence must show that no panel depends on personal data, raw secrets, or an undocumented cross-workspace permission. That evidence means the second assertion is valid for Curate an operator workbook but leaves this checkpoint's prohibited state untested.
- ✓ **D. Verify the positive properties for Build a layered signal inventory. Then, independently verify that no unsupported or deprecated metric is used as a release gate.** — The relevant observation is that the design identifies platform, application, dependency, and business signals with explicit owners; No unsupported or deprecated metric is used as a release gate. That evidence means two independent observations prevent a passing positive check from concealing an unsafe parallel state.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q08 — answer B

A recommendation on 'Build a layered signal inventory' is requested by site reliability engineering. The board wants the Well-Architected consequence of mitigating this risk: A desired metric is unavailable at the resource SKU or namespace. Which course of action provides the consequence attributable to this checkpoint?

- ✗ **A. Use the Verify action routing and noise controls consequence as the result for Build a layered signal inventory; then treat it as established that a pillar statement remains valid when moved away from Verify action routing and noise controls.** — The review is governed by this fact: operational Excellence: severity and action routing send actionable work to durable, accountable teams. That evidence means that tradeoff belongs to Verify action routing and noise controls and does not explain this checkpoint's decision.
- ✓ **B. Record this consequence: Performance Efficiency: signals aligned to saturation and latency expose capacity bottlenecks without indiscriminate telemetry. Next, tie it to LAB02-REQ-01.** — The applicable design condition is that performance Efficiency: signals aligned to saturation and latency expose capacity bottlenecks without indiscriminate telemetry. That evidence means it states the authored pillar consequence of the control evaluated at Build a layered signal inventory.
- ✗ **C. Remove the control responsible for the Build a layered signal inventory outcome. Independently, use as justification the claim that a low cost classification outweighs the mandatory architecture state.** — The retained result must be reconciled with the fact that the required outcome at Build a layered signal inventory. That evidence means cost Optimization cannot remove the acceptance condition 'The design identifies platform, application, dependency, and business signals with explicit owners'.
- ✗ **D. Treat 'Performance Efficiency: signals aligned to saturation and latency expose capacity bottlenecks without indiscriminate telemetry' as proof that all five pillars pass. Next, accept without proof that the checkpoint 'Build a layered signal inventory' no longer needs its separate negative check.** — The decision tension comes from the fact that no unsupported or deprecated metric is used as a release gate. That evidence means one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q09 — answer D

'Build a layered signal inventory' is assigned to application owners. A material change now applies: The payment API adopts a bursty promotion model that triples legitimate traffic for fifteen minutes, so static latency and error-rate thresholds must be revised without masking genuine customer impact. Which finding constitutes the correct revision to the decision record?

- ✗ **A. Retain Service-centric alerts with shared action groups and curated workbooks at Build a layered signal inventory without recalculating criteria or eligibility; as a separate check, base approval on the claim that the original weighted result is permanent.** — The traceable checkpoint outcome is that service-centric alerts with shared action groups and curated workbooks. That evidence means the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Resource-by-resource static thresholds with team-specific receivers for Build a layered signal inventory without rechecking its mandatory constraints. Afterward, use the premise that being different from the current design is an architecture criterion.** — The failure model establishes that resource-by-resource static thresholds with team-specific receivers. That evidence means being different is not a criterion, and the candidate still must avoid the prohibited state at Build a layered signal inventory.
- ✗ **C. Keep External monitoring only with Azure telemetry exported downstream eligible at Build a layered signal inventory by downgrading LAB02-REQ-01; next, consider it sufficient that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The recovery guidance assumes that lAB02-REQ-01. That evidence means an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.
- ✓ **D. Re-score Service-centric alerts with shared action groups and curated workbooks and both alternatives for Build a layered signal inventory. As another control, supersede the ADR using the changed evidence for LAB02-REQ-01.** — The safe operating boundary says that service-centric alerts with shared action groups and curated workbooks at Build a layered signal inventory. That evidence means the material change 'The payment API adopts a bursty promotion model that triples legitimate traffic for fifteen minutes, so static latency and error-rate thresholds must be revised without masking genuine customer impact.' requires fresh eligibility, weighted analysis, and a superseding decision.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q10 — answer B

An assurance review of 'Build a layered signal inventory' includes security operations. After a partial run, cleanup must follow this dependency: No resource cleanup is required for this read-only inventory checkpoint. Which recommendation delivers the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Define a query-based service-level alert before reconciling the current dependency. Before sign-off, rely on the claim that removing a parent needed to identify Build a layered signal inventory is harmless.** — The command-level assertion is anchored in the fact that delete the scheduled-query rule before deleting its action group or workspace dependency. That evidence means a cleanup rule for Define a query-based service-level alert cannot override the dependency declared for Build a layered signal inventory.
- ✓ **B. Verify exact run-state IDs and ownership tags for Build a layered signal inventory. In addition, follow this dependency rule without purge: No resource cleanup is required for this read-only inventory checkpoint.** — The WAF consequence identifies that no resource cleanup is required for this read-only inventory checkpoint. That evidence means exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **C. Delete candidates by display name before comparing the Build a layered signal inventory ownership tags; as an independent condition, rely on the belief that the dependency rule 'No resource cleanup is required for this read-only inventory checkpoint' is optional.** — metric namespace, aggregation, grain, owner, and business symptom mapping. The resulting architectural conclusion is that names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Build a layered signal inventory negative assertion 'No unsupported or deprecated metric is used as a release gate'; during the same review, proceed on the belief that remaining command logs are sufficient recovery evidence.** — The controlling fact is that no unsupported or deprecated metric is used as a release gate. The resulting architectural conclusion is that irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q11 — answer B

Approval of 'Design platform and resource-health alerts' is questioned by security operations. Approval requires a positive result plus this independent negative assertion: Broad administrative activity does not page the reliability team without a material condition. Which recommendation supplies the acceptance rule that makes LAB02-REQ-02 testable?

- ✗ **A. Select Resource-by-resource static thresholds with team-specific receivers before checking Design platform and resource-health alerts. In addition, accept without proof that a successful deployment will later prove the architecture constraint.** — The relevant observation is that broad administrative activity does not page the reliability team without a material condition. The resulting architectural conclusion is that a deployment result cannot prove LAB02-REQ-02, and Resource-by-resource static thresholds with team-specific receivers still has to meet the mandatory boundary.
- ✓ **B. Require the documented positive state for Design platform and resource-health alerts; as an independent condition, verify that broad administrative activity does not page the reliability team without a material condition.** — The authored acceptance boundary states that resource Health and Service Health alerts are separated from routine administrative events and have owned severities. The resulting architectural conclusion is that the positive state and an independent negative assertion jointly make LAB02-REQ-02 testable.
- ✗ **C. Use the passing result from Build a layered signal inventory to approve Design platform and resource-health alerts; before approval, rely on the claim that one control establishes an unrelated acceptance boundary.** — The checkpoint specifically records that the design identifies platform, application, dependency, and business signals with explicit owners. The resulting architectural conclusion is that that outcome belongs to Build a layered signal inventory and leaves Design platform and resource-health alerts unverified.
- ✗ **D. Choose External monitoring only with Azure telemetry exported downstream and skip the Design platform and resource-health alerts negative assertion. Separately, rely on the belief that the candidate has the lowest implementation effort.** — The scenario makes clear that detect and triage material service degradation before customers report it while reducing unactionable alerts. The resulting architectural conclusion is that implementation effort cannot justify skipping the negative assertion or displace LAB02-REQ-02.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q12 — answer C

The implementation review has reached 'Design platform and resource-health alerts'. The selected architecture is Service-centric alerts with shared action groups and curated workbooks; object existence alone is not success. Choose the intended successful finding.

- ✗ **A. Use only the negative assertion 'Broad administrative activity does not page the reliability team without a material condition' as the success result. Then, consider it sufficient that absence proves every required positive property.** — The applicable design condition is that broad administrative activity does not page the reliability team without a material condition. The resulting architectural conclusion is that this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Define a query-based service-level alert as the result for Design platform and resource-health alerts; afterward, take it as conclusive that a property from the current checkpoint does not need to be inspected.** — The review is governed by this fact: the selected log alert evaluates an auditable customer-impact query over a suitable window and frequency. The resulting architectural conclusion is that evidence for Define a query-based service-level alert cannot substitute for the properties required at Design platform and resource-health alerts.
- ✓ **C. Record resource Health and Service Health alerts are separated from routine administrative events and have owned severities; then classify it as success for LAB02-REQ-02.** — The architecture evidence must show that resource Health and Service Health alerts are separated from routine administrative events and have owned severities. The resulting architectural conclusion is that this is the authored target state for Design platform and resource-health alerts and directly supports LAB02-REQ-02.
- ✗ **D. Record the failure condition 'Subscription scope or action authorization is narrower than the intended failure domain' as a successful state; then treat it as established that the command returned an object.** — The retained result must be reconciled with the fact that subscription scope or action authorization is narrower than the intended failure domain. The resulting architectural conclusion is that resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q13 — answer B

The approach to 'Design platform and resource-health alerts' is challenged by site reliability engineering. Evidence must address this risk without retaining credentials: Subscription scope or action authorization is narrower than the intended failure domain. Which answer describes sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Curate an operator workbook for Design platform and resource-health alerts; in a separate step, proceed on the belief that a related checkpoint proves the current expected state.** — The safe operating boundary says that workbook resource ID, display name, query-purpose inventory, and accessibility review. The resulting architectural conclusion is that that evidence supports Curate an operator workbook, so it cannot demonstrate Resource Health and Service Health alerts are separated from routine administrative events and have owned severities.
- ✓ **B. Retain alert scope, category, status, severity rationale, and owner alias using synthetic contacts. Also, exclude credentials and unrelated response fields.** — The decision tension comes from the fact that alert scope, category, status, severity rationale, and owner alias using synthetic contacts. The resulting architectural conclusion is that it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **C. Store unredacted Design platform and resource-health alerts output with operator, tenant, token, and request context. As another control, treat as decisive the assertion that reproduction requires every captured field.** — The traceable checkpoint outcome is that unredacted implementation output. The resulting architectural conclusion is that identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **D. Record only the Design platform and resource-health alerts positive inspection's exit status; as a separate check, base approval on the claim that projected properties and assertion results can be reconstructed later.** — The failure model establishes that the positive inspection's exit status. The resulting architectural conclusion is that an exit code alone does not show whether resource Health and Service Health alerts are separated from routine administrative events and have owned severities.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q14 — answer C

A decision test for 'Design platform and resource-health alerts' includes application owners. The target is Resource Health and Service Health alerts are separated from routine administrative events and have owned severities, but the latest evidence does not show it. What should be recorded as the most likely cause?

- ✗ **A. Treat 'An action group exists but a receiver is disabled, unverified, or unsupported in the region' as grounds to reject Design platform and resource-health alerts. Separately, use as justification the claim that verify action routing and noise controls's failure model applies unchanged here.** — The WAF consequence identifies that an action group exists but a receiver is disabled, unverified, or unsupported in the region. The resulting architectural conclusion is that that condition belongs to Verify action routing and noise controls and does not by itself invalidate Service-centric alerts with shared action groups and curated workbooks.
- ✗ **B. Ignore the negative assertion 'Broad administrative activity does not page the reliability team without a material condition'; for this decision, accept without proof that a later material change will make it unnecessary.** — The command-level assertion is anchored in the fact that broad administrative activity does not page the reliability team without a material condition. The resulting architectural conclusion is that the negative assertion must be evaluated now, independent of a later business change.
- ✓ **C. Investigate subscription scope or action authorization is narrower than the intended failure domain. Afterward, isolate that cause before changing Service-centric alerts with shared action groups and curated workbooks.** — The recovery guidance assumes that subscription scope or action authorization is narrower than the intended failure domain. The resulting architectural conclusion is that it is the checkpoint's causal failure model and should be isolated before retrying Design platform and resource-health alerts.
- ✗ **D. Investigate Build a layered signal inventory instead of diagnosing Design platform and resource-health alerts. Before sign-off, rely on the claim that a passing result at Build a layered signal inventory identifies the current cause.** — the design identifies platform, application, dependency, and business signals with explicit owners. Under the stated constraint, a passing result at Build a layered signal inventory gives no causal evidence for the failure at Design platform and resource-health alerts.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q15 — answer A

The architecture board reconsiders 'Design platform and resource-health alerts' with security operations. The run encountered this modeled failure: Subscription scope or action authorization is narrower than the intended failure domain. Which proposal supplies the safest recovery action?

- ✓ **A. Reduce scope to an authorized management boundary and document any coverage gap. Separately, preserve the current run identity and evidence.** — The controlling fact is that reduce scope to an authorized management boundary and document any coverage gap. Under the stated constraint, it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **B. Perform cleanup immediately: Remove test activity-log alerts before action groups when cleanup is authorized; then use the premise that the failed operation and its returned identifiers do not need reconciliation.** — The authored acceptance boundary states that remove test activity-log alerts before action groups when cleanup is authorized. Under the stated constraint, cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **C. Create a different run identity before diagnosing 'Subscription scope or action authorization is narrower than the intended failure domain'. Independently, consider it sufficient that the first state record and returned identifiers can be discarded.** — The relevant observation is that subscription scope or action authorization is narrower than the intended failure domain. Under the stated constraint, discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Build a layered signal inventory instead. Next, take it as conclusive that success at Build a layered signal inventory will repair the failed state at Design platform and resource-health alerts.** — The checkpoint specifically records that the design identifies platform, application, dependency, and business signals with explicit owners. Under the stated constraint, altering an already separate checkpoint does not repair the modeled failure at Design platform and resource-health alerts.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q16 — answer D

A review of 'Design platform and resource-health alerts' begins with input from service desk. Without making a new change, the team must inspect the risk 'Subscription scope or action authorization is narrower than the intended failure domain' using the Azure PowerShell lane. Which option best represents the read-only, lane-correct inspection?

- ✗ **A. Rerun the Design platform and resource-health alerts implementation command and infer the expected state; as a separate check, rely on the belief that absence of a shell error proves every property.** — The architecture evidence must show that the implementation command. Under the stated constraint, it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Design platform and resource-health alerts: Broad administrative activity does not page the reliability team without a material condition. Afterward, proceed on the belief that an empty negative result reports every required positive property.** — The applicable design condition is that the negative inspection. Under the stated constraint, absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **C. Run the positive inspection for Define a query-based service-level alert and apply it to Design platform and resource-health alerts; next, treat as decisive the assertion that any command from the same lane proves the current checkpoint.** — The review is governed by this fact: the positive inspection for Define a query-based service-level alert. Under the stated constraint, it is lane-correct but proves Define a query-based service-level alert, not Design platform and resource-health alerts.
- ✓ **D. Inspect the documented properties for Design platform and resource-health alerts; during the same review, retain this evidence: alert scope, category, status, severity rationale, and owner alias using synthetic contacts.** — The scenario makes clear that resource Health and Service Health alerts are separated from routine administrative events and have owned severities. Under the stated constraint, the read-only inspection directly tests the properties required at Design platform and resource-health alerts.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q17 — answer B

'Design platform and resource-health alerts' awaits approval from site reliability engineering. A passing positive check does not by itself prove this negative assertion: Broad administrative activity does not page the reliability team without a material condition. Which course of action provides the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Design platform and resource-health alerts and report full compliance. Before sign-off, treat it as established that every prohibited parallel state must therefore be absent.** — The decision tension comes from the fact that resource Health and Service Health alerts are separated from routine administrative events and have owned severities. Under the stated constraint, the positive result alone does not test the explicit anti-condition 'Broad administrative activity does not page the reliability team without a material condition'.
- ✓ **B. Verify the positive properties for Design platform and resource-health alerts. Independently, independently verify that broad administrative activity does not page the reliability team without a material condition.** — The retained result must be reconciled with the fact that resource Health and Service Health alerts are separated from routine administrative events and have owned severities; Broad administrative activity does not page the reliability team without a material condition. Under the stated constraint, two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **C. Prove only that broad administrative activity does not page the reliability team without a material condition and report the intended configuration as present; as an independent condition, use as justification the claim that absence is equivalent to positive-state evidence.** — The safe operating boundary says that broad administrative activity does not page the reliability team without a material condition. Under the stated constraint, absence evidence cannot demonstrate the required positive state 'Resource Health and Service Health alerts are separated from routine administrative events and have owned severities'.
- ✗ **D. Use Curate an operator workbook's negative assertion for Design platform and resource-health alerts; for the recorded decision, accept without proof that negative assertions are interchangeable between checkpoints.** — The traceable checkpoint outcome is that no panel depends on personal data, raw secrets, or an undocumented cross-workspace permission. Under the stated constraint, the second assertion is valid for Curate an operator workbook but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q18 — answer B

'Design platform and resource-health alerts' is reopened at the request of application owners. The board wants the Well-Architected consequence of mitigating this risk: Subscription scope or action authorization is narrower than the intended failure domain. Which finding constitutes the consequence attributable to this checkpoint?

- ✗ **A. Use the Verify action routing and noise controls consequence as the result for Design platform and resource-health alerts. Next, base approval on the claim that a pillar statement remains valid when moved away from Verify action routing and noise controls.** — The recovery guidance assumes that operational Excellence: severity and action routing send actionable work to durable, accountable teams. Under the stated constraint, that tradeoff belongs to Verify action routing and noise controls and does not explain this checkpoint's decision.
- ✓ **B. Record this consequence: Reliability: resource and service-health signals cover failures outside the application process; in a separate step, tie it to LAB02-REQ-02.** — The failure model establishes that reliability: resource and service-health signals cover failures outside the application process. Under the stated constraint, it states the authored pillar consequence of the control evaluated at Design platform and resource-health alerts.
- ✗ **C. Remove the control responsible for the Design platform and resource-health alerts outcome, and then use the premise that a low cost classification outweighs the mandatory architecture state.** — The WAF consequence identifies that the required outcome at Design platform and resource-health alerts. Under the stated constraint, cost Optimization cannot remove the acceptance condition 'Resource Health and Service Health alerts are separated from routine administrative events and have owned severities'.
- ✗ **D. Treat 'Reliability: resource and service-health signals cover failures outside the application process' as proof that all five pillars pass. Also, consider it sufficient that the checkpoint 'Design platform and resource-health alerts' no longer needs its separate negative check.** — The command-level assertion is anchored in the fact that broad administrative activity does not page the reliability team without a material condition. Under the stated constraint, one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q19 — answer C

A design review of 'Design platform and resource-health alerts' includes security operations. A material change now applies: The payment API adopts a bursty promotion model that triples legitimate traffic for fifteen minutes, so static latency and error-rate thresholds must be revised without masking genuine customer impact. Which recommendation delivers the correct revision to the decision record?

- ✗ **A. Retain Service-centric alerts with shared action groups and curated workbooks at Design platform and resource-health alerts without recalculating criteria or eligibility; next, rely on the claim that the original weighted result is permanent.** — The controlling fact is that service-centric alerts with shared action groups and curated workbooks. This matters because the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Resource-by-resource static thresholds with team-specific receivers for Design platform and resource-health alerts without rechecking its mandatory constraints. In addition, rely on the belief that being different from the current design is an architecture criterion.** — The authored acceptance boundary states that resource-by-resource static thresholds with team-specific receivers. This matters because being different is not a criterion, and the candidate still must avoid the prohibited state at Design platform and resource-health alerts.
- ✓ **C. Re-score Service-centric alerts with shared action groups and curated workbooks and both alternatives for Design platform and resource-health alerts; next, supersede the ADR using the changed evidence for LAB02-REQ-02.** — service-centric alerts with shared action groups and curated workbooks at Design platform and resource-health alerts. This matters because the material change 'The payment API adopts a bursty promotion model that triples legitimate traffic for fifteen minutes, so static latency and error-rate thresholds must be revised without masking genuine customer impact.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **D. Keep External monitoring only with Azure telemetry exported downstream eligible at Design platform and resource-health alerts by downgrading LAB02-REQ-02; before approval, proceed on the belief that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The relevant observation is that lAB02-REQ-02. This matters because an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q20 — answer A

The team asks service desk to assess 'Design platform and resource-health alerts'. After a partial run, cleanup must follow this dependency: Remove test activity-log alerts before action groups when cleanup is authorized. Which response meets the need for the dependency-safe cleanup plan?

- ✓ **A. Verify exact run-state IDs and ownership tags for Design platform and resource-health alerts; for this decision, follow this dependency rule without purge: Remove test activity-log alerts before action groups when cleanup is authorized.** — The checkpoint specifically records that remove test activity-log alerts before action groups when cleanup is authorized. This matters because exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **B. Apply the cleanup rule for Define a query-based service-level alert before reconciling the current dependency; as another gate, take it as conclusive that removing a parent needed to identify Design platform and resource-health alerts is harmless.** — The scenario makes clear that delete the scheduled-query rule before deleting its action group or workspace dependency. This matters because a cleanup rule for Define a query-based service-level alert cannot override the dependency declared for Design platform and resource-health alerts.
- ✗ **C. Delete candidates by display name before comparing the Design platform and resource-health alerts ownership tags. Then, treat it as established that the dependency rule 'Remove test activity-log alerts before action groups when cleanup is authorized' is optional.** — The architecture evidence must show that alert scope, category, status, severity rationale, and owner alias using synthetic contacts. This matters because names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Design platform and resource-health alerts negative assertion 'Broad administrative activity does not page the reliability team without a material condition'; afterward, use as justification the claim that remaining command logs are sufficient recovery evidence.** — The applicable design condition is that broad administrative activity does not page the reliability team without a material condition. This matters because irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q21 — answer A

A recommendation on 'Define a query-based service-level alert' is requested by service desk. Approval requires a positive result plus this independent negative assertion: No rule uses an evaluation cadence that can systematically miss its own observation window. Choose the acceptance rule that makes LAB02-REQ-03 testable.

- ✓ **A. Require the documented positive state for Define a query-based service-level alert; afterward, verify that no rule uses an evaluation cadence that can systematically miss its own observation window.** — The review is governed by this fact: the selected log alert evaluates an auditable customer-impact query over a suitable window and frequency. This matters because the positive state and an independent negative assertion jointly make LAB02-REQ-03 testable.
- ✗ **B. Select Resource-by-resource static thresholds with team-specific receivers before checking Define a query-based service-level alert. Separately, consider it sufficient that a successful deployment will later prove the architecture constraint.** — The retained result must be reconciled with the fact that no rule uses an evaluation cadence that can systematically miss its own observation window. This matters because a deployment result cannot prove LAB02-REQ-03, and Resource-by-resource static thresholds with team-specific receivers still has to meet the mandatory boundary.
- ✗ **C. Use the passing result from Build a layered signal inventory to approve Define a query-based service-level alert; for this decision, take it as conclusive that one control establishes an unrelated acceptance boundary.** — The decision tension comes from the fact that the design identifies platform, application, dependency, and business signals with explicit owners. This matters because that outcome belongs to Build a layered signal inventory and leaves Define a query-based service-level alert unverified.
- ✗ **D. Choose External monitoring only with Azure telemetry exported downstream and skip the Define a query-based service-level alert negative assertion. Before sign-off, treat it as established that the candidate has the lowest implementation effort.** — The safe operating boundary says that detect and triage material service degradation before customers report it while reducing unactionable alerts. This matters because implementation effort cannot justify skipping the negative assertion or displace LAB02-REQ-03.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q22 — answer B

'Define a query-based service-level alert' is assigned to site reliability engineering. The selected architecture is Service-centric alerts with shared action groups and curated workbooks; object existence alone is not success. Which answer describes the intended successful finding?

- ✗ **A. Use only the negative assertion 'No rule uses an evaluation cadence that can systematically miss its own observation window' as the success result; then proceed on the belief that absence proves every required positive property.** — The failure model establishes that no rule uses an evaluation cadence that can systematically miss its own observation window. This matters because this is the independent prohibited-state assertion, not a successful finding.
- ✓ **B. Record the selected log alert evaluates an auditable customer-impact query over a suitable window and frequency, and then classify it as success for LAB02-REQ-03.** — The traceable checkpoint outcome is that the selected log alert evaluates an auditable customer-impact query over a suitable window and frequency. This matters because this is the authored target state for Define a query-based service-level alert and directly supports LAB02-REQ-03.
- ✗ **C. Use the successful finding from Design platform and resource-health alerts as the result for Define a query-based service-level alert. Independently, treat as decisive the assertion that a property from the current checkpoint does not need to be inspected.** — The recovery guidance assumes that resource Health and Service Health alerts are separated from routine administrative events and have owned severities. This matters because evidence for Design platform and resource-health alerts cannot substitute for the properties required at Define a query-based service-level alert.
- ✗ **D. Record the failure condition 'Query latency or ingestion delay exceeds the intended detection time' as a successful state. Next, base approval on the claim that the command returned an object.** — The WAF consequence identifies that query latency or ingestion delay exceeds the intended detection time. This matters because resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q23 — answer D

An assurance review of 'Define a query-based service-level alert' includes application owners. Evidence must address this risk without retaining credentials: Query latency or ingestion delay exceeds the intended detection time. What should be recorded as sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Curate an operator workbook for Define a query-based service-level alert; as a separate check, use as justification the claim that a related checkpoint proves the current expected state.** — workbook resource ID, display name, query-purpose inventory, and accessibility review. The checkpoint therefore requires that that evidence supports Curate an operator workbook, so it cannot demonstrate The selected log alert evaluates an auditable customer-impact query over a suitable window and frequency.
- ✗ **B. Store unredacted Define a query-based service-level alert output with operator, tenant, token, and request context. Afterward, accept without proof that reproduction requires every captured field.** — The controlling fact is that unredacted implementation output. The checkpoint therefore requires that identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **C. Record only the Define a query-based service-level alert positive inspection's exit status; next, rely on the claim that projected properties and assertion results can be reconstructed later.** — The authored acceptance boundary states that the positive inspection's exit status. The checkpoint therefore requires that an exit code alone does not show whether the selected log alert evaluates an auditable customer-impact query over a suitable window and frequency.
- ✓ **D. Retain sanitized KQL fingerprint, window, frequency, threshold, severity, and failing-period configuration; as a separate check, exclude credentials and unrelated response fields.** — The command-level assertion is anchored in the fact that sanitized KQL fingerprint, window, frequency, threshold, severity, and failing-period configuration. This matters because it captures the checkpoint's observable properties while keeping the evidence boundary narrow.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q24 — answer D

Approval of 'Define a query-based service-level alert' is questioned by security operations. The target is The selected log alert evaluates an auditable customer-impact query over a suitable window and frequency, but the latest evidence does not show it. Which proposal supplies the most likely cause?

- ✗ **A. Treat 'An action group exists but a receiver is disabled, unverified, or unsupported in the region' as grounds to reject Define a query-based service-level alert. Before sign-off, use the premise that verify action routing and noise controls's failure model applies unchanged here.** — The checkpoint specifically records that an action group exists but a receiver is disabled, unverified, or unsupported in the region. The checkpoint therefore requires that that condition belongs to Verify action routing and noise controls and does not by itself invalidate Service-centric alerts with shared action groups and curated workbooks.
- ✗ **B. Ignore the negative assertion 'No rule uses an evaluation cadence that can systematically miss its own observation window'; as an independent condition, consider it sufficient that a later material change will make it unnecessary.** — The scenario makes clear that no rule uses an evaluation cadence that can systematically miss its own observation window. The checkpoint therefore requires that the negative assertion must be evaluated now, independent of a later business change.
- ✗ **C. Investigate Build a layered signal inventory instead of diagnosing Define a query-based service-level alert; as another gate, take it as conclusive that a passing result at Build a layered signal inventory identifies the current cause.** — The architecture evidence must show that the design identifies platform, application, dependency, and business signals with explicit owners. The checkpoint therefore requires that a passing result at Build a layered signal inventory gives no causal evidence for the failure at Define a query-based service-level alert.
- ✓ **D. Investigate query latency or ingestion delay exceeds the intended detection time; before approval, isolate that cause before changing Service-centric alerts with shared action groups and curated workbooks.** — The relevant observation is that query latency or ingestion delay exceeds the intended detection time. The checkpoint therefore requires that it is the checkpoint's causal failure model and should be isolated before retrying Define a query-based service-level alert.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q25 — answer A

The implementation review has reached 'Define a query-based service-level alert'. The run encountered this modeled failure: Query latency or ingestion delay exceeds the intended detection time. Which option best represents the safest recovery action?

- ✓ **A. Test against synthetic fixtures, widen the window only as needed, and document slower detection; as an independent condition, preserve the current run identity and evidence.** — The applicable design condition is that test against synthetic fixtures, widen the window only as needed, and document slower detection. The checkpoint therefore requires that it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **B. Perform cleanup immediately: Delete the scheduled-query rule before deleting its action group or workspace dependency. Next, rely on the belief that the failed operation and its returned identifiers do not need reconciliation.** — The review is governed by this fact: delete the scheduled-query rule before deleting its action group or workspace dependency. The checkpoint therefore requires that cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **C. Create a different run identity before diagnosing 'Query latency or ingestion delay exceeds the intended detection time', and then proceed on the belief that the first state record and returned identifiers can be discarded.** — The retained result must be reconciled with the fact that query latency or ingestion delay exceeds the intended detection time. The checkpoint therefore requires that discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Build a layered signal inventory instead. Also, treat as decisive the assertion that success at Build a layered signal inventory will repair the failed state at Define a query-based service-level alert.** — The decision tension comes from the fact that the design identifies platform, application, dependency, and business signals with explicit owners. The checkpoint therefore requires that altering an already separate checkpoint does not repair the modeled failure at Define a query-based service-level alert.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q26 — answer B

The approach to 'Define a query-based service-level alert' is challenged by site reliability engineering. Without making a new change, the team must inspect the risk 'Query latency or ingestion delay exceeds the intended detection time' using the Azure PowerShell lane. Which course of action provides the read-only, lane-correct inspection?

- ✗ **A. Rerun the Define a query-based service-level alert implementation command and infer the expected state; next, treat it as established that absence of a shell error proves every property.** — The traceable checkpoint outcome is that the implementation command. The checkpoint therefore requires that it can mutate state and shell success does not independently assert the expected properties.
- ✓ **B. Inspect the documented properties for Define a query-based service-level alert; then retain this evidence: sanitized KQL fingerprint, window, frequency, threshold, severity, and failing-period configuration.** — The safe operating boundary says that the selected log alert evaluates an auditable customer-impact query over a suitable window and frequency. The checkpoint therefore requires that the read-only inspection directly tests the properties required at Define a query-based service-level alert.
- ✗ **C. Run only this negative inspection for Define a query-based service-level alert: No rule uses an evaluation cadence that can systematically miss its own observation window. In addition, use as justification the claim that an empty negative result reports every required positive property.** — The failure model establishes that the negative inspection. The checkpoint therefore requires that absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Design platform and resource-health alerts and apply it to Define a query-based service-level alert; before approval, accept without proof that any command from the same lane proves the current checkpoint.** — The recovery guidance assumes that the positive inspection for Design platform and resource-health alerts. The checkpoint therefore requires that it is lane-correct but proves Design platform and resource-health alerts, not Define a query-based service-level alert.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q27 — answer A

A decision test for 'Define a query-based service-level alert' includes application owners. A passing positive check does not by itself prove this negative assertion: No rule uses an evaluation cadence that can systematically miss its own observation window. Which finding constitutes the assertion pair that proves both conditions independently?

- ✓ **A. Verify the positive properties for Define a query-based service-level alert. Also, independently verify that no rule uses an evaluation cadence that can systematically miss its own observation window.** — The WAF consequence identifies that the selected log alert evaluates an auditable customer-impact query over a suitable window and frequency; No rule uses an evaluation cadence that can systematically miss its own observation window. The checkpoint therefore requires that two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **B. Verify only the positive result for Define a query-based service-level alert and report full compliance; without relying on inference, base approval on the claim that every prohibited parallel state must therefore be absent.** — The command-level assertion is anchored in the fact that the selected log alert evaluates an auditable customer-impact query over a suitable window and frequency. The checkpoint therefore requires that the positive result alone does not test the explicit anti-condition 'No rule uses an evaluation cadence that can systematically miss its own observation window'.
- ✗ **C. Prove only that no rule uses an evaluation cadence that can systematically miss its own observation window and report the intended configuration as present. Then, use the premise that absence is equivalent to positive-state evidence.** — no rule uses an evaluation cadence that can systematically miss its own observation window. In the decision record, absence evidence cannot demonstrate the required positive state 'The selected log alert evaluates an auditable customer-impact query over a suitable window and frequency'.
- ✗ **D. Use Curate an operator workbook's negative assertion for Define a query-based service-level alert; afterward, consider it sufficient that negative assertions are interchangeable between checkpoints.** — The controlling fact is that no panel depends on personal data, raw secrets, or an undocumented cross-workspace permission. In the decision record, the second assertion is valid for Curate an operator workbook but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q28 — answer C

The architecture board reconsiders 'Define a query-based service-level alert' with security operations. The board wants the Well-Architected consequence of mitigating this risk: Query latency or ingestion delay exceeds the intended detection time. Which recommendation delivers the consequence attributable to this checkpoint?

- ✗ **A. Use the Verify action routing and noise controls consequence as the result for Define a query-based service-level alert. Also, rely on the claim that a pillar statement remains valid when moved away from Verify action routing and noise controls.** — The relevant observation is that operational Excellence: severity and action routing send actionable work to durable, accountable teams. In the decision record, that tradeoff belongs to Verify action routing and noise controls and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Define a query-based service-level alert outcome; in a separate step, rely on the belief that a low cost classification outweighs the mandatory architecture state.** — The checkpoint specifically records that the required outcome at Define a query-based service-level alert. In the decision record, cost Optimization cannot remove the acceptance condition 'The selected log alert evaluates an auditable customer-impact query over a suitable window and frequency'.
- ✓ **C. Record this consequence: Cost Optimization: query cadence balances detection value against repeated log-query consumption. Afterward, tie it to LAB02-REQ-03.** — The authored acceptance boundary states that cost Optimization: query cadence balances detection value against repeated log-query consumption. In the decision record, it states the authored pillar consequence of the control evaluated at Define a query-based service-level alert.
- ✗ **D. Treat 'Cost Optimization: query cadence balances detection value against repeated log-query consumption' as proof that all five pillars pass. As another control, proceed on the belief that the checkpoint 'Define a query-based service-level alert' no longer needs its separate negative check.** — The scenario makes clear that no rule uses an evaluation cadence that can systematically miss its own observation window. In the decision record, one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q29 — answer A

A review of 'Define a query-based service-level alert' begins with input from service desk. A material change now applies: The payment API adopts a bursty promotion model that triples legitimate traffic for fifteen minutes, so static latency and error-rate thresholds must be revised without masking genuine customer impact. Which response meets the need for the correct revision to the decision record?

- ✓ **A. Re-score Service-centric alerts with shared action groups and curated workbooks and both alternatives for Define a query-based service-level alert. Separately, supersede the ADR using the changed evidence for LAB02-REQ-03.** — The architecture evidence must show that service-centric alerts with shared action groups and curated workbooks at Define a query-based service-level alert. In the decision record, the material change 'The payment API adopts a bursty promotion model that triples legitimate traffic for fifteen minutes, so static latency and error-rate thresholds must be revised without masking genuine customer impact.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **B. Retain Service-centric alerts with shared action groups and curated workbooks at Define a query-based service-level alert without recalculating criteria or eligibility; before approval, take it as conclusive that the original weighted result is permanent.** — The applicable design condition is that service-centric alerts with shared action groups and curated workbooks. In the decision record, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **C. Select Resource-by-resource static thresholds with team-specific receivers for Define a query-based service-level alert without rechecking its mandatory constraints. Separately, treat it as established that being different from the current design is an architecture criterion.** — The review is governed by this fact: resource-by-resource static thresholds with team-specific receivers. In the decision record, being different is not a criterion, and the candidate still must avoid the prohibited state at Define a query-based service-level alert.
- ✗ **D. Keep External monitoring only with Azure telemetry exported downstream eligible at Define a query-based service-level alert by downgrading LAB02-REQ-03; for this decision, use as justification the claim that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The retained result must be reconciled with the fact that lAB02-REQ-03. In the decision record, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q30 — answer A

'Define a query-based service-level alert' awaits approval from site reliability engineering. After a partial run, cleanup must follow this dependency: Delete the scheduled-query rule before deleting its action group or workspace dependency. Which choice should be approved as the dependency-safe cleanup plan?

- ✓ **A. Verify exact run-state IDs and ownership tags for Define a query-based service-level alert; without relying on inference, follow this dependency rule without purge: Delete the scheduled-query rule before deleting its action group or workspace dependency.** — The decision tension comes from the fact that delete the scheduled-query rule before deleting its action group or workspace dependency. In the decision record, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **B. Apply the cleanup rule for Design platform and resource-health alerts before reconciling the current dependency; afterward, treat as decisive the assertion that removing a parent needed to identify Define a query-based service-level alert is harmless.** — The safe operating boundary says that remove test activity-log alerts before action groups when cleanup is authorized. In the decision record, a cleanup rule for Design platform and resource-health alerts cannot override the dependency declared for Define a query-based service-level alert.
- ✗ **C. Delete candidates by display name before comparing the Define a query-based service-level alert ownership tags; then base approval on the claim that the dependency rule 'Delete the scheduled-query rule before deleting its action group or workspace dependency' is optional.** — The traceable checkpoint outcome is that sanitized KQL fingerprint, window, frequency, threshold, severity, and failing-period configuration. In the decision record, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Define a query-based service-level alert negative assertion 'No rule uses an evaluation cadence that can systematically miss its own observation window'. Independently, use the premise that remaining command logs are sufficient recovery evidence.** — The failure model establishes that no rule uses an evaluation cadence that can systematically miss its own observation window. In the decision record, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q31 — answer A

'Curate an operator workbook' is reopened at the request of site reliability engineering. Approval requires a positive result plus this independent negative assertion: No panel depends on personal data, raw secrets, or an undocumented cross-workspace permission. Which answer describes the acceptance rule that makes LAB02-REQ-04 testable?

- ✓ **A. Require the documented positive state for Curate an operator workbook. Next, verify that no panel depends on personal data, raw secrets, or an undocumented cross-workspace permission.** — The recovery guidance assumes that the workbook leads from business health to dependencies and resource diagnostics without exposing sensitive dimensions. In the decision record, the positive state and an independent negative assertion jointly make LAB02-REQ-04 testable.
- ✗ **B. Select Resource-by-resource static thresholds with team-specific receivers before checking Curate an operator workbook. Before sign-off, proceed on the belief that a successful deployment will later prove the architecture constraint.** — The WAF consequence identifies that no panel depends on personal data, raw secrets, or an undocumented cross-workspace permission. In the decision record, a deployment result cannot prove LAB02-REQ-04, and Resource-by-resource static thresholds with team-specific receivers still has to meet the mandatory boundary.
- ✗ **C. Use the passing result from Build a layered signal inventory to approve Curate an operator workbook; as an independent condition, treat as decisive the assertion that one control establishes an unrelated acceptance boundary.** — The command-level assertion is anchored in the fact that the design identifies platform, application, dependency, and business signals with explicit owners. In the decision record, that outcome belongs to Build a layered signal inventory and leaves Curate an operator workbook unverified.
- ✗ **D. Choose External monitoring only with Azure telemetry exported downstream and skip the Curate an operator workbook negative assertion; without relying on inference, base approval on the claim that the candidate has the lowest implementation effort.** — detect and triage material service degradation before customers report it while reducing unactionable alerts. The independent assertion shows why implementation effort cannot justify skipping the negative assertion or displace LAB02-REQ-04.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q32 — answer D

A design review of 'Curate an operator workbook' includes application owners. The selected architecture is Service-centric alerts with shared action groups and curated workbooks; object existence alone is not success. What should be recorded as the intended successful finding?

- ✗ **A. Use only the negative assertion 'No panel depends on personal data, raw secrets, or an undocumented cross-workspace permission' as the success result. Next, use as justification the claim that absence proves every required positive property.** — The authored acceptance boundary states that no panel depends on personal data, raw secrets, or an undocumented cross-workspace permission. The independent assertion shows why this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Design platform and resource-health alerts as the result for Curate an operator workbook, and then accept without proof that a property from the current checkpoint does not need to be inspected.** — The relevant observation is that resource Health and Service Health alerts are separated from routine administrative events and have owned severities. The independent assertion shows why evidence for Design platform and resource-health alerts cannot substitute for the properties required at Curate an operator workbook.
- ✗ **C. Record the failure condition 'A cross-workspace query cannot resolve because the operator lacks access to one workspace' as a successful state. Also, rely on the claim that the command returned an object.** — The checkpoint specifically records that a cross-workspace query cannot resolve because the operator lacks access to one workspace. The independent assertion shows why resource existence or command output does not convert the documented failure condition into success.
- ✓ **D. Record the workbook leads from business health to dependencies and resource diagnostics without exposing sensitive dimensions. As another control, classify it as success for LAB02-REQ-04.** — The controlling fact is that the workbook leads from business health to dependencies and resource diagnostics without exposing sensitive dimensions. The independent assertion shows why this is the authored target state for Curate an operator workbook and directly supports LAB02-REQ-04.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q33 — answer C

The team asks security operations to assess 'Curate an operator workbook'. Evidence must address this risk without retaining credentials: A cross-workspace query cannot resolve because the operator lacks access to one workspace. Which proposal supplies sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Define a query-based service-level alert for Curate an operator workbook; next, use the premise that a related checkpoint proves the current expected state.** — The architecture evidence must show that sanitized KQL fingerprint, window, frequency, threshold, severity, and failing-period configuration. The independent assertion shows why that evidence supports Define a query-based service-level alert, so it cannot demonstrate The workbook leads from business health to dependencies and resource diagnostics without exposing sensitive dimensions.
- ✗ **B. Store unredacted Curate an operator workbook output with operator, tenant, token, and request context. In addition, consider it sufficient that reproduction requires every captured field.** — The applicable design condition is that unredacted implementation output. The independent assertion shows why identity, tenant, or token material exceeds the non-secret evidence contract.
- ✓ **C. Retain workbook resource ID, display name, query-purpose inventory, and accessibility review. In addition, exclude credentials and unrelated response fields.** — The scenario makes clear that workbook resource ID, display name, query-purpose inventory, and accessibility review. The independent assertion shows why it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **D. Record only the Curate an operator workbook positive inspection's exit status; before approval, take it as conclusive that projected properties and assertion results can be reconstructed later.** — The review is governed by this fact: the positive inspection's exit status. The independent assertion shows why an exit code alone does not show whether the workbook leads from business health to dependencies and resource diagnostics without exposing sensitive dimensions.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q34 — answer A

A recommendation on 'Curate an operator workbook' is requested by service desk. The target is The workbook leads from business health to dependencies and resource diagnostics without exposing sensitive dimensions, but the latest evidence does not show it. Which option best represents the most likely cause?

- ✓ **A. Investigate a cross-workspace query cannot resolve because the operator lacks access to one workspace. Before sign-off, isolate that cause before changing Service-centric alerts with shared action groups and curated workbooks.** — The retained result must be reconciled with the fact that a cross-workspace query cannot resolve because the operator lacks access to one workspace. The independent assertion shows why it is the checkpoint's causal failure model and should be isolated before retrying Curate an operator workbook.
- ✗ **B. Treat 'An action group exists but a receiver is disabled, unverified, or unsupported in the region' as grounds to reject Curate an operator workbook; before closing the checkpoint, rely on the belief that verify action routing and noise controls's failure model applies unchanged here.** — The decision tension comes from the fact that an action group exists but a receiver is disabled, unverified, or unsupported in the region. The independent assertion shows why that condition belongs to Verify action routing and noise controls and does not by itself invalidate Service-centric alerts with shared action groups and curated workbooks.
- ✗ **C. Ignore the negative assertion 'No panel depends on personal data, raw secrets, or an undocumented cross-workspace permission'. Then, proceed on the belief that a later material change will make it unnecessary.** — The safe operating boundary says that no panel depends on personal data, raw secrets, or an undocumented cross-workspace permission. The independent assertion shows why the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Build a layered signal inventory instead of diagnosing Curate an operator workbook; afterward, treat as decisive the assertion that a passing result at Build a layered signal inventory identifies the current cause.** — The traceable checkpoint outcome is that the design identifies platform, application, dependency, and business signals with explicit owners. The independent assertion shows why a passing result at Build a layered signal inventory gives no causal evidence for the failure at Curate an operator workbook.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q35 — answer C

'Curate an operator workbook' is assigned to site reliability engineering. The run encountered this modeled failure: A cross-workspace query cannot resolve because the operator lacks access to one workspace. Which course of action provides the safest recovery action?

- ✗ **A. Perform cleanup immediately: Delete the workbook before its supporting workspace only when it was created by this run. Also, treat it as established that the failed operation and its returned identifiers do not need reconciliation.** — The recovery guidance assumes that delete the workbook before its supporting workspace only when it was created by this run. The independent assertion shows why cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **B. Create a different run identity before diagnosing 'A cross-workspace query cannot resolve because the operator lacks access to one workspace'; in a separate step, use as justification the claim that the first state record and returned identifiers can be discarded.** — The WAF consequence identifies that a cross-workspace query cannot resolve because the operator lacks access to one workspace. The independent assertion shows why discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✓ **C. Validate workspace-scoped RBAC and replace inaccessible panels with an explicit coverage notice; afterward, preserve the current run identity and evidence.** — The failure model establishes that validate workspace-scoped RBAC and replace inaccessible panels with an explicit coverage notice. The independent assertion shows why it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **D. Change Build a layered signal inventory instead. As another control, accept without proof that success at Build a layered signal inventory will repair the failed state at Curate an operator workbook.** — The command-level assertion is anchored in the fact that the design identifies platform, application, dependency, and business signals with explicit owners. The independent assertion shows why altering an already separate checkpoint does not repair the modeled failure at Curate an operator workbook.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q36 — answer B

An assurance review of 'Curate an operator workbook' includes application owners. Without making a new change, the team must inspect the risk 'A cross-workspace query cannot resolve because the operator lacks access to one workspace' using the Azure PowerShell lane. Which finding constitutes the read-only, lane-correct inspection?

- ✗ **A. Rerun the Curate an operator workbook implementation command and infer the expected state; before approval, base approval on the claim that absence of a shell error proves every property.** — The controlling fact is that the implementation command. Operationally, it can mutate state and shell success does not independently assert the expected properties.
- ✓ **B. Inspect the documented properties for Curate an operator workbook, and then retain this evidence: workbook resource ID, display name, query-purpose inventory, and accessibility review.** — the workbook leads from business health to dependencies and resource diagnostics without exposing sensitive dimensions. Operationally, the read-only inspection directly tests the properties required at Curate an operator workbook.
- ✗ **C. Run only this negative inspection for Curate an operator workbook: No panel depends on personal data, raw secrets, or an undocumented cross-workspace permission. Separately, use the premise that an empty negative result reports every required positive property.** — The authored acceptance boundary states that the negative inspection. Operationally, absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Design platform and resource-health alerts and apply it to Curate an operator workbook; for this decision, consider it sufficient that any command from the same lane proves the current checkpoint.** — The relevant observation is that the positive inspection for Design platform and resource-health alerts. Operationally, it is lane-correct but proves Design platform and resource-health alerts, not Curate an operator workbook.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q37 — answer A

Approval of 'Curate an operator workbook' is questioned by security operations. A passing positive check does not by itself prove this negative assertion: No panel depends on personal data, raw secrets, or an undocumented cross-workspace permission. Which recommendation delivers the assertion pair that proves both conditions independently?

- ✓ **A. Verify the positive properties for Curate an operator workbook; as a separate check, independently verify that no panel depends on personal data, raw secrets, or an undocumented cross-workspace permission.** — The checkpoint specifically records that the workbook leads from business health to dependencies and resource diagnostics without exposing sensitive dimensions; No panel depends on personal data, raw secrets, or an undocumented cross-workspace permission. Operationally, two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **B. Verify only the positive result for Curate an operator workbook and report full compliance; afterward, rely on the claim that every prohibited parallel state must therefore be absent.** — The scenario makes clear that the workbook leads from business health to dependencies and resource diagnostics without exposing sensitive dimensions. Operationally, the positive result alone does not test the explicit anti-condition 'No panel depends on personal data, raw secrets, or an undocumented cross-workspace permission'.
- ✗ **C. Prove only that no panel depends on personal data, raw secrets, or an undocumented cross-workspace permission and report the intended configuration as present; then rely on the belief that absence is equivalent to positive-state evidence.** — The architecture evidence must show that no panel depends on personal data, raw secrets, or an undocumented cross-workspace permission. Operationally, absence evidence cannot demonstrate the required positive state 'The workbook leads from business health to dependencies and resource diagnostics without exposing sensitive dimensions'.
- ✗ **D. Use Define a query-based service-level alert's negative assertion for Curate an operator workbook. Independently, proceed on the belief that negative assertions are interchangeable between checkpoints.** — The applicable design condition is that no rule uses an evaluation cadence that can systematically miss its own observation window. Operationally, the second assertion is valid for Define a query-based service-level alert but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q38 — answer C

The implementation review has reached 'Curate an operator workbook'. The board wants the Well-Architected consequence of mitigating this risk: A cross-workspace query cannot resolve because the operator lacks access to one workspace. Which response meets the need for the consequence attributable to this checkpoint?

- ✗ **A. Use the Verify action routing and noise controls consequence as the result for Curate an operator workbook. As another control, take it as conclusive that a pillar statement remains valid when moved away from Verify action routing and noise controls.** — The retained result must be reconciled with the fact that operational Excellence: severity and action routing send actionable work to durable, accountable teams. Operationally, that tradeoff belongs to Verify action routing and noise controls and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Curate an operator workbook outcome; as a separate check, treat it as established that a low cost classification outweighs the mandatory architecture state.** — The decision tension comes from the fact that the required outcome at Curate an operator workbook. Operationally, cost Optimization cannot remove the acceptance condition 'The workbook leads from business health to dependencies and resource diagnostics without exposing sensitive dimensions'.
- ✓ **C. Record this consequence: Security: curated views expose only the telemetry dimensions operators need for diagnosis; before approval, tie it to LAB02-REQ-04.** — The review is governed by this fact: security: curated views expose only the telemetry dimensions operators need for diagnosis. Operationally, it states the authored pillar consequence of the control evaluated at Curate an operator workbook.
- ✗ **D. Treat 'Security: curated views expose only the telemetry dimensions operators need for diagnosis' as proof that all five pillars pass. Afterward, use as justification the claim that the checkpoint 'Curate an operator workbook' no longer needs its separate negative check.** — The safe operating boundary says that no panel depends on personal data, raw secrets, or an undocumented cross-workspace permission. Operationally, one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q39 — answer D

The approach to 'Curate an operator workbook' is challenged by site reliability engineering. A material change now applies: The payment API adopts a bursty promotion model that triples legitimate traffic for fifteen minutes, so static latency and error-rate thresholds must be revised without masking genuine customer impact. Which choice should be approved as the correct revision to the decision record?

- ✗ **A. Retain Service-centric alerts with shared action groups and curated workbooks at Curate an operator workbook without recalculating criteria or eligibility; for this decision, treat as decisive the assertion that the original weighted result is permanent.** — The failure model establishes that service-centric alerts with shared action groups and curated workbooks. Operationally, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Resource-by-resource static thresholds with team-specific receivers for Curate an operator workbook without rechecking its mandatory constraints. Before sign-off, base approval on the claim that being different from the current design is an architecture criterion.** — The recovery guidance assumes that resource-by-resource static thresholds with team-specific receivers. Operationally, being different is not a criterion, and the candidate still must avoid the prohibited state at Curate an operator workbook.
- ✗ **C. Keep External monitoring only with Azure telemetry exported downstream eligible at Curate an operator workbook by downgrading LAB02-REQ-04; as an independent condition, use the premise that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The WAF consequence identifies that lAB02-REQ-04. Operationally, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.
- ✓ **D. Re-score Service-centric alerts with shared action groups and curated workbooks and both alternatives for Curate an operator workbook; as an independent condition, supersede the ADR using the changed evidence for LAB02-REQ-04.** — The traceable checkpoint outcome is that service-centric alerts with shared action groups and curated workbooks at Curate an operator workbook. Operationally, the material change 'The payment API adopts a bursty promotion model that triples legitimate traffic for fifteen minutes, so static latency and error-rate thresholds must be revised without masking genuine customer impact.' requires fresh eligibility, weighted analysis, and a superseding decision.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q40 — answer C

A decision test for 'Curate an operator workbook' includes application owners. After a partial run, cleanup must follow this dependency: Delete the workbook before its supporting workspace only when it was created by this run. What should the team use as the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Design platform and resource-health alerts before reconciling the current dependency. Independently, accept without proof that removing a parent needed to identify Curate an operator workbook is harmless.** — remove test activity-log alerts before action groups when cleanup is authorized. The requirement-to-evidence link establishes that a cleanup rule for Design platform and resource-health alerts cannot override the dependency declared for Curate an operator workbook.
- ✗ **B. Delete candidates by display name before comparing the Curate an operator workbook ownership tags. Next, rely on the claim that the dependency rule 'Delete the workbook before its supporting workspace only when it was created by this run' is optional.** — The controlling fact is that workbook resource ID, display name, query-purpose inventory, and accessibility review. The requirement-to-evidence link establishes that names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✓ **C. Verify exact run-state IDs and ownership tags for Curate an operator workbook; then follow this dependency rule without purge: Delete the workbook before its supporting workspace only when it was created by this run.** — The command-level assertion is anchored in the fact that delete the workbook before its supporting workspace only when it was created by this run. Operationally, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **D. Destroy recoverable copies before retaining the Curate an operator workbook negative assertion 'No panel depends on personal data, raw secrets, or an undocumented cross-workspace permission', and then rely on the belief that remaining command logs are sufficient recovery evidence.** — The authored acceptance boundary states that no panel depends on personal data, raw secrets, or an undocumented cross-workspace permission. The requirement-to-evidence link establishes that irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q41 — answer C

The architecture board reconsiders 'Verify action routing and noise controls' with application owners. Approval requires a positive result plus this independent negative assertion: No personal mailbox or receiver without an accountable service owner is present. What should be recorded as the acceptance rule that makes LAB02-REQ-05 testable?

- ✗ **A. Select Resource-by-resource static thresholds with team-specific receivers before checking Verify action routing and noise controls; for the final assessment, use as justification the claim that a successful deployment will later prove the architecture constraint.** — The checkpoint specifically records that no personal mailbox or receiver without an accountable service owner is present. The requirement-to-evidence link establishes that a deployment result cannot prove LAB02-REQ-05, and Resource-by-resource static thresholds with team-specific receivers still has to meet the mandatory boundary.
- ✗ **B. Use the passing result from Build a layered signal inventory to approve Verify action routing and noise controls. Then, accept without proof that one control establishes an unrelated acceptance boundary.** — The scenario makes clear that the design identifies platform, application, dependency, and business signals with explicit owners. The requirement-to-evidence link establishes that that outcome belongs to Build a layered signal inventory and leaves Verify action routing and noise controls unverified.
- ✓ **C. Require the documented positive state for Verify action routing and noise controls; in a separate step, verify that no personal mailbox or receiver without an accountable service owner is present.** — The relevant observation is that every actionable severity maps to a durable team-owned receiver and documented suppression rule. The requirement-to-evidence link establishes that the positive state and an independent negative assertion jointly make LAB02-REQ-05 testable.
- ✗ **D. Choose External monitoring only with Azure telemetry exported downstream and skip the Verify action routing and noise controls negative assertion; afterward, rely on the claim that the candidate has the lowest implementation effort.** — The architecture evidence must show that detect and triage material service degradation before customers report it while reducing unactionable alerts. The requirement-to-evidence link establishes that implementation effort cannot justify skipping the negative assertion or displace LAB02-REQ-05.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q42 — answer D

A review of 'Verify action routing and noise controls' begins with input from security operations. The selected architecture is Service-centric alerts with shared action groups and curated workbooks; object existence alone is not success. Which proposal supplies the intended successful finding?

- ✗ **A. Use only the negative assertion 'No personal mailbox or receiver without an accountable service owner is present' as the success result. Also, use the premise that absence proves every required positive property.** — The review is governed by this fact: no personal mailbox or receiver without an accountable service owner is present. The requirement-to-evidence link establishes that this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Design platform and resource-health alerts as the result for Verify action routing and noise controls; in a separate step, consider it sufficient that a property from the current checkpoint does not need to be inspected.** — The retained result must be reconciled with the fact that resource Health and Service Health alerts are separated from routine administrative events and have owned severities. The requirement-to-evidence link establishes that evidence for Design platform and resource-health alerts cannot substitute for the properties required at Verify action routing and noise controls.
- ✗ **C. Record the failure condition 'An action group exists but a receiver is disabled, unverified, or unsupported in the region' as a successful state. As another control, take it as conclusive that the command returned an object.** — The decision tension comes from the fact that an action group exists but a receiver is disabled, unverified, or unsupported in the region. The requirement-to-evidence link establishes that resource existence or command output does not convert the documented failure condition into success.
- ✓ **D. Record every actionable severity maps to a durable team-owned receiver and documented suppression rule; next, classify it as success for LAB02-REQ-05.** — The applicable design condition is that every actionable severity maps to a durable team-owned receiver and documented suppression rule. The requirement-to-evidence link establishes that this is the authored target state for Verify action routing and noise controls and directly supports LAB02-REQ-05.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q43 — answer A

'Verify action routing and noise controls' awaits approval from service desk. Evidence must address this risk without retaining credentials: An action group exists but a receiver is disabled, unverified, or unsupported in the region. Which option best represents sufficient, properly scoped evidence?

- ✓ **A. Retain receiver type, synthetic endpoint label, severity routing table, suppression window, and owner; for this decision, exclude credentials and unrelated response fields.** — The safe operating boundary says that receiver type, synthetic endpoint label, severity routing table, suppression window, and owner. The requirement-to-evidence link establishes that it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **B. Substitute the evidence from Define a query-based service-level alert for Verify action routing and noise controls; before approval, rely on the belief that a related checkpoint proves the current expected state.** — The traceable checkpoint outcome is that sanitized KQL fingerprint, window, frequency, threshold, severity, and failing-period configuration. The requirement-to-evidence link establishes that that evidence supports Define a query-based service-level alert, so it cannot demonstrate Every actionable severity maps to a durable team-owned receiver and documented suppression rule.
- ✗ **C. Store unredacted Verify action routing and noise controls output with operator, tenant, token, and request context. Separately, proceed on the belief that reproduction requires every captured field.** — The failure model establishes that unredacted implementation output. The requirement-to-evidence link establishes that identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **D. Record only the Verify action routing and noise controls positive inspection's exit status; for this decision, treat as decisive the assertion that projected properties and assertion results can be reconstructed later.** — The recovery guidance assumes that the positive inspection's exit status. The requirement-to-evidence link establishes that an exit code alone does not show whether every actionable severity maps to a durable team-owned receiver and documented suppression rule.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q44 — answer B

'Verify action routing and noise controls' is reopened at the request of site reliability engineering. The target is Every actionable severity maps to a durable team-owned receiver and documented suppression rule, but the latest evidence does not show it. Which course of action provides the most likely cause?

- ✗ **A. Treat 'A cross-workspace query cannot resolve because the operator lacks access to one workspace' as grounds to reject Verify action routing and noise controls; afterward, treat it as established that curate an operator workbook's failure model applies unchanged here.** — The command-level assertion is anchored in the fact that a cross-workspace query cannot resolve because the operator lacks access to one workspace. The requirement-to-evidence link establishes that that condition belongs to Curate an operator workbook and does not by itself invalidate Service-centric alerts with shared action groups and curated workbooks.
- ✓ **B. Investigate an action group exists but a receiver is disabled, unverified, or unsupported in the region. Then, isolate that cause before changing Service-centric alerts with shared action groups and curated workbooks.** — The WAF consequence identifies that an action group exists but a receiver is disabled, unverified, or unsupported in the region. The requirement-to-evidence link establishes that it is the checkpoint's causal failure model and should be isolated before retrying Verify action routing and noise controls.
- ✗ **C. Ignore the negative assertion 'No personal mailbox or receiver without an accountable service owner is present'; then use as justification the claim that a later material change will make it unnecessary.** — no personal mailbox or receiver without an accountable service owner is present. Consequently, the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Build a layered signal inventory instead of diagnosing Verify action routing and noise controls. Independently, accept without proof that a passing result at Build a layered signal inventory identifies the current cause.** — The controlling fact is that the design identifies platform, application, dependency, and business signals with explicit owners. Consequently, a passing result at Build a layered signal inventory gives no causal evidence for the failure at Verify action routing and noise controls.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q45 — answer D

A design review of 'Verify action routing and noise controls' includes application owners. The run encountered this modeled failure: An action group exists but a receiver is disabled, unverified, or unsupported in the region. Which finding constitutes the safest recovery action?

- ✗ **A. Perform cleanup immediately: Delete alert rules before deleting the shared action group. As another control, base approval on the claim that the failed operation and its returned identifiers do not need reconciliation.** — The relevant observation is that delete alert rules before deleting the shared action group. Consequently, cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **B. Create a different run identity before diagnosing 'An action group exists but a receiver is disabled, unverified, or unsupported in the region'; as a separate check, use the premise that the first state record and returned identifiers can be discarded.** — The checkpoint specifically records that an action group exists but a receiver is disabled, unverified, or unsupported in the region. Consequently, discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **C. Change Build a layered signal inventory instead. Afterward, consider it sufficient that success at Build a layered signal inventory will repair the failed state at Verify action routing and noise controls.** — The scenario makes clear that the design identifies platform, application, dependency, and business signals with explicit owners. Consequently, altering an already separate checkpoint does not repair the modeled failure at Verify action routing and noise controls.
- ✓ **D. Correct the synthetic routing design and retest the alert-to-owner mapping without sending notifications. Next, preserve the current run identity and evidence.** — The authored acceptance boundary states that correct the synthetic routing design and retest the alert-to-owner mapping without sending notifications. Consequently, it corrects the narrow cause while retaining the same recovery trail and decision scope.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q46 — answer C

The team asks security operations to assess 'Verify action routing and noise controls'. Without making a new change, the team must inspect the risk 'An action group exists but a receiver is disabled, unverified, or unsupported in the region' using the Azure PowerShell lane. Which recommendation delivers the read-only, lane-correct inspection?

- ✗ **A. Rerun the Verify action routing and noise controls implementation command and infer the expected state; for this decision, rely on the claim that absence of a shell error proves every property.** — The applicable design condition is that the implementation command. Consequently, it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Verify action routing and noise controls: No personal mailbox or receiver without an accountable service owner is present. Before sign-off, rely on the belief that an empty negative result reports every required positive property.** — The review is governed by this fact: the negative inspection. Consequently, absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✓ **C. Inspect the documented properties for Verify action routing and noise controls. As another control, retain this evidence: receiver type, synthetic endpoint label, severity routing table, suppression window, and owner.** — The architecture evidence must show that every actionable severity maps to a durable team-owned receiver and documented suppression rule. Consequently, the read-only inspection directly tests the properties required at Verify action routing and noise controls.
- ✗ **D. Run the positive inspection for Design platform and resource-health alerts and apply it to Verify action routing and noise controls; as an independent condition, proceed on the belief that any command from the same lane proves the current checkpoint.** — The retained result must be reconciled with the fact that the positive inspection for Design platform and resource-health alerts. Consequently, it is lane-correct but proves Design platform and resource-health alerts, not Verify action routing and noise controls.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q47 — answer B

A recommendation on 'Verify action routing and noise controls' is requested by service desk. A passing positive check does not by itself prove this negative assertion: No personal mailbox or receiver without an accountable service owner is present. Which response meets the need for the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Verify action routing and noise controls and report full compliance. Independently, take it as conclusive that every prohibited parallel state must therefore be absent.** — The safe operating boundary says that every actionable severity maps to a durable team-owned receiver and documented suppression rule. Consequently, the positive result alone does not test the explicit anti-condition 'No personal mailbox or receiver without an accountable service owner is present'.
- ✓ **B. Verify the positive properties for Verify action routing and noise controls. In addition, independently verify that no personal mailbox or receiver without an accountable service owner is present.** — The decision tension comes from the fact that every actionable severity maps to a durable team-owned receiver and documented suppression rule; No personal mailbox or receiver without an accountable service owner is present. Consequently, two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **C. Prove only that no personal mailbox or receiver without an accountable service owner is present and report the intended configuration as present. Next, treat it as established that absence is equivalent to positive-state evidence.** — The traceable checkpoint outcome is that no personal mailbox or receiver without an accountable service owner is present. Consequently, absence evidence cannot demonstrate the required positive state 'Every actionable severity maps to a durable team-owned receiver and documented suppression rule'.
- ✗ **D. Use Define a query-based service-level alert's negative assertion for Verify action routing and noise controls, and then use as justification the claim that negative assertions are interchangeable between checkpoints.** — The failure model establishes that no rule uses an evaluation cadence that can systematically miss its own observation window. Consequently, the second assertion is valid for Define a query-based service-level alert but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q48 — answer C

'Verify action routing and noise controls' is assigned to site reliability engineering. The board wants the Well-Architected consequence of mitigating this risk: An action group exists but a receiver is disabled, unverified, or unsupported in the region. Which choice should be approved as the consequence attributable to this checkpoint?

- ✗ **A. Use the Curate an operator workbook consequence as the result for Verify action routing and noise controls. Afterward, treat as decisive the assertion that a pillar statement remains valid when moved away from Curate an operator workbook.** — The WAF consequence identifies that security: curated views expose only the telemetry dimensions operators need for diagnosis. Consequently, that tradeoff belongs to Curate an operator workbook and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Verify action routing and noise controls outcome; next, base approval on the claim that a low cost classification outweighs the mandatory architecture state.** — The command-level assertion is anchored in the fact that the required outcome at Verify action routing and noise controls. Consequently, cost Optimization cannot remove the acceptance condition 'Every actionable severity maps to a durable team-owned receiver and documented suppression rule'.
- ✓ **C. Record this consequence: Operational Excellence: severity and action routing send actionable work to durable, accountable teams. Before sign-off, tie it to LAB02-REQ-05.** — The recovery guidance assumes that operational Excellence: severity and action routing send actionable work to durable, accountable teams. Consequently, it states the authored pillar consequence of the control evaluated at Verify action routing and noise controls.
- ✗ **D. Treat 'Operational Excellence: severity and action routing send actionable work to durable, accountable teams' as proof that all five pillars pass. In addition, use the premise that the checkpoint 'Verify action routing and noise controls' no longer needs its separate negative check.** — no personal mailbox or receiver without an accountable service owner is present. For this case, one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q49 — answer A

An assurance review of 'Verify action routing and noise controls' includes application owners. A material change now applies: The payment API adopts a bursty promotion model that triples legitimate traffic for fifteen minutes, so static latency and error-rate thresholds must be revised without masking genuine customer impact. What should the team use as the correct revision to the decision record?

- ✓ **A. Re-score Service-centric alerts with shared action groups and curated workbooks and both alternatives for Verify action routing and noise controls; afterward, supersede the ADR using the changed evidence for LAB02-REQ-05.** — The controlling fact is that service-centric alerts with shared action groups and curated workbooks at Verify action routing and noise controls. For this case, the material change 'The payment API adopts a bursty promotion model that triples legitimate traffic for fifteen minutes, so static latency and error-rate thresholds must be revised without masking genuine customer impact.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **B. Retain Service-centric alerts with shared action groups and curated workbooks at Verify action routing and noise controls without recalculating criteria or eligibility; as an independent condition, accept without proof that the original weighted result is permanent.** — The authored acceptance boundary states that service-centric alerts with shared action groups and curated workbooks. For this case, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **C. Select Resource-by-resource static thresholds with team-specific receivers for Verify action routing and noise controls without rechecking its mandatory constraints; before approval, rely on the claim that being different from the current design is an architecture criterion.** — The relevant observation is that resource-by-resource static thresholds with team-specific receivers. For this case, being different is not a criterion, and the candidate still must avoid the prohibited state at Verify action routing and noise controls.
- ✗ **D. Keep External monitoring only with Azure telemetry exported downstream eligible at Verify action routing and noise controls by downgrading LAB02-REQ-05. Then, rely on the belief that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The checkpoint specifically records that lAB02-REQ-05. For this case, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)

## LAB02-Q50 — answer A

Approval of 'Verify action routing and noise controls' is questioned by security operations. After a partial run, cleanup must follow this dependency: Delete alert rules before deleting the shared action group. Which option best establishes the dependency-safe cleanup plan?

- ✓ **A. Verify exact run-state IDs and ownership tags for Verify action routing and noise controls, and then follow this dependency rule without purge: Delete alert rules before deleting the shared action group.** — The scenario makes clear that delete alert rules before deleting the shared action group. For this case, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **B. Apply the cleanup rule for Design platform and resource-health alerts before reconciling the current dependency, and then consider it sufficient that removing a parent needed to identify Verify action routing and noise controls is harmless.** — The architecture evidence must show that remove test activity-log alerts before action groups when cleanup is authorized. For this case, a cleanup rule for Design platform and resource-health alerts cannot override the dependency declared for Verify action routing and noise controls.
- ✗ **C. Delete candidates by display name before comparing the Verify action routing and noise controls ownership tags. Also, take it as conclusive that the dependency rule 'Delete alert rules before deleting the shared action group' is optional.** — The applicable design condition is that receiver type, synthetic endpoint label, severity routing table, suppression window, and owner. For this case, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Verify action routing and noise controls negative assertion 'No personal mailbox or receiver without an accountable service owner is present'; in a separate step, treat it as established that remaining command logs are sufficient recovery evidence.** — The review is governed by this fact: no personal mailbox or receiver without an accountable service owner is present. For this case, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/azure-monitor/best-practices-alerts (verified 2026-09-02)
<!-- END GENERATED AZ305 V1 -->
