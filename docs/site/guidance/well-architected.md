# Well-Architected review

Use all five Azure Well-Architected Framework pillars for every decision. A statement about one pillar cannot stand in for another, and an improvement often transfers cost or complexity elsewhere.

| Pillar | Ask | Useful evidence | Common hidden trade-off |
| --- | --- | --- | --- |
| Reliability | What fails, at what scope, and how does service recover? | Failure-domain map, recovery test, RTO/RPO assertion | Extra replicas without a tested recovery process |
| Security | Which identities, networks, data paths, and control planes are trusted? | Denied-path test, role assignment review, encryption configuration | Operational bypass introduced for convenience |
| Cost Optimization | Which meters, commitments, retention, egress, and idle capacity dominate? | Assumption-based estimate, budget threshold, utilization review | Paying for redundancy that does not meet the target |
| Operational Excellence | How is change observed, approved, rolled back, and learned from? | Deployment record, alert routing, runbook exercise, ADR history | A managed service with unclear team ownership |
| Performance Efficiency | Which latency, throughput, concurrency, and scaling signals matter? | Load model, percentile target, scaling behavior | Peak tuning that creates sustained idle cost |

## Cross-pillar method

For each candidate, write one consequence per pillar in concrete terms. Then describe at least one interaction, such as private networking improving security while increasing name-resolution and connectivity operations, or multi-region replication improving recovery while increasing write latency and transfer cost.

## Evidence test

Phrase each claim so it can fail. “Highly available” is not testable; “the design tolerates one zonal fault and recovers within the stated RTO without data loss beyond the stated RPO” is testable. Pair that positive assertion with a negative one, such as proving no single-zone dependency remains on the critical path.

See the [Azure Well-Architected Framework](https://learn.microsoft.com/en-us/azure/well-architected/) for current primary guidance. This repository freezes its source registry for offline validation; revisit service guidance before a future production decision.
