# Migration field guide

Migration is a controlled change to a business system, not a copy command. The target architecture, dependency map, coexistence period, data movement, cutover, rollback, and operating ownership must agree.

## Discovery to waves

1. **Discover** workloads, identities, network flows, data stores, certificates, schedules, and operational dependencies.
2. **Assess** compatibility, performance baseline, business criticality, RTO/RPO, compliance, cost, and team readiness.
3. **Choose a strategy** for each workload: retain, retire, rehost, relocate, replatform, refactor, rebuild, or replace.
4. **Design the landing boundary** for hierarchy, policy, identity, networking, monitoring, protection, and cost ownership.
5. **Group waves** by dependencies and blast radius, not organizational convenience alone.
6. **Rehearse** data sync, cutover, validation, rollback, and communications with measurable gates.
7. **Transition operations** only when monitoring, backup, access, runbooks, and ownership are accepted.
8. **Decommission** after the agreed observation period and a verified rollback decision.

## Data movement choices

Compare online and offline transfer against dataset size, daily change rate, available bandwidth, transfer window, encryption, chain of custody, downtime tolerance, and validation method. A fast bulk seed can still fail the migration if final synchronization and reconciliation are undefined.

For databases, separate schema compatibility, log or change replication, application cutover, connection handling, and rollback. For unstructured data, preserve metadata and authorization semantics in addition to object bytes.

## Cutover gate

A credible gate has an owner and an observable threshold. Include dependency health, replication lag, data reconciliation, authentication, critical transaction paths, performance percentiles, monitoring visibility, backup status, and business approval. Define the last reversible point before the event begins.

## Safe practice

LAB-22 is a design simulation. LAB-23 uses safe analogues for workload and data migration. LAB-27 integrates hybrid discovery, waves, rollback, and target-state decisions offline. No repository test starts a migration appliance, moves tenant data, or changes a live endpoint.

Use the current [Azure Migrate documentation](https://learn.microsoft.com/en-us/azure/migrate/) before production planning.
