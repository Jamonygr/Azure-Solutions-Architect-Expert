<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-11 answer key

Use after completing the learner assessment. Every choice has a specific explanation.

## LAB11-Q01 — answer B

'Match service semantics to access patterns' is assigned to analytics consumers. Approval requires a positive result plus this independent negative assertion: SMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload. Which choice gives the team the acceptance rule that makes LAB11-REQ-01 testable?

- ✗ **A. Select Flat Azure Blob Storage containers with prefix conventions before checking Match service semantics to access patterns, and then accept without proof that a successful deployment will later prove the architecture constraint.** — The traceable checkpoint outcome is that sMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload. In the decision record, a deployment result cannot prove LAB11-REQ-01, and Flat Azure Blob Storage containers with prefix conventions still has to meet the mandatory boundary.
- ✓ **B. Require the documented positive state for Match service semantics to access patterns. Before sign-off, verify that sMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload.** — The safe operating boundary says that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. In the decision record, the positive state and an independent negative assertion jointly make LAB11-REQ-01 testable.
- ✗ **C. Use the passing result from Create a hierarchical namespace boundary to approve Match service semantics to access patterns. Also, rely on the claim that one control establishes an unrelated acceptance boundary.** — The failure model establishes that the account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags. In the decision record, that outcome belongs to Create a hierarchical namespace boundary and leaves Match service semantics to access patterns unverified.
- ✗ **D. Choose Azure Files shares mounted by analytics and document clients and skip the Match service semantics to access patterns negative assertion; in a separate step, rely on the belief that the candidate has the lowest implementation effort.** — The recovery guidance assumes that consolidate unstructured content for governed analytics while preserving scalable access and clear ownership. In the decision record, implementation effort cannot justify skipping the negative assertion or displace LAB11-REQ-01.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q02 — answer A

An assurance review of 'Match service semantics to access patterns' includes information security. The selected architecture is ADLS Gen2 on a hierarchical-namespace StorageV2 account; object existence alone is not success. What is the intended successful finding?

- ✓ **A. Record object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace; afterward, classify it as success for LAB11-REQ-01.** — The WAF consequence identifies that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. In the decision record, this is the authored target state for Match service semantics to access patterns and directly supports LAB11-REQ-01.
- ✗ **B. Use only the negative assertion 'SMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload' as the success result. In addition, consider it sufficient that absence proves every required positive property.** — The command-level assertion is anchored in the fact that sMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload. In the decision record, this is the independent prohibited-state assertion, not a successful finding.
- ✗ **C. Use the successful finding from Design filesystem and directory ownership as the result for Match service semantics to access patterns; before approval, take it as conclusive that a property from the current checkpoint does not need to be inspected.** — filesystems represent durable data-product boundaries and directories have group-owned default and access ACLs. The independent assertion shows why evidence for Design filesystem and directory ownership cannot substitute for the properties required at Match service semantics to access patterns.
- ✗ **D. Record the failure condition 'A consumer has a mandatory SMB or NFS behavior not supported by the selected endpoint design' as a successful state. Separately, treat it as established that the command returned an object.** — The controlling fact is that a consumer has a mandatory SMB or NFS behavior not supported by the selected endpoint design. The independent assertion shows why resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q03 — answer D

Approval of 'Match service semantics to access patterns' is questioned by data platform engineering. Evidence must address this risk without retaining credentials: A consumer has a mandatory SMB or NFS behavior not supported by the selected endpoint design. Which recommendation supplies sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Define encryption and key dependency for Match service semantics to access patterns. Then, proceed on the belief that a related checkpoint proves the current expected state.** — The relevant observation is that encryption services, key-source class, identity type, non-secret vault reference, and rotation owner. The independent assertion shows why that evidence supports Define encryption and key dependency, so it cannot demonstrate Object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace.
- ✗ **B. Store unredacted Match service semantics to access patterns output with operator, tenant, token, and request context; afterward, treat as decisive the assertion that reproduction requires every captured field.** — The checkpoint specifically records that unredacted implementation output. The independent assertion shows why identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **C. Record only the Match service semantics to access patterns positive inspection's exit status; then base approval on the claim that projected properties and assertion results can be reconstructed later.** — The scenario makes clear that the positive inspection's exit status. The independent assertion shows why an exit code alone does not show whether object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace.
- ✓ **D. Retain data classes, object-size distribution, protocol needs, namespace choice, and service-fit matrix, and then exclude credentials and unrelated response fields.** — The authored acceptance boundary states that data classes, object-size distribution, protocol needs, namespace choice, and service-fit matrix. The independent assertion shows why it captures the checkpoint's observable properties while keeping the evidence boundary narrow.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q04 — answer C

The implementation review has reached 'Match service semantics to access patterns'. The target is Object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace, but the latest evidence does not show it. Choose the most likely cause.

- ✗ **A. Treat 'Only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently' as grounds to reject Match service semantics to access patterns; in a separate step, use as justification the claim that validate private endpoint access's failure model applies unchanged here.** — The applicable design condition is that only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently. The independent assertion shows why that condition belongs to Validate private endpoint access and does not by itself invalidate ADLS Gen2 on a hierarchical-namespace StorageV2 account.
- ✗ **B. Ignore the negative assertion 'SMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload'. As another control, accept without proof that a later material change will make it unnecessary.** — The review is governed by this fact: sMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload. The independent assertion shows why the negative assertion must be evaluated now, independent of a later business change.
- ✓ **C. Investigate a consumer has a mandatory SMB or NFS behavior not supported by the selected endpoint design; as a separate check, isolate that cause before changing ADLS Gen2 on a hierarchical-namespace StorageV2 account.** — The architecture evidence must show that a consumer has a mandatory SMB or NFS behavior not supported by the selected endpoint design. The independent assertion shows why it is the checkpoint's causal failure model and should be isolated before retrying Match service semantics to access patterns.
- ✗ **D. Investigate Create a hierarchical namespace boundary instead of diagnosing Match service semantics to access patterns; as a separate check, rely on the claim that a passing result at Create a hierarchical namespace boundary identifies the current cause.** — The retained result must be reconciled with the fact that the account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags. The independent assertion shows why a passing result at Create a hierarchical namespace boundary gives no causal evidence for the failure at Match service semantics to access patterns.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q05 — answer D

The approach to 'Match service semantics to access patterns' is challenged by analytics consumers. The run encountered this modeled failure: A consumer has a mandatory SMB or NFS behavior not supported by the selected endpoint design. Which answer describes the safest recovery action?

- ✗ **A. Perform cleanup immediately: This selection checkpoint is read-only; subsequent cleanup follows filesystem-to-account order. Separately, use the premise that the failed operation and its returned identifiers do not need reconciliation.** — The safe operating boundary says that this selection checkpoint is read-only; subsequent cleanup follows filesystem-to-account order. The independent assertion shows why cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **B. Create a different run identity before diagnosing 'A consumer has a mandatory SMB or NFS behavior not supported by the selected endpoint design'; for this decision, consider it sufficient that the first state record and returned identifiers can be discarded.** — The traceable checkpoint outcome is that a consumer has a mandatory SMB or NFS behavior not supported by the selected endpoint design. The independent assertion shows why discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **C. Change Create a hierarchical namespace boundary instead. Before sign-off, take it as conclusive that success at Create a hierarchical namespace boundary will repair the failed state at Match service semantics to access patterns.** — The failure model establishes that the account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags. The independent assertion shows why altering an already separate checkpoint does not repair the modeled failure at Match service semantics to access patterns.
- ✓ **D. Isolate that data class and evaluate Azure Files rather than forcing one service across incompatible protocols; before approval, preserve the current run identity and evidence.** — The decision tension comes from the fact that isolate that data class and evaluate Azure Files rather than forcing one service across incompatible protocols. The independent assertion shows why it corrects the narrow cause while retaining the same recovery trail and decision scope.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q06 — answer C

A decision test for 'Match service semantics to access patterns' includes information security. Without making a new change, the team must inspect the risk 'A consumer has a mandatory SMB or NFS behavior not supported by the selected endpoint design' using the Azure PowerShell lane. What should be recorded as the read-only, lane-correct inspection?

- ✗ **A. Rerun the Match service semantics to access patterns implementation command and infer the expected state; then rely on the belief that absence of a shell error proves every property.** — The WAF consequence identifies that the implementation command. The independent assertion shows why it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Match service semantics to access patterns: SMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload. Independently, proceed on the belief that an empty negative result reports every required positive property.** — The command-level assertion is anchored in the fact that the negative inspection. The independent assertion shows why absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✓ **C. Inspect the documented properties for Match service semantics to access patterns; as an independent condition, retain this evidence: data classes, object-size distribution, protocol needs, namespace choice, and service-fit matrix.** — The recovery guidance assumes that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. The independent assertion shows why the read-only inspection directly tests the properties required at Match service semantics to access patterns.
- ✗ **D. Run the positive inspection for Design filesystem and directory ownership and apply it to Match service semantics to access patterns. Next, treat as decisive the assertion that any command from the same lane proves the current checkpoint.** — the positive inspection for Design filesystem and directory ownership. Operationally, it is lane-correct but proves Design filesystem and directory ownership, not Match service semantics to access patterns.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q07 — answer A

The architecture board reconsiders 'Match service semantics to access patterns' with data platform engineering. A passing positive check does not by itself prove this negative assertion: SMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload. Which proposal supplies the assertion pair that proves both conditions independently?

- ✓ **A. Verify the positive properties for Match service semantics to access patterns; then independently verify that sMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload.** — The controlling fact is that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace; SMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload. Operationally, two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **B. Verify only the positive result for Match service semantics to access patterns and report full compliance; as a separate check, treat it as established that every prohibited parallel state must therefore be absent.** — The authored acceptance boundary states that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. Operationally, the positive result alone does not test the explicit anti-condition 'SMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload'.
- ✗ **C. Prove only that sMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload and report the intended configuration as present. Afterward, use as justification the claim that absence is equivalent to positive-state evidence.** — The relevant observation is that sMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload. Operationally, absence evidence cannot demonstrate the required positive state 'Object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace'.
- ✗ **D. Use Define encryption and key dependency's negative assertion for Match service semantics to access patterns; next, accept without proof that negative assertions are interchangeable between checkpoints.** — The checkpoint specifically records that a customer-managed key is not referenced without an identity capable of unwrapping it. Operationally, the second assertion is valid for Define encryption and key dependency but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q08 — answer D

A review of 'Match service semantics to access patterns' begins with input from supplier integration team. The board wants the Well-Architected consequence of mitigating this risk: A consumer has a mandatory SMB or NFS behavior not supported by the selected endpoint design. Which option best represents the consequence attributable to this checkpoint?

- ✗ **A. Use the Validate private endpoint access consequence as the result for Match service semantics to access patterns. Before sign-off, base approval on the claim that a pillar statement remains valid when moved away from Validate private endpoint access.** — The architecture evidence must show that security: denied public access and explicit dfs connectivity constrain unintended data paths. Operationally, that tradeoff belongs to Validate private endpoint access and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Match service semantics to access patterns outcome; as an independent condition, use the premise that a moderate cost classification outweighs the mandatory architecture state.** — The applicable design condition is that the required outcome at Match service semantics to access patterns. Operationally, cost Optimization cannot remove the acceptance condition 'Object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace'.
- ✗ **C. Treat 'Performance Efficiency: hierarchical namespace semantics align directory operations with analytics access patterns' as proof that all five pillars pass; before closing the checkpoint, consider it sufficient that the checkpoint 'Match service semantics to access patterns' no longer needs its separate negative check.** — The review is governed by this fact: sMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload. Operationally, one positive command cannot establish every pillar, especially while the negative state remains unchecked.
- ✓ **D. Record this consequence: Performance Efficiency: hierarchical namespace semantics align directory operations with analytics access patterns. Also, tie it to LAB11-REQ-01.** — The scenario makes clear that performance Efficiency: hierarchical namespace semantics align directory operations with analytics access patterns. Operationally, it states the authored pillar consequence of the control evaluated at Match service semantics to access patterns.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q09 — answer D

'Match service semantics to access patterns' awaits approval from analytics consumers. A material change now applies: The legal department introduces collaborative document shares that require native SMB locking and Windows ACL behavior, but analytics ingestion must remain object-native; revise the service boundaries. Which course of action provides the correct revision to the decision record?

- ✗ **A. Retain ADLS Gen2 on a hierarchical-namespace StorageV2 account at Match service semantics to access patterns without recalculating criteria or eligibility. Next, rely on the claim that the original weighted result is permanent.** — The decision tension comes from the fact that aDLS Gen2 on a hierarchical-namespace StorageV2 account. Operationally, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Flat Azure Blob Storage containers with prefix conventions for Match service semantics to access patterns without rechecking its mandatory constraints, and then rely on the belief that being different from the current design is an architecture criterion.** — The safe operating boundary says that flat Azure Blob Storage containers with prefix conventions. Operationally, being different is not a criterion, and the candidate still must avoid the prohibited state at Match service semantics to access patterns.
- ✗ **C. Keep Azure Files shares mounted by analytics and document clients eligible at Match service semantics to access patterns by downgrading LAB11-REQ-01. Also, proceed on the belief that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The traceable checkpoint outcome is that lAB11-REQ-01. Operationally, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.
- ✓ **D. Re-score ADLS Gen2 on a hierarchical-namespace StorageV2 account and both alternatives for Match service semantics to access patterns. Afterward, supersede the ADR using the changed evidence for LAB11-REQ-01.** — The retained result must be reconciled with the fact that aDLS Gen2 on a hierarchical-namespace StorageV2 account at Match service semantics to access patterns. Operationally, the material change 'The legal department introduces collaborative document shares that require native SMB locking and Windows ACL behavior, but analytics ingestion must remain object-native; revise the service boundaries.' requires fresh eligibility, weighted analysis, and a superseding decision.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q10 — answer A

'Match service semantics to access patterns' is reopened at the request of information security. After a partial run, cleanup must follow this dependency: This selection checkpoint is read-only; subsequent cleanup follows filesystem-to-account order. Which finding constitutes the dependency-safe cleanup plan?

- ✓ **A. Verify exact run-state IDs and ownership tags for Match service semantics to access patterns. Separately, follow this dependency rule without purge: This selection checkpoint is read-only; subsequent cleanup follows filesystem-to-account order.** — The failure model establishes that this selection checkpoint is read-only; subsequent cleanup follows filesystem-to-account order. Operationally, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **B. Apply the cleanup rule for Design filesystem and directory ownership before reconciling the current dependency; next, take it as conclusive that removing a parent needed to identify Match service semantics to access patterns is harmless.** — The recovery guidance assumes that remove child paths before filesystems and retain no file content as evidence. Operationally, a cleanup rule for Design filesystem and directory ownership cannot override the dependency declared for Match service semantics to access patterns.
- ✗ **C. Delete candidates by display name before comparing the Match service semantics to access patterns ownership tags. In addition, treat it as established that the dependency rule 'This selection checkpoint is read-only; subsequent cleanup follows filesystem-to-account order' is optional.** — The WAF consequence identifies that data classes, object-size distribution, protocol needs, namespace choice, and service-fit matrix. Operationally, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Match service semantics to access patterns negative assertion 'SMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload'; before approval, use as justification the claim that remaining command logs are sufficient recovery evidence.** — The command-level assertion is anchored in the fact that sMB semantics or arbitrary relational queries are not claimed for the selected data-lake workload. Operationally, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-1](../README.md#checkpoint-1)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q11 — answer A

A design review of 'Create a hierarchical namespace boundary' includes information security. Approval requires a positive result plus this independent negative assertion: Public containers and Shared Key dependence are not accepted for workload access. What is the acceptance rule that makes LAB11-REQ-02 testable?

- ✓ **A. Require the documented positive state for Create a hierarchical namespace boundary. Then, verify that public containers and Shared Key dependence are not accepted for workload access.** — the account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags. The requirement-to-evidence link establishes that the positive state and an independent negative assertion jointly make LAB11-REQ-02 testable.
- ✗ **B. Select Flat Azure Blob Storage containers with prefix conventions before checking Create a hierarchical namespace boundary; in a separate step, consider it sufficient that a successful deployment will later prove the architecture constraint.** — The controlling fact is that public containers and Shared Key dependence are not accepted for workload access. The requirement-to-evidence link establishes that a deployment result cannot prove LAB11-REQ-02, and Flat Azure Blob Storage containers with prefix conventions still has to meet the mandatory boundary.
- ✗ **C. Use the passing result from Match service semantics to access patterns to approve Create a hierarchical namespace boundary. As another control, take it as conclusive that one control establishes an unrelated acceptance boundary.** — The authored acceptance boundary states that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. The requirement-to-evidence link establishes that that outcome belongs to Match service semantics to access patterns and leaves Create a hierarchical namespace boundary unverified.
- ✗ **D. Choose Azure Files shares mounted by analytics and document clients and skip the Create a hierarchical namespace boundary negative assertion; as a separate check, treat it as established that the candidate has the lowest implementation effort.** — The relevant observation is that consolidate unstructured content for governed analytics while preserving scalable access and clear ownership. The requirement-to-evidence link establishes that implementation effort cannot justify skipping the negative assertion or displace LAB11-REQ-02.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q12 — answer B

The team asks data platform engineering to assess 'Create a hierarchical namespace boundary'. The selected architecture is ADLS Gen2 on a hierarchical-namespace StorageV2 account; object existence alone is not success. Which recommendation supplies the intended successful finding?

- ✗ **A. Use only the negative assertion 'Public containers and Shared Key dependence are not accepted for workload access' as the success result. Separately, proceed on the belief that absence proves every required positive property.** — The scenario makes clear that public containers and Shared Key dependence are not accepted for workload access. The requirement-to-evidence link establishes that this is the independent prohibited-state assertion, not a successful finding.
- ✓ **B. Record the account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags. Next, classify it as success for LAB11-REQ-02.** — The checkpoint specifically records that the account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags. The requirement-to-evidence link establishes that this is the authored target state for Create a hierarchical namespace boundary and directly supports LAB11-REQ-02.
- ✗ **C. Use the successful finding from Design filesystem and directory ownership as the result for Create a hierarchical namespace boundary; for this decision, treat as decisive the assertion that a property from the current checkpoint does not need to be inspected.** — The architecture evidence must show that filesystems represent durable data-product boundaries and directories have group-owned default and access ACLs. The requirement-to-evidence link establishes that evidence for Design filesystem and directory ownership cannot substitute for the properties required at Create a hierarchical namespace boundary.
- ✗ **D. Record the failure condition 'Hierarchical namespace cannot be enabled after an incompatible account was already created' as a successful state. Before sign-off, base approval on the claim that the command returned an object.** — The applicable design condition is that hierarchical namespace cannot be enabled after an incompatible account was already created. The requirement-to-evidence link establishes that resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q13 — answer B

A recommendation on 'Create a hierarchical namespace boundary' is requested by supplier integration team. Evidence must address this risk without retaining credentials: Hierarchical namespace cannot be enabled after an incompatible account was already created. Choose sufficient, properly scoped evidence.

- ✗ **A. Substitute the evidence from Define encryption and key dependency for Create a hierarchical namespace boundary; then use as justification the claim that a related checkpoint proves the current expected state.** — The retained result must be reconciled with the fact that encryption services, key-source class, identity type, non-secret vault reference, and rotation owner. The requirement-to-evidence link establishes that that evidence supports Define encryption and key dependency, so it cannot demonstrate The account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags.
- ✓ **B. Retain account name, kind, namespace state, TLS version, public-access state, SKU, and ownership tags. As another control, exclude credentials and unrelated response fields.** — The review is governed by this fact: account name, kind, namespace state, TLS version, public-access state, SKU, and ownership tags. The requirement-to-evidence link establishes that it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **C. Store unredacted Create a hierarchical namespace boundary output with operator, tenant, token, and request context. Independently, accept without proof that reproduction requires every captured field.** — The decision tension comes from the fact that unredacted implementation output. The requirement-to-evidence link establishes that identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **D. Record only the Create a hierarchical namespace boundary positive inspection's exit status. Next, rely on the claim that projected properties and assertion results can be reconstructed later.** — The safe operating boundary says that the positive inspection's exit status. The requirement-to-evidence link establishes that an exit code alone does not show whether the account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q14 — answer D

'Create a hierarchical namespace boundary' is assigned to analytics consumers. The target is The account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags, but the latest evidence does not show it. Which answer describes the most likely cause?

- ✗ **A. Treat 'Only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently' as grounds to reject Create a hierarchical namespace boundary; as a separate check, use the premise that validate private endpoint access's failure model applies unchanged here.** — The failure model establishes that only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently. The requirement-to-evidence link establishes that that condition belongs to Validate private endpoint access and does not by itself invalidate ADLS Gen2 on a hierarchical-namespace StorageV2 account.
- ✗ **B. Ignore the negative assertion 'Public containers and Shared Key dependence are not accepted for workload access'. Afterward, consider it sufficient that a later material change will make it unnecessary.** — The recovery guidance assumes that public containers and Shared Key dependence are not accepted for workload access. The requirement-to-evidence link establishes that the negative assertion must be evaluated now, independent of a later business change.
- ✗ **C. Investigate Match service semantics to access patterns instead of diagnosing Create a hierarchical namespace boundary; next, take it as conclusive that a passing result at Match service semantics to access patterns identifies the current cause.** — The WAF consequence identifies that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. The requirement-to-evidence link establishes that a passing result at Match service semantics to access patterns gives no causal evidence for the failure at Create a hierarchical namespace boundary.
- ✓ **D. Investigate hierarchical namespace cannot be enabled after an incompatible account was already created. In addition, isolate that cause before changing ADLS Gen2 on a hierarchical-namespace StorageV2 account.** — The traceable checkpoint outcome is that hierarchical namespace cannot be enabled after an incompatible account was already created. The requirement-to-evidence link establishes that it is the checkpoint's causal failure model and should be isolated before retrying Create a hierarchical namespace boundary.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q15 — answer A

An assurance review of 'Create a hierarchical namespace boundary' includes information security. The run encountered this modeled failure: Hierarchical namespace cannot be enabled after an incompatible account was already created. What should be recorded as the safest recovery action?

- ✓ **A. Stop before data ingestion, create a correctly designed account, and migrate only synthetic lab data. Before sign-off, preserve the current run identity and evidence.** — The command-level assertion is anchored in the fact that stop before data ingestion, create a correctly designed account, and migrate only synthetic lab data. The requirement-to-evidence link establishes that it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **B. Perform cleanup immediately: Delete run-owned filesystems and private endpoints before deleting the account. Before sign-off, rely on the belief that the failed operation and its returned identifiers do not need reconciliation.** — delete run-owned filesystems and private endpoints before deleting the account. Consequently, cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **C. Create a different run identity before diagnosing 'Hierarchical namespace cannot be enabled after an incompatible account was already created'; as an independent condition, proceed on the belief that the first state record and returned identifiers can be discarded.** — The controlling fact is that hierarchical namespace cannot be enabled after an incompatible account was already created. Consequently, discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Match service semantics to access patterns instead; for the final assessment, treat as decisive the assertion that success at Match service semantics to access patterns will repair the failed state at Create a hierarchical namespace boundary.** — The authored acceptance boundary states that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. Consequently, altering an already separate checkpoint does not repair the modeled failure at Create a hierarchical namespace boundary.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q16 — answer C

Approval of 'Create a hierarchical namespace boundary' is questioned by data platform engineering. Without making a new change, the team must inspect the risk 'Hierarchical namespace cannot be enabled after an incompatible account was already created' using the Azure PowerShell lane. Which proposal supplies the read-only, lane-correct inspection?

- ✗ **A. Rerun the Create a hierarchical namespace boundary implementation command and infer the expected state. Next, treat it as established that absence of a shell error proves every property.** — The checkpoint specifically records that the implementation command. Consequently, it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Create a hierarchical namespace boundary: Public containers and Shared Key dependence are not accepted for workload access, and then use as justification the claim that an empty negative result reports every required positive property.** — The scenario makes clear that the negative inspection. Consequently, absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✓ **C. Inspect the documented properties for Create a hierarchical namespace boundary; afterward, retain this evidence: account name, kind, namespace state, TLS version, public-access state, SKU, and ownership tags.** — The relevant observation is that the account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags. Consequently, the read-only inspection directly tests the properties required at Create a hierarchical namespace boundary.
- ✗ **D. Run the positive inspection for Design filesystem and directory ownership and apply it to Create a hierarchical namespace boundary. Also, accept without proof that any command from the same lane proves the current checkpoint.** — The architecture evidence must show that the positive inspection for Design filesystem and directory ownership. Consequently, it is lane-correct but proves Design filesystem and directory ownership, not Create a hierarchical namespace boundary.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q17 — answer C

The implementation review has reached 'Create a hierarchical namespace boundary'. A passing positive check does not by itself prove this negative assertion: Public containers and Shared Key dependence are not accepted for workload access. Which option best represents the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Create a hierarchical namespace boundary and report full compliance; next, base approval on the claim that every prohibited parallel state must therefore be absent.** — The review is governed by this fact: the account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags. Consequently, the positive result alone does not test the explicit anti-condition 'Public containers and Shared Key dependence are not accepted for workload access'.
- ✗ **B. Prove only that public containers and Shared Key dependence are not accepted for workload access and report the intended configuration as present. In addition, use the premise that absence is equivalent to positive-state evidence.** — The retained result must be reconciled with the fact that public containers and Shared Key dependence are not accepted for workload access. Consequently, absence evidence cannot demonstrate the required positive state 'The account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags'.
- ✓ **C. Verify the positive properties for Create a hierarchical namespace boundary, and then independently verify that public containers and Shared Key dependence are not accepted for workload access.** — The applicable design condition is that the account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags; Public containers and Shared Key dependence are not accepted for workload access. Consequently, two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **D. Use Define encryption and key dependency's negative assertion for Create a hierarchical namespace boundary; before approval, consider it sufficient that negative assertions are interchangeable between checkpoints.** — The decision tension comes from the fact that a customer-managed key is not referenced without an identity capable of unwrapping it. Consequently, the second assertion is valid for Define encryption and key dependency but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q18 — answer A

The approach to 'Create a hierarchical namespace boundary' is challenged by analytics consumers. The board wants the Well-Architected consequence of mitigating this risk: Hierarchical namespace cannot be enabled after an incompatible account was already created. Which course of action provides the consequence attributable to this checkpoint?

- ✓ **A. Record this consequence: Reliability: choosing hierarchical namespace before ingestion avoids a disruptive late account migration; as a separate check, tie it to LAB11-REQ-02.** — The safe operating boundary says that reliability: choosing hierarchical namespace before ingestion avoids a disruptive late account migration. Consequently, it states the authored pillar consequence of the control evaluated at Create a hierarchical namespace boundary.
- ✗ **B. Use the Validate private endpoint access consequence as the result for Create a hierarchical namespace boundary; separately, rely on the claim that a pillar statement remains valid when moved away from Validate private endpoint access.** — The traceable checkpoint outcome is that security: denied public access and explicit dfs connectivity constrain unintended data paths. Consequently, that tradeoff belongs to Validate private endpoint access and does not explain this checkpoint's decision.
- ✗ **C. Remove the control responsible for the Create a hierarchical namespace boundary outcome. Then, rely on the belief that a moderate cost classification outweighs the mandatory architecture state.** — The failure model establishes that the required outcome at Create a hierarchical namespace boundary. Consequently, cost Optimization cannot remove the acceptance condition 'The account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags'.
- ✗ **D. Treat 'Reliability: choosing hierarchical namespace before ingestion avoids a disruptive late account migration' as proof that all five pillars pass; afterward, proceed on the belief that the checkpoint 'Create a hierarchical namespace boundary' no longer needs its separate negative check.** — The recovery guidance assumes that public containers and Shared Key dependence are not accepted for workload access. Consequently, one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q19 — answer D

A decision test for 'Create a hierarchical namespace boundary' includes information security. A material change now applies: The legal department introduces collaborative document shares that require native SMB locking and Windows ACL behavior, but analytics ingestion must remain object-native; revise the service boundaries. Which finding constitutes the correct revision to the decision record?

- ✗ **A. Retain ADLS Gen2 on a hierarchical-namespace StorageV2 account at Create a hierarchical namespace boundary without recalculating criteria or eligibility. Also, take it as conclusive that the original weighted result is permanent.** — The command-level assertion is anchored in the fact that aDLS Gen2 on a hierarchical-namespace StorageV2 account. Consequently, the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Flat Azure Blob Storage containers with prefix conventions for Create a hierarchical namespace boundary without rechecking its mandatory constraints; in a separate step, treat it as established that being different from the current design is an architecture criterion.** — flat Azure Blob Storage containers with prefix conventions. For this case, being different is not a criterion, and the candidate still must avoid the prohibited state at Create a hierarchical namespace boundary.
- ✗ **C. Keep Azure Files shares mounted by analytics and document clients eligible at Create a hierarchical namespace boundary by downgrading LAB11-REQ-02. As another control, use as justification the claim that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The controlling fact is that lAB11-REQ-02. For this case, an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.
- ✓ **D. Re-score ADLS Gen2 on a hierarchical-namespace StorageV2 account and both alternatives for Create a hierarchical namespace boundary; before approval, supersede the ADR using the changed evidence for LAB11-REQ-02.** — The WAF consequence identifies that aDLS Gen2 on a hierarchical-namespace StorageV2 account at Create a hierarchical namespace boundary. Consequently, the material change 'The legal department introduces collaborative document shares that require native SMB locking and Windows ACL behavior, but analytics ingestion must remain object-native; revise the service boundaries.' requires fresh eligibility, weighted analysis, and a superseding decision.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q20 — answer C

The architecture board reconsiders 'Create a hierarchical namespace boundary' with data platform engineering. After a partial run, cleanup must follow this dependency: Delete run-owned filesystems and private endpoints before deleting the account. Which recommendation delivers the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Design filesystem and directory ownership before reconciling the current dependency; before approval, treat as decisive the assertion that removing a parent needed to identify Create a hierarchical namespace boundary is harmless.** — The relevant observation is that remove child paths before filesystems and retain no file content as evidence. For this case, a cleanup rule for Design filesystem and directory ownership cannot override the dependency declared for Create a hierarchical namespace boundary.
- ✗ **B. Delete candidates by display name before comparing the Create a hierarchical namespace boundary ownership tags. Separately, base approval on the claim that the dependency rule 'Delete run-owned filesystems and private endpoints before deleting the account' is optional.** — The checkpoint specifically records that account name, kind, namespace state, TLS version, public-access state, SKU, and ownership tags. For this case, names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✓ **C. Verify exact run-state IDs and ownership tags for Create a hierarchical namespace boundary; as an independent condition, follow this dependency rule without purge: Delete run-owned filesystems and private endpoints before deleting the account.** — The authored acceptance boundary states that delete run-owned filesystems and private endpoints before deleting the account. For this case, exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **D. Destroy recoverable copies before retaining the Create a hierarchical namespace boundary negative assertion 'Public containers and Shared Key dependence are not accepted for workload access'; for this decision, use the premise that remaining command logs are sufficient recovery evidence.** — The scenario makes clear that public containers and Shared Key dependence are not accepted for workload access. For this case, irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-2](../README.md#checkpoint-2)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q21 — answer B

A review of 'Design filesystem and directory ownership' begins with input from data platform engineering. Approval requires a positive result plus this independent negative assertion: World-writable paths and user-owned production directories are absent. Which recommendation supplies the acceptance rule that makes LAB11-REQ-03 testable?

- ✗ **A. Select Flat Azure Blob Storage containers with prefix conventions before checking Design filesystem and directory ownership; as a separate check, proceed on the belief that a successful deployment will later prove the architecture constraint.** — The applicable design condition is that world-writable paths and user-owned production directories are absent. For this case, a deployment result cannot prove LAB11-REQ-03, and Flat Azure Blob Storage containers with prefix conventions still has to meet the mandatory boundary.
- ✓ **B. Require the documented positive state for Design filesystem and directory ownership. Independently, verify that world-writable paths and user-owned production directories are absent.** — The architecture evidence must show that filesystems represent durable data-product boundaries and directories have group-owned default and access ACLs. For this case, the positive state and an independent negative assertion jointly make LAB11-REQ-03 testable.
- ✗ **C. Use the passing result from Match service semantics to access patterns to approve Design filesystem and directory ownership. Afterward, treat as decisive the assertion that one control establishes an unrelated acceptance boundary.** — The review is governed by this fact: object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. For this case, that outcome belongs to Match service semantics to access patterns and leaves Design filesystem and directory ownership unverified.
- ✗ **D. Choose Azure Files shares mounted by analytics and document clients and skip the Design filesystem and directory ownership negative assertion; next, base approval on the claim that the candidate has the lowest implementation effort.** — The retained result must be reconciled with the fact that consolidate unstructured content for governed analytics while preserving scalable access and clear ownership. For this case, implementation effort cannot justify skipping the negative assertion or displace LAB11-REQ-03.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q22 — answer A

'Design filesystem and directory ownership' awaits approval from supplier integration team. The selected architecture is ADLS Gen2 on a hierarchical-namespace StorageV2 account; object existence alone is not success. Choose the intended successful finding.

- ✓ **A. Record filesystems represent durable data-product boundaries and directories have group-owned default and access ACLs; in a separate step, classify it as success for LAB11-REQ-03.** — The decision tension comes from the fact that filesystems represent durable data-product boundaries and directories have group-owned default and access ACLs. For this case, this is the authored target state for Design filesystem and directory ownership and directly supports LAB11-REQ-03.
- ✗ **B. Use only the negative assertion 'World-writable paths and user-owned production directories are absent' as the success result. Before sign-off, use as justification the claim that absence proves every required positive property.** — The safe operating boundary says that world-writable paths and user-owned production directories are absent. For this case, this is the independent prohibited-state assertion, not a successful finding.
- ✗ **C. Use the successful finding from Create a hierarchical namespace boundary as the result for Design filesystem and directory ownership; as an independent condition, accept without proof that a property from the current checkpoint does not need to be inspected.** — The traceable checkpoint outcome is that the account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags. For this case, evidence for Create a hierarchical namespace boundary cannot substitute for the properties required at Design filesystem and directory ownership.
- ✗ **D. Record the failure condition 'Azure RBAC grants endpoint access but POSIX ACL traversal denies a child path' as a successful state; separately, rely on the claim that the command returned an object.** — The failure model establishes that azure RBAC grants endpoint access but POSIX ACL traversal denies a child path. For this case, resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q23 — answer B

'Design filesystem and directory ownership' is reopened at the request of analytics consumers. Evidence must address this risk without retaining credentials: Azure RBAC grants endpoint access but POSIX ACL traversal denies a child path. Which answer describes sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Define encryption and key dependency for Design filesystem and directory ownership. Next, use the premise that a related checkpoint proves the current expected state.** — The WAF consequence identifies that encryption services, key-source class, identity type, non-secret vault reference, and rotation owner. For this case, that evidence supports Define encryption and key dependency, so it cannot demonstrate Filesystems represent durable data-product boundaries and directories have group-owned default and access ACLs.
- ✓ **B. Retain synthetic filesystem and path names, owner and group labels, normalized ACL summary, and data-product owner; next, exclude credentials and unrelated response fields.** — The recovery guidance assumes that synthetic filesystem and path names, owner and group labels, normalized ACL summary, and data-product owner. For this case, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **C. Store unredacted Design filesystem and directory ownership output with operator, tenant, token, and request context, and then consider it sufficient that reproduction requires every captured field.** — The command-level assertion is anchored in the fact that unredacted implementation output. For this case, identity, tenant, or token material exceeds the non-secret evidence contract.
- ✗ **D. Record only the Design filesystem and directory ownership positive inspection's exit status. Also, take it as conclusive that projected properties and assertion results can be reconstructed later.** — the positive inspection's exit status. That evidence means an exit code alone does not show whether filesystems represent durable data-product boundaries and directories have group-owned default and access ACLs.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q24 — answer A

A design review of 'Design filesystem and directory ownership' includes information security. The target is Filesystems represent durable data-product boundaries and directories have group-owned default and access ACLs, but the latest evidence does not show it. What should be recorded as the most likely cause?

- ✓ **A. Investigate azure RBAC grants endpoint access but POSIX ACL traversal denies a child path; for this decision, isolate that cause before changing ADLS Gen2 on a hierarchical-namespace StorageV2 account.** — The controlling fact is that azure RBAC grants endpoint access but POSIX ACL traversal denies a child path. That evidence means it is the checkpoint's causal failure model and should be isolated before retrying Design filesystem and directory ownership.
- ✗ **B. Treat 'Only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently' as grounds to reject Design filesystem and directory ownership; next, rely on the belief that validate private endpoint access's failure model applies unchanged here.** — The authored acceptance boundary states that only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently. That evidence means that condition belongs to Validate private endpoint access and does not by itself invalidate ADLS Gen2 on a hierarchical-namespace StorageV2 account.
- ✗ **C. Ignore the negative assertion 'World-writable paths and user-owned production directories are absent'. In addition, proceed on the belief that a later material change will make it unnecessary.** — The relevant observation is that world-writable paths and user-owned production directories are absent. That evidence means the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Match service semantics to access patterns instead of diagnosing Design filesystem and directory ownership; before approval, treat as decisive the assertion that a passing result at Match service semantics to access patterns identifies the current cause.** — The checkpoint specifically records that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. That evidence means a passing result at Match service semantics to access patterns gives no causal evidence for the failure at Design filesystem and directory ownership.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q25 — answer D

The team asks data platform engineering to assess 'Design filesystem and directory ownership'. The run encountered this modeled failure: Azure RBAC grants endpoint access but POSIX ACL traversal denies a child path. Which proposal supplies the safest recovery action?

- ✗ **A. Perform cleanup immediately: Remove child paths before filesystems and retain no file content as evidence; independently, treat it as established that the failed operation and its returned identifiers do not need reconciliation.** — The architecture evidence must show that remove child paths before filesystems and retain no file content as evidence. That evidence means cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **B. Create a different run identity before diagnosing 'Azure RBAC grants endpoint access but POSIX ACL traversal denies a child path'. Then, use as justification the claim that the first state record and returned identifiers can be discarded.** — The applicable design condition is that azure RBAC grants endpoint access but POSIX ACL traversal denies a child path. That evidence means discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **C. Change Match service semantics to access patterns instead; afterward, accept without proof that success at Match service semantics to access patterns will repair the failed state at Design filesystem and directory ownership.** — The review is governed by this fact: object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. That evidence means altering an already separate checkpoint does not repair the modeled failure at Design filesystem and directory ownership.
- ✓ **D. Trace execute permission on every parent and apply the minimum group ACL with a corresponding default ACL. Then, preserve the current run identity and evidence.** — The scenario makes clear that trace execute permission on every parent and apply the minimum group ACL with a corresponding default ACL. That evidence means it corrects the narrow cause while retaining the same recovery trail and decision scope.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q26 — answer C

A recommendation on 'Design filesystem and directory ownership' is requested by supplier integration team. Without making a new change, the team must inspect the risk 'Azure RBAC grants endpoint access but POSIX ACL traversal denies a child path' using the Azure PowerShell lane. Which option best represents the read-only, lane-correct inspection?

- ✗ **A. Rerun the Design filesystem and directory ownership implementation command and infer the expected state. Also, base approval on the claim that absence of a shell error proves every property.** — The decision tension comes from the fact that the implementation command. That evidence means it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Design filesystem and directory ownership: World-writable paths and user-owned production directories are absent; in a separate step, use the premise that an empty negative result reports every required positive property.** — The safe operating boundary says that the negative inspection. That evidence means absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✓ **C. Inspect the documented properties for Design filesystem and directory ownership. Next, retain this evidence: synthetic filesystem and path names, owner and group labels, normalized ACL summary, and data-product owner.** — The retained result must be reconciled with the fact that filesystems represent durable data-product boundaries and directories have group-owned default and access ACLs. That evidence means the read-only inspection directly tests the properties required at Design filesystem and directory ownership.
- ✗ **D. Run the positive inspection for Create a hierarchical namespace boundary and apply it to Design filesystem and directory ownership. As another control, consider it sufficient that any command from the same lane proves the current checkpoint.** — The traceable checkpoint outcome is that the positive inspection for Create a hierarchical namespace boundary. That evidence means it is lane-correct but proves Create a hierarchical namespace boundary, not Design filesystem and directory ownership.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q27 — answer C

'Design filesystem and directory ownership' is assigned to analytics consumers. A passing positive check does not by itself prove this negative assertion: World-writable paths and user-owned production directories are absent. Which course of action provides the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Design filesystem and directory ownership and report full compliance; before approval, rely on the claim that every prohibited parallel state must therefore be absent.** — The recovery guidance assumes that filesystems represent durable data-product boundaries and directories have group-owned default and access ACLs. That evidence means the positive result alone does not test the explicit anti-condition 'World-writable paths and user-owned production directories are absent'.
- ✗ **B. Prove only that world-writable paths and user-owned production directories are absent and report the intended configuration as present. Separately, rely on the belief that absence is equivalent to positive-state evidence.** — The WAF consequence identifies that world-writable paths and user-owned production directories are absent. That evidence means absence evidence cannot demonstrate the required positive state 'Filesystems represent durable data-product boundaries and directories have group-owned default and access ACLs'.
- ✓ **C. Verify the positive properties for Design filesystem and directory ownership. As another control, independently verify that world-writable paths and user-owned production directories are absent.** — The failure model establishes that filesystems represent durable data-product boundaries and directories have group-owned default and access ACLs; World-writable paths and user-owned production directories are absent. That evidence means two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **D. Use Define encryption and key dependency's negative assertion for Design filesystem and directory ownership; for this decision, proceed on the belief that negative assertions are interchangeable between checkpoints.** — The command-level assertion is anchored in the fact that a customer-managed key is not referenced without an identity capable of unwrapping it. That evidence means the second assertion is valid for Define encryption and key dependency but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q28 — answer B

An assurance review of 'Design filesystem and directory ownership' includes information security. The board wants the Well-Architected consequence of mitigating this risk: Azure RBAC grants endpoint access but POSIX ACL traversal denies a child path. Which finding constitutes the consequence attributable to this checkpoint?

- ✗ **A. Use the Validate private endpoint access consequence as the result for Design filesystem and directory ownership; afterward, take it as conclusive that a pillar statement remains valid when moved away from Validate private endpoint access.** — The controlling fact is that security: denied public access and explicit dfs connectivity constrain unintended data paths. The resulting architectural conclusion is that that tradeoff belongs to Validate private endpoint access and does not explain this checkpoint's decision.
- ✓ **B. Record this consequence: Operational Excellence: data-product filesystem ownership and inherited ACLs create a supportable namespace. In addition, tie it to LAB11-REQ-03.** — operational Excellence: data-product filesystem ownership and inherited ACLs create a supportable namespace. The resulting architectural conclusion is that it states the authored pillar consequence of the control evaluated at Design filesystem and directory ownership.
- ✗ **C. Remove the control responsible for the Design filesystem and directory ownership outcome; then treat it as established that a moderate cost classification outweighs the mandatory architecture state.** — The authored acceptance boundary states that the required outcome at Design filesystem and directory ownership. The resulting architectural conclusion is that cost Optimization cannot remove the acceptance condition 'Filesystems represent durable data-product boundaries and directories have group-owned default and access ACLs'.
- ✗ **D. Treat 'Operational Excellence: data-product filesystem ownership and inherited ACLs create a supportable namespace' as proof that all five pillars pass. Independently, use as justification the claim that the checkpoint 'Design filesystem and directory ownership' no longer needs its separate negative check.** — The relevant observation is that world-writable paths and user-owned production directories are absent. The resulting architectural conclusion is that one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q29 — answer C

Approval of 'Design filesystem and directory ownership' is questioned by data platform engineering. A material change now applies: The legal department introduces collaborative document shares that require native SMB locking and Windows ACL behavior, but analytics ingestion must remain object-native; revise the service boundaries. Which recommendation delivers the correct revision to the decision record?

- ✗ **A. Retain ADLS Gen2 on a hierarchical-namespace StorageV2 account at Design filesystem and directory ownership without recalculating criteria or eligibility. As another control, treat as decisive the assertion that the original weighted result is permanent.** — The scenario makes clear that aDLS Gen2 on a hierarchical-namespace StorageV2 account. The resulting architectural conclusion is that the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Flat Azure Blob Storage containers with prefix conventions for Design filesystem and directory ownership without rechecking its mandatory constraints; as a separate check, base approval on the claim that being different from the current design is an architecture criterion.** — The architecture evidence must show that flat Azure Blob Storage containers with prefix conventions. The resulting architectural conclusion is that being different is not a criterion, and the candidate still must avoid the prohibited state at Design filesystem and directory ownership.
- ✓ **C. Re-score ADLS Gen2 on a hierarchical-namespace StorageV2 account and both alternatives for Design filesystem and directory ownership. Before sign-off, supersede the ADR using the changed evidence for LAB11-REQ-03.** — The checkpoint specifically records that aDLS Gen2 on a hierarchical-namespace StorageV2 account at Design filesystem and directory ownership. The resulting architectural conclusion is that the material change 'The legal department introduces collaborative document shares that require native SMB locking and Windows ACL behavior, but analytics ingestion must remain object-native; revise the service boundaries.' requires fresh eligibility, weighted analysis, and a superseding decision.
- ✗ **D. Keep Azure Files shares mounted by analytics and document clients eligible at Design filesystem and directory ownership by downgrading LAB11-REQ-03. Afterward, use the premise that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The applicable design condition is that lAB11-REQ-03. The resulting architectural conclusion is that an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q30 — answer A

The implementation review has reached 'Design filesystem and directory ownership'. After a partial run, cleanup must follow this dependency: Remove child paths before filesystems and retain no file content as evidence. Which response meets the need for the dependency-safe cleanup plan?

- ✓ **A. Verify exact run-state IDs and ownership tags for Design filesystem and directory ownership; afterward, follow this dependency rule without purge: Remove child paths before filesystems and retain no file content as evidence.** — The review is governed by this fact: remove child paths before filesystems and retain no file content as evidence. The resulting architectural conclusion is that exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **B. Apply the cleanup rule for Create a hierarchical namespace boundary before reconciling the current dependency; for this decision, accept without proof that removing a parent needed to identify Design filesystem and directory ownership is harmless.** — The retained result must be reconciled with the fact that delete run-owned filesystems and private endpoints before deleting the account. The resulting architectural conclusion is that a cleanup rule for Create a hierarchical namespace boundary cannot override the dependency declared for Design filesystem and directory ownership.
- ✗ **C. Delete candidates by display name before comparing the Design filesystem and directory ownership ownership tags. Before sign-off, rely on the claim that the dependency rule 'Remove child paths before filesystems and retain no file content as evidence' is optional.** — The decision tension comes from the fact that synthetic filesystem and path names, owner and group labels, normalized ACL summary, and data-product owner. The resulting architectural conclusion is that names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Design filesystem and directory ownership negative assertion 'World-writable paths and user-owned production directories are absent'; as an independent condition, rely on the belief that remaining command logs are sufficient recovery evidence.** — The safe operating boundary says that world-writable paths and user-owned production directories are absent. The resulting architectural conclusion is that irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-3](../README.md#checkpoint-3)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q31 — answer B

The approach to 'Define encryption and key dependency' is challenged by supplier integration team. Approval requires a positive result plus this independent negative assertion: A customer-managed key is not referenced without an identity capable of unwrapping it. Choose the acceptance rule that makes LAB11-REQ-04 testable.

- ✗ **A. Select Flat Azure Blob Storage containers with prefix conventions before checking Define encryption and key dependency; next, use as justification the claim that a successful deployment will later prove the architecture constraint.** — The failure model establishes that a customer-managed key is not referenced without an identity capable of unwrapping it. The resulting architectural conclusion is that a deployment result cannot prove LAB11-REQ-04, and Flat Azure Blob Storage containers with prefix conventions still has to meet the mandatory boundary.
- ✓ **B. Require the documented positive state for Define encryption and key dependency. Also, verify that a customer-managed key is not referenced without an identity capable of unwrapping it.** — The traceable checkpoint outcome is that service encryption is enabled and any customer-managed-key choice includes managed identity, vault, rotation, and availability ownership. The resulting architectural conclusion is that the positive state and an independent negative assertion jointly make LAB11-REQ-04 testable.
- ✗ **C. Use the passing result from Match service semantics to access patterns to approve Define encryption and key dependency. In addition, accept without proof that one control establishes an unrelated acceptance boundary.** — The recovery guidance assumes that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. The resulting architectural conclusion is that that outcome belongs to Match service semantics to access patterns and leaves Define encryption and key dependency unverified.
- ✗ **D. Choose Azure Files shares mounted by analytics and document clients and skip the Define encryption and key dependency negative assertion; before approval, rely on the claim that the candidate has the lowest implementation effort.** — The WAF consequence identifies that consolidate unstructured content for governed analytics while preserving scalable access and clear ownership. The resulting architectural conclusion is that implementation effort cannot justify skipping the negative assertion or displace LAB11-REQ-04.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q32 — answer C

A decision test for 'Define encryption and key dependency' includes analytics consumers. The selected architecture is ADLS Gen2 on a hierarchical-namespace StorageV2 account; object existence alone is not success. Which answer describes the intended successful finding?

- ✗ **A. Use only the negative assertion 'A customer-managed key is not referenced without an identity capable of unwrapping it' as the success result; before approval, use the premise that absence proves every required positive property.** — a customer-managed key is not referenced without an identity capable of unwrapping it. Under the stated constraint, this is the independent prohibited-state assertion, not a successful finding.
- ✗ **B. Use the successful finding from Create a hierarchical namespace boundary as the result for Define encryption and key dependency. Then, consider it sufficient that a property from the current checkpoint does not need to be inspected.** — The controlling fact is that the account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags. Under the stated constraint, evidence for Create a hierarchical namespace boundary cannot substitute for the properties required at Define encryption and key dependency.
- ✓ **C. Record service encryption is enabled and any customer-managed-key choice includes managed identity, vault, rotation, and availability ownership. Afterward, classify it as success for LAB11-REQ-04.** — The command-level assertion is anchored in the fact that service encryption is enabled and any customer-managed-key choice includes managed identity, vault, rotation, and availability ownership. The resulting architectural conclusion is that this is the authored target state for Define encryption and key dependency and directly supports LAB11-REQ-04.
- ✗ **D. Record the failure condition 'The storage identity lacks key permissions or cannot reach the vault network path' as a successful state; afterward, take it as conclusive that the command returned an object.** — The authored acceptance boundary states that the storage identity lacks key permissions or cannot reach the vault network path. Under the stated constraint, resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q33 — answer C

The architecture board reconsiders 'Define encryption and key dependency' with information security. Evidence must address this risk without retaining credentials: The storage identity lacks key permissions or cannot reach the vault network path. What should be recorded as sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Design filesystem and directory ownership for Define encryption and key dependency. Also, rely on the belief that a related checkpoint proves the current expected state.** — The checkpoint specifically records that synthetic filesystem and path names, owner and group labels, normalized ACL summary, and data-product owner. Under the stated constraint, that evidence supports Design filesystem and directory ownership, so it cannot demonstrate Service encryption is enabled and any customer-managed-key choice includes managed identity, vault, rotation, and availability ownership.
- ✗ **B. Store unredacted Define encryption and key dependency output with operator, tenant, token, and request context; in a separate step, proceed on the belief that reproduction requires every captured field.** — The scenario makes clear that unredacted implementation output. Under the stated constraint, identity, tenant, or token material exceeds the non-secret evidence contract.
- ✓ **C. Retain encryption services, key-source class, identity type, non-secret vault reference, and rotation owner. Separately, exclude credentials and unrelated response fields.** — The relevant observation is that encryption services, key-source class, identity type, non-secret vault reference, and rotation owner. Under the stated constraint, it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **D. Record only the Define encryption and key dependency positive inspection's exit status. As another control, treat as decisive the assertion that projected properties and assertion results can be reconstructed later.** — The architecture evidence must show that the positive inspection's exit status. Under the stated constraint, an exit code alone does not show whether service encryption is enabled and any customer-managed-key choice includes managed identity, vault, rotation, and availability ownership.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q34 — answer A

A review of 'Define encryption and key dependency' begins with input from data platform engineering. The target is Service encryption is enabled and any customer-managed-key choice includes managed identity, vault, rotation, and availability ownership, but the latest evidence does not show it. Which proposal supplies the most likely cause?

- ✓ **A. Investigate the storage identity lacks key permissions or cannot reach the vault network path; for the recorded decision, isolate that cause before changing ADLS Gen2 on a hierarchical-namespace StorageV2 account.** — The applicable design condition is that the storage identity lacks key permissions or cannot reach the vault network path. Under the stated constraint, it is the checkpoint's causal failure model and should be isolated before retrying Define encryption and key dependency.
- ✗ **B. Treat 'Only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently' as grounds to reject Define encryption and key dependency; before approval, treat it as established that validate private endpoint access's failure model applies unchanged here.** — The review is governed by this fact: only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently. Under the stated constraint, that condition belongs to Validate private endpoint access and does not by itself invalidate ADLS Gen2 on a hierarchical-namespace StorageV2 account.
- ✗ **C. Ignore the negative assertion 'A customer-managed key is not referenced without an identity capable of unwrapping it'. Separately, use as justification the claim that a later material change will make it unnecessary.** — The retained result must be reconciled with the fact that a customer-managed key is not referenced without an identity capable of unwrapping it. Under the stated constraint, the negative assertion must be evaluated now, independent of a later business change.
- ✗ **D. Investigate Match service semantics to access patterns instead of diagnosing Define encryption and key dependency; for this decision, accept without proof that a passing result at Match service semantics to access patterns identifies the current cause.** — The decision tension comes from the fact that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. Under the stated constraint, a passing result at Match service semantics to access patterns gives no causal evidence for the failure at Define encryption and key dependency.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q35 — answer D

'Define encryption and key dependency' awaits approval from supplier integration team. The run encountered this modeled failure: The storage identity lacks key permissions or cannot reach the vault network path. Which option best represents the safest recovery action?

- ✗ **A. Perform cleanup immediately: Restore the recorded key source before removing any run-owned key association; never purge keys; afterward, base approval on the claim that the failed operation and its returned identifiers do not need reconciliation.** — The traceable checkpoint outcome is that restore the recorded key source before removing any run-owned key association; never purge keys. Under the stated constraint, cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✗ **B. Create a different run identity before diagnosing 'The storage identity lacks key permissions or cannot reach the vault network path'; then use the premise that the first state record and returned identifiers can be discarded.** — The failure model establishes that the storage identity lacks key permissions or cannot reach the vault network path. Under the stated constraint, discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **C. Change Match service semantics to access patterns instead. Independently, consider it sufficient that success at Match service semantics to access patterns will repair the failed state at Define encryption and key dependency.** — The recovery guidance assumes that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. Under the stated constraint, altering an already separate checkpoint does not repair the modeled failure at Define encryption and key dependency.
- ✓ **D. Validate identity, Key Vault RBAC, key state, DNS, and network reachability independently. Independently, preserve the current run identity and evidence.** — The safe operating boundary says that validate identity, Key Vault RBAC, key state, DNS, and network reachability independently. Under the stated constraint, it corrects the narrow cause while retaining the same recovery trail and decision scope.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q36 — answer B

'Define encryption and key dependency' is reopened at the request of analytics consumers. Without making a new change, the team must inspect the risk 'The storage identity lacks key permissions or cannot reach the vault network path' using the Azure PowerShell lane. Which course of action provides the read-only, lane-correct inspection?

- ✗ **A. Rerun the Define encryption and key dependency implementation command and infer the expected state. As another control, rely on the claim that absence of a shell error proves every property.** — The command-level assertion is anchored in the fact that the implementation command. Under the stated constraint, it can mutate state and shell success does not independently assert the expected properties.
- ✓ **B. Inspect the documented properties for Define encryption and key dependency; in a separate step, retain this evidence: encryption services, key-source class, identity type, non-secret vault reference, and rotation owner.** — The WAF consequence identifies that service encryption is enabled and any customer-managed-key choice includes managed identity, vault, rotation, and availability ownership. Under the stated constraint, the read-only inspection directly tests the properties required at Define encryption and key dependency.
- ✗ **C. Run only this negative inspection for Define encryption and key dependency: A customer-managed key is not referenced without an identity capable of unwrapping it; as a separate check, rely on the belief that an empty negative result reports every required positive property.** — the negative inspection. This matters because absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✗ **D. Run the positive inspection for Create a hierarchical namespace boundary and apply it to Define encryption and key dependency. Afterward, proceed on the belief that any command from the same lane proves the current checkpoint.** — The controlling fact is that the positive inspection for Create a hierarchical namespace boundary. This matters because it is lane-correct but proves Create a hierarchical namespace boundary, not Define encryption and key dependency.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q37 — answer B

A design review of 'Define encryption and key dependency' includes information security. A passing positive check does not by itself prove this negative assertion: A customer-managed key is not referenced without an identity capable of unwrapping it. Which finding constitutes the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Define encryption and key dependency and report full compliance; for this decision, take it as conclusive that every prohibited parallel state must therefore be absent.** — The relevant observation is that service encryption is enabled and any customer-managed-key choice includes managed identity, vault, rotation, and availability ownership. This matters because the positive result alone does not test the explicit anti-condition 'A customer-managed key is not referenced without an identity capable of unwrapping it'.
- ✓ **B. Verify the positive properties for Define encryption and key dependency; next, independently verify that a customer-managed key is not referenced without an identity capable of unwrapping it.** — The authored acceptance boundary states that service encryption is enabled and any customer-managed-key choice includes managed identity, vault, rotation, and availability ownership; A customer-managed key is not referenced without an identity capable of unwrapping it. This matters because two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **C. Prove only that a customer-managed key is not referenced without an identity capable of unwrapping it and report the intended configuration as present. Before sign-off, treat it as established that absence is equivalent to positive-state evidence.** — The checkpoint specifically records that a customer-managed key is not referenced without an identity capable of unwrapping it. This matters because absence evidence cannot demonstrate the required positive state 'Service encryption is enabled and any customer-managed-key choice includes managed identity, vault, rotation, and availability ownership'.
- ✗ **D. Use Design filesystem and directory ownership's negative assertion for Define encryption and key dependency; as an independent condition, use as justification the claim that negative assertions are interchangeable between checkpoints.** — The scenario makes clear that world-writable paths and user-owned production directories are absent. This matters because the second assertion is valid for Design filesystem and directory ownership but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q38 — answer A

The team asks data platform engineering to assess 'Define encryption and key dependency'. The board wants the Well-Architected consequence of mitigating this risk: The storage identity lacks key permissions or cannot reach the vault network path. Which recommendation delivers the consequence attributable to this checkpoint?

- ✓ **A. Record this consequence: Cost Optimization: customer-managed keys are adopted only when custody requirements justify their lifecycle overhead; for this decision, tie it to LAB11-REQ-04.** — The architecture evidence must show that cost Optimization: customer-managed keys are adopted only when custody requirements justify their lifecycle overhead. This matters because it states the authored pillar consequence of the control evaluated at Define encryption and key dependency.
- ✗ **B. Use the Validate private endpoint access consequence as the result for Define encryption and key dependency. Independently, treat as decisive the assertion that a pillar statement remains valid when moved away from Validate private endpoint access.** — The applicable design condition is that security: denied public access and explicit dfs connectivity constrain unintended data paths. This matters because that tradeoff belongs to Validate private endpoint access and does not explain this checkpoint's decision.
- ✗ **C. Remove the control responsible for the Define encryption and key dependency outcome. Next, base approval on the claim that a moderate cost classification outweighs the mandatory architecture state.** — The review is governed by this fact: the required outcome at Define encryption and key dependency. This matters because cost Optimization cannot remove the acceptance condition 'Service encryption is enabled and any customer-managed-key choice includes managed identity, vault, rotation, and availability ownership'.
- ✗ **D. Treat 'Cost Optimization: customer-managed keys are adopted only when custody requirements justify their lifecycle overhead' as proof that all five pillars pass, and then use the premise that the checkpoint 'Define encryption and key dependency' no longer needs its separate negative check.** — The retained result must be reconciled with the fact that a customer-managed key is not referenced without an identity capable of unwrapping it. This matters because one positive command cannot establish every pillar, especially while the negative state remains unchecked.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q39 — answer D

A recommendation on 'Define encryption and key dependency' is requested by supplier integration team. A material change now applies: The legal department introduces collaborative document shares that require native SMB locking and Windows ACL behavior, but analytics ingestion must remain object-native; revise the service boundaries. Which response meets the need for the correct revision to the decision record?

- ✗ **A. Retain ADLS Gen2 on a hierarchical-namespace StorageV2 account at Define encryption and key dependency without recalculating criteria or eligibility. Afterward, accept without proof that the original weighted result is permanent.** — The safe operating boundary says that aDLS Gen2 on a hierarchical-namespace StorageV2 account. This matters because the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Flat Azure Blob Storage containers with prefix conventions for Define encryption and key dependency without rechecking its mandatory constraints; next, rely on the claim that being different from the current design is an architecture criterion.** — The traceable checkpoint outcome is that flat Azure Blob Storage containers with prefix conventions. This matters because being different is not a criterion, and the candidate still must avoid the prohibited state at Define encryption and key dependency.
- ✗ **C. Keep Azure Files shares mounted by analytics and document clients eligible at Define encryption and key dependency by downgrading LAB11-REQ-04. In addition, rely on the belief that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The failure model establishes that lAB11-REQ-04. This matters because an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.
- ✓ **D. Re-score ADLS Gen2 on a hierarchical-namespace StorageV2 account and both alternatives for Define encryption and key dependency. Then, supersede the ADR using the changed evidence for LAB11-REQ-04.** — The decision tension comes from the fact that aDLS Gen2 on a hierarchical-namespace StorageV2 account at Define encryption and key dependency. This matters because the material change 'The legal department introduces collaborative document shares that require native SMB locking and Windows ACL behavior, but analytics ingestion must remain object-native; revise the service boundaries.' requires fresh eligibility, weighted analysis, and a superseding decision.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q40 — answer B

'Define encryption and key dependency' is assigned to analytics consumers. After a partial run, cleanup must follow this dependency: Restore the recorded key source before removing any run-owned key association; never purge keys. Which choice should be approved as the dependency-safe cleanup plan?

- ✗ **A. Apply the cleanup rule for Create a hierarchical namespace boundary before reconciling the current dependency; as an independent condition, consider it sufficient that removing a parent needed to identify Define encryption and key dependency is harmless.** — The WAF consequence identifies that delete run-owned filesystems and private endpoints before deleting the account. This matters because a cleanup rule for Create a hierarchical namespace boundary cannot override the dependency declared for Define encryption and key dependency.
- ✓ **B. Verify exact run-state IDs and ownership tags for Define encryption and key dependency. Next, follow this dependency rule without purge: Restore the recorded key source before removing any run-owned key association; never purge keys.** — The recovery guidance assumes that restore the recorded key source before removing any run-owned key association; never purge keys. This matters because exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **C. Delete candidates by display name before comparing the Define encryption and key dependency ownership tags; for the recorded decision, take it as conclusive that the dependency rule 'Restore the recorded key source before removing any run-owned key association; never purge keys' is optional.** — The command-level assertion is anchored in the fact that encryption services, key-source class, identity type, non-secret vault reference, and rotation owner. This matters because names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Define encryption and key dependency negative assertion 'A customer-managed key is not referenced without an identity capable of unwrapping it'. Then, treat it as established that remaining command logs are sufficient recovery evidence.** — a customer-managed key is not referenced without an identity capable of unwrapping it. The checkpoint therefore requires that irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-4](../README.md#checkpoint-4)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q41 — answer A

An assurance review of 'Validate private endpoint access' includes analytics consumers. Approval requires a positive result plus this independent negative assertion: Public network access is not retained to compensate for a missing dfs endpoint or DNS record. Which answer describes the acceptance rule that makes LAB11-REQ-05 testable?

- ✓ **A. Require the documented positive state for Validate private endpoint access; as a separate check, verify that public network access is not retained to compensate for a missing dfs endpoint or DNS record.** — The controlling fact is that the dfs private endpoint is approved, private DNS resolves correctly, and the default network action is deny. The checkpoint therefore requires that the positive state and an independent negative assertion jointly make LAB11-REQ-05 testable.
- ✗ **B. Select Flat Azure Blob Storage containers with prefix conventions before checking Validate private endpoint access; before approval, use the premise that a successful deployment will later prove the architecture constraint.** — The authored acceptance boundary states that public network access is not retained to compensate for a missing dfs endpoint or DNS record. The checkpoint therefore requires that a deployment result cannot prove LAB11-REQ-05, and Flat Azure Blob Storage containers with prefix conventions still has to meet the mandatory boundary.
- ✗ **C. Use the passing result from Match service semantics to access patterns to approve Validate private endpoint access. Separately, consider it sufficient that one control establishes an unrelated acceptance boundary.** — The relevant observation is that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. The checkpoint therefore requires that that outcome belongs to Match service semantics to access patterns and leaves Validate private endpoint access unverified.
- ✗ **D. Choose Azure Files shares mounted by analytics and document clients and skip the Validate private endpoint access negative assertion; for this decision, take it as conclusive that the candidate has the lowest implementation effort.** — The checkpoint specifically records that consolidate unstructured content for governed analytics while preserving scalable access and clear ownership. The checkpoint therefore requires that implementation effort cannot justify skipping the negative assertion or displace LAB11-REQ-05.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q42 — answer B

Approval of 'Validate private endpoint access' is questioned by information security. The selected architecture is ADLS Gen2 on a hierarchical-namespace StorageV2 account; object existence alone is not success. What should be recorded as the intended successful finding?

- ✗ **A. Use only the negative assertion 'Public network access is not retained to compensate for a missing dfs endpoint or DNS record' as the success result; afterward, rely on the belief that absence proves every required positive property.** — The architecture evidence must show that public network access is not retained to compensate for a missing dfs endpoint or DNS record. The checkpoint therefore requires that this is the independent prohibited-state assertion, not a successful finding.
- ✓ **B. Record the dfs private endpoint is approved, private DNS resolves correctly, and the default network action is deny; before approval, classify it as success for LAB11-REQ-05.** — The scenario makes clear that the dfs private endpoint is approved, private DNS resolves correctly, and the default network action is deny. The checkpoint therefore requires that this is the authored target state for Validate private endpoint access and directly supports LAB11-REQ-05.
- ✗ **C. Use the successful finding from Create a hierarchical namespace boundary as the result for Validate private endpoint access; then proceed on the belief that a property from the current checkpoint does not need to be inspected.** — The applicable design condition is that the account has hierarchical namespace, blocked public blob access, current TLS minimum, and run ownership tags. The checkpoint therefore requires that evidence for Create a hierarchical namespace boundary cannot substitute for the properties required at Validate private endpoint access.
- ✗ **D. Record the failure condition 'Only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently' as a successful state. Independently, treat as decisive the assertion that the command returned an object.** — The review is governed by this fact: only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently. The checkpoint therefore requires that resource existence or command output does not convert the documented failure condition into success.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q43 — answer C

The implementation review has reached 'Validate private endpoint access'. Evidence must address this risk without retaining credentials: Only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently. Which proposal supplies sufficient, properly scoped evidence?

- ✗ **A. Substitute the evidence from Design filesystem and directory ownership for Validate private endpoint access. As another control, treat it as established that a related checkpoint proves the current expected state.** — The decision tension comes from the fact that synthetic filesystem and path names, owner and group labels, normalized ACL summary, and data-product owner. The checkpoint therefore requires that that evidence supports Design filesystem and directory ownership, so it cannot demonstrate The dfs private endpoint is approved, private DNS resolves correctly, and the default network action is deny.
- ✗ **B. Store unredacted Validate private endpoint access output with operator, tenant, token, and request context; as a separate check, use as justification the claim that reproduction requires every captured field.** — The safe operating boundary says that unredacted implementation output. The checkpoint therefore requires that identity, tenant, or token material exceeds the non-secret evidence contract.
- ✓ **C. Retain endpoint ID, dfs group, approval state, subnet, private DNS label, and network default action; as an independent condition, exclude credentials and unrelated response fields.** — The retained result must be reconciled with the fact that endpoint ID, dfs group, approval state, subnet, private DNS label, and network default action. The checkpoint therefore requires that it captures the checkpoint's observable properties while keeping the evidence boundary narrow.
- ✗ **D. Record only the Validate private endpoint access positive inspection's exit status. Afterward, accept without proof that projected properties and assertion results can be reconstructed later.** — The traceable checkpoint outcome is that the positive inspection's exit status. The checkpoint therefore requires that an exit code alone does not show whether the dfs private endpoint is approved, private DNS resolves correctly, and the default network action is deny.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q44 — answer D

The approach to 'Validate private endpoint access' is challenged by supplier integration team. The target is The dfs private endpoint is approved, private DNS resolves correctly, and the default network action is deny, but the latest evidence does not show it. Which option best represents the most likely cause?

- ✗ **A. Treat 'The storage identity lacks key permissions or cannot reach the vault network path' as grounds to reject Validate private endpoint access; for this decision, base approval on the claim that define encryption and key dependency's failure model applies unchanged here.** — The recovery guidance assumes that the storage identity lacks key permissions or cannot reach the vault network path. The checkpoint therefore requires that that condition belongs to Define encryption and key dependency and does not by itself invalidate ADLS Gen2 on a hierarchical-namespace StorageV2 account.
- ✗ **B. Ignore the negative assertion 'Public network access is not retained to compensate for a missing dfs endpoint or DNS record'. Before sign-off, use the premise that a later material change will make it unnecessary.** — The WAF consequence identifies that public network access is not retained to compensate for a missing dfs endpoint or DNS record. The checkpoint therefore requires that the negative assertion must be evaluated now, independent of a later business change.
- ✗ **C. Investigate Match service semantics to access patterns instead of diagnosing Validate private endpoint access; as an independent condition, consider it sufficient that a passing result at Match service semantics to access patterns identifies the current cause.** — The command-level assertion is anchored in the fact that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. The checkpoint therefore requires that a passing result at Match service semantics to access patterns gives no causal evidence for the failure at Validate private endpoint access.
- ✓ **D. Investigate only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently; then isolate that cause before changing ADLS Gen2 on a hierarchical-namespace StorageV2 account.** — The failure model establishes that only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently. The checkpoint therefore requires that it is the checkpoint's causal failure model and should be isolated before retrying Validate private endpoint access.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q45 — answer B

A decision test for 'Validate private endpoint access' includes analytics consumers. The run encountered this modeled failure: Only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently. Which course of action provides the safest recovery action?

- ✗ **A. Perform cleanup immediately: Remove private DNS records and endpoints before the account; preserve shared network resources. Independently, rely on the claim that the failed operation and its returned identifiers do not need reconciliation.** — The controlling fact is that remove private DNS records and endpoints before the account; preserve shared network resources. In the decision record, cleanup before reconciliation can erase evidence or strand a partially created dependency.
- ✓ **B. Add and validate the dfs private endpoint and DNS zone without opening public access. Also, preserve the current run identity and evidence.** — add and validate the dfs private endpoint and DNS zone without opening public access. In the decision record, it corrects the narrow cause while retaining the same recovery trail and decision scope.
- ✗ **C. Create a different run identity before diagnosing 'Only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently'. Next, rely on the belief that the first state record and returned identifiers can be discarded.** — The authored acceptance boundary states that only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently. In the decision record, discarding the original run identity breaks ownership reconciliation and can duplicate a partial operation.
- ✗ **D. Change Match service semantics to access patterns instead, and then proceed on the belief that success at Match service semantics to access patterns will repair the failed state at Validate private endpoint access.** — The relevant observation is that object scale, analytics engines, directory operations, and access patterns justify StorageV2 with hierarchical namespace. In the decision record, altering an already separate checkpoint does not repair the modeled failure at Validate private endpoint access.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q46 — answer C

The architecture board reconsiders 'Validate private endpoint access' with information security. Without making a new change, the team must inspect the risk 'Only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently' using the Azure PowerShell lane. Which finding constitutes the read-only, lane-correct inspection?

- ✗ **A. Rerun the Validate private endpoint access implementation command and infer the expected state. Afterward, take it as conclusive that absence of a shell error proves every property.** — The scenario makes clear that the implementation command. In the decision record, it can mutate state and shell success does not independently assert the expected properties.
- ✗ **B. Run only this negative inspection for Validate private endpoint access: Public network access is not retained to compensate for a missing dfs endpoint or DNS record; next, treat it as established that an empty negative result reports every required positive property.** — The architecture evidence must show that the negative inspection. In the decision record, absence of the prohibited condition is necessary but does not establish the positive architecture state.
- ✓ **C. Inspect the documented properties for Validate private endpoint access. Afterward, retain this evidence: endpoint ID, dfs group, approval state, subnet, private DNS label, and network default action.** — The checkpoint specifically records that the dfs private endpoint is approved, private DNS resolves correctly, and the default network action is deny. In the decision record, the read-only inspection directly tests the properties required at Validate private endpoint access.
- ✗ **D. Run the positive inspection for Create a hierarchical namespace boundary and apply it to Validate private endpoint access. In addition, use as justification the claim that any command from the same lane proves the current checkpoint.** — The applicable design condition is that the positive inspection for Create a hierarchical namespace boundary. In the decision record, it is lane-correct but proves Create a hierarchical namespace boundary, not Validate private endpoint access.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q47 — answer B

A review of 'Validate private endpoint access' begins with input from data platform engineering. A passing positive check does not by itself prove this negative assertion: Public network access is not retained to compensate for a missing dfs endpoint or DNS record. Which recommendation delivers the assertion pair that proves both conditions independently?

- ✗ **A. Verify only the positive result for Validate private endpoint access and report full compliance; as an independent condition, treat as decisive the assertion that every prohibited parallel state must therefore be absent.** — The retained result must be reconciled with the fact that the dfs private endpoint is approved, private DNS resolves correctly, and the default network action is deny. In the decision record, the positive result alone does not test the explicit anti-condition 'Public network access is not retained to compensate for a missing dfs endpoint or DNS record'.
- ✓ **B. Verify the positive properties for Validate private endpoint access. Separately, independently verify that public network access is not retained to compensate for a missing dfs endpoint or DNS record.** — The review is governed by this fact: the dfs private endpoint is approved, private DNS resolves correctly, and the default network action is deny; Public network access is not retained to compensate for a missing dfs endpoint or DNS record. In the decision record, two independent observations prevent a passing positive check from concealing an unsafe parallel state.
- ✗ **C. Prove only that public network access is not retained to compensate for a missing dfs endpoint or DNS record and report the intended configuration as present; as another gate, base approval on the claim that absence is equivalent to positive-state evidence.** — The decision tension comes from the fact that public network access is not retained to compensate for a missing dfs endpoint or DNS record. In the decision record, absence evidence cannot demonstrate the required positive state 'The dfs private endpoint is approved, private DNS resolves correctly, and the default network action is deny'.
- ✗ **D. Use Design filesystem and directory ownership's negative assertion for Validate private endpoint access. Then, use the premise that negative assertions are interchangeable between checkpoints.** — The safe operating boundary says that world-writable paths and user-owned production directories are absent. In the decision record, the second assertion is valid for Design filesystem and directory ownership but leaves this checkpoint's prohibited state untested.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q48 — answer D

'Validate private endpoint access' awaits approval from supplier integration team. The board wants the Well-Architected consequence of mitigating this risk: Only a blob endpoint exists, so hierarchical namespace operations resolve or authorize inconsistently. Which response meets the need for the consequence attributable to this checkpoint?

- ✗ **A. Use the Define encryption and key dependency consequence as the result for Validate private endpoint access, and then accept without proof that a pillar statement remains valid when moved away from Define encryption and key dependency.** — The failure model establishes that cost Optimization: customer-managed keys are adopted only when custody requirements justify their lifecycle overhead. In the decision record, that tradeoff belongs to Define encryption and key dependency and does not explain this checkpoint's decision.
- ✗ **B. Remove the control responsible for the Validate private endpoint access outcome. Also, rely on the claim that a moderate cost classification outweighs the mandatory architecture state.** — The recovery guidance assumes that the required outcome at Validate private endpoint access. In the decision record, cost Optimization cannot remove the acceptance condition 'The dfs private endpoint is approved, private DNS resolves correctly, and the default network action is deny'.
- ✗ **C. Treat 'Security: denied public access and explicit dfs connectivity constrain unintended data paths' as proof that all five pillars pass; in a separate step, rely on the belief that the checkpoint 'Validate private endpoint access' no longer needs its separate negative check.** — The WAF consequence identifies that public network access is not retained to compensate for a missing dfs endpoint or DNS record. In the decision record, one positive command cannot establish every pillar, especially while the negative state remains unchecked.
- ✓ **D. Record this consequence: Security: denied public access and explicit dfs connectivity constrain unintended data paths; before closing the checkpoint, tie it to LAB11-REQ-05.** — The traceable checkpoint outcome is that security: denied public access and explicit dfs connectivity constrain unintended data paths. In the decision record, it states the authored pillar consequence of the control evaluated at Validate private endpoint access.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q49 — answer D

'Validate private endpoint access' is reopened at the request of analytics consumers. A material change now applies: The legal department introduces collaborative document shares that require native SMB locking and Windows ACL behavior, but analytics ingestion must remain object-native; revise the service boundaries. Which choice should be approved as the correct revision to the decision record?

- ✗ **A. Retain ADLS Gen2 on a hierarchical-namespace StorageV2 account at Validate private endpoint access without recalculating criteria or eligibility. In addition, consider it sufficient that the original weighted result is permanent.** — aDLS Gen2 on a hierarchical-namespace StorageV2 account. The independent assertion shows why the original ADR remains historical evidence, but its score cannot answer a changed mandatory condition.
- ✗ **B. Select Flat Azure Blob Storage containers with prefix conventions for Validate private endpoint access without rechecking its mandatory constraints; before approval, take it as conclusive that being different from the current design is an architecture criterion.** — The controlling fact is that flat Azure Blob Storage containers with prefix conventions. The independent assertion shows why being different is not a criterion, and the candidate still must avoid the prohibited state at Validate private endpoint access.
- ✗ **C. Keep Azure Files shares mounted by analytics and document clients eligible at Validate private endpoint access by downgrading LAB11-REQ-05. Separately, treat it as established that stakeholder approval is unnecessary when that requirement blocks the candidate.** — The authored acceptance boundary states that lAB11-REQ-05. The independent assertion shows why an architect cannot silently downgrade a stakeholder-owned mandatory requirement to protect a candidate.
- ✓ **D. Re-score ADLS Gen2 on a hierarchical-namespace StorageV2 account and both alternatives for Validate private endpoint access. Independently, supersede the ADR using the changed evidence for LAB11-REQ-05.** — The command-level assertion is anchored in the fact that aDLS Gen2 on a hierarchical-namespace StorageV2 account at Validate private endpoint access. In the decision record, the material change 'The legal department introduces collaborative document shares that require native SMB locking and Windows ACL behavior, but analytics ingestion must remain object-native; revise the service boundaries.' requires fresh eligibility, weighted analysis, and a superseding decision.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)

## LAB11-Q50 — answer A

A design review of 'Validate private endpoint access' includes information security. After a partial run, cleanup must follow this dependency: Remove private DNS records and endpoints before the account; preserve shared network resources. What should the team use as the dependency-safe cleanup plan?

- ✓ **A. Verify exact run-state IDs and ownership tags for Validate private endpoint access; in a separate step, follow this dependency rule without purge: Remove private DNS records and endpoints before the account; preserve shared network resources.** — The relevant observation is that remove private DNS records and endpoints before the account; preserve shared network resources. The independent assertion shows why exact identity, complete ownership tags, and the authored dependency order constrain cleanup and preserve recovery.
- ✗ **B. Apply the cleanup rule for Create a hierarchical namespace boundary before reconciling the current dependency. Then, proceed on the belief that removing a parent needed to identify Validate private endpoint access is harmless.** — The checkpoint specifically records that delete run-owned filesystems and private endpoints before deleting the account. The independent assertion shows why a cleanup rule for Create a hierarchical namespace boundary cannot override the dependency declared for Validate private endpoint access.
- ✗ **C. Delete candidates by display name before comparing the Validate private endpoint access ownership tags; afterward, treat as decisive the assertion that the dependency rule 'Remove private DNS records and endpoints before the account; preserve shared network resources' is optional.** — The scenario makes clear that endpoint ID, dfs group, approval state, subnet, private DNS label, and network default action. The independent assertion shows why names are not ownership proof; deletion requires the exact recorded identifier and every required tag.
- ✗ **D. Destroy recoverable copies before retaining the Validate private endpoint access negative assertion 'Public network access is not retained to compensate for a missing dfs endpoint or DNS record'; then base approval on the claim that remaining command logs are sufficient recovery evidence.** — The architecture evidence must show that public network access is not retained to compensate for a missing dfs endpoint or DNS record. The independent assertion shows why irreversible purge is outside the lab contract and destroys evidence needed for residual-state validation.

Remediation: [checkpoint-5](../README.md#checkpoint-5)

Source: https://learn.microsoft.com/en-us/azure/storage/blobs/data-lake-storage-introduction (verified 2026-09-02)
<!-- END GENERATED AZ305 V1 -->
