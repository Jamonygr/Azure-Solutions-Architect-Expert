<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-05 solution rationale

The recommended architecture is **Azure Key Vault Premium with RBAC and private endpoints** with a weighted total of 88/100. Premium vaults provide HSM-backed keys, secret and certificate management, managed-identity access, and a bounded private application interface. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Azure Managed HSM with centralized HSM administration:** The initial shared application scope does not justify moving every asset into a costlier key-only HSM pool.
- **Application-owned encrypted configuration in general-purpose storage:** It provides weaker centralized control and creates duplicated key-management code across payment applications.
- **Plaintext secrets in deployment variables and source-controlled parameters:** The proposal is ineligible because it cannot meet the mandatory secret-protection boundary.

## Risks and mitigations

- **Enabling a private endpoint without validated name resolution can make the vault unreachable to payment workloads.** — Test private DNS resolution and a permitted managed-identity operation before disabling the public path.
- **Separating Managed HSM administration can leave too few trained recovery officers.** — Assign independent deputies, rehearse quorum and recovery procedures, and monitor administrator-role expiry.

## Initial Well-Architected consequences

- **reliability:** Soft delete, purge protection, tested rotation, and explicit HSM recovery ownership reduce key-loss outages.
- **security:** RBAC, private endpoints, managed identities, and a separate single-tenant HSM boundary enforce cryptographic least privilege.
- **costOptimization:** Premium vaults remain the economical shared service and Managed HSM is limited to the workload that mandates it.
- **operationalExcellence:** Expiry inventory, rotation alerts, and recovery drills turn cryptographic lifecycle into an auditable runbook.
- **performanceEfficiency:** Applications reuse managed identities and private endpoints while key-operation throughput is benchmarked per service.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: The acquired card-processing workload requires single-tenant FIPS-validated HSM administration and cannot share the payment application vault boundary; revise the selected service and operating model.

The revised decision is **Azure Managed HSM with centralized HSM administration**. LAB05-REQ-01 makes the cryptographic service boundary a mandatory decision, so the acquired processor selects single-tenant Managed HSM while shared secrets and certificates remain in Key Vault. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Dedicated HSM recovery officers and drills become necessary for the acquired workload.
- **security:** The processor receives a nonshared HSM trust and administration boundary.
- **costOptimization:** Only mandated processor keys incur the continuously allocated HSM cost.
- **operationalExcellence:** Two service inventories and escalation paths must be maintained without mixing ownership.
- **performanceEfficiency:** Processor key-operation throughput is sized independently from ordinary vault transactions.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
