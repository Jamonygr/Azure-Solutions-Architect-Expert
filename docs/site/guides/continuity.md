# Business continuity field guide

Begin with business impact. Service labels such as “zone redundant” or “geo replicated” are design inputs; they are not a recovery strategy by themselves.

<figure class="az305-visual">
  <img src="../assets/infographics/continuity-targets.svg" alt="Continuity design connecting business impact, failure scope, RTO, RPO, replication, backup, and recovery exercises">
  <figcaption>Recovery targets become credible only when dependencies, sequencing, and tests agree.</figcaption>
</figure>

## Translate impact into targets

| Input | Question | Resulting decision |
| --- | --- | --- |
| Maximum tolerable outage | When does interruption become unacceptable? | Recovery time objective and recovery sequence |
| Maximum tolerable data loss | How much committed work may be lost? | Recovery point objective and replication or backup frequency |
| Failure scope | Component, zone, region, tenant, operator, or dependency? | Isolation boundary and recovery topology |
| Consistency need | Can reads be stale or writes conflict during failover? | Replication and application behavior |
| Recovery dependency | Which identity, DNS, key, network, and control plane must still work? | Independent or protected supporting services |
| Exercise tolerance | How often can recovery be tested? | Automation, drill design, evidence, and cost |

## High availability, backup, and disaster recovery

- **High availability** reduces interruption for anticipated local failures.
- **Backup** preserves recoverable versions against deletion, corruption, or destructive change.
- **Disaster recovery** restores an acceptable business service after a larger failure.

One does not imply the others. Replicating corruption is not backup; a backup with an untested multi-day restore may not meet RTO; regional capacity without dependency recovery may not produce a working application.

## Recovery design checklist

- Map every critical dependency and its recovery order.
- State whether failover is automatic, operator-approved, or business-approved.
- Define data reconciliation and split-brain prevention.
- Protect recovery credentials, keys, configuration, DNS, and monitoring.
- Test both failover and failback.
- Capture independent assertions for recovered service and absence of stale or unsafe routes.
- Include backup immutability, retention, deletion protection, and restore authorization where required.
- Price normal operation, test operation, and disaster operation separately.

LAB-14 through LAB-17 apply these principles to hybrid workloads, compute, relational data, and semi-structured or unstructured data. Consult current [Azure reliability guidance](https://learn.microsoft.com/en-us/azure/reliability/) before a live design.
