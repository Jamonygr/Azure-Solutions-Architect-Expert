<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-17 solution rationale

The recommended architecture is **Cosmos DB multi-region writes with zone redundancy plus GZRS Blob Storage** with a weighted total of 93/100. Multi-write Cosmos DB supports global editorial availability and explicit conflicts while GZRS protects and serves public objects. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Single write region with secondary reads plus RA-GRS Blob Storage and manual failover:** Its slower recovery and manual decision path are weaker for active global editorial operations.
- **Independent regional data stacks synchronized by an application-owned event log:** The custom synchronization burden is not justified before the new restricted-content boundary appears.
- **Replicate every document and media object to all regions:** It is disqualified because restricted-document replication would breach the mandatory rights agreement.

## Risks and mitigations

- **Misclassification can send a restricted document into globally replicated public storage.** — Enforce classification at ingestion and assert account, container, and replication placement before publication.
- **Multi-write conflict resolution can preserve a technically valid but editorially wrong version.** — Use deterministic domain rules, retain conflicting versions, and require an editor-owned reconciliation workflow.

## Initial Well-Architected consequences

- **reliability:** Multi-region document writes and global public media delivery reduce regional outage while exposing conflict behavior.
- **security:** Classification and country-bound storage keep rights-controlled content out of global replication paths.
- **costOptimization:** Replication and throughput are allocated by content class instead of copying every object worldwide.
- **operationalExcellence:** Conflict, classification, failover, and publication evidence make regional recovery auditable.
- **performanceEfficiency:** Public objects use globally distributed retrieval while restricted content avoids unnecessary egress and replicas.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: A new rights agreement forbids document replication outside one country, but global consumers must still retrieve public media within two seconds.

The revised decision is **Independent regional data stacks synchronized by an application-owned event log**. LAB17-REQ-03 makes object replication boundaries explicit, so restricted documents move to an independent in-country stack while public media remains globally distributed. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Public media stays multi-region while restricted content accepts the documented in-country failure domain.
- **security:** Rights-controlled bytes never enter the cross-region event or blob replication path.
- **costOptimization:** Only globally consumable media carries worldwide replication and egress cost.
- **operationalExcellence:** Classification and event-contract tests become mandatory publication gates.
- **performanceEfficiency:** Edge-served public media meets the two-second target without exporting restricted documents.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
