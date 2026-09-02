<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-10 answer key

Use after completing the learner assessment. Every choice has a specific explanation.

## LAB10-Q01 — answer B

Approval of 'Choose API and consistency deliberately' is questioned by product data owners. Approval requires a positive result plus this independent negative assertion: Strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off. What best demonstrates the acceptance rule that makes LAB10-REQ-01 testable?

- ✗ **A. Select Azure Table Storage with denormalized entities and account-level scale before checking Choose API and consistency deliberately. Separately, treat it as established that a successful deployment will later prove the architecture constraint.** — The command-level assertion is anchored in the fact that strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off. The checkpoint therefore requires that a deployment result cannot prove LAB10-REQ-01, and Azure Table Storage with denormalized entities and account-level scale still has to meet the mandatory boundary.
- ✓ **B. Require the documented positive state for Choose API and consistency deliberately; afterward, verify that strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off.** — The WAF consequence identifies that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. The checkpoint therefore requires that the positive state and an independent negative assertion jointly make LAB10-REQ-01 testable.
- ✗ **C. Use the passing result from Design a high-cardinality partition key to approve Choose API and consistency deliberately; for this decision, use as justification the claim that one control establishes an unrelated acceptance boundary.** — the tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants. In the decision record, that outcome belongs to Design a high-cardinality partition key and leaves Choose API and consistency deliberately unverified.
- ✗ **D. Choose Azure SQL Database with JSON columns and relational indexes and skip the Choose API and consistency deliberately negative assertion. Before sign-off, accept without proof that the candidate has the lowest implementation effort.** — The controlling fact is that serve a variable global catalog workload with predictable latency and controlled throughput cost. In the decision record, implementation effort cannot justify skipping the negative assertion or displace LAB10-REQ-01.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q02 — answer C

The implementation review has reached 'Choose API and consistency deliberately'. The selected architecture is Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning; object existence alone is not success. Which option is the intended successful finding?

- ✗ **A. Use only the negative assertion 'Strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off' as the success result; then base approval on the claim that absence proves every required positive property.** — The relevant observation is that strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off. In the decision record, this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Minimize indexing write amplification as the result for Choose API and consistency deliberately. Independently, use the premise that a property from the current checkpoint does not need to be inspected.** — The checkpoint specifically records that indexed paths serve known filters and ordering while large descriptive payloads are explicitly excluded. In the decision record, evidence for Minimize indexing write amplification cannot substitute for the properties required at Choose API and consistency deliberately.
- ✓ **C. Record the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior, and then classify it as success for LAB10-REQ-01.** — The authored acceptance boundary states that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. In the decision record, this is the authored target state for Choose API and consistency deliberately and directly supports LAB10-REQ-01.
- ✗ **D. Record the failure condition 'A required read guarantee cannot be expressed with Session consistency and session-token propagation' as a successful state. Next, consider it sufficient that the command returned an object.** — The scenario makes clear that a required read guarantee cannot be expressed with Session consistency and session-token propagation. In the decision record, resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q03 — answer B

The approach to 'Choose API and consistency deliberately' is challenged by finOps. Evidence must address this risk without retaining credentials: A required read guarantee cannot be expressed with Session consistency and session-token propagation. What should the architect select as sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Bound autoscale throughput for Choose API and consistency deliberately; as a separate check, rely on the claim that a related checkpoint proves the current expected state.** — The applicable design condition is that throughput mode, maximum RU/s, minimum billing implication, scale trigger, and cost owner. In the decision record, that evidence supports Bound autoscale throughput, so it cannot demonstrate The NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior.
- ✓ **B. Retain account label, API kind, consistency, region count, application session boundary, and rationale; as a separate check, exclude credentials and unrelated response fields.** — The architecture evidence must show that account label, API kind, consistency, region count, application session boundary, and rationale. In the decision record, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **C. Store unredacted Choose API and consistency deliberately output with operator, tenant, token, and request context. Afterward, rely on the belief that reproduction requires every captured field.** — The review is governed by this fact: unredacted implementation output. In the decision record, identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **D. Record only the Choose API and consistency deliberately positive inspection's exit status; next, proceed on the belief that projected properties and assertion results can be reconstructed later.** — The retained result must be reconciled with the fact that the positive inspection's exit status. In the decision record, an exit code alone does not show whether the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q04 — answer A

A decision test for 'Choose API and consistency deliberately' includes digital commerce engineering. The target is The NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior, but the latest evidence does not show it. Select the most likely cause.

- ✓ **A. Investigate a required read guarantee cannot be expressed with Session consistency and session-token propagation; before approval, isolate that cause before changing Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning.** — The decision tension comes from the fact that a required read guarantee cannot be expressed with Session consistency and session-token propagation. In the decision record, it is the checkpoint's causal failure model and should be isolated before retrying Choose API and consistency deliberately.
- ✗ **B. Treat 'The wrong subresource group or DNS zone produces a public endpoint resolution' as grounds to reject Choose API and consistency deliberately. Before sign-off, take it as conclusive that restrict the account network boundary's failure model applies unchanged here.** — The safe operating boundary says that the wrong subresource group or DNS zone produces a public endpoint resolution. In the decision record, that condition belongs to Restrict the account network boundary and does not by itself invalidate Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning.
- ✗ **C. Ignore the negative assertion 'Strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off'; as an independent condition, treat it as established that a later material change will make it unnecessary.** — The traceable checkpoint outcome is that strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off. In the decision record, the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Design a high-cardinality partition key instead of diagnosing Choose API and consistency deliberately; as another gate, use as justification the claim that a passing result at Design a high-cardinality partition key identifies the current cause.** — The failure model establishes that the tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants. In the decision record, a passing result at Design a high-cardinality partition key gives no causal evidence for the failure at Choose API and consistency deliberately.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q05 — answer C

The architecture board reconsiders 'Choose API and consistency deliberately' with product data owners. The run encountered this modeled failure: A required read guarantee cannot be expressed with Session consistency and session-token propagation. Which response provides the safest recovery action?

- ✗ **A. Perform cleanup immediately: Delete containers and databases before the run-owned account; never treat account deletion as data recovery. Next, treat as decisive the assertion that the failed operation and its returned identifiers do not need reconciliation.** — The WAF consequence identifies that delete containers and databases before the run-owned account; never treat account deletion as data recovery. In the decision record, cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **B. Create a different run identity before diagnosing 'A required read guarantee cannot be expressed with Session consistency and session-token propagation', and then base approval on the claim that the first state record and returned identifiers can be discarded.** — The command-level assertion is anchored in the fact that a required read guarantee cannot be expressed with Session consistency and session-token propagation. In the decision record, discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✓ **C. Model the exact anomaly, then compare Bounded Staleness or Strong consistency against latency and availability; as an independent condition, preserve the current run identity and evidence.** — The recovery guidance assumes that model the exact anomaly, then compare Bounded Staleness or Strong consistency against latency and availability. In the decision record, it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **D. Change Design a high-cardinality partition key instead. Also, use the premise that success at Design a high-cardinality partition key will repair the failed state at Choose API and consistency deliberately.** — the tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants. The independent assertion shows why altering an already separate checkpoint does not repair the modeled failure at Choose API and consistency deliberately.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q06 — answer C

A review of 'Choose API and consistency deliberately' begins with input from security architecture. Without making a new change, the team must inspect the risk 'A required read guarantee cannot be expressed with Session consistency and session-token propagation' using the Azure CLI lane. Which choice gives the team the read-only, lane-correct inspection?

- ✗ **A. Rerun the Choose API and consistency deliberately implementation command and infer the expected state; next, accept without proof that absence of a shell error proves every property.** — The authored acceptance boundary states that the implementation command. The independent assertion shows why it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Choose API and consistency deliberately: Strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off. In addition, rely on the claim that an empty negative result reports every required positive property.** — The relevant observation is that the negative inspection. The independent assertion shows why absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✓ **C. Inspect the documented properties for Choose API and consistency deliberately; then retain this evidence: account label, API kind, consistency, region count, application session boundary, and rationale.** — The controlling fact is that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. The independent assertion shows why the read-only inspection directly tests the properties required at Choose API and consistency deliberately.
- ✗ **D. Run the positive inspection for Minimize indexing write amplification and apply it to Choose API and consistency deliberately; before approval, rely on the belief that any command from the same lane proves the current checkpoint.** — The checkpoint specifically records that the positive inspection for Minimize indexing write amplification. The independent assertion shows why it is lane-correct but proves Minimize indexing write amplification, not Choose API and consistency deliberately.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q07 — answer D

'Choose API and consistency deliberately' awaits approval from finOps. A passing positive check does not by itself prove this negative assertion: Strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off. What is the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Choose API and consistency deliberately and report full compliance; without relying on inference, consider it sufficient that every prohibited parallel state must therefore be absent.** — The architecture evidence must show that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. The independent assertion shows why the positive result alone does not test the explicit anti-condition 'Strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off'.
- ✗ **B. Prove only that strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off and report the intended configuration as present. Then, take it as conclusive that absence is equivalent to positive-state evidence.** — The applicable design condition is that strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off. The independent assertion shows why absence evidence cannot demonstrate the required positive state 'The NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior'.
- ✗ **C. Use Bound autoscale throughput's negative assertion for Choose API and consistency deliberately; afterward, treat it as established that negative assertions are interchangeable between checkpoints.** — The review is governed by this fact: the configured maximum does not exceed the approved cost envelope. The independent assertion shows why the second assertion is valid for Bound autoscale throughput but leaves this checkpoint's prohibited state untested.
- ✓ **D. Verify the positive properties for Choose API and consistency deliberately. Also, independently verify that strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off.** — The scenario makes clear that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior; Strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off. The independent assertion shows why two independent observations prevent a passing positive check from concealing an unsafe parallel state.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q08 — answer A

'Choose API and consistency deliberately' is reopened at the request of digital commerce engineering. The board wants the Well-Architected consequence of mitigating this risk: A required read guarantee cannot be expressed with Session consistency and session-token propagation. Which recommendation supplies the consequence attributable to this checkpoint?

- ✓ **A. Record this consequence: Reliability: a documented consistency contract makes read behavior predictable across sessions and regions. Afterward, tie it to LAB10-REQ-01.** — The retained result must be reconciled with the fact that reliability: a documented consistency contract makes read behavior predictable across sessions and regions. The independent assertion shows why it states the authored pillar consequence of the control evaluated at Choose API and consistency deliberately.
- ✗ **B. Use the Restrict the account network boundary consequence as the result for Choose API and consistency deliberately. Also, proceed on the belief that a pillar statement remains valid when moved away from Restrict the account network boundary.** — The decision tension comes from the fact that security: private connectivity prevents unrestricted public access to the semi-structured data account. The independent assertion shows why that tradeoff belongs to Restrict the account network boundary and does not explain this checkpoint's decision.
- ✗ **C. Remove the control responsible for the Choose API and consistency deliberately outcome; in a separate step, treat as decisive the assertion that a moderate cost classification outweighs the mandatory architecture state.** — The safe operating boundary says that the required outcome at Choose API and consistency deliberately. The independent assertion shows why cost Optimization cannot remove the acceptance condition 'The NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior'.
- ✗ **D. Treat 'Reliability: a documented consistency contract makes read behavior predictable across sessions and regions' as proof that all five pillars pass. As another control, base approval on the claim that the checkpoint 'Choose API and consistency deliberately' no longer needs its separate negative check.** — The traceable checkpoint outcome is that strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off. The independent assertion shows why one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q09 — answer C

A design review of 'Choose API and consistency deliberately' includes product data owners. A material change now applies: One enterprise tenant grows to forty percent of all traffic and requires per-tenant cost attribution and data isolation; revise partition and container strategy without breaking other tenants. Choose the correct revision to the decision record.

- ✗ **A. Retain Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning at Choose API and consistency deliberately without recalculating criteria or eligibility; before approval, use as justification the claim that the original weighted result is permanent.** — The recovery guidance assumes that azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning. The independent assertion shows why the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Azure Table Storage with denormalized entities and account-level scale for Choose API and consistency deliberately without rechecking its mandatory constraints. Separately, accept without proof that being different from the current design is an architecture criterion.** — The WAF consequence identifies that azure Table Storage with denormalized entities and account-level scale. The independent assertion shows why being different is not a criterion, and the candidate still must avoid the prohibited state at Choose API and consistency deliberately.
- ✓ **C. Re-score Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning and both alternatives for Choose API and consistency deliberately. Separately, supersede the ADR using the changed evidence for LAB10-REQ-01.** — The failure model establishes that azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning at Choose API and consistency deliberately. The independent assertion shows why the material change 'One enterprise tenant grows to forty percent of all traffic and requires per-tenant cost attribution and data isolation; revise partition and container strategy without breaking other tenants.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **D. Keep Azure SQL Database with JSON columns and relational indexes eligible at Choose API and consistency deliberately by downgrading LAB10-REQ-01; for this decision, rely on the claim that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The command-level assertion is anchored in the fact that lAB10-REQ-01. The independent assertion shows why an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q10 — answer B

The team asks security architecture to assess 'Choose API and consistency deliberately'. After a partial run, cleanup must follow this dependency: Delete containers and databases before the run-owned account; never treat account deletion as data recovery. Which answer describes the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Minimize indexing write amplification before reconciling the current dependency; afterward, use the premise that removing a parent needed to identify Choose API and consistency deliberately is harmless.** — The controlling fact is that restore the original indexing policy before deleting a retained container. Operationally, a cleanup rule for Minimize indexing write amplification cannot override the dependency declared for Choose API and consistency deliberately.
- ✓ **B. Verify exact run-state IDs and ownership tags for Choose API and consistency deliberately; for the final assessment, follow this dependency rule without purge: Delete containers and databases before the run-owned account; never treat account deletion as data recovery.** — delete containers and databases before the run-owned account; never treat account deletion as data recovery. Operationally, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **C. Delete candidates by display name before comparing the Choose API and consistency deliberately ownership tags; then consider it sufficient that the dependency rule 'Delete containers and databases before the run-owned account; never treat account deletion as data recovery' is optional.** — The authored acceptance boundary states that account label, API kind, consistency, region count, application session boundary, and rationale. Operationally, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Choose API and consistency deliberately negative assertion 'Strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off'. Independently, take it as conclusive that remaining command logs are sufficient recovery evidence.** — The relevant observation is that strong consistency is not selected reflexively for a multi-region catalog without its latency and availability trade-off. Operationally, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q11 — answer A

A recommendation on 'Design a high-cardinality partition key' is requested by security architecture. Approval requires a positive result plus this independent negative assertion: A low-cardinality mutable property such as status is not used as the partition key. Which option is the acceptance rule that makes LAB10-REQ-02 testable?

- ✓ **A. Require the documented positive state for Design a high-cardinality partition key. Next, verify that a low-cardinality mutable property such as status is not used as the partition key.** — The checkpoint specifically records that the tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants. Operationally, the positive state and an independent negative assertion jointly make LAB10-REQ-02 testable.
- ✗ **B. Select Azure Table Storage with denormalized entities and account-level scale before checking Design a high-cardinality partition key. Before sign-off, base approval on the claim that a successful deployment will later prove the architecture constraint.** — The scenario makes clear that a low-cardinality mutable property such as status is not used as the partition key. Operationally, a deployment result cannot prove LAB10-REQ-02, and Azure Table Storage with denormalized entities and account-level scale still has to meet the mandatory boundary.
- ✗ **C. Use the passing result from Choose API and consistency deliberately to approve Design a high-cardinality partition key; as an independent condition, use the premise that one control establishes an unrelated acceptance boundary.** — The architecture evidence must show that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. Operationally, that outcome belongs to Choose API and consistency deliberately and leaves Design a high-cardinality partition key unverified.
- ✗ **D. Choose Azure SQL Database with JSON columns and relational indexes and skip the Design a high-cardinality partition key negative assertion; without relying on inference, consider it sufficient that the candidate has the lowest implementation effort.** — The applicable design condition is that serve a variable global catalog workload with predictable latency and controlled throughput cost. Operationally, implementation effort cannot justify skipping the negative assertion or displace LAB10-REQ-02.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q12 — answer B

'Design a high-cardinality partition key' is assigned to finOps. The selected architecture is Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning; object existence alone is not success. What should the architect select as the intended successful finding?

- ✗ **A. Use only the negative assertion 'A low-cardinality mutable property such as status is not used as the partition key' as the success result. Next, rely on the claim that absence proves every required positive property.** — The retained result must be reconciled with the fact that a low-cardinality mutable property such as status is not used as the partition key. Operationally, this is the independent prohibited-state assertion, not a successful finding.
- ✓ **B. Record the tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants. As another control, classify it as success for LAB10-REQ-02.** — The review is governed by this fact: the tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants. Operationally, this is the authored target state for Design a high-cardinality partition key and directly supports LAB10-REQ-02.
- ✗ **C. Use the successful finding from Minimize indexing write amplification as the result for Design a high-cardinality partition key, and then rely on the belief that a property from the current checkpoint does not need to be inspected.** — The decision tension comes from the fact that indexed paths serve known filters and ordering while large descriptive payloads are explicitly excluded. Operationally, evidence for Minimize indexing write amplification cannot substitute for the properties required at Design a high-cardinality partition key.
- ✗ **D. Record the failure condition 'One tenant can exceed logical-partition storage or throughput limits' as a successful state. Also, proceed on the belief that the command returned an object.** — The safe operating boundary says that one tenant can exceed logical-partition storage or throughput limits. Operationally, resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q13 — answer D

An assurance review of 'Design a high-cardinality partition key' includes digital commerce engineering. Evidence must address this risk without retaining credentials: One tenant can exceed logical-partition storage or throughput limits. Select sufficient, properly scoped evidence.

- ✗ **A. Substitute the evidence from Bound autoscale throughput for Design a high-cardinality partition key; next, take it as conclusive that a related checkpoint proves the current expected state.** — The failure model establishes that throughput mode, maximum RU/s, minimum billing implication, scale trigger, and cost owner. Operationally, that evidence supports Bound autoscale throughput, so it cannot demonstrate The tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants.
- ✗ **B. Store unredacted Design a high-cardinality partition key output with operator, tenant, token, and request context. In addition, treat it as established that reproduction requires every captured field.** — The recovery guidance assumes that unredacted implementation output. Operationally, identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **C. Record only the Design a high-cardinality partition key positive inspection's exit status; before approval, use as justification the claim that projected properties and assertion results can be reconstructed later.** — The WAF consequence identifies that the positive inspection's exit status. Operationally, an exit code alone does not show whether the tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants.
- ✓ **D. Retain partition-key path, cardinality estimate, largest logical partition estimate, query patterns, and hotspot mitigation. In addition, exclude credentials and unrelated response fields.** — The traceable checkpoint outcome is that partition-key path, cardinality estimate, largest logical partition estimate, query patterns, and hotspot mitigation. Operationally, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q14 — answer A

Approval of 'Design a high-cardinality partition key' is questioned by product data owners. The target is The tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants, but the latest evidence does not show it. Which response provides the most likely cause?

- ✓ **A. Investigate one tenant can exceed logical-partition storage or throughput limits. Before sign-off, isolate that cause before changing Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning.** — The command-level assertion is anchored in the fact that one tenant can exceed logical-partition storage or throughput limits. Operationally, it is the checkpoint's causal failure model and should be isolated before retrying Design a high-cardinality partition key.
- ✗ **B. Treat 'The wrong subresource group or DNS zone produces a public endpoint resolution' as grounds to reject Design a high-cardinality partition key; before closing the checkpoint, treat as decisive the assertion that restrict the account network boundary's failure model applies unchanged here.** — the wrong subresource group or DNS zone produces a public endpoint resolution. The requirement-to-evidence link establishes that that condition belongs to Restrict the account network boundary and does not by itself invalidate Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning.
- ✗ **C. Ignore the negative assertion 'A low-cardinality mutable property such as status is not used as the partition key'. Then, base approval on the claim that a later material change will make it unnecessary.** — The controlling fact is that a low-cardinality mutable property such as status is not used as the partition key. The requirement-to-evidence link establishes that the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Choose API and consistency deliberately instead of diagnosing Design a high-cardinality partition key; afterward, use the premise that a passing result at Choose API and consistency deliberately identifies the current cause.** — The authored acceptance boundary states that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. The requirement-to-evidence link establishes that a passing result at Choose API and consistency deliberately gives no causal evidence for the failure at Design a high-cardinality partition key.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q15 — answer B

The implementation review has reached 'Design a high-cardinality partition key'. The run encountered this modeled failure: One tenant can exceed logical-partition storage or throughput limits. Which choice gives the team the safest recovery action?

- ✗ **A. Perform cleanup immediately: Delete the run-owned container before its database and account. Also, accept without proof that the failed operation and its returned identifiers do not need reconciliation.** — The checkpoint specifically records that delete the run-owned container before its database and account. The requirement-to-evidence link establishes that cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✓ **B. Evaluate a hierarchical tenant-and-category key or synthetic suffix using measured access patterns; afterward, preserve the current run identity and evidence.** — The relevant observation is that evaluate a hierarchical tenant-and-category key or synthetic suffix using measured access patterns. The requirement-to-evidence link establishes that it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **C. Create a different run identity before diagnosing 'One tenant can exceed logical-partition storage or throughput limits'; in a separate step, rely on the claim that the first state record and returned identifiers can be discarded.** — The scenario makes clear that one tenant can exceed logical-partition storage or throughput limits. The requirement-to-evidence link establishes that discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Choose API and consistency deliberately instead. As another control, rely on the belief that success at Choose API and consistency deliberately will repair the failed state at Design a high-cardinality partition key.** — The architecture evidence must show that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. The requirement-to-evidence link establishes that altering an already separate checkpoint does not repair the modeled failure at Design a high-cardinality partition key.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q16 — answer A

The approach to 'Design a high-cardinality partition key' is challenged by finOps. Without making a new change, the team must inspect the risk 'One tenant can exceed logical-partition storage or throughput limits' using the Azure CLI lane. What is the read-only, lane-correct inspection?

- ✓ **A. Inspect the documented properties for Design a high-cardinality partition key, and then retain this evidence: partition-key path, cardinality estimate, largest logical partition estimate, query patterns, and hotspot mitigation.** — The applicable design condition is that the tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants. The requirement-to-evidence link establishes that the read-only inspection directly tests the properties required at Design a high-cardinality partition key.
- ✗ **B. Rerun the Design a high-cardinality partition key implementation command and infer the expected state; before approval, consider it sufficient that absence of a shell error proves every property.** — The review is governed by this fact: the implementation command. The requirement-to-evidence link establishes that it can mutate state and shell success does not independently assert the expected properties.
- ✗ **C. Run only this negative inspection for Design a high-cardinality partition key: A low-cardinality mutable property such as status is not used as the partition key. Separately, take it as conclusive that an empty negative result reports every required positive property.** — The retained result must be reconciled with the fact that the negative inspection. The requirement-to-evidence link establishes that absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Minimize indexing write amplification and apply it to Design a high-cardinality partition key; for this decision, treat it as established that any command from the same lane proves the current checkpoint.** — The decision tension comes from the fact that the positive inspection for Minimize indexing write amplification. The requirement-to-evidence link establishes that it is lane-correct but proves Minimize indexing write amplification, not Design a high-cardinality partition key.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q17 — answer D

A decision test for 'Design a high-cardinality partition key' includes digital commerce engineering. A passing positive check does not by itself prove this negative assertion: A low-cardinality mutable property such as status is not used as the partition key. Which recommendation supplies the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Design a high-cardinality partition key and report full compliance; afterward, proceed on the belief that every prohibited parallel state must therefore be absent.** — The traceable checkpoint outcome is that the tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants. The requirement-to-evidence link establishes that the positive result alone does not test the explicit anti-condition 'A low-cardinality mutable property such as status is not used as the partition key'.
- ✗ **B. Prove only that a low-cardinality mutable property such as status is not used as the partition key and report the intended configuration as present; then treat as decisive the assertion that absence is equivalent to positive-state evidence.** — The failure model establishes that a low-cardinality mutable property such as status is not used as the partition key. The requirement-to-evidence link establishes that absence evidence cannot demonstrate the required positive state 'The tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants'.
- ✗ **C. Use Bound autoscale throughput's negative assertion for Design a high-cardinality partition key. Independently, base approval on the claim that negative assertions are interchangeable between checkpoints.** — The recovery guidance assumes that the configured maximum does not exceed the approved cost envelope. The requirement-to-evidence link establishes that the second assertion is valid for Bound autoscale throughput but leaves this checkpoint's prohibited state untested.
- ✓ **D. Verify the positive properties for Design a high-cardinality partition key; as a separate check, independently verify that a low-cardinality mutable property such as status is not used as the partition key.** — The safe operating boundary says that the tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants; A low-cardinality mutable property such as status is not used as the partition key. The requirement-to-evidence link establishes that two independent observations prevent a passing positive check from concealing an unsafe parallel state.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q18 — answer A

The architecture board reconsiders 'Design a high-cardinality partition key' with product data owners. The board wants the Well-Architected consequence of mitigating this risk: One tenant can exceed logical-partition storage or throughput limits. Choose the consequence attributable to this checkpoint.

- ✓ **A. Record this consequence: Performance Efficiency: a high-cardinality access-aligned key distributes storage and request units; before approval, tie it to LAB10-REQ-02.** — The WAF consequence identifies that performance Efficiency: a high-cardinality access-aligned key distributes storage and request units. The requirement-to-evidence link establishes that it states the authored pillar consequence of the control evaluated at Design a high-cardinality partition key.
- ✗ **B. Use the Restrict the account network boundary consequence as the result for Design a high-cardinality partition key. As another control, use as justification the claim that a pillar statement remains valid when moved away from Restrict the account network boundary.** — The command-level assertion is anchored in the fact that security: private connectivity prevents unrestricted public access to the semi-structured data account. The requirement-to-evidence link establishes that that tradeoff belongs to Restrict the account network boundary and does not explain this checkpoint's decision.
- ✗ **C. Remove the control responsible for the Design a high-cardinality partition key outcome; as a separate check, accept without proof that a moderate cost classification outweighs the mandatory architecture state.** — the required outcome at Design a high-cardinality partition key. Consequently, cost Optimization cannot remove the acceptance condition 'The tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants'.
- ✗ **D. Treat 'Performance Efficiency: a high-cardinality access-aligned key distributes storage and request units' as proof that all five pillars pass. Afterward, rely on the claim that the checkpoint 'Design a high-cardinality partition key' no longer needs its separate negative check.** — The controlling fact is that a low-cardinality mutable property such as status is not used as the partition key. Consequently, one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q19 — answer D

A review of 'Design a high-cardinality partition key' begins with input from security architecture. A material change now applies: One enterprise tenant grows to forty percent of all traffic and requires per-tenant cost attribution and data isolation; revise partition and container strategy without breaking other tenants. Which answer describes the correct revision to the decision record?

- ✗ **A. Retain Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning at Design a high-cardinality partition key without recalculating criteria or eligibility; for this decision, use the premise that the original weighted result is permanent.** — The relevant observation is that azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning. Consequently, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Azure Table Storage with denormalized entities and account-level scale for Design a high-cardinality partition key without rechecking its mandatory constraints. Before sign-off, consider it sufficient that being different from the current design is an architecture criterion.** — The checkpoint specifically records that azure Table Storage with denormalized entities and account-level scale. Consequently, being different is not a criterion, and the candidate still must avoid the prohibited state at Design a high-cardinality partition key.
- ✗ **C. Keep Azure SQL Database with JSON columns and relational indexes eligible at Design a high-cardinality partition key by downgrading LAB10-REQ-02; as an independent condition, take it as conclusive that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The scenario makes clear that lAB10-REQ-02. Consequently, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.
- ✓ **D. Re-score Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning and both alternatives for Design a high-cardinality partition key; as an independent condition, supersede the ADR using the changed evidence for LAB10-REQ-02.** — The authored acceptance boundary states that azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning at Design a high-cardinality partition key. Consequently, the material change 'One enterprise tenant grows to forty percent of all traffic and requires per-tenant cost attribution and data isolation; revise partition and container strategy without breaking other tenants.' requires fresh eligibility, weighted analysis, and a superseding decision.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q20 — answer A

'Design a high-cardinality partition key' awaits approval from finOps. After a partial run, cleanup must follow this dependency: Delete the run-owned container before its database and account. What should be recorded as the dependency-safe cleanup plan?

- ✓ **A. Verify exact run-state IDs and ownership tags for Design a high-cardinality partition key; then follow this dependency rule without purge: Delete the run-owned container before its database and account.** — The architecture evidence must show that delete the run-owned container before its database and account. Consequently, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **B. Apply the cleanup rule for Minimize indexing write amplification before reconciling the current dependency. Independently, rely on the belief that removing a parent needed to identify Design a high-cardinality partition key is harmless.** — The applicable design condition is that restore the original indexing policy before deleting a retained container. Consequently, a cleanup rule for Minimize indexing write amplification cannot override the dependency declared for Design a high-cardinality partition key.
- ✗ **C. Delete candidates by display name before comparing the Design a high-cardinality partition key ownership tags. Next, proceed on the belief that the dependency rule 'Delete the run-owned container before its database and account' is optional.** — The review is governed by this fact: partition-key path, cardinality estimate, largest logical partition estimate, query patterns, and hotspot mitigation. Consequently, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Design a high-cardinality partition key negative assertion 'A low-cardinality mutable property such as status is not used as the partition key', and then treat as decisive the assertion that remaining command logs are sufficient recovery evidence.** — The retained result must be reconciled with the fact that a low-cardinality mutable property such as status is not used as the partition key. Consequently, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q21 — answer C

'Minimize indexing write amplification' is reopened at the request of finOps. Approval requires a positive result plus this independent negative assertion: A blanket include-all policy is not retained when measured writes and unused fields make it wasteful. What should the architect select as the acceptance rule that makes LAB10-REQ-03 testable?

- ✗ **A. Select Azure Table Storage with denormalized entities and account-level scale before checking Minimize indexing write amplification; for the final assessment, rely on the claim that a successful deployment will later prove the architecture constraint.** — The safe operating boundary says that a blanket include-all policy is not retained when measured writes and unused fields make it wasteful. Consequently, a deployment result cannot prove LAB10-REQ-03, and Azure Table Storage with denormalized entities and account-level scale still has to meet the mandatory boundary.
- ✗ **B. Use the passing result from Choose API and consistency deliberately to approve Minimize indexing write amplification. Then, rely on the belief that one control establishes an unrelated acceptance boundary.** — The traceable checkpoint outcome is that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. Consequently, that outcome belongs to Choose API and consistency deliberately and leaves Minimize indexing write amplification unverified.
- ✓ **C. Require the documented positive state for Minimize indexing write amplification; in a separate step, verify that a blanket include-all policy is not retained when measured writes and unused fields make it wasteful.** — The decision tension comes from the fact that indexed paths serve known filters and ordering while large descriptive payloads are explicitly excluded. Consequently, the positive state and an independent negative assertion jointly make LAB10-REQ-03 testable.
- ✗ **D. Choose Azure SQL Database with JSON columns and relational indexes and skip the Minimize indexing write amplification negative assertion; afterward, proceed on the belief that the candidate has the lowest implementation effort.** — The failure model establishes that serve a variable global catalog workload with predictable latency and controlled throughput cost. Consequently, implementation effort cannot justify skipping the negative assertion or displace LAB10-REQ-03.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q22 — answer B

A design review of 'Minimize indexing write amplification' includes digital commerce engineering. The selected architecture is Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning; object existence alone is not success. Select the intended successful finding.

- ✗ **A. Use only the negative assertion 'A blanket include-all policy is not retained when measured writes and unused fields make it wasteful' as the success result. Also, take it as conclusive that absence proves every required positive property.** — The WAF consequence identifies that a blanket include-all policy is not retained when measured writes and unused fields make it wasteful. Consequently, this is the independent prohibited-state assertion, not a successful finding.
- ✓ **B. Record indexed paths serve known filters and ordering while large descriptive payloads are explicitly excluded; next, classify it as success for LAB10-REQ-03.** — The recovery guidance assumes that indexed paths serve known filters and ordering while large descriptive payloads are explicitly excluded. Consequently, this is the authored target state for Minimize indexing write amplification and directly supports LAB10-REQ-03.
- ✗ **C. Use the successful finding from Design a high-cardinality partition key as the result for Minimize indexing write amplification; in a separate step, treat it as established that a property from the current checkpoint does not need to be inspected.** — The command-level assertion is anchored in the fact that the tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants. Consequently, evidence for Design a high-cardinality partition key cannot substitute for the properties required at Minimize indexing write amplification.
- ✗ **D. Record the failure condition 'A production query requires a path or composite order omitted from the policy' as a successful state. As another control, use as justification the claim that the command returned an object.** — a production query requires a path or composite order omitted from the policy. For this case, resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q23 — answer B

The team asks product data owners to assess 'Minimize indexing write amplification'. Evidence must address this risk without retaining credentials: A production query requires a path or composite order omitted from the policy. Which response provides sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Bound autoscale throughput for Minimize indexing write amplification; before approval, treat as decisive the assertion that a related checkpoint proves the current expected state.** — The authored acceptance boundary states that throughput mode, maximum RU/s, minimum billing implication, scale trigger, and cost owner. For this case, that evidence supports Bound autoscale throughput, so it cannot demonstrate Indexed paths serve known filters and ordering while large descriptive payloads are explicitly excluded.
- ✓ **B. Retain index-policy hash, included and excluded paths, composite indexes, query examples, and RU estimate; for this decision, exclude credentials and unrelated response fields.** — The controlling fact is that index-policy hash, included and excluded paths, composite indexes, query examples, and RU estimate. For this case, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **C. Store unredacted Minimize indexing write amplification output with operator, tenant, token, and request context. Separately, base approval on the claim that reproduction requires every captured field.** — The relevant observation is that unredacted implementation output. For this case, identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **D. Record only the Minimize indexing write amplification positive inspection's exit status; for this decision, use the premise that projected properties and assertion results can be reconstructed later.** — The checkpoint specifically records that the positive inspection's exit status. For this case, an exit code alone does not show whether indexed paths serve known filters and ordering while large descriptive payloads are explicitly excluded.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q24 — answer D

A recommendation on 'Minimize indexing write amplification' is requested by security architecture. The target is Indexed paths serve known filters and ordering while large descriptive payloads are explicitly excluded, but the latest evidence does not show it. Which choice gives the team the most likely cause?

- ✗ **A. Treat 'The wrong subresource group or DNS zone produces a public endpoint resolution' as grounds to reject Minimize indexing write amplification; afterward, accept without proof that restrict the account network boundary's failure model applies unchanged here.** — The architecture evidence must show that the wrong subresource group or DNS zone produces a public endpoint resolution. For this case, that condition belongs to Restrict the account network boundary and does not by itself invalidate Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning.
- ✗ **B. Ignore the negative assertion 'A blanket include-all policy is not retained when measured writes and unused fields make it wasteful'; then rely on the claim that a later material change will make it unnecessary.** — The applicable design condition is that a blanket include-all policy is not retained when measured writes and unused fields make it wasteful. For this case, the negative assertion must be evaluated now, independent of a later business change.
- ✗ **C. Investigate Choose API and consistency deliberately instead of diagnosing Minimize indexing write amplification. Independently, rely on the belief that a passing result at Choose API and consistency deliberately identifies the current cause.** — The review is governed by this fact: the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. For this case, a passing result at Choose API and consistency deliberately gives no causal evidence for the failure at Minimize indexing write amplification.
- ✓ **D. Investigate a production query requires a path or composite order omitted from the policy. Then, isolate that cause before changing Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning.** — The scenario makes clear that a production query requires a path or composite order omitted from the policy. For this case, it is the checkpoint's causal failure model and should be isolated before retrying Minimize indexing write amplification.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q25 — answer D

'Minimize indexing write amplification' is assigned to finOps. The run encountered this modeled failure: A production query requires a path or composite order omitted from the policy. What is the safest recovery action?

- ✗ **A. Perform cleanup immediately: Restore the original indexing policy before deleting a retained container. As another control, consider it sufficient that the failed operation and its returned identifiers do not need reconciliation.** — The decision tension comes from the fact that restore the original indexing policy before deleting a retained container. For this case, cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **B. Create a different run identity before diagnosing 'A production query requires a path or composite order omitted from the policy'; as a separate check, take it as conclusive that the first state record and returned identifiers can be discarded.** — The safe operating boundary says that a production query requires a path or composite order omitted from the policy. For this case, discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **C. Change Choose API and consistency deliberately instead. Afterward, treat it as established that success at Choose API and consistency deliberately will repair the failed state at Minimize indexing write amplification.** — The traceable checkpoint outcome is that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. For this case, altering an already separate checkpoint does not repair the modeled failure at Minimize indexing write amplification.
- ✓ **D. Add the narrowest supported index after evaluating transformation cost and expected RU reduction. Next, preserve the current run identity and evidence.** — The retained result must be reconciled with the fact that add the narrowest supported index after evaluating transformation cost and expected RU reduction. For this case, it corrects the narrow cause while retaining the same recovery trail and decision scope.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q26 — answer D

An assurance review of 'Minimize indexing write amplification' includes digital commerce engineering. Without making a new change, the team must inspect the risk 'A production query requires a path or composite order omitted from the policy' using the Azure CLI lane. Which recommendation supplies the read-only, lane-correct inspection?

- ✗ **A. Rerun the Minimize indexing write amplification implementation command and infer the expected state; for this decision, proceed on the belief that absence of a shell error proves every property.** — The recovery guidance assumes that the implementation command. For this case, it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Minimize indexing write amplification: A blanket include-all policy is not retained when measured writes and unused fields make it wasteful. Before sign-off, treat as decisive the assertion that an empty negative result reports every required positive property.** — The WAF consequence identifies that the negative inspection. For this case, absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **C. Run the positive inspection for Design a high-cardinality partition key and apply it to Minimize indexing write amplification; as an independent condition, base approval on the claim that any command from the same lane proves the current checkpoint.** — The command-level assertion is anchored in the fact that the positive inspection for Design a high-cardinality partition key. For this case, it is lane-correct but proves Design a high-cardinality partition key, not Minimize indexing write amplification.
- ✓ **D. Inspect the documented properties for Minimize indexing write amplification. As another control, retain this evidence: index-policy hash, included and excluded paths, composite indexes, query examples, and RU estimate.** — The failure model establishes that indexed paths serve known filters and ordering while large descriptive payloads are explicitly excluded. For this case, the read-only inspection directly tests the properties required at Minimize indexing write amplification.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q27 — answer B

Approval of 'Minimize indexing write amplification' is questioned by product data owners. A passing positive check does not by itself prove this negative assertion: A blanket include-all policy is not retained when measured writes and unused fields make it wasteful. Choose the assertion pair that proves both conditions independently.

- ✗ **A. Verify only the positive result for Minimize indexing write amplification and report full compliance. Independently, use as justification the claim that every prohibited parallel state must therefore be absent.** — The controlling fact is that indexed paths serve known filters and ordering while large descriptive payloads are explicitly excluded. That evidence means the positive result alone does not test the explicit anti-condition 'A blanket include-all policy is not retained when measured writes and unused fields make it wasteful'.
- ✓ **B. Verify the positive properties for Minimize indexing write amplification. In addition, independently verify that a blanket include-all policy is not retained when measured writes and unused fields make it wasteful.** — indexed paths serve known filters and ordering while large descriptive payloads are explicitly excluded; A blanket include-all policy is not retained when measured writes and unused fields make it wasteful. That evidence means two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **C. Prove only that a blanket include-all policy is not retained when measured writes and unused fields make it wasteful and report the intended configuration as present. Next, accept without proof that absence is equivalent to positive-state evidence.** — The authored acceptance boundary states that a blanket include-all policy is not retained when measured writes and unused fields make it wasteful. That evidence means absence evidence cannot demonstrate the required positive state 'Indexed paths serve known filters and ordering while large descriptive payloads are explicitly excluded'.
- ✗ **D. Use Bound autoscale throughput's negative assertion for Minimize indexing write amplification, and then rely on the claim that negative assertions are interchangeable between checkpoints.** — The relevant observation is that the configured maximum does not exceed the approved cost envelope. That evidence means the second assertion is valid for Bound autoscale throughput but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q28 — answer A

The implementation review has reached 'Minimize indexing write amplification'. The board wants the Well-Architected consequence of mitigating this risk: A production query requires a path or composite order omitted from the policy. Which answer describes the consequence attributable to this checkpoint?

- ✓ **A. Record this consequence: Operational Excellence: a versioned indexing policy makes query support and write amplification reviewable. Before sign-off, tie it to LAB10-REQ-03.** — The checkpoint specifically records that operational Excellence: a versioned indexing policy makes query support and write amplification reviewable. That evidence means it states the authored pillar consequence of the control evaluated at Minimize indexing write amplification.
- ✗ **B. Use the Restrict the account network boundary consequence as the result for Minimize indexing write amplification. Afterward, use the premise that a pillar statement remains valid when moved away from Restrict the account network boundary.** — The scenario makes clear that security: private connectivity prevents unrestricted public access to the semi-structured data account. That evidence means that tradeoff belongs to Restrict the account network boundary and does not explain this checkpoint's decision.
- ✗ **C. Remove the control responsible for the Minimize indexing write amplification outcome; next, consider it sufficient that a moderate cost classification outweighs the mandatory architecture state.** — The architecture evidence must show that the required outcome at Minimize indexing write amplification. That evidence means cost Optimization cannot remove the acceptance condition 'Indexed paths serve known filters and ordering while large descriptive payloads are explicitly excluded'.
- ✗ **D. Treat 'Operational Excellence: a versioned indexing policy makes query support and write amplification reviewable' as proof that all five pillars pass. In addition, take it as conclusive that the checkpoint 'Minimize indexing write amplification' no longer needs its separate negative check.** — The applicable design condition is that a blanket include-all policy is not retained when measured writes and unused fields make it wasteful. That evidence means one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q29 — answer C

The approach to 'Minimize indexing write amplification' is challenged by finOps. A material change now applies: One enterprise tenant grows to forty percent of all traffic and requires per-tenant cost attribution and data isolation; revise partition and container strategy without breaking other tenants. What should be recorded as the correct revision to the decision record?

- ✗ **A. Retain Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning at Minimize indexing write amplification without recalculating criteria or eligibility; as an independent condition, rely on the belief that the original weighted result is permanent.** — The retained result must be reconciled with the fact that azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning. That evidence means the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Azure Table Storage with denormalized entities and account-level scale for Minimize indexing write amplification without rechecking its mandatory constraints; before approval, proceed on the belief that being different from the current design is an architecture criterion.** — The decision tension comes from the fact that azure Table Storage with denormalized entities and account-level scale. That evidence means being different is not a criterion, and the candidate still must avoid the prohibited state at Minimize indexing write amplification.
- ✓ **C. Re-score Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning and both alternatives for Minimize indexing write amplification; afterward, supersede the ADR using the changed evidence for LAB10-REQ-03.** — The review is governed by this fact: azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning at Minimize indexing write amplification. That evidence means the material change 'One enterprise tenant grows to forty percent of all traffic and requires per-tenant cost attribution and data isolation; revise partition and container strategy without breaking other tenants.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **D. Keep Azure SQL Database with JSON columns and relational indexes eligible at Minimize indexing write amplification by downgrading LAB10-REQ-03. Then, treat as decisive the assertion that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The safe operating boundary says that lAB10-REQ-03. That evidence means an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q30 — answer B

A decision test for 'Minimize indexing write amplification' includes digital commerce engineering. After a partial run, cleanup must follow this dependency: Restore the original indexing policy before deleting a retained container. Which proposal supplies the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Design a high-cardinality partition key before reconciling the current dependency, and then treat it as established that removing a parent needed to identify Minimize indexing write amplification is harmless.** — The failure model establishes that delete the run-owned container before its database and account. That evidence means a cleanup rule for Design a high-cardinality partition key cannot override the dependency declared for Minimize indexing write amplification.
- ✓ **B. Verify exact run-state IDs and ownership tags for Minimize indexing write amplification, and then follow this dependency rule without purge: Restore the original indexing policy before deleting a retained container.** — The traceable checkpoint outcome is that restore the original indexing policy before deleting a retained container. That evidence means exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **C. Delete candidates by display name before comparing the Minimize indexing write amplification ownership tags. Also, use as justification the claim that the dependency rule 'Restore the original indexing policy before deleting a retained container' is optional.** — The recovery guidance assumes that index-policy hash, included and excluded paths, composite indexes, query examples, and RU estimate. That evidence means names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Minimize indexing write amplification negative assertion 'A blanket include-all policy is not retained when measured writes and unused fields make it wasteful'; in a separate step, accept without proof that remaining command logs are sufficient recovery evidence.** — The WAF consequence identifies that a blanket include-all policy is not retained when measured writes and unused fields make it wasteful. That evidence means irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q31 — answer C

The architecture board reconsiders 'Bound autoscale throughput' with digital commerce engineering. Approval requires a positive result plus this independent negative assertion: The configured maximum does not exceed the approved cost envelope. Select the acceptance rule that makes LAB10-REQ-04 testable.

- ✗ **A. Select Azure Table Storage with denormalized entities and account-level scale before checking Bound autoscale throughput; afterward, take it as conclusive that a successful deployment will later prove the architecture constraint.** — the configured maximum does not exceed the approved cost envelope. The resulting architectural conclusion is that a deployment result cannot prove LAB10-REQ-04, and Azure Table Storage with denormalized entities and account-level scale still has to meet the mandatory boundary.
- ✗ **B. Use the passing result from Choose API and consistency deliberately to approve Bound autoscale throughput; then treat it as established that one control establishes an unrelated acceptance boundary.** — The controlling fact is that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. The resulting architectural conclusion is that that outcome belongs to Choose API and consistency deliberately and leaves Bound autoscale throughput unverified.
- ✓ **C. Require the documented positive state for Bound autoscale throughput. Afterward, verify that the configured maximum does not exceed the approved cost envelope.** — The command-level assertion is anchored in the fact that autoscale absorbs seasonal bursts up to an approved maximum RU/s with alerts for sustained saturation. That evidence means the positive state and an independent negative assertion jointly make LAB10-REQ-04 testable.
- ✗ **D. Choose Azure SQL Database with JSON columns and relational indexes and skip the Bound autoscale throughput negative assertion. Independently, use as justification the claim that the candidate has the lowest implementation effort.** — The authored acceptance boundary states that serve a variable global catalog workload with predictable latency and controlled throughput cost. The resulting architectural conclusion is that implementation effort cannot justify skipping the negative assertion or displace LAB10-REQ-04.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q32 — answer B

A review of 'Bound autoscale throughput' begins with input from product data owners. The selected architecture is Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning; object existence alone is not success. Which response provides the intended successful finding?

- ✗ **A. Use only the negative assertion 'The configured maximum does not exceed the approved cost envelope' as the success result. As another control, treat as decisive the assertion that absence proves every required positive property.** — The checkpoint specifically records that the configured maximum does not exceed the approved cost envelope. The resulting architectural conclusion is that this is the independent prohibited-state assertion, not a successful finding.
- ✓ **B. Record autoscale absorbs seasonal bursts up to an approved maximum RU/s with alerts for sustained saturation. Separately, classify it as success for LAB10-REQ-04.** — The relevant observation is that autoscale absorbs seasonal bursts up to an approved maximum RU/s with alerts for sustained saturation. The resulting architectural conclusion is that this is the authored target state for Bound autoscale throughput and directly supports LAB10-REQ-04.
- ✗ **C. Use the successful finding from Design a high-cardinality partition key as the result for Bound autoscale throughput; as a separate check, base approval on the claim that a property from the current checkpoint does not need to be inspected.** — The scenario makes clear that the tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants. The resulting architectural conclusion is that evidence for Design a high-cardinality partition key cannot substitute for the properties required at Bound autoscale throughput.
- ✗ **D. Record the failure condition 'Shared-container tenants cannot be attributed or one partition consumes the full maximum' as a successful state. Afterward, use the premise that the command returned an object.** — The architecture evidence must show that shared-container tenants cannot be attributed or one partition consumes the full maximum. The resulting architectural conclusion is that resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q33 — answer C

'Bound autoscale throughput' awaits approval from security architecture. Evidence must address this risk without retaining credentials: Shared-container tenants cannot be attributed or one partition consumes the full maximum. Which choice gives the team sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Minimize indexing write amplification for Bound autoscale throughput; for this decision, accept without proof that a related checkpoint proves the current expected state.** — The review is governed by this fact: index-policy hash, included and excluded paths, composite indexes, query examples, and RU estimate. The resulting architectural conclusion is that that evidence supports Minimize indexing write amplification, so it cannot demonstrate Autoscale absorbs seasonal bursts up to an approved maximum RU/s with alerts for sustained saturation.
- ✗ **B. Store unredacted Bound autoscale throughput output with operator, tenant, token, and request context. Before sign-off, rely on the claim that reproduction requires every captured field.** — The retained result must be reconciled with the fact that unredacted implementation output. The resulting architectural conclusion is that identity, tenant, or token material exceeds the non-secret evidence contract.
- ✓ **C. Retain throughput mode, maximum RU/s, minimum billing implication, scale trigger, and cost owner; during the same review, exclude credentials and unrelated response fields.** — The applicable design condition is that throughput mode, maximum RU/s, minimum billing implication, scale trigger, and cost owner. The resulting architectural conclusion is that it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **D. Record only the Bound autoscale throughput positive inspection's exit status; as an independent condition, rely on the belief that projected properties and assertion results can be reconstructed later.** — The decision tension comes from the fact that the positive inspection's exit status. The resulting architectural conclusion is that an exit code alone does not show whether autoscale absorbs seasonal bursts up to an approved maximum RU/s with alerts for sustained saturation.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q34 — answer C

'Bound autoscale throughput' is reopened at the request of finOps. The target is Autoscale absorbs seasonal bursts up to an approved maximum RU/s with alerts for sustained saturation, but the latest evidence does not show it. What is the most likely cause?

- ✗ **A. Treat 'The wrong subresource group or DNS zone produces a public endpoint resolution' as grounds to reject Bound autoscale throughput. Independently, consider it sufficient that restrict the account network boundary's failure model applies unchanged here.** — The traceable checkpoint outcome is that the wrong subresource group or DNS zone produces a public endpoint resolution. The resulting architectural conclusion is that that condition belongs to Restrict the account network boundary and does not by itself invalidate Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning.
- ✗ **B. Ignore the negative assertion 'The configured maximum does not exceed the approved cost envelope'. Next, take it as conclusive that a later material change will make it unnecessary.** — The failure model establishes that the configured maximum does not exceed the approved cost envelope. The resulting architectural conclusion is that the negative assertion must be evaluated now, independent of a later business change.
- ✓ **C. Investigate shared-container tenants cannot be attributed or one partition consumes the full maximum. Independently, isolate that cause before changing Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning.** — The safe operating boundary says that shared-container tenants cannot be attributed or one partition consumes the full maximum. The resulting architectural conclusion is that it is the checkpoint's causal failure model and should be isolated before retrying Bound autoscale throughput.
- ✗ **D. Investigate Choose API and consistency deliberately instead of diagnosing Bound autoscale throughput, and then treat it as established that a passing result at Choose API and consistency deliberately identifies the current cause.** — The recovery guidance assumes that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. The resulting architectural conclusion is that a passing result at Choose API and consistency deliberately gives no causal evidence for the failure at Bound autoscale throughput.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q35 — answer A

A design review of 'Bound autoscale throughput' includes digital commerce engineering. The run encountered this modeled failure: Shared-container tenants cannot be attributed or one partition consumes the full maximum. Which recommendation supplies the safest recovery action?

- ✓ **A. Measure normalized RU consumption by tenant and reconsider dedicated containers or partitioning before raising the maximum; in a separate step, preserve the current run identity and evidence.** — The WAF consequence identifies that measure normalized RU consumption by tenant and reconsider dedicated containers or partitioning before raising the maximum. The resulting architectural conclusion is that it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **B. Perform cleanup immediately: Restore recorded throughput mode only when the service supports reversal; otherwise record the limitation. Afterward, proceed on the belief that the failed operation and its returned identifiers do not need reconciliation.** — The command-level assertion is anchored in the fact that restore recorded throughput mode only when the service supports reversal; otherwise record the limitation. The resulting architectural conclusion is that cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **C. Create a different run identity before diagnosing 'Shared-container tenants cannot be attributed or one partition consumes the full maximum'; next, treat as decisive the assertion that the first state record and returned identifiers can be discarded.** — shared-container tenants cannot be attributed or one partition consumes the full maximum. Under the stated constraint, discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Choose API and consistency deliberately instead. In addition, base approval on the claim that success at Choose API and consistency deliberately will repair the failed state at Bound autoscale throughput.** — The controlling fact is that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. Under the stated constraint, altering an already separate checkpoint does not repair the modeled failure at Bound autoscale throughput.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q36 — answer D

The team asks product data owners to assess 'Bound autoscale throughput'. Without making a new change, the team must inspect the risk 'Shared-container tenants cannot be attributed or one partition consumes the full maximum' using the Azure CLI lane. Choose the read-only, lane-correct inspection.

- ✗ **A. Rerun the Bound autoscale throughput implementation command and infer the expected state; as an independent condition, use as justification the claim that absence of a shell error proves every property.** — The relevant observation is that the implementation command. Under the stated constraint, it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Bound autoscale throughput: The configured maximum does not exceed the approved cost envelope; as a second control, accept without proof that an empty negative result reports every required positive property.** — The checkpoint specifically records that the negative inspection. Under the stated constraint, absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **C. Run the positive inspection for Design a high-cardinality partition key and apply it to Bound autoscale throughput. Then, rely on the claim that any command from the same lane proves the current checkpoint.** — The scenario makes clear that the positive inspection for Design a high-cardinality partition key. Under the stated constraint, it is lane-correct but proves Design a high-cardinality partition key, not Bound autoscale throughput.
- ✓ **D. Inspect the documented properties for Bound autoscale throughput; next, retain this evidence: throughput mode, maximum RU/s, minimum billing implication, scale trigger, and cost owner.** — The authored acceptance boundary states that autoscale absorbs seasonal bursts up to an approved maximum RU/s with alerts for sustained saturation. Under the stated constraint, the read-only inspection directly tests the properties required at Bound autoscale throughput.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q37 — answer B

A recommendation on 'Bound autoscale throughput' is requested by security architecture. A passing positive check does not by itself prove this negative assertion: The configured maximum does not exceed the approved cost envelope. Which answer describes the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Bound autoscale throughput and report full compliance, and then use the premise that every prohibited parallel state must therefore be absent.** — The applicable design condition is that autoscale absorbs seasonal bursts up to an approved maximum RU/s with alerts for sustained saturation. Under the stated constraint, the positive result alone does not test the explicit anti-condition 'The configured maximum does not exceed the approved cost envelope'.
- ✓ **B. Verify the positive properties for Bound autoscale throughput; for this decision, independently verify that the configured maximum does not exceed the approved cost envelope.** — The architecture evidence must show that autoscale absorbs seasonal bursts up to an approved maximum RU/s with alerts for sustained saturation; The configured maximum does not exceed the approved cost envelope. Under the stated constraint, two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **C. Prove only that the configured maximum does not exceed the approved cost envelope and report the intended configuration as present. Also, consider it sufficient that absence is equivalent to positive-state evidence.** — The review is governed by this fact: the configured maximum does not exceed the approved cost envelope. Under the stated constraint, absence evidence cannot demonstrate the required positive state 'Autoscale absorbs seasonal bursts up to an approved maximum RU/s with alerts for sustained saturation'.
- ✗ **D. Use Minimize indexing write amplification's negative assertion for Bound autoscale throughput; in a separate step, take it as conclusive that negative assertions are interchangeable between checkpoints.** — The retained result must be reconciled with the fact that a blanket include-all policy is not retained when measured writes and unused fields make it wasteful. Under the stated constraint, the second assertion is valid for Minimize indexing write amplification but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q38 — answer D

'Bound autoscale throughput' is assigned to finOps. The board wants the Well-Architected consequence of mitigating this risk: Shared-container tenants cannot be attributed or one partition consumes the full maximum. What should be recorded as the consequence attributable to this checkpoint?

- ✗ **A. Use the Restrict the account network boundary consequence as the result for Bound autoscale throughput. In addition, rely on the belief that a pillar statement remains valid when moved away from Restrict the account network boundary.** — The safe operating boundary says that security: private connectivity prevents unrestricted public access to the semi-structured data account. Under the stated constraint, that tradeoff belongs to Restrict the account network boundary and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Bound autoscale throughput outcome; before approval, proceed on the belief that a moderate cost classification outweighs the mandatory architecture state.** — The traceable checkpoint outcome is that the required outcome at Bound autoscale throughput. Under the stated constraint, cost Optimization cannot remove the acceptance condition 'Autoscale absorbs seasonal bursts up to an approved maximum RU/s with alerts for sustained saturation'.
- ✗ **C. Treat 'Cost Optimization: a governed autoscale maximum absorbs bursts while bounding throughput spend' as proof that all five pillars pass. Separately, treat as decisive the assertion that the checkpoint 'Bound autoscale throughput' no longer needs its separate negative check.** — The failure model establishes that the configured maximum does not exceed the approved cost envelope. Under the stated constraint, one positive command cannot establish every pillar, especially while the negative state remains unchecked.
- ✓ **D. Record this consequence: Cost Optimization: a governed autoscale maximum absorbs bursts while bounding throughput spend. Then, tie it to LAB10-REQ-04.** — The decision tension comes from the fact that cost Optimization: a governed autoscale maximum absorbs bursts while bounding throughput spend. Under the stated constraint, it states the authored pillar consequence of the control evaluated at Bound autoscale throughput.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q39 — answer A

An assurance review of 'Bound autoscale throughput' includes digital commerce engineering. A material change now applies: One enterprise tenant grows to forty percent of all traffic and requires per-tenant cost attribution and data isolation; revise partition and container strategy without breaking other tenants. Which proposal supplies the correct revision to the decision record?

- ✓ **A. Re-score Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning and both alternatives for Bound autoscale throughput. Next, supersede the ADR using the changed evidence for LAB10-REQ-04.** — The recovery guidance assumes that azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning at Bound autoscale throughput. Under the stated constraint, the material change 'One enterprise tenant grows to forty percent of all traffic and requires per-tenant cost attribution and data isolation; revise partition and container strategy without breaking other tenants.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **B. Retain Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning at Bound autoscale throughput without recalculating criteria or eligibility. Then, treat it as established that the original weighted result is permanent.** — The WAF consequence identifies that azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning. Under the stated constraint, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **C. Select Azure Table Storage with denormalized entities and account-level scale for Bound autoscale throughput without rechecking its mandatory constraints; afterward, use as justification the claim that being different from the current design is an architecture criterion.** — The command-level assertion is anchored in the fact that azure Table Storage with denormalized entities and account-level scale. Under the stated constraint, being different is not a criterion, and the candidate still must avoid the prohibited state at Bound autoscale throughput.
- ✗ **D. Keep Azure SQL Database with JSON columns and relational indexes eligible at Bound autoscale throughput by downgrading LAB10-REQ-04; then accept without proof that stakeholder approval is unnecessary when that requirement blocks the candidate.** — lAB10-REQ-04. This matters because an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q40 — answer A

Approval of 'Bound autoscale throughput' is questioned by product data owners. After a partial run, cleanup must follow this dependency: Restore recorded throughput mode only when the service supports reversal; otherwise record the limitation. Which option best represents the dependency-safe cleanup plan?

- ✓ **A. Verify exact run-state IDs and ownership tags for Bound autoscale throughput. As another control, follow this dependency rule without purge: Restore recorded throughput mode only when the service supports reversal; otherwise record the limitation.** — The controlling fact is that restore recorded throughput mode only when the service supports reversal; otherwise record the limitation. This matters because exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **B. Apply the cleanup rule for Design a high-cardinality partition key before reconciling the current dependency; in a separate step, base approval on the claim that removing a parent needed to identify Bound autoscale throughput is harmless.** — The authored acceptance boundary states that delete the run-owned container before its database and account. This matters because a cleanup rule for Design a high-cardinality partition key cannot override the dependency declared for Bound autoscale throughput.
- ✗ **C. Delete candidates by display name before comparing the Bound autoscale throughput ownership tags. As another control, use the premise that the dependency rule 'Restore recorded throughput mode only when the service supports reversal; otherwise record the limitation' is optional.** — The relevant observation is that throughput mode, maximum RU/s, minimum billing implication, scale trigger, and cost owner. This matters because names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Bound autoscale throughput negative assertion 'The configured maximum does not exceed the approved cost envelope'; as a separate check, consider it sufficient that remaining command logs are sufficient recovery evidence.** — The checkpoint specifically records that the configured maximum does not exceed the approved cost envelope. This matters because irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q41 — answer D

The implementation review has reached 'Restrict the account network boundary'. Approval requires a positive result plus this independent negative assertion: Unrestricted public network access is not retained as a fallback. Which response provides the acceptance rule that makes LAB10-REQ-05 testable?

- ✗ **A. Select Azure Table Storage with denormalized entities and account-level scale before checking Restrict the account network boundary. Independently, treat as decisive the assertion that a successful deployment will later prove the architecture constraint.** — The architecture evidence must show that unrestricted public network access is not retained as a fallback. This matters because a deployment result cannot prove LAB10-REQ-05, and Azure Table Storage with denormalized entities and account-level scale still has to meet the mandatory boundary.
- ✗ **B. Use the passing result from Choose API and consistency deliberately to approve Restrict the account network boundary. Next, base approval on the claim that one control establishes an unrelated acceptance boundary.** — The applicable design condition is that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. This matters because that outcome belongs to Choose API and consistency deliberately and leaves Restrict the account network boundary unverified.
- ✗ **C. Choose Azure SQL Database with JSON columns and relational indexes and skip the Restrict the account network boundary negative assertion, and then use the premise that the candidate has the lowest implementation effort.** — The review is governed by this fact: serve a variable global catalog workload with predictable latency and controlled throughput cost. This matters because implementation effort cannot justify skipping the negative assertion or displace LAB10-REQ-05.
- ✓ **D. Require the documented positive state for Restrict the account network boundary; before approval, verify that unrestricted public network access is not retained as a fallback.** — The scenario makes clear that application access resolves through an approved private endpoint and the intended private DNS zone. This matters because the positive state and an independent negative assertion jointly make LAB10-REQ-05 testable.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q42 — answer C

The approach to 'Restrict the account network boundary' is challenged by security architecture. The selected architecture is Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning; object existence alone is not success. Which choice gives the team the intended successful finding?

- ✗ **A. Use only the negative assertion 'Unrestricted public network access is not retained as a fallback' as the success result. Afterward, accept without proof that absence proves every required positive property.** — The decision tension comes from the fact that unrestricted public network access is not retained as a fallback. This matters because this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Design a high-cardinality partition key as the result for Restrict the account network boundary; next, rely on the claim that a property from the current checkpoint does not need to be inspected.** — The safe operating boundary says that the tenant-aware key distributes writes, supports dominant reads, and has a mitigation for exceptionally large tenants. This matters because evidence for Design a high-cardinality partition key cannot substitute for the properties required at Restrict the account network boundary.
- ✓ **C. Record application access resolves through an approved private endpoint and the intended private DNS zone; as an independent condition, classify it as success for LAB10-REQ-05.** — The retained result must be reconciled with the fact that application access resolves through an approved private endpoint and the intended private DNS zone. This matters because this is the authored target state for Restrict the account network boundary and directly supports LAB10-REQ-05.
- ✗ **D. Record the failure condition 'The wrong subresource group or DNS zone produces a public endpoint resolution' as a successful state. In addition, rely on the belief that the command returned an object.** — The traceable checkpoint outcome is that the wrong subresource group or DNS zone produces a public endpoint resolution. This matters because resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q43 — answer C

A decision test for 'Restrict the account network boundary' includes finOps. Evidence must address this risk without retaining credentials: The wrong subresource group or DNS zone produces a public endpoint resolution. What is sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Minimize indexing write amplification for Restrict the account network boundary; as an independent condition, consider it sufficient that a related checkpoint proves the current expected state.** — The recovery guidance assumes that index-policy hash, included and excluded paths, composite indexes, query examples, and RU estimate. This matters because that evidence supports Minimize indexing write amplification, so it cannot demonstrate Application access resolves through an approved private endpoint and the intended private DNS zone.
- ✗ **B. Store unredacted Restrict the account network boundary output with operator, tenant, token, and request context; during the same review, take it as conclusive that reproduction requires every captured field.** — The WAF consequence identifies that unredacted implementation output. This matters because identity, tenant, or token material exceeds the non-secret evidence contract.
- ✓ **C. Retain account ID, endpoint ID, group ID, approval state, subnet, and private DNS zone label; then exclude credentials and unrelated response fields.** — The failure model establishes that account ID, endpoint ID, group ID, approval state, subnet, and private DNS zone label. This matters because it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **D. Record only the Restrict the account network boundary positive inspection's exit status. Then, treat it as established that projected properties and assertion results can be reconstructed later.** — The command-level assertion is anchored in the fact that the positive inspection's exit status. This matters because an exit code alone does not show whether application access resolves through an approved private endpoint and the intended private DNS zone.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q44 — answer D

The architecture board reconsiders 'Restrict the account network boundary' with digital commerce engineering. The target is Application access resolves through an approved private endpoint and the intended private DNS zone, but the latest evidence does not show it. Which recommendation supplies the most likely cause?

- ✗ **A. Treat 'Shared-container tenants cannot be attributed or one partition consumes the full maximum' as grounds to reject Restrict the account network boundary, and then proceed on the belief that bound autoscale throughput's failure model applies unchanged here.** — The controlling fact is that shared-container tenants cannot be attributed or one partition consumes the full maximum. The checkpoint therefore requires that that condition belongs to Bound autoscale throughput and does not by itself invalidate Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning.
- ✗ **B. Ignore the negative assertion 'Unrestricted public network access is not retained as a fallback'. Also, treat as decisive the assertion that a later material change will make it unnecessary.** — The authored acceptance boundary states that unrestricted public network access is not retained as a fallback. The checkpoint therefore requires that the negative assertion must be evaluated now, independent of a later business change.
- ✗ **C. Investigate Choose API and consistency deliberately instead of diagnosing Restrict the account network boundary; in a separate step, base approval on the claim that a passing result at Choose API and consistency deliberately identifies the current cause.** — The relevant observation is that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. The checkpoint therefore requires that a passing result at Choose API and consistency deliberately gives no causal evidence for the failure at Restrict the account network boundary.
- ✓ **D. Investigate the wrong subresource group or DNS zone produces a public endpoint resolution. Also, isolate that cause before changing Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning.** — the wrong subresource group or DNS zone produces a public endpoint resolution. The checkpoint therefore requires that it is the checkpoint's causal failure model and should be isolated before retrying Restrict the account network boundary.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q45 — answer B

A review of 'Restrict the account network boundary' begins with input from product data owners. The run encountered this modeled failure: The wrong subresource group or DNS zone produces a public endpoint resolution. Choose the safest recovery action.

- ✗ **A. Perform cleanup immediately: Remove DNS records and the private endpoint before the account; preserve shared network assets. In addition, use as justification the claim that the failed operation and its returned identifiers do not need reconciliation.** — The scenario makes clear that remove DNS records and the private endpoint before the account; preserve shared network assets. The checkpoint therefore requires that cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✓ **B. Validate Sql group selection, private DNS linking, and endpoint approval independently. Afterward, preserve the current run identity and evidence.** — The checkpoint specifically records that validate Sql group selection, private DNS linking, and endpoint approval independently. The checkpoint therefore requires that it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **C. Create a different run identity before diagnosing 'The wrong subresource group or DNS zone produces a public endpoint resolution'; before approval, accept without proof that the first state record and returned identifiers can be discarded.** — The architecture evidence must show that the wrong subresource group or DNS zone produces a public endpoint resolution. The checkpoint therefore requires that discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Choose API and consistency deliberately instead. Separately, rely on the claim that success at Choose API and consistency deliberately will repair the failed state at Restrict the account network boundary.** — The applicable design condition is that the NoSQL API and Session consistency support session read-your-writes with documented cross-session behavior. The checkpoint therefore requires that altering an already separate checkpoint does not repair the modeled failure at Restrict the account network boundary.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q46 — answer A

'Restrict the account network boundary' awaits approval from security architecture. Without making a new change, the team must inspect the risk 'The wrong subresource group or DNS zone produces a public endpoint resolution' using the Azure CLI lane. Which answer describes the read-only, lane-correct inspection?

- ✓ **A. Inspect the documented properties for Restrict the account network boundary. Separately, retain this evidence: account ID, endpoint ID, group ID, approval state, subnet, and private DNS zone label.** — The review is governed by this fact: application access resolves through an approved private endpoint and the intended private DNS zone. The checkpoint therefore requires that the read-only inspection directly tests the properties required at Restrict the account network boundary.
- ✗ **B. Rerun the Restrict the account network boundary implementation command and infer the expected state. Then, use the premise that absence of a shell error proves every property.** — The retained result must be reconciled with the fact that the implementation command. The checkpoint therefore requires that it can mutate state and shell success does not independently assert the expected properties.
- ✗ **C. Run only this negative inspection for Restrict the account network boundary: Unrestricted public network access is not retained as a fallback; afterward, consider it sufficient that an empty negative result reports every required positive property.** — The decision tension comes from the fact that the negative inspection. The checkpoint therefore requires that absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Design a high-cardinality partition key and apply it to Restrict the account network boundary; then take it as conclusive that any command from the same lane proves the current checkpoint.** — The safe operating boundary says that the positive inspection for Design a high-cardinality partition key. The checkpoint therefore requires that it is lane-correct but proves Design a high-cardinality partition key, not Restrict the account network boundary.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q47 — answer B

'Restrict the account network boundary' is reopened at the request of finOps. A passing positive check does not by itself prove this negative assertion: Unrestricted public network access is not retained as a fallback. What should be recorded as the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Restrict the account network boundary and report full compliance; in a separate step, rely on the belief that every prohibited parallel state must therefore be absent.** — The failure model establishes that application access resolves through an approved private endpoint and the intended private DNS zone. The checkpoint therefore requires that the positive result alone does not test the explicit anti-condition 'Unrestricted public network access is not retained as a fallback'.
- ✓ **B. Verify the positive properties for Restrict the account network boundary; without relying on inference, independently verify that unrestricted public network access is not retained as a fallback.** — The traceable checkpoint outcome is that application access resolves through an approved private endpoint and the intended private DNS zone; Unrestricted public network access is not retained as a fallback. The checkpoint therefore requires that two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **C. Prove only that unrestricted public network access is not retained as a fallback and report the intended configuration as present. As another control, proceed on the belief that absence is equivalent to positive-state evidence.** — The recovery guidance assumes that unrestricted public network access is not retained as a fallback. The checkpoint therefore requires that absence evidence cannot demonstrate the required positive state 'Application access resolves through an approved private endpoint and the intended private DNS zone'.
- ✗ **D. Use Minimize indexing write amplification's negative assertion for Restrict the account network boundary; as a separate check, treat as decisive the assertion that negative assertions are interchangeable between checkpoints.** — The WAF consequence identifies that a blanket include-all policy is not retained when measured writes and unused fields make it wasteful. The checkpoint therefore requires that the second assertion is valid for Minimize indexing write amplification but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q48 — answer C

A design review of 'Restrict the account network boundary' includes digital commerce engineering. The board wants the Well-Architected consequence of mitigating this risk: The wrong subresource group or DNS zone produces a public endpoint resolution. Which proposal supplies the consequence attributable to this checkpoint?

- ✗ **A. Use the Bound autoscale throughput consequence as the result for Restrict the account network boundary. Separately, treat it as established that a pillar statement remains valid when moved away from Bound autoscale throughput.** — cost Optimization: a governed autoscale maximum absorbs bursts while bounding throughput spend. In the decision record, that tradeoff belongs to Bound autoscale throughput and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Restrict the account network boundary outcome; for this decision, use as justification the claim that a moderate cost classification outweighs the mandatory architecture state.** — The controlling fact is that the required outcome at Restrict the account network boundary. In the decision record, cost Optimization cannot remove the acceptance condition 'Application access resolves through an approved private endpoint and the intended private DNS zone'.
- ✓ **C. Record this consequence: Security: private connectivity prevents unrestricted public access to the semi-structured data account. Independently, tie it to LAB10-REQ-05.** — The command-level assertion is anchored in the fact that security: private connectivity prevents unrestricted public access to the semi-structured data account. The checkpoint therefore requires that it states the authored pillar consequence of the control evaluated at Restrict the account network boundary.
- ✗ **D. Treat 'Security: private connectivity prevents unrestricted public access to the semi-structured data account' as proof that all five pillars pass. Before sign-off, accept without proof that the checkpoint 'Restrict the account network boundary' no longer needs its separate negative check.** — The authored acceptance boundary states that unrestricted public network access is not retained as a fallback. In the decision record, one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q49 — answer A

The team asks product data owners to assess 'Restrict the account network boundary'. A material change now applies: One enterprise tenant grows to forty percent of all traffic and requires per-tenant cost attribution and data isolation; revise partition and container strategy without breaking other tenants. Which option best represents the correct revision to the decision record?

- ✓ **A. Re-score Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning and both alternatives for Restrict the account network boundary; in a separate step, supersede the ADR using the changed evidence for LAB10-REQ-05.** — The relevant observation is that azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning at Restrict the account network boundary. In the decision record, the material change 'One enterprise tenant grows to forty percent of all traffic and requires per-tenant cost attribution and data isolation; revise partition and container strategy without breaking other tenants.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **B. Retain Azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning at Restrict the account network boundary without recalculating criteria or eligibility; then base approval on the claim that the original weighted result is permanent.** — The checkpoint specifically records that azure Cosmos DB for NoSQL with hierarchical tenant-aware partitioning. In the decision record, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **C. Select Azure Table Storage with denormalized entities and account-level scale for Restrict the account network boundary without rechecking its mandatory constraints. Independently, use the premise that being different from the current design is an architecture criterion.** — The scenario makes clear that azure Table Storage with denormalized entities and account-level scale. In the decision record, being different is not a criterion, and the candidate still must avoid the prohibited state at Restrict the account network boundary.
- ✗ **D. Keep Azure SQL Database with JSON columns and relational indexes eligible at Restrict the account network boundary by downgrading LAB10-REQ-05. Next, consider it sufficient that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The architecture evidence must show that lAB10-REQ-05. In the decision record, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)

## LAB10-Q50 — answer D

A recommendation on 'Restrict the account network boundary' is requested by security architecture. After a partial run, cleanup must follow this dependency: Remove DNS records and the private endpoint before the account; preserve shared network assets. Which course of action provides the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Design a high-cardinality partition key before reconciling the current dependency; as a separate check, rely on the claim that removing a parent needed to identify Restrict the account network boundary is harmless.** — The review is governed by this fact: delete the run-owned container before its database and account. In the decision record, a cleanup rule for Design a high-cardinality partition key cannot override the dependency declared for Restrict the account network boundary.
- ✗ **B. Delete candidates by display name before comparing the Restrict the account network boundary ownership tags. Afterward, rely on the belief that the dependency rule 'Remove DNS records and the private endpoint before the account; preserve shared network assets' is optional.** — The retained result must be reconciled with the fact that account ID, endpoint ID, group ID, approval state, subnet, and private DNS zone label. In the decision record, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **C. Destroy recoverable copies before retaining the Restrict the account network boundary negative assertion 'Unrestricted public network access is not retained as a fallback'; next, proceed on the belief that remaining command logs are sufficient recovery evidence.** — The decision tension comes from the fact that unrestricted public network access is not retained as a fallback. In the decision record, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.
- ✓ **D. Verify exact run-state IDs and ownership tags for Restrict the account network boundary; next, follow this dependency rule without purge: Remove DNS records and the private endpoint before the account; preserve shared network assets.** — The applicable design condition is that remove DNS records and the private endpoint before the account; preserve shared network assets. In the decision record, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/cosmos-db/partitioning-overview (verified 2026-09-02)
<!-- END GENERATED AZ305 V1 -->
