# Cost-control guide

Cost Optimization begins with workload facts and ownership, not a price lookup. The labs use bounded examples in West Europe and North Europe, but no offline fixture claims a current charge.

## Build the cost model

Model the units that change the bill:

- provisioned and consumed compute, including scale floor and peak duration;
- stored data, operations, transactions, indexing, backup copies, and retention;
- inter-zone, inter-region, hybrid, and internet transfer;
- gateway, firewall, private endpoint, public IP, and inspection hours;
- logs, metrics, traces, ingestion, archive, search, and export;
- recovery replicas, reserved capacity, savings plans, and licensing benefits;
- nonproduction uptime, test frequency, and abandoned resources.

State quantity, unit, region, term, utilization assumption, and source date. Use ranges when demand is uncertain and sensitivity-test the largest driver.

## Execution safeguards

A cost-bearing path requires both `-Execute` and `-AcknowledgeCost`. That acknowledgement is not a budget approval; it confirms the operator crossed the lab’s explicit safety gate. Preview the intended resources, confirm quota and regional availability, set an expiry tag, and define cleanup before deployment.

## Decision traps

- Lowest hourly rate can be the most expensive option after operations, transfer, or idle capacity.
- Redundancy adds value only when it satisfies a tested availability or recovery target.
- Aggressive log retention can obscure a missing evidence or compliance requirement.
- A managed service can reduce operating cost while increasing direct service spend.
- A reservation is a forecast commitment, not automatic savings.

Before a future live exercise, use the current [Azure pricing calculator](https://azure.microsoft.com/en-us/pricing/calculator/) and service pricing pages. Record assumptions; never commit an organization’s billing export or account identifiers.
