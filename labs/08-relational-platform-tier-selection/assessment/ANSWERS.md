<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-08 answer key

Use after completing the learner assessment. Every choice has a specific explanation.

## LAB08-Q01 — answer A

The architecture board reconsiders 'Convert workload facts into platform criteria' with finOps. Approval requires a positive result plus this independent negative assertion: Retired service tiers or unverified regional capabilities are not used in the decision. Which course of action provides the acceptance rule that makes LAB08-REQ-01 testable?

- ✓ **A. Require the documented positive state for Convert workload facts into platform criteria; as a separate check, verify that retired service tiers or unverified regional capabilities are not used in the decision.** — The architecture evidence must show that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. This matters because the positive state and an independent negative assertion jointly make LAB08-REQ-01 testable.
- ✗ **B. Select Azure SQL Managed Instance General Purpose before checking Convert workload facts into platform criteria; before approval, base approval on the claim that a successful deployment will later prove the architecture constraint.** — The applicable design condition is that retired service tiers or unverified regional capabilities are not used in the decision. This matters because a deployment result cannot prove LAB08-REQ-01, and Azure SQL Managed Instance General Purpose still has to meet the mandatory boundary.
- ✗ **C. Use the passing result from Establish a logical server boundary to approve Convert workload facts into platform criteria. Separately, use the premise that one control establishes an unrelated acceptance boundary.** — The review is governed by this fact: the logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency. This matters because that outcome belongs to Establish a logical server boundary and leaves Convert workload facts into platform criteria unverified.
- ✗ **D. Choose Azure Database for PostgreSQL Flexible Server General Purpose and skip the Convert workload facts into platform criteria negative assertion; for this decision, consider it sufficient that the candidate has the lowest implementation effort.** — The retained result must be reconciled with the fact that modernize the database with less operational toil and cost while retaining transactional correctness and month-end capacity. This matters because implementation effort cannot justify skipping the negative assertion or displace LAB08-REQ-01.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q02 — answer A

A review of 'Convert workload facts into platform criteria' begins with input from application engineering. The selected architecture is Azure SQL Database General Purpose serverless; object existence alone is not success. Which finding constitutes the intended successful finding?

- ✓ **A. Record compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers; before approval, classify it as success for LAB08-REQ-01.** — The decision tension comes from the fact that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. This matters because this is the authored target state for Convert workload facts into platform criteria and directly supports LAB08-REQ-01.
- ✗ **B. Use only the negative assertion 'Retired service tiers or unverified regional capabilities are not used in the decision' as the success result; afterward, rely on the claim that absence proves every required positive property.** — The safe operating boundary says that retired service tiers or unverified regional capabilities are not used in the decision. This matters because this is the independent prohibited-state assertion, not a successful finding.
- ✗ **C. Use the successful finding from Configure an elastic serverless database as the result for Convert workload facts into platform criteria; then rely on the belief that a property from the current checkpoint does not need to be inspected.** — The traceable checkpoint outcome is that general Purpose serverless supplies bounded autoscaling and one-hour autopause for the intermittent workload. This matters because evidence for Configure an elastic serverless database cannot substitute for the properties required at Convert workload facts into platform criteria.
- ✗ **D. Record the failure condition 'A required feature is instance-scoped or unavailable in the target region and tier' as a successful state. Independently, proceed on the belief that the command returned an object.** — The failure model establishes that a required feature is instance-scoped or unavailable in the target region and tier. This matters because resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q03 — answer B

'Convert workload facts into platform criteria' awaits approval from database administration. Evidence must address this risk without retaining credentials: A required feature is instance-scoped or unavailable in the target region and tier. Which recommendation delivers sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Require private application connectivity for Convert workload facts into platform criteria. As another control, take it as conclusive that a related checkpoint proves the current expected state.** — The WAF consequence identifies that private endpoint ID, connection status, subnet ID, DNS zone label, and firewall-rule count. This matters because that evidence supports Require private application connectivity, so it cannot demonstrate Compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers.
- ✓ **B. Retain sanitized workload fact sheet, edition names, supported families, region, and decision criteria; as an independent condition, exclude credentials and unrelated response fields.** — The recovery guidance assumes that sanitized workload fact sheet, edition names, supported families, region, and decision criteria. This matters because it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **C. Store unredacted Convert workload facts into platform criteria output with operator, tenant, token, and request context; as a separate check, treat it as established that reproduction requires every captured field.** — The command-level assertion is anchored in the fact that unredacted implementation output. This matters because identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **D. Record only the Convert workload facts into platform criteria positive inspection's exit status. Afterward, use as justification the claim that projected properties and assertion results can be reconstructed later.** — the positive inspection's exit status. The checkpoint therefore requires that an exit code alone does not show whether compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q04 — answer B

'Convert workload facts into platform criteria' is reopened at the request of information security. The target is Compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers, but the latest evidence does not show it. Which response meets the need for the most likely cause?

- ✗ **A. Treat 'Observed capacity demand contradicts the serverless cost or latency assumptions' as grounds to reject Convert workload facts into platform criteria; for this decision, treat as decisive the assertion that validate the service-tier decision's failure model applies unchanged here.** — The authored acceptance boundary states that observed capacity demand contradicts the serverless cost or latency assumptions. The checkpoint therefore requires that that condition belongs to Validate the service-tier decision and does not by itself invalidate Azure SQL Database General Purpose serverless.
- ✓ **B. Investigate a required feature is instance-scoped or unavailable in the target region and tier; then isolate that cause before changing Azure SQL Database General Purpose serverless.** — The controlling fact is that a required feature is instance-scoped or unavailable in the target region and tier. The checkpoint therefore requires that it is the checkpoint's causal failure model and should be isolated before retrying Convert workload facts into platform criteria.
- ✗ **C. Ignore the negative assertion 'Retired service tiers or unverified regional capabilities are not used in the decision'. Before sign-off, base approval on the claim that a later material change will make it unnecessary.** — The relevant observation is that retired service tiers or unverified regional capabilities are not used in the decision. The checkpoint therefore requires that the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Establish a logical server boundary instead of diagnosing Convert workload facts into platform criteria; as an independent condition, use the premise that a passing result at Establish a logical server boundary identifies the current cause.** — The checkpoint specifically records that the logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency. The checkpoint therefore requires that a passing result at Establish a logical server boundary gives no causal evidence for the failure at Convert workload facts into platform criteria.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q05 — answer A

A design review of 'Convert workload facts into platform criteria' includes finOps. The run encountered this modeled failure: A required feature is instance-scoped or unavailable in the target region and tier. Which choice should be approved as the safest recovery action?

- ✓ **A. Reclassify the requirement as mandatory and rescore Managed Instance before choosing a larger database tier. Also, preserve the current run identity and evidence.** — The scenario makes clear that reclassify the requirement as mandatory and rescore Managed Instance before choosing a larger database tier. The checkpoint therefore requires that it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **B. Perform cleanup immediately: This regional capability query creates no resource. Independently, accept without proof that the failed operation and its returned identifiers do not need reconciliation.** — The architecture evidence must show that this regional capability query creates no resource. The checkpoint therefore requires that cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **C. Create a different run identity before diagnosing 'A required feature is instance-scoped or unavailable in the target region and tier'. Next, rely on the claim that the first state record and returned identifiers can be discarded.** — The applicable design condition is that a required feature is instance-scoped or unavailable in the target region and tier. The checkpoint therefore requires that discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Establish a logical server boundary instead, and then rely on the belief that success at Establish a logical server boundary will repair the failed state at Convert workload facts into platform criteria.** — The review is governed by this fact: the logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency. The checkpoint therefore requires that altering an already separate checkpoint does not repair the modeled failure at Convert workload facts into platform criteria.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q06 — answer A

The team asks application engineering to assess 'Convert workload facts into platform criteria'. Without making a new change, the team must inspect the risk 'A required feature is instance-scoped or unavailable in the target region and tier' using the Azure CLI lane. What should the team use as the read-only, lane-correct inspection?

- ✓ **A. Inspect the documented properties for Convert workload facts into platform criteria. Afterward, retain this evidence: sanitized workload fact sheet, edition names, supported families, region, and decision criteria.** — The retained result must be reconciled with the fact that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. The checkpoint therefore requires that the read-only inspection directly tests the properties required at Convert workload facts into platform criteria.
- ✗ **B. Rerun the Convert workload facts into platform criteria implementation command and infer the expected state. Afterward, consider it sufficient that absence of a shell error proves every property.** — The decision tension comes from the fact that the implementation command. The checkpoint therefore requires that it can mutate state and shell success does not independently assert the expected properties.
- ✗ **C. Run only this negative inspection for Convert workload facts into platform criteria: Retired service tiers or unverified regional capabilities are not used in the decision; next, take it as conclusive that an empty negative result reports every required positive property.** — The safe operating boundary says that the negative inspection. The checkpoint therefore requires that absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Configure an elastic serverless database and apply it to Convert workload facts into platform criteria. In addition, treat it as established that any command from the same lane proves the current checkpoint.** — The traceable checkpoint outcome is that the positive inspection for Configure an elastic serverless database. The checkpoint therefore requires that it is lane-correct but proves Configure an elastic serverless database, not Convert workload facts into platform criteria.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q07 — answer A

A recommendation on 'Convert workload facts into platform criteria' is requested by database administration. A passing positive check does not by itself prove this negative assertion: Retired service tiers or unverified regional capabilities are not used in the decision. Which option best establishes the assertion pair that proves both conditions independently?

- ✓ **A. Verify the positive properties for Convert workload facts into platform criteria. Separately, independently verify that retired service tiers or unverified regional capabilities are not used in the decision.** — The failure model establishes that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers; Retired service tiers or unverified regional capabilities are not used in the decision. The checkpoint therefore requires that two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **B. Verify only the positive result for Convert workload facts into platform criteria and report full compliance; as an independent condition, proceed on the belief that every prohibited parallel state must therefore be absent.** — The recovery guidance assumes that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. The checkpoint therefore requires that the positive result alone does not test the explicit anti-condition 'Retired service tiers or unverified regional capabilities are not used in the decision'.
- ✗ **C. Prove only that retired service tiers or unverified regional capabilities are not used in the decision and report the intended configuration as present; as another gate, treat as decisive the assertion that absence is equivalent to positive-state evidence.** — The WAF consequence identifies that retired service tiers or unverified regional capabilities are not used in the decision. The checkpoint therefore requires that absence evidence cannot demonstrate the required positive state 'Compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers'.
- ✗ **D. Use Require private application connectivity's negative assertion for Convert workload facts into platform criteria. Then, base approval on the claim that negative assertions are interchangeable between checkpoints.** — The command-level assertion is anchored in the fact that the Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors. The checkpoint therefore requires that the second assertion is valid for Require private application connectivity but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q08 — answer D

'Convert workload facts into platform criteria' is assigned to information security. The board wants the Well-Architected consequence of mitigating this risk: A required feature is instance-scoped or unavailable in the target region and tier. Which answer identifies the consequence attributable to this checkpoint?

- ✗ **A. Use the Validate the service-tier decision consequence as the result for Convert workload facts into platform criteria, and then use as justification the claim that a pillar statement remains valid when moved away from Validate the service-tier decision.** — The controlling fact is that operational Excellence: configuration and usage evidence tie the deployed database back to the reviewed service decision. In the decision record, that tradeoff belongs to Validate the service-tier decision and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Convert workload facts into platform criteria outcome. Also, accept without proof that a moderate cost classification outweighs the mandatory architecture state.** — The authored acceptance boundary states that the required outcome at Convert workload facts into platform criteria. In the decision record, cost Optimization cannot remove the acceptance condition 'Compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers'.
- ✗ **C. Treat 'Performance Efficiency: measured workload demand and compatibility select a supported service tier' as proof that all five pillars pass; in a separate step, rely on the claim that the checkpoint 'Convert workload facts into platform criteria' no longer needs its separate negative check.** — The relevant observation is that retired service tiers or unverified regional capabilities are not used in the decision. In the decision record, one positive command cannot establish every pillar, especially while the negative state remains unchecked.
- ✓ **D. Record this consequence: Performance Efficiency: measured workload demand and compatibility select a supported service tier; without relying on inference, tie it to LAB08-REQ-01.** — performance Efficiency: measured workload demand and compatibility select a supported service tier. In the decision record, it states the authored pillar consequence of the control evaluated at Convert workload facts into platform criteria.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q09 — answer C

An assurance review of 'Convert workload facts into platform criteria' includes finOps. A material change now applies: The acquired application reveals a hard dependency on SQL Agent, cross-database transactions, and instance-level collation; revise the platform choice without treating a larger SQL Database tier as compatibility. What recommendation gives the reviewers the correct revision to the decision record?

- ✗ **A. Retain Azure SQL Database General Purpose serverless at Convert workload facts into platform criteria without recalculating criteria or eligibility. In addition, use the premise that the original weighted result is permanent.** — The scenario makes clear that azure SQL Database General Purpose serverless. In the decision record, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Azure SQL Managed Instance General Purpose for Convert workload facts into platform criteria without rechecking its mandatory constraints; before approval, consider it sufficient that being different from the current design is an architecture criterion.** — The architecture evidence must show that azure SQL Managed Instance General Purpose. In the decision record, being different is not a criterion, and the candidate still must avoid the prohibited state at Convert workload facts into platform criteria.
- ✓ **C. Re-score Azure SQL Database General Purpose serverless and both alternatives for Convert workload facts into platform criteria. Independently, supersede the ADR using the changed evidence for LAB08-REQ-01.** — The checkpoint specifically records that azure SQL Database General Purpose serverless at Convert workload facts into platform criteria. In the decision record, the material change 'The acquired application reveals a hard dependency on SQL Agent, cross-database transactions, and instance-level collation; revise the platform choice without treating a larger SQL Database tier as compatibility.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **D. Keep Azure Database for PostgreSQL Flexible Server General Purpose eligible at Convert workload facts into platform criteria by downgrading LAB08-REQ-01. Separately, take it as conclusive that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The applicable design condition is that lAB08-REQ-01. In the decision record, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q10 — answer C

Approval of 'Convert workload facts into platform criteria' is questioned by application engineering. After a partial run, cleanup must follow this dependency: This regional capability query creates no resource. Which action produces the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Configure an elastic serverless database before reconciling the current dependency. Then, rely on the belief that removing a parent needed to identify Convert workload facts into platform criteria is harmless.** — The retained result must be reconciled with the fact that delete the run-owned database before its logical server; do not purge backups. In the decision record, a cleanup rule for Configure an elastic serverless database cannot override the dependency declared for Convert workload facts into platform criteria.
- ✗ **B. Delete candidates by display name before comparing the Convert workload facts into platform criteria ownership tags; afterward, proceed on the belief that the dependency rule 'This regional capability query creates no resource' is optional.** — The decision tension comes from the fact that sanitized workload fact sheet, edition names, supported families, region, and decision criteria. In the decision record, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✓ **C. Verify exact run-state IDs and ownership tags for Convert workload facts into platform criteria; in a separate step, follow this dependency rule without purge: This regional capability query creates no resource.** — The review is governed by this fact: this regional capability query creates no resource. In the decision record, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **D. Destroy recoverable copies before retaining the Convert workload facts into platform criteria negative assertion 'Retired service tiers or unverified regional capabilities are not used in the decision'; then treat as decisive the assertion that remaining command logs are sufficient recovery evidence.** — The safe operating boundary says that retired service tiers or unverified regional capabilities are not used in the decision. In the decision record, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q11 — answer D

The implementation review has reached 'Establish a logical server boundary'. Approval requires a positive result plus this independent negative assertion: No personal administrator or legacy SQL administrator is part of the access design. Which finding constitutes the acceptance rule that makes LAB08-REQ-02 testable?

- ✗ **A. Select Azure SQL Managed Instance General Purpose before checking Establish a logical server boundary; for this decision, rely on the claim that a successful deployment will later prove the architecture constraint.** — The failure model establishes that no personal administrator or legacy SQL administrator is part of the access design. In the decision record, a deployment result cannot prove LAB08-REQ-02, and Azure SQL Managed Instance General Purpose still has to meet the mandatory boundary.
- ✗ **B. Use the passing result from Convert workload facts into platform criteria to approve Establish a logical server boundary. Before sign-off, rely on the belief that one control establishes an unrelated acceptance boundary.** — The recovery guidance assumes that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. In the decision record, that outcome belongs to Convert workload facts into platform criteria and leaves Establish a logical server boundary unverified.
- ✗ **C. Choose Azure Database for PostgreSQL Flexible Server General Purpose and skip the Establish a logical server boundary negative assertion; as an independent condition, proceed on the belief that the candidate has the lowest implementation effort.** — The WAF consequence identifies that modernize the database with less operational toil and cost while retaining transactional correctness and month-end capacity. In the decision record, implementation effort cannot justify skipping the negative assertion or displace LAB08-REQ-02.
- ✓ **D. Require the documented positive state for Establish a logical server boundary. In addition, verify that no personal administrator or legacy SQL administrator is part of the access design.** — The traceable checkpoint outcome is that the logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency. In the decision record, the positive state and an independent negative assertion jointly make LAB08-REQ-02 testable.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q12 — answer A

The approach to 'Establish a logical server boundary' is challenged by database administration. The selected architecture is Azure SQL Database General Purpose serverless; object existence alone is not success. Which recommendation delivers the intended successful finding?

- ✓ **A. Record the logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency. Before sign-off, classify it as success for LAB08-REQ-02.** — The command-level assertion is anchored in the fact that the logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency. In the decision record, this is the authored target state for Establish a logical server boundary and directly supports LAB08-REQ-02.
- ✗ **B. Use only the negative assertion 'No personal administrator or legacy SQL administrator is part of the access design' as the success result. Independently, take it as conclusive that absence proves every required positive property.** — no personal administrator or legacy SQL administrator is part of the access design. The independent assertion shows why this is the independent prohibited-state assertion, not a successful finding.
- ✗ **C. Use the successful finding from Configure an elastic serverless database as the result for Establish a logical server boundary. Next, treat it as established that a property from the current checkpoint does not need to be inspected.** — The controlling fact is that general Purpose serverless supplies bounded autoscaling and one-hour autopause for the intermittent workload. The independent assertion shows why evidence for Configure an elastic serverless database cannot substitute for the properties required at Establish a logical server boundary.
- ✗ **D. Record the failure condition 'Directory object lookup or SQL Entra-only authentication is unavailable to the executing identity' as a successful state, and then use as justification the claim that the command returned an object.** — The authored acceptance boundary states that directory object lookup or SQL Entra-only authentication is unavailable to the executing identity. The independent assertion shows why resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q13 — answer D

A decision test for 'Establish a logical server boundary' includes information security. Evidence must address this risk without retaining credentials: Directory object lookup or SQL Entra-only authentication is unavailable to the executing identity. Which response meets the need for sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Require private application connectivity for Establish a logical server boundary. Afterward, treat as decisive the assertion that a related checkpoint proves the current expected state.** — The checkpoint specifically records that private endpoint ID, connection status, subnet ID, DNS zone label, and firewall-rule count. The independent assertion shows why that evidence supports Require private application connectivity, so it cannot demonstrate The logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency.
- ✗ **B. Store unredacted Establish a logical server boundary output with operator, tenant, token, and request context; next, base approval on the claim that reproduction requires every captured field.** — The scenario makes clear that unredacted implementation output. The independent assertion shows why identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **C. Record only the Establish a logical server boundary positive inspection's exit status. In addition, use the premise that projected properties and assertion results can be reconstructed later.** — The architecture evidence must show that the positive inspection's exit status. The independent assertion shows why an exit code alone does not show whether the logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency.
- ✓ **D. Retain server label, region, administrator group label, authentication mode, and resource ID without credentials; afterward, exclude credentials and unrelated response fields.** — The relevant observation is that server label, region, administrator group label, authentication mode, and resource ID without credentials. The independent assertion shows why it captures the checkpoint's observable properties while keeping the evidence boundary narrow.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q14 — answer B

The architecture board reconsiders 'Establish a logical server boundary' with finOps. The target is The logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency, but the latest evidence does not show it. Which choice should be approved as the most likely cause?

- ✗ **A. Treat 'Observed capacity demand contradicts the serverless cost or latency assumptions' as grounds to reject Establish a logical server boundary; as an independent condition, accept without proof that validate the service-tier decision's failure model applies unchanged here.** — The review is governed by this fact: observed capacity demand contradicts the serverless cost or latency assumptions. The independent assertion shows why that condition belongs to Validate the service-tier decision and does not by itself invalidate Azure SQL Database General Purpose serverless.
- ✓ **B. Investigate directory object lookup or SQL Entra-only authentication is unavailable to the executing identity, and then isolate that cause before changing Azure SQL Database General Purpose serverless.** — The applicable design condition is that directory object lookup or SQL Entra-only authentication is unavailable to the executing identity. The independent assertion shows why it is the checkpoint's causal failure model and should be isolated before retrying Establish a logical server boundary.
- ✗ **C. Ignore the negative assertion 'No personal administrator or legacy SQL administrator is part of the access design'; without relying on inference, rely on the claim that a later material change will make it unnecessary.** — The retained result must be reconciled with the fact that no personal administrator or legacy SQL administrator is part of the access design. The independent assertion shows why the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Convert workload facts into platform criteria instead of diagnosing Establish a logical server boundary. Then, rely on the belief that a passing result at Convert workload facts into platform criteria identifies the current cause.** — The decision tension comes from the fact that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. The independent assertion shows why a passing result at Convert workload facts into platform criteria gives no causal evidence for the failure at Establish a logical server boundary.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q15 — answer D

A review of 'Establish a logical server boundary' begins with input from application engineering. The run encountered this modeled failure: Directory object lookup or SQL Entra-only authentication is unavailable to the executing identity. What should the team use as the safest recovery action?

- ✗ **A. Perform cleanup immediately: Delete databases and private endpoints before the run-owned logical server, and then consider it sufficient that the failed operation and its returned identifiers do not need reconciliation.** — The traceable checkpoint outcome is that delete databases and private endpoints before the run-owned logical server. The independent assertion shows why cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **B. Create a different run identity before diagnosing 'Directory object lookup or SQL Entra-only authentication is unavailable to the executing identity'. Also, take it as conclusive that the first state record and returned identifiers can be discarded.** — The failure model establishes that directory object lookup or SQL Entra-only authentication is unavailable to the executing identity. The independent assertion shows why discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **C. Change Convert workload facts into platform criteria instead; in a separate step, treat it as established that success at Convert workload facts into platform criteria will repair the failed state at Establish a logical server boundary.** — The recovery guidance assumes that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. The independent assertion shows why altering an already separate checkpoint does not repair the modeled failure at Establish a logical server boundary.
- ✓ **D. Confirm the group object ID and delegated permission; do not substitute a committed password; as a separate check, preserve the current run identity and evidence.** — The safe operating boundary says that confirm the group object ID and delegated permission; do not substitute a committed password. The independent assertion shows why it corrects the narrow cause while retaining the same recovery trail and decision scope.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q16 — answer C

'Establish a logical server boundary' awaits approval from database administration. Without making a new change, the team must inspect the risk 'Directory object lookup or SQL Entra-only authentication is unavailable to the executing identity' using the Azure CLI lane. Which option best establishes the read-only, lane-correct inspection?

- ✗ **A. Rerun the Establish a logical server boundary implementation command and infer the expected state. In addition, proceed on the belief that absence of a shell error proves every property.** — The command-level assertion is anchored in the fact that the implementation command. The independent assertion shows why it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Establish a logical server boundary: No personal administrator or legacy SQL administrator is part of the access design; before approval, treat as decisive the assertion that an empty negative result reports every required positive property.** — the negative inspection. Operationally, absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✓ **C. Inspect the documented properties for Establish a logical server boundary; before approval, retain this evidence: server label, region, administrator group label, authentication mode, and resource ID without credentials.** — The WAF consequence identifies that the logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency. The independent assertion shows why the read-only inspection directly tests the properties required at Establish a logical server boundary.
- ✗ **D. Run the positive inspection for Configure an elastic serverless database and apply it to Establish a logical server boundary. Separately, base approval on the claim that any command from the same lane proves the current checkpoint.** — The controlling fact is that the positive inspection for Configure an elastic serverless database. Operationally, it is lane-correct but proves Configure an elastic serverless database, not Establish a logical server boundary.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q17 — answer C

'Establish a logical server boundary' is reopened at the request of information security. A passing positive check does not by itself prove this negative assertion: No personal administrator or legacy SQL administrator is part of the access design. Which answer identifies the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Establish a logical server boundary and report full compliance. Then, use as justification the claim that every prohibited parallel state must therefore be absent.** — The relevant observation is that the logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency. Operationally, the positive result alone does not test the explicit anti-condition 'No personal administrator or legacy SQL administrator is part of the access design'.
- ✗ **B. Prove only that no personal administrator or legacy SQL administrator is part of the access design and report the intended configuration as present; afterward, accept without proof that absence is equivalent to positive-state evidence.** — The checkpoint specifically records that no personal administrator or legacy SQL administrator is part of the access design. Operationally, absence evidence cannot demonstrate the required positive state 'The logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency'.
- ✓ **C. Verify the positive properties for Establish a logical server boundary; as an independent condition, independently verify that no personal administrator or legacy SQL administrator is part of the access design.** — The authored acceptance boundary states that the logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency; No personal administrator or legacy SQL administrator is part of the access design. Operationally, two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **D. Use Require private application connectivity's negative assertion for Establish a logical server boundary; then rely on the claim that negative assertions are interchangeable between checkpoints.** — The scenario makes clear that the Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors. Operationally, the second assertion is valid for Require private application connectivity but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q18 — answer B

A design review of 'Establish a logical server boundary' includes finOps. The board wants the Well-Architected consequence of mitigating this risk: Directory object lookup or SQL Entra-only authentication is unavailable to the executing identity. What recommendation gives the reviewers the consequence attributable to this checkpoint?

- ✗ **A. Use the Validate the service-tier decision consequence as the result for Establish a logical server boundary; in a separate step, use the premise that a pillar statement remains valid when moved away from Validate the service-tier decision.** — The applicable design condition is that operational Excellence: configuration and usage evidence tie the deployed database back to the reviewed service decision. Operationally, that tradeoff belongs to Validate the service-tier decision and does not explain this checkpoint's decision.
- ✓ **B. Record this consequence: Security: Entra-only authentication and group administration remove personal and password-based control paths; then tie it to LAB08-REQ-02.** — The architecture evidence must show that security: Entra-only authentication and group administration remove personal and password-based control paths. Operationally, it states the authored pillar consequence of the control evaluated at Establish a logical server boundary.
- ✗ **C. Remove the control responsible for the Establish a logical server boundary outcome. As another control, consider it sufficient that a moderate cost classification outweighs the mandatory architecture state.** — The review is governed by this fact: the required outcome at Establish a logical server boundary. Operationally, cost Optimization cannot remove the acceptance condition 'The logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency'.
- ✗ **D. Treat 'Security: Entra-only authentication and group administration remove personal and password-based control paths' as proof that all five pillars pass; as a separate check, take it as conclusive that the checkpoint 'Establish a logical server boundary' no longer needs its separate negative check.** — The retained result must be reconciled with the fact that no personal administrator or legacy SQL administrator is part of the access design. Operationally, one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q19 — answer D

The team asks application engineering to assess 'Establish a logical server boundary'. A material change now applies: The acquired application reveals a hard dependency on SQL Agent, cross-database transactions, and instance-level collation; revise the platform choice without treating a larger SQL Database tier as compatibility. Which action produces the correct revision to the decision record?

- ✗ **A. Retain Azure SQL Database General Purpose serverless at Establish a logical server boundary without recalculating criteria or eligibility. Separately, rely on the belief that the original weighted result is permanent.** — The safe operating boundary says that azure SQL Database General Purpose serverless. Operationally, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Azure SQL Managed Instance General Purpose for Establish a logical server boundary without rechecking its mandatory constraints; for this decision, proceed on the belief that being different from the current design is an architecture criterion.** — The traceable checkpoint outcome is that azure SQL Managed Instance General Purpose. Operationally, being different is not a criterion, and the candidate still must avoid the prohibited state at Establish a logical server boundary.
- ✗ **C. Keep Azure Database for PostgreSQL Flexible Server General Purpose eligible at Establish a logical server boundary by downgrading LAB08-REQ-02. Before sign-off, treat as decisive the assertion that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The failure model establishes that lAB08-REQ-02. Operationally, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.
- ✓ **D. Re-score Azure SQL Database General Purpose serverless and both alternatives for Establish a logical server boundary. Also, supersede the ADR using the changed evidence for LAB08-REQ-02.** — The decision tension comes from the fact that azure SQL Database General Purpose serverless at Establish a logical server boundary. Operationally, the material change 'The acquired application reveals a hard dependency on SQL Agent, cross-database transactions, and instance-level collation; revise the platform choice without treating a larger SQL Database tier as compatibility.' requires fresh eligibility, weighted analysis, and a superseding decision.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q20 — answer B

A recommendation on 'Establish a logical server boundary' is requested by database administration. After a partial run, cleanup must follow this dependency: Delete databases and private endpoints before the run-owned logical server. What best demonstrates the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Configure an elastic serverless database before reconciling the current dependency; then treat it as established that removing a parent needed to identify Establish a logical server boundary is harmless.** — The WAF consequence identifies that delete the run-owned database before its logical server; do not purge backups. Operationally, a cleanup rule for Configure an elastic serverless database cannot override the dependency declared for Establish a logical server boundary.
- ✓ **B. Verify exact run-state IDs and ownership tags for Establish a logical server boundary. Afterward, follow this dependency rule without purge: Delete databases and private endpoints before the run-owned logical server.** — The recovery guidance assumes that delete databases and private endpoints before the run-owned logical server. Operationally, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **C. Delete candidates by display name before comparing the Establish a logical server boundary ownership tags. Independently, use as justification the claim that the dependency rule 'Delete databases and private endpoints before the run-owned logical server' is optional.** — The command-level assertion is anchored in the fact that server label, region, administrator group label, authentication mode, and resource ID without credentials. Operationally, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Establish a logical server boundary negative assertion 'No personal administrator or legacy SQL administrator is part of the access design'. Next, accept without proof that remaining command logs are sufficient recovery evidence.** — no personal administrator or legacy SQL administrator is part of the access design. The requirement-to-evidence link establishes that irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q21 — answer B

'Configure an elastic serverless database' is assigned to database administration. Approval requires a positive result plus this independent negative assertion: A continuously provisioned premium or warehouse tier is not selected without a requirement. Which recommendation delivers the acceptance rule that makes LAB08-REQ-03 testable?

- ✗ **A. Select Azure SQL Managed Instance General Purpose before checking Configure an elastic serverless database; as an independent condition, take it as conclusive that a successful deployment will later prove the architecture constraint.** — The authored acceptance boundary states that a continuously provisioned premium or warehouse tier is not selected without a requirement. The requirement-to-evidence link establishes that a deployment result cannot prove LAB08-REQ-03, and Azure SQL Managed Instance General Purpose still has to meet the mandatory boundary.
- ✓ **B. Require the documented positive state for Configure an elastic serverless database; for this decision, verify that a continuously provisioned premium or warehouse tier is not selected without a requirement.** — The controlling fact is that general Purpose serverless supplies bounded autoscaling and one-hour autopause for the intermittent workload. The requirement-to-evidence link establishes that the positive state and an independent negative assertion jointly make LAB08-REQ-03 testable.
- ✗ **C. Use the passing result from Convert workload facts into platform criteria to approve Configure an elastic serverless database; before closing the checkpoint, treat it as established that one control establishes an unrelated acceptance boundary.** — The relevant observation is that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. The requirement-to-evidence link establishes that that outcome belongs to Convert workload facts into platform criteria and leaves Configure an elastic serverless database unverified.
- ✗ **D. Choose Azure Database for PostgreSQL Flexible Server General Purpose and skip the Configure an elastic serverless database negative assertion. Then, use as justification the claim that the candidate has the lowest implementation effort.** — The checkpoint specifically records that modernize the database with less operational toil and cost while retaining transactional correctness and month-end capacity. The requirement-to-evidence link establishes that implementation effort cannot justify skipping the negative assertion or displace LAB08-REQ-03.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q22 — answer A

An assurance review of 'Configure an elastic serverless database' includes information security. The selected architecture is Azure SQL Database General Purpose serverless; object existence alone is not success. Which response meets the need for the intended successful finding?

- ✓ **A. Record general Purpose serverless supplies bounded autoscaling and one-hour autopause for the intermittent workload. Then, classify it as success for LAB08-REQ-03.** — The scenario makes clear that general Purpose serverless supplies bounded autoscaling and one-hour autopause for the intermittent workload. The requirement-to-evidence link establishes that this is the authored target state for Configure an elastic serverless database and directly supports LAB08-REQ-03.
- ✗ **B. Use only the negative assertion 'A continuously provisioned premium or warehouse tier is not selected without a requirement' as the success result, and then treat as decisive the assertion that absence proves every required positive property.** — The architecture evidence must show that a continuously provisioned premium or warehouse tier is not selected without a requirement. The requirement-to-evidence link establishes that this is the independent prohibited-state assertion, not a successful finding.
- ✗ **C. Use the successful finding from Establish a logical server boundary as the result for Configure an elastic serverless database. Also, base approval on the claim that a property from the current checkpoint does not need to be inspected.** — The applicable design condition is that the logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency. The requirement-to-evidence link establishes that evidence for Establish a logical server boundary cannot substitute for the properties required at Configure an elastic serverless database.
- ✗ **D. Record the failure condition 'Features such as geo replicas or sustained minimum activity prevent autopause or serverless use' as a successful state; in a separate step, use the premise that the command returned an object.** — The review is governed by this fact: features such as geo replicas or sustained minimum activity prevent autopause or serverless use. The requirement-to-evidence link establishes that resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q23 — answer C

Approval of 'Configure an elastic serverless database' is questioned by finOps. Evidence must address this risk without retaining credentials: Features such as geo replicas or sustained minimum activity prevent autopause or serverless use. Which choice should be approved as sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Require private application connectivity for Configure an elastic serverless database. In addition, accept without proof that a related checkpoint proves the current expected state.** — The decision tension comes from the fact that private endpoint ID, connection status, subnet ID, DNS zone label, and firewall-rule count. The requirement-to-evidence link establishes that that evidence supports Require private application connectivity, so it cannot demonstrate General Purpose serverless supplies bounded autoscaling and one-hour autopause for the intermittent workload.
- ✗ **B. Store unredacted Configure an elastic serverless database output with operator, tenant, token, and request context; before approval, rely on the claim that reproduction requires every captured field.** — The safe operating boundary says that unredacted implementation output. The requirement-to-evidence link establishes that identity, tenant, or token material exceeds the non-secret evidence contract.
- ✓ **C. Retain database label, edition, family, maximum and minimum vCores, autopause delay, and zone decision. Next, exclude credentials and unrelated response fields.** — The retained result must be reconciled with the fact that database label, edition, family, maximum and minimum vCores, autopause delay, and zone decision. The requirement-to-evidence link establishes that it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **D. Record only the Configure an elastic serverless database positive inspection's exit status. Separately, rely on the belief that projected properties and assertion results can be reconstructed later.** — The traceable checkpoint outcome is that the positive inspection's exit status. The requirement-to-evidence link establishes that an exit code alone does not show whether general Purpose serverless supplies bounded autoscaling and one-hour autopause for the intermittent workload.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q24 — answer D

The implementation review has reached 'Configure an elastic serverless database'. The target is General Purpose serverless supplies bounded autoscaling and one-hour autopause for the intermittent workload, but the latest evidence does not show it. What should the team use as the most likely cause?

- ✗ **A. Treat 'Observed capacity demand contradicts the serverless cost or latency assumptions' as grounds to reject Configure an elastic serverless database. Then, consider it sufficient that validate the service-tier decision's failure model applies unchanged here.** — The recovery guidance assumes that observed capacity demand contradicts the serverless cost or latency assumptions. The requirement-to-evidence link establishes that that condition belongs to Validate the service-tier decision and does not by itself invalidate Azure SQL Database General Purpose serverless.
- ✗ **B. Ignore the negative assertion 'A continuously provisioned premium or warehouse tier is not selected without a requirement'; afterward, take it as conclusive that a later material change will make it unnecessary.** — The WAF consequence identifies that a continuously provisioned premium or warehouse tier is not selected without a requirement. The requirement-to-evidence link establishes that the negative assertion must be evaluated now, independent of a later business change.
- ✗ **C. Investigate Convert workload facts into platform criteria instead of diagnosing Configure an elastic serverless database; then treat it as established that a passing result at Convert workload facts into platform criteria identifies the current cause.** — The command-level assertion is anchored in the fact that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. The requirement-to-evidence link establishes that a passing result at Convert workload facts into platform criteria gives no causal evidence for the failure at Configure an elastic serverless database.
- ✓ **D. Investigate features such as geo replicas or sustained minimum activity prevent autopause or serverless use. As another control, isolate that cause before changing Azure SQL Database General Purpose serverless.** — The failure model establishes that features such as geo replicas or sustained minimum activity prevent autopause or serverless use. The requirement-to-evidence link establishes that it is the checkpoint's causal failure model and should be isolated before retrying Configure an elastic serverless database.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q25 — answer A

The approach to 'Configure an elastic serverless database' is challenged by database administration. The run encountered this modeled failure: Features such as geo replicas or sustained minimum activity prevent autopause or serverless use. Which option best establishes the safest recovery action?

- ✓ **A. Measure the blocking dependency and compare provisioned General Purpose without changing database engine. In addition, preserve the current run identity and evidence.** — measure the blocking dependency and compare provisioned General Purpose without changing database engine. Consequently, it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **B. Perform cleanup immediately: Delete the run-owned database before its logical server; do not purge backups; in a separate step, proceed on the belief that the failed operation and its returned identifiers do not need reconciliation.** — The controlling fact is that delete the run-owned database before its logical server; do not purge backups. Consequently, cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **C. Create a different run identity before diagnosing 'Features such as geo replicas or sustained minimum activity prevent autopause or serverless use'. As another control, treat as decisive the assertion that the first state record and returned identifiers can be discarded.** — The authored acceptance boundary states that features such as geo replicas or sustained minimum activity prevent autopause or serverless use. Consequently, discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Convert workload facts into platform criteria instead; as a separate check, base approval on the claim that success at Convert workload facts into platform criteria will repair the failed state at Configure an elastic serverless database.** — The relevant observation is that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. Consequently, altering an already separate checkpoint does not repair the modeled failure at Configure an elastic serverless database.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q26 — answer C

A decision test for 'Configure an elastic serverless database' includes information security. Without making a new change, the team must inspect the risk 'Features such as geo replicas or sustained minimum activity prevent autopause or serverless use' using the Azure CLI lane. Which answer identifies the read-only, lane-correct inspection?

- ✗ **A. Rerun the Configure an elastic serverless database implementation command and infer the expected state. Separately, use as justification the claim that absence of a shell error proves every property.** — The scenario makes clear that the implementation command. Consequently, it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Configure an elastic serverless database: A continuously provisioned premium or warehouse tier is not selected without a requirement; for this decision, accept without proof that an empty negative result reports every required positive property.** — The architecture evidence must show that the negative inspection. Consequently, absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✓ **C. Inspect the documented properties for Configure an elastic serverless database. Before sign-off, retain this evidence: database label, edition, family, maximum and minimum vCores, autopause delay, and zone decision.** — The checkpoint specifically records that general Purpose serverless supplies bounded autoscaling and one-hour autopause for the intermittent workload. Consequently, the read-only inspection directly tests the properties required at Configure an elastic serverless database.
- ✗ **D. Run the positive inspection for Establish a logical server boundary and apply it to Configure an elastic serverless database. Before sign-off, rely on the claim that any command from the same lane proves the current checkpoint.** — The applicable design condition is that the positive inspection for Establish a logical server boundary. Consequently, it is lane-correct but proves Establish a logical server boundary, not Configure an elastic serverless database.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q27 — answer C

The architecture board reconsiders 'Configure an elastic serverless database' with finOps. A passing positive check does not by itself prove this negative assertion: A continuously provisioned premium or warehouse tier is not selected without a requirement. What recommendation gives the reviewers the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Configure an elastic serverless database and report full compliance; then use the premise that every prohibited parallel state must therefore be absent.** — The retained result must be reconciled with the fact that general Purpose serverless supplies bounded autoscaling and one-hour autopause for the intermittent workload. Consequently, the positive result alone does not test the explicit anti-condition 'A continuously provisioned premium or warehouse tier is not selected without a requirement'.
- ✗ **B. Prove only that a continuously provisioned premium or warehouse tier is not selected without a requirement and report the intended configuration as present. Independently, consider it sufficient that absence is equivalent to positive-state evidence.** — The decision tension comes from the fact that a continuously provisioned premium or warehouse tier is not selected without a requirement. Consequently, absence evidence cannot demonstrate the required positive state 'General Purpose serverless supplies bounded autoscaling and one-hour autopause for the intermittent workload'.
- ✓ **C. Verify the positive properties for Configure an elastic serverless database; afterward, independently verify that a continuously provisioned premium or warehouse tier is not selected without a requirement.** — The review is governed by this fact: general Purpose serverless supplies bounded autoscaling and one-hour autopause for the intermittent workload; A continuously provisioned premium or warehouse tier is not selected without a requirement. Consequently, two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **D. Use Require private application connectivity's negative assertion for Configure an elastic serverless database. Next, take it as conclusive that negative assertions are interchangeable between checkpoints.** — The safe operating boundary says that the Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors. Consequently, the second assertion is valid for Require private application connectivity but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q28 — answer C

A review of 'Configure an elastic serverless database' begins with input from application engineering. The board wants the Well-Architected consequence of mitigating this risk: Features such as geo replicas or sustained minimum activity prevent autopause or serverless use. Which action produces the consequence attributable to this checkpoint?

- ✗ **A. Use the Validate the service-tier decision consequence as the result for Configure an elastic serverless database; as a separate check, rely on the belief that a pillar statement remains valid when moved away from Validate the service-tier decision.** — The failure model establishes that operational Excellence: configuration and usage evidence tie the deployed database back to the reviewed service decision. Consequently, that tradeoff belongs to Validate the service-tier decision and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Configure an elastic serverless database outcome. Afterward, proceed on the belief that a moderate cost classification outweighs the mandatory architecture state.** — The recovery guidance assumes that the required outcome at Configure an elastic serverless database. Consequently, cost Optimization cannot remove the acceptance condition 'General Purpose serverless supplies bounded autoscaling and one-hour autopause for the intermittent workload'.
- ✓ **C. Record this consequence: Cost Optimization: serverless compute scales down during idle periods within an approved capacity ceiling, and then tie it to LAB08-REQ-03.** — The traceable checkpoint outcome is that cost Optimization: serverless compute scales down during idle periods within an approved capacity ceiling. Consequently, it states the authored pillar consequence of the control evaluated at Configure an elastic serverless database.
- ✗ **D. Treat 'Cost Optimization: serverless compute scales down during idle periods within an approved capacity ceiling' as proof that all five pillars pass; next, treat as decisive the assertion that the checkpoint 'Configure an elastic serverless database' no longer needs its separate negative check.** — The WAF consequence identifies that a continuously provisioned premium or warehouse tier is not selected without a requirement. Consequently, one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q29 — answer D

'Configure an elastic serverless database' awaits approval from database administration. A material change now applies: The acquired application reveals a hard dependency on SQL Agent, cross-database transactions, and instance-level collation; revise the platform choice without treating a larger SQL Database tier as compatibility. What best demonstrates the correct revision to the decision record?

- ✗ **A. Retain Azure SQL Database General Purpose serverless at Configure an elastic serverless database without recalculating criteria or eligibility. Before sign-off, treat it as established that the original weighted result is permanent.** — azure SQL Database General Purpose serverless. For this case, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Azure SQL Managed Instance General Purpose for Configure an elastic serverless database without rechecking its mandatory constraints; as an independent condition, use as justification the claim that being different from the current design is an architecture criterion.** — The controlling fact is that azure SQL Managed Instance General Purpose. For this case, being different is not a criterion, and the candidate still must avoid the prohibited state at Configure an elastic serverless database.
- ✗ **C. Keep Azure Database for PostgreSQL Flexible Server General Purpose eligible at Configure an elastic serverless database by downgrading LAB08-REQ-03; independently, accept without proof that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The authored acceptance boundary states that lAB08-REQ-03. For this case, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.
- ✓ **D. Re-score Azure SQL Database General Purpose serverless and both alternatives for Configure an elastic serverless database; as a separate check, supersede the ADR using the changed evidence for LAB08-REQ-03.** — The command-level assertion is anchored in the fact that azure SQL Database General Purpose serverless at Configure an elastic serverless database. Consequently, the material change 'The acquired application reveals a hard dependency on SQL Agent, cross-database transactions, and instance-level collation; revise the platform choice without treating a larger SQL Database tier as compatibility.' requires fresh eligibility, weighted analysis, and a superseding decision.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q30 — answer D

'Configure an elastic serverless database' is reopened at the request of information security. After a partial run, cleanup must follow this dependency: Delete the run-owned database before its logical server; do not purge backups. Which option is the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Establish a logical server boundary before reconciling the current dependency. Next, base approval on the claim that removing a parent needed to identify Configure an elastic serverless database is harmless.** — The checkpoint specifically records that delete databases and private endpoints before the run-owned logical server. For this case, a cleanup rule for Establish a logical server boundary cannot override the dependency declared for Configure an elastic serverless database.
- ✗ **B. Delete candidates by display name before comparing the Configure an elastic serverless database ownership tags, and then use the premise that the dependency rule 'Delete the run-owned database before its logical server; do not purge backups' is optional.** — The scenario makes clear that database label, edition, family, maximum and minimum vCores, autopause delay, and zone decision. For this case, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **C. Destroy recoverable copies before retaining the Configure an elastic serverless database negative assertion 'A continuously provisioned premium or warehouse tier is not selected without a requirement'. Also, consider it sufficient that remaining command logs are sufficient recovery evidence.** — The architecture evidence must show that a continuously provisioned premium or warehouse tier is not selected without a requirement. For this case, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.
- ✓ **D. Verify exact run-state IDs and ownership tags for Configure an elastic serverless database; before approval, follow this dependency rule without purge: Delete the run-owned database before its logical server; do not purge backups.** — The relevant observation is that delete the run-owned database before its logical server; do not purge backups. For this case, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q31 — answer B

A design review of 'Require private application connectivity' includes information security. Approval requires a positive result plus this independent negative assertion: The Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors. Which response meets the need for the acceptance rule that makes LAB08-REQ-04 testable?

- ✗ **A. Select Azure SQL Managed Instance General Purpose before checking Require private application connectivity. Then, treat as decisive the assertion that a successful deployment will later prove the architecture constraint.** — The review is governed by this fact: the Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors. For this case, a deployment result cannot prove LAB08-REQ-04, and Azure SQL Managed Instance General Purpose still has to meet the mandatory boundary.
- ✓ **B. Require the documented positive state for Require private application connectivity; before approval, verify that the Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors.** — The applicable design condition is that the application reaches the logical server through an approved private endpoint and private DNS path. For this case, the positive state and an independent negative assertion jointly make LAB08-REQ-04 testable.
- ✗ **C. Use the passing result from Convert workload facts into platform criteria to approve Require private application connectivity; afterward, base approval on the claim that one control establishes an unrelated acceptance boundary.** — The retained result must be reconciled with the fact that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. For this case, that outcome belongs to Convert workload facts into platform criteria and leaves Require private application connectivity unverified.
- ✗ **D. Choose Azure Database for PostgreSQL Flexible Server General Purpose and skip the Require private application connectivity negative assertion; then use the premise that the candidate has the lowest implementation effort.** — The decision tension comes from the fact that modernize the database with less operational toil and cost while retaining transactional correctness and month-end capacity. For this case, implementation effort cannot justify skipping the negative assertion or displace LAB08-REQ-04.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q32 — answer D

The team asks finOps to assess 'Require private application connectivity'. The selected architecture is Azure SQL Database General Purpose serverless; object existence alone is not success. Which choice should be approved as the intended successful finding?

- ✗ **A. Use only the negative assertion 'The Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors' as the success result; in a separate step, accept without proof that absence proves every required positive property.** — The traceable checkpoint outcome is that the Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors. For this case, this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Establish a logical server boundary as the result for Require private application connectivity. As another control, rely on the claim that a property from the current checkpoint does not need to be inspected.** — The failure model establishes that the logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency. For this case, evidence for Establish a logical server boundary cannot substitute for the properties required at Require private application connectivity.
- ✗ **C. Record the failure condition 'Private DNS resolves incorrectly or the endpoint connection remains pending' as a successful state; as a separate check, rely on the belief that the command returned an object.** — The recovery guidance assumes that private DNS resolves incorrectly or the endpoint connection remains pending. For this case, resource existence or command output does not convert the documented failure condition into success.
- ✓ **D. Record the application reaches the logical server through an approved private endpoint and private DNS path. Independently, classify it as success for LAB08-REQ-04.** — The safe operating boundary says that the application reaches the logical server through an approved private endpoint and private DNS path. For this case, this is the authored target state for Require private application connectivity and directly supports LAB08-REQ-04.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q33 — answer A

A recommendation on 'Require private application connectivity' is requested by application engineering. Evidence must address this risk without retaining credentials: Private DNS resolves incorrectly or the endpoint connection remains pending. What should the team use as sufficient, properly scoped evidence?

- ✓ **A. Retain private endpoint ID, connection status, subnet ID, DNS zone label, and firewall-rule count; in a separate step, exclude credentials and unrelated response fields.** — The WAF consequence identifies that private endpoint ID, connection status, subnet ID, DNS zone label, and firewall-rule count. For this case, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **B. Substitute the evidence from Configure an elastic serverless database for Require private application connectivity. Separately, consider it sufficient that a related checkpoint proves the current expected state.** — The command-level assertion is anchored in the fact that database label, edition, family, maximum and minimum vCores, autopause delay, and zone decision. For this case, that evidence supports Configure an elastic serverless database, so it cannot demonstrate The application reaches the logical server through an approved private endpoint and private DNS path.
- ✗ **C. Store unredacted Require private application connectivity output with operator, tenant, token, and request context; for this decision, take it as conclusive that reproduction requires every captured field.** — unredacted implementation output. That evidence means identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **D. Record only the Require private application connectivity positive inspection's exit status. Before sign-off, treat it as established that projected properties and assertion results can be reconstructed later.** — The controlling fact is that the positive inspection's exit status. That evidence means an exit code alone does not show whether the application reaches the logical server through an approved private endpoint and private DNS path.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q34 — answer A

'Require private application connectivity' is assigned to database administration. The target is The application reaches the logical server through an approved private endpoint and private DNS path, but the latest evidence does not show it. Which option best establishes the most likely cause?

- ✓ **A. Investigate private DNS resolves incorrectly or the endpoint connection remains pending; next, isolate that cause before changing Azure SQL Database General Purpose serverless.** — The authored acceptance boundary states that private DNS resolves incorrectly or the endpoint connection remains pending. That evidence means it is the checkpoint's causal failure model and should be isolated before retrying Require private application connectivity.
- ✗ **B. Treat 'Observed capacity demand contradicts the serverless cost or latency assumptions' as grounds to reject Require private application connectivity; then proceed on the belief that validate the service-tier decision's failure model applies unchanged here.** — The relevant observation is that observed capacity demand contradicts the serverless cost or latency assumptions. That evidence means that condition belongs to Validate the service-tier decision and does not by itself invalidate Azure SQL Database General Purpose serverless.
- ✗ **C. Ignore the negative assertion 'The Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors'. Independently, treat as decisive the assertion that a later material change will make it unnecessary.** — The checkpoint specifically records that the Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors. That evidence means the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Convert workload facts into platform criteria instead of diagnosing Require private application connectivity. Next, base approval on the claim that a passing result at Convert workload facts into platform criteria identifies the current cause.** — The scenario makes clear that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. That evidence means a passing result at Convert workload facts into platform criteria gives no causal evidence for the failure at Require private application connectivity.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q35 — answer D

An assurance review of 'Require private application connectivity' includes information security. The run encountered this modeled failure: Private DNS resolves incorrectly or the endpoint connection remains pending. Which answer identifies the safest recovery action?

- ✗ **A. Perform cleanup immediately: Delete private DNS records and endpoint connections before server cleanup; preserve shared zones; as a separate check, use as justification the claim that the failed operation and its returned identifiers do not need reconciliation.** — The applicable design condition is that delete private DNS records and endpoint connections before server cleanup; preserve shared zones. That evidence means cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **B. Create a different run identity before diagnosing 'Private DNS resolves incorrectly or the endpoint connection remains pending'. Afterward, accept without proof that the first state record and returned identifiers can be discarded.** — The review is governed by this fact: private DNS resolves incorrectly or the endpoint connection remains pending. That evidence means discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **C. Change Convert workload facts into platform criteria instead; next, rely on the claim that success at Convert workload facts into platform criteria will repair the failed state at Require private application connectivity.** — The retained result must be reconciled with the fact that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. That evidence means altering an already separate checkpoint does not repair the modeled failure at Require private application connectivity.
- ✓ **D. Correct DNS linkage and approval independently before disabling or reopening any network path; for this decision, preserve the current run identity and evidence.** — The architecture evidence must show that correct DNS linkage and approval independently before disabling or reopening any network path. That evidence means it corrects the narrow cause while retaining the same recovery trail and decision scope.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q36 — answer B

Approval of 'Require private application connectivity' is questioned by finOps. Without making a new change, the team must inspect the risk 'Private DNS resolves incorrectly or the endpoint connection remains pending' using the Azure CLI lane. What recommendation gives the reviewers the read-only, lane-correct inspection?

- ✗ **A. Rerun the Require private application connectivity implementation command and infer the expected state. Before sign-off, use the premise that absence of a shell error proves every property.** — The safe operating boundary says that the implementation command. That evidence means it can mutate state and shell success does not independently assert the expected properties.
- ✓ **B. Inspect the documented properties for Require private application connectivity. Then, retain this evidence: private endpoint ID, connection status, subnet ID, DNS zone label, and firewall-rule count.** — The decision tension comes from the fact that the application reaches the logical server through an approved private endpoint and private DNS path. That evidence means the read-only inspection directly tests the properties required at Require private application connectivity.
- ✗ **C. Run only this negative inspection for Require private application connectivity: The Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors; as an independent condition, consider it sufficient that an empty negative result reports every required positive property.** — The traceable checkpoint outcome is that the negative inspection. That evidence means absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Establish a logical server boundary and apply it to Require private application connectivity; before approval, take it as conclusive that any command from the same lane proves the current checkpoint.** — The failure model establishes that the positive inspection for Establish a logical server boundary. That evidence means it is lane-correct but proves Establish a logical server boundary, not Require private application connectivity.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q37 — answer C

The implementation review has reached 'Require private application connectivity'. A passing positive check does not by itself prove this negative assertion: The Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors. Which action produces the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Require private application connectivity and report full compliance. Next, rely on the belief that every prohibited parallel state must therefore be absent.** — The WAF consequence identifies that the application reaches the logical server through an approved private endpoint and private DNS path. That evidence means the positive result alone does not test the explicit anti-condition 'The Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors'.
- ✗ **B. Prove only that the Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors and report the intended configuration as present, and then proceed on the belief that absence is equivalent to positive-state evidence.** — The command-level assertion is anchored in the fact that the Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors. That evidence means absence evidence cannot demonstrate the required positive state 'The application reaches the logical server through an approved private endpoint and private DNS path'.
- ✓ **C. Verify the positive properties for Require private application connectivity. Next, independently verify that the Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors.** — The recovery guidance assumes that the application reaches the logical server through an approved private endpoint and private DNS path; The Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors. That evidence means two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **D. Use Configure an elastic serverless database's negative assertion for Require private application connectivity. Also, treat as decisive the assertion that negative assertions are interchangeable between checkpoints.** — a continuously provisioned premium or warehouse tier is not selected without a requirement. The resulting architectural conclusion is that the second assertion is valid for Configure an elastic serverless database but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q38 — answer B

The approach to 'Require private application connectivity' is challenged by database administration. The board wants the Well-Architected consequence of mitigating this risk: Private DNS resolves incorrectly or the endpoint connection remains pending. What best demonstrates the consequence attributable to this checkpoint?

- ✗ **A. Use the Validate the service-tier decision consequence as the result for Require private application connectivity; next, treat it as established that a pillar statement remains valid when moved away from Validate the service-tier decision.** — The authored acceptance boundary states that operational Excellence: configuration and usage evidence tie the deployed database back to the reviewed service decision. The resulting architectural conclusion is that that tradeoff belongs to Validate the service-tier decision and does not explain this checkpoint's decision.
- ✓ **B. Record this consequence: Reliability: private DNS and endpoint approval are explicit, independently testable application dependencies. As another control, tie it to LAB08-REQ-04.** — The controlling fact is that reliability: private DNS and endpoint approval are explicit, independently testable application dependencies. The resulting architectural conclusion is that it states the authored pillar consequence of the control evaluated at Require private application connectivity.
- ✗ **C. Remove the control responsible for the Require private application connectivity outcome. In addition, use as justification the claim that a moderate cost classification outweighs the mandatory architecture state.** — The relevant observation is that the required outcome at Require private application connectivity. The resulting architectural conclusion is that cost Optimization cannot remove the acceptance condition 'The application reaches the logical server through an approved private endpoint and private DNS path'.
- ✗ **D. Treat 'Reliability: private DNS and endpoint approval are explicit, independently testable application dependencies' as proof that all five pillars pass; before approval, accept without proof that the checkpoint 'Require private application connectivity' no longer needs its separate negative check.** — The checkpoint specifically records that the Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors. The resulting architectural conclusion is that one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q39 — answer B

A decision test for 'Require private application connectivity' includes information security. A material change now applies: The acquired application reveals a hard dependency on SQL Agent, cross-database transactions, and instance-level collation; revise the platform choice without treating a larger SQL Database tier as compatibility. Which option is the correct revision to the decision record?

- ✗ **A. Retain Azure SQL Database General Purpose serverless at Require private application connectivity without recalculating criteria or eligibility; as a second control, base approval on the claim that the original weighted result is permanent.** — The architecture evidence must show that azure SQL Database General Purpose serverless. The resulting architectural conclusion is that the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✓ **B. Re-score Azure SQL Database General Purpose serverless and both alternatives for Require private application connectivity. In addition, supersede the ADR using the changed evidence for LAB08-REQ-04.** — The scenario makes clear that azure SQL Database General Purpose serverless at Require private application connectivity. The resulting architectural conclusion is that the material change 'The acquired application reveals a hard dependency on SQL Agent, cross-database transactions, and instance-level collation; revise the platform choice without treating a larger SQL Database tier as compatibility.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **C. Select Azure SQL Managed Instance General Purpose for Require private application connectivity without rechecking its mandatory constraints. Then, use the premise that being different from the current design is an architecture criterion.** — The applicable design condition is that azure SQL Managed Instance General Purpose. The resulting architectural conclusion is that being different is not a criterion, and the candidate still must avoid the prohibited state at Require private application connectivity.
- ✗ **D. Keep Azure Database for PostgreSQL Flexible Server General Purpose eligible at Require private application connectivity by downgrading LAB08-REQ-04; afterward, consider it sufficient that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The review is governed by this fact: lAB08-REQ-04. The resulting architectural conclusion is that an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q40 — answer A

The architecture board reconsiders 'Require private application connectivity' with finOps. After a partial run, cleanup must follow this dependency: Delete private DNS records and endpoint connections before server cleanup; preserve shared zones. What should the architect select as the dependency-safe cleanup plan?

- ✓ **A. Verify exact run-state IDs and ownership tags for Require private application connectivity. Before sign-off, follow this dependency rule without purge: Delete private DNS records and endpoint connections before server cleanup; preserve shared zones.** — The retained result must be reconciled with the fact that delete private DNS records and endpoint connections before server cleanup; preserve shared zones. The resulting architectural conclusion is that exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **B. Apply the cleanup rule for Establish a logical server boundary before reconciling the current dependency. Also, rely on the claim that removing a parent needed to identify Require private application connectivity is harmless.** — The decision tension comes from the fact that delete databases and private endpoints before the run-owned logical server. The resulting architectural conclusion is that a cleanup rule for Establish a logical server boundary cannot override the dependency declared for Require private application connectivity.
- ✗ **C. Delete candidates by display name before comparing the Require private application connectivity ownership tags; in a separate step, rely on the belief that the dependency rule 'Delete private DNS records and endpoint connections before server cleanup; preserve shared zones' is optional.** — The safe operating boundary says that private endpoint ID, connection status, subnet ID, DNS zone label, and firewall-rule count. The resulting architectural conclusion is that names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Require private application connectivity negative assertion 'The Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors'. As another control, proceed on the belief that remaining command logs are sufficient recovery evidence.** — The traceable checkpoint outcome is that the Azure-services firewall bypass is absent and public access is not the recovery path for DNS errors. The resulting architectural conclusion is that irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q41 — answer C

A review of 'Validate the service-tier decision' begins with input from finOps. Approval requires a positive result plus this independent negative assertion: No reported database usage dimension is already at its service limit. Which choice should be approved as the acceptance rule that makes LAB08-REQ-05 testable?

- ✗ **A. Select Azure SQL Managed Instance General Purpose before checking Validate the service-tier decision; then accept without proof that a successful deployment will later prove the architecture constraint.** — The recovery guidance assumes that no reported database usage dimension is already at its service limit. The resulting architectural conclusion is that a deployment result cannot prove LAB08-REQ-05, and Azure SQL Managed Instance General Purpose still has to meet the mandatory boundary.
- ✗ **B. Use the passing result from Convert workload facts into platform criteria to approve Validate the service-tier decision. Independently, rely on the claim that one control establishes an unrelated acceptance boundary.** — The WAF consequence identifies that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. The resulting architectural conclusion is that that outcome belongs to Convert workload facts into platform criteria and leaves Validate the service-tier decision unverified.
- ✓ **C. Require the documented positive state for Validate the service-tier decision; then verify that no reported database usage dimension is already at its service limit.** — The failure model establishes that provisioned configuration matches the selected candidate and all mandatory compatibility and capacity requirements. The resulting architectural conclusion is that the positive state and an independent negative assertion jointly make LAB08-REQ-05 testable.
- ✗ **D. Choose Azure Database for PostgreSQL Flexible Server General Purpose and skip the Validate the service-tier decision negative assertion. Next, rely on the belief that the candidate has the lowest implementation effort.** — The command-level assertion is anchored in the fact that modernize the database with less operational toil and cost while retaining transactional correctness and month-end capacity. The resulting architectural conclusion is that implementation effort cannot justify skipping the negative assertion or displace LAB08-REQ-05.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q42 — answer D

'Validate the service-tier decision' awaits approval from application engineering. The selected architecture is Azure SQL Database General Purpose serverless; object existence alone is not success. What should the team use as the intended successful finding?

- ✗ **A. Use only the negative assertion 'No reported database usage dimension is already at its service limit' as the success result; as a separate check, consider it sufficient that absence proves every required positive property.** — The controlling fact is that no reported database usage dimension is already at its service limit. Under the stated constraint, this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Establish a logical server boundary as the result for Validate the service-tier decision. Afterward, take it as conclusive that a property from the current checkpoint does not need to be inspected.** — The authored acceptance boundary states that the logical server has a group-owned Microsoft Entra administrator and no SQL authentication dependency. Under the stated constraint, evidence for Establish a logical server boundary cannot substitute for the properties required at Validate the service-tier decision.
- ✗ **C. Record the failure condition 'Observed capacity demand contradicts the serverless cost or latency assumptions' as a successful state; next, treat it as established that the command returned an object.** — The relevant observation is that observed capacity demand contradicts the serverless cost or latency assumptions. Under the stated constraint, resource existence or command output does not convert the documented failure condition into success.
- ✓ **D. Record provisioned configuration matches the selected candidate and all mandatory compatibility and capacity requirements. Also, classify it as success for LAB08-REQ-05.** — provisioned configuration matches the selected candidate and all mandatory compatibility and capacity requirements. Under the stated constraint, this is the authored target state for Validate the service-tier decision and directly supports LAB08-REQ-05.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q43 — answer C

'Validate the service-tier decision' is reopened at the request of database administration. Evidence must address this risk without retaining credentials: Observed capacity demand contradicts the serverless cost or latency assumptions. Which option best establishes sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Configure an elastic serverless database for Validate the service-tier decision. Before sign-off, proceed on the belief that a related checkpoint proves the current expected state.** — The scenario makes clear that database label, edition, family, maximum and minimum vCores, autopause delay, and zone decision. Under the stated constraint, that evidence supports Configure an elastic serverless database, so it cannot demonstrate Provisioned configuration matches the selected candidate and all mandatory compatibility and capacity requirements.
- ✗ **B. Store unredacted Validate the service-tier decision output with operator, tenant, token, and request context; as an independent condition, treat as decisive the assertion that reproduction requires every captured field.** — The architecture evidence must show that unredacted implementation output. Under the stated constraint, identity, tenant, or token material exceeds the non-secret evidence contract.
- ✓ **C. Retain sKU, status, objective, capacity bounds, utilization assumptions, and selected-candidate traceability. Afterward, exclude credentials and unrelated response fields.** — The checkpoint specifically records that sKU, status, objective, capacity bounds, utilization assumptions, and selected-candidate traceability. Under the stated constraint, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **D. Record only the Validate the service-tier decision positive inspection's exit status; as a second control, base approval on the claim that projected properties and assertion results can be reconstructed later.** — The applicable design condition is that the positive inspection's exit status. Under the stated constraint, an exit code alone does not show whether provisioned configuration matches the selected candidate and all mandatory compatibility and capacity requirements.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q44 — answer B

A design review of 'Validate the service-tier decision' includes information security. The target is Provisioned configuration matches the selected candidate and all mandatory compatibility and capacity requirements, but the latest evidence does not show it. Which answer identifies the most likely cause?

- ✗ **A. Treat 'Private DNS resolves incorrectly or the endpoint connection remains pending' as grounds to reject Validate the service-tier decision. Next, use as justification the claim that require private application connectivity's failure model applies unchanged here.** — The retained result must be reconciled with the fact that private DNS resolves incorrectly or the endpoint connection remains pending. Under the stated constraint, that condition belongs to Require private application connectivity and does not by itself invalidate Azure SQL Database General Purpose serverless.
- ✓ **B. Investigate observed capacity demand contradicts the serverless cost or latency assumptions. Separately, isolate that cause before changing Azure SQL Database General Purpose serverless.** — The review is governed by this fact: observed capacity demand contradicts the serverless cost or latency assumptions. Under the stated constraint, it is the checkpoint's causal failure model and should be isolated before retrying Validate the service-tier decision.
- ✗ **C. Ignore the negative assertion 'No reported database usage dimension is already at its service limit', and then accept without proof that a later material change will make it unnecessary.** — The decision tension comes from the fact that no reported database usage dimension is already at its service limit. Under the stated constraint, the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Convert workload facts into platform criteria instead of diagnosing Validate the service-tier decision. Also, rely on the claim that a passing result at Convert workload facts into platform criteria identifies the current cause.** — The safe operating boundary says that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. Under the stated constraint, a passing result at Convert workload facts into platform criteria gives no causal evidence for the failure at Validate the service-tier decision.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q45 — answer A

The team asks finOps to assess 'Validate the service-tier decision'. The run encountered this modeled failure: Observed capacity demand contradicts the serverless cost or latency assumptions. What recommendation gives the reviewers the safest recovery action?

- ✓ **A. Re-run the decision matrix with measured demand and choose provisioned compute or another tier deliberately; for the recorded decision, preserve the current run identity and evidence.** — The traceable checkpoint outcome is that re-run the decision matrix with measured demand and choose provisioned compute or another tier deliberately. Under the stated constraint, it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **B. Perform cleanup immediately: Retain only sanitized configuration evidence, then follow database-to-server cleanup order; next, use the premise that the failed operation and its returned identifiers do not need reconciliation.** — The failure model establishes that retain only sanitized configuration evidence, then follow database-to-server cleanup order. Under the stated constraint, cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **C. Create a different run identity before diagnosing 'Observed capacity demand contradicts the serverless cost or latency assumptions'. In addition, consider it sufficient that the first state record and returned identifiers can be discarded.** — The recovery guidance assumes that observed capacity demand contradicts the serverless cost or latency assumptions. Under the stated constraint, discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Convert workload facts into platform criteria instead; before approval, take it as conclusive that success at Convert workload facts into platform criteria will repair the failed state at Validate the service-tier decision.** — The WAF consequence identifies that compatibility, transaction, scale, latency, maintenance, and cost facts map to supported current service tiers. Under the stated constraint, altering an already separate checkpoint does not repair the modeled failure at Validate the service-tier decision.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q46 — answer A

A recommendation on 'Validate the service-tier decision' is requested by application engineering. Without making a new change, the team must inspect the risk 'Observed capacity demand contradicts the serverless cost or latency assumptions' using the Azure CLI lane. Which action produces the read-only, lane-correct inspection?

- ✓ **A. Inspect the documented properties for Validate the service-tier decision. Independently, retain this evidence: sKU, status, objective, capacity bounds, utilization assumptions, and selected-candidate traceability.** — The command-level assertion is anchored in the fact that provisioned configuration matches the selected candidate and all mandatory compatibility and capacity requirements. Under the stated constraint, the read-only inspection directly tests the properties required at Validate the service-tier decision.
- ✗ **B. Rerun the Validate the service-tier decision implementation command and infer the expected state; during the same review, rely on the belief that absence of a shell error proves every property.** — the implementation command. This matters because it can mutate state and shell success does not independently assert the expected properties.
- ✗ **C. Run only this negative inspection for Validate the service-tier decision: No reported database usage dimension is already at its service limit. Then, proceed on the belief that an empty negative result reports every required positive property.** — The controlling fact is that the negative inspection. This matters because absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Establish a logical server boundary and apply it to Validate the service-tier decision; afterward, treat as decisive the assertion that any command from the same lane proves the current checkpoint.** — The authored acceptance boundary states that the positive inspection for Establish a logical server boundary. This matters because it is lane-correct but proves Establish a logical server boundary, not Validate the service-tier decision.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q47 — answer D

'Validate the service-tier decision' is assigned to database administration. A passing positive check does not by itself prove this negative assertion: No reported database usage dimension is already at its service limit. What best demonstrates the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Validate the service-tier decision and report full compliance. Also, treat it as established that every prohibited parallel state must therefore be absent.** — The checkpoint specifically records that provisioned configuration matches the selected candidate and all mandatory compatibility and capacity requirements. This matters because the positive result alone does not test the explicit anti-condition 'No reported database usage dimension is already at its service limit'.
- ✗ **B. Prove only that no reported database usage dimension is already at its service limit and report the intended configuration as present; in a separate step, use as justification the claim that absence is equivalent to positive-state evidence.** — The scenario makes clear that no reported database usage dimension is already at its service limit. This matters because absence evidence cannot demonstrate the required positive state 'Provisioned configuration matches the selected candidate and all mandatory compatibility and capacity requirements'.
- ✗ **C. Use Configure an elastic serverless database's negative assertion for Validate the service-tier decision. As another control, accept without proof that negative assertions are interchangeable between checkpoints.** — The architecture evidence must show that a continuously provisioned premium or warehouse tier is not selected without a requirement. This matters because the second assertion is valid for Configure an elastic serverless database but leaves this checkpoint's prohibited state untested.
- ✓ **D. Verify the positive properties for Validate the service-tier decision; in a separate step, independently verify that no reported database usage dimension is already at its service limit.** — The relevant observation is that provisioned configuration matches the selected candidate and all mandatory compatibility and capacity requirements; No reported database usage dimension is already at its service limit. This matters because two independent observations prevent a passing positive check from concealing an unsafe parallel state.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q48 — answer B

An assurance review of 'Validate the service-tier decision' includes information security. The board wants the Well-Architected consequence of mitigating this risk: Observed capacity demand contradicts the serverless cost or latency assumptions. Which option is the consequence attributable to this checkpoint?

- ✗ **A. Use the Require private application connectivity consequence as the result for Validate the service-tier decision; before approval, base approval on the claim that a pillar statement remains valid when moved away from Require private application connectivity.** — The review is governed by this fact: reliability: private DNS and endpoint approval are explicit, independently testable application dependencies. This matters because that tradeoff belongs to Require private application connectivity and does not explain this checkpoint's decision.
- ✓ **B. Record this consequence: Operational Excellence: configuration and usage evidence tie the deployed database back to the reviewed service decision; next, tie it to LAB08-REQ-05.** — The applicable design condition is that operational Excellence: configuration and usage evidence tie the deployed database back to the reviewed service decision. This matters because it states the authored pillar consequence of the control evaluated at Validate the service-tier decision.
- ✗ **C. Remove the control responsible for the Validate the service-tier decision outcome. Separately, use the premise that a moderate cost classification outweighs the mandatory architecture state.** — The retained result must be reconciled with the fact that the required outcome at Validate the service-tier decision. This matters because cost Optimization cannot remove the acceptance condition 'Provisioned configuration matches the selected candidate and all mandatory compatibility and capacity requirements'.
- ✗ **D. Treat 'Operational Excellence: configuration and usage evidence tie the deployed database back to the reviewed service decision' as proof that all five pillars pass; for this decision, consider it sufficient that the checkpoint 'Validate the service-tier decision' no longer needs its separate negative check.** — The decision tension comes from the fact that no reported database usage dimension is already at its service limit. This matters because one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q49 — answer C

Approval of 'Validate the service-tier decision' is questioned by finOps. A material change now applies: The acquired application reveals a hard dependency on SQL Agent, cross-database transactions, and instance-level collation; revise the platform choice without treating a larger SQL Database tier as compatibility. What should the architect select as the correct revision to the decision record?

- ✗ **A. Retain Azure SQL Database General Purpose serverless at Validate the service-tier decision without recalculating criteria or eligibility; afterward, rely on the claim that the original weighted result is permanent.** — The traceable checkpoint outcome is that azure SQL Database General Purpose serverless. This matters because the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Azure SQL Managed Instance General Purpose for Validate the service-tier decision without rechecking its mandatory constraints; then rely on the belief that being different from the current design is an architecture criterion.** — The failure model establishes that azure SQL Managed Instance General Purpose. This matters because being different is not a criterion, and the candidate still must avoid the prohibited state at Validate the service-tier decision.
- ✓ **C. Re-score Azure SQL Database General Purpose serverless and both alternatives for Validate the service-tier decision; for this decision, supersede the ADR using the changed evidence for LAB08-REQ-05.** — The safe operating boundary says that azure SQL Database General Purpose serverless at Validate the service-tier decision. This matters because the material change 'The acquired application reveals a hard dependency on SQL Agent, cross-database transactions, and instance-level collation; revise the platform choice without treating a larger SQL Database tier as compatibility.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **D. Keep Azure Database for PostgreSQL Flexible Server General Purpose eligible at Validate the service-tier decision by downgrading LAB08-REQ-05. Independently, proceed on the belief that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The recovery guidance assumes that lAB08-REQ-05. This matters because an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)

## LAB08-Q50 — answer B

The implementation review has reached 'Validate the service-tier decision'. After a partial run, cleanup must follow this dependency: Retain only sanitized configuration evidence, then follow database-to-server cleanup order. Select the dependency-safe cleanup plan.

- ✗ **A. Apply the cleanup rule for Establish a logical server boundary before reconciling the current dependency. As another control, take it as conclusive that removing a parent needed to identify Validate the service-tier decision is harmless.** — The command-level assertion is anchored in the fact that delete databases and private endpoints before the run-owned logical server. This matters because a cleanup rule for Establish a logical server boundary cannot override the dependency declared for Validate the service-tier decision.
- ✓ **B. Verify exact run-state IDs and ownership tags for Validate the service-tier decision. Then, follow this dependency rule without purge: Retain only sanitized configuration evidence, then follow database-to-server cleanup order.** — The WAF consequence identifies that retain only sanitized configuration evidence, then follow database-to-server cleanup order. This matters because exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **C. Delete candidates by display name before comparing the Validate the service-tier decision ownership tags; as a separate check, treat it as established that the dependency rule 'Retain only sanitized configuration evidence, then follow database-to-server cleanup order' is optional.** — sKU, status, objective, capacity bounds, utilization assumptions, and selected-candidate traceability. The checkpoint therefore requires that names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Validate the service-tier decision negative assertion 'No reported database usage dimension is already at its service limit'. Afterward, use as justification the claim that remaining command logs are sufficient recovery evidence.** — The controlling fact is that no reported database usage dimension is already at its service limit. The checkpoint therefore requires that irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/architecture/guide/technology-choices/data-stores-getting-started (verified 2026-09-02)
<!-- END GENERATED AZ305 V1 -->
