# Job-ready architect path

The certification blueprint is the syllabus; the deliverables below make the practice transferable to architecture work. Use the full requirements and decision artifacts rather than treating a service name as the answer.

## Portfolio packet

For one lab in each domain, produce a sanitized packet containing:

- a requirement set with stakeholder, outcome, constraints, assumptions, SLO, RTO/RPO, scale, latency, and budget facts;
- a candidate matrix with criteria totaling 100, integer scores from 1–5, disqualifiers, and weighted totals;
- an ADR with selected and rejected alternatives, risks, mitigations, and all five WAF pillars;
- an evidence index that pairs every checkpoint with one positive and one negative assertion;
- a material-change addendum showing the mandatory requirement that justified any override;
- a cleanup record that proves no active managed object remains.

Synthetic values and `.invalid` names are appropriate. Do not include tenant identifiers, subscription identifiers, account data, tokens, secrets, live command output, or unsanitized screenshots.

## Review conversation

Practice a ten-minute design review in this order:

1. State the business outcome and two non-negotiable constraints.
2. Describe the failure modes that shaped the topology.
3. Name the selected candidate and the strongest rejected alternative.
4. Explain the discriminating requirements and operational ownership.
5. Walk one positive and one negative assertion.
6. Describe cost drivers and the safe analogue.
7. Apply the material change and say whether the ADR must change.

## Capstone sequence

Use **LAB-26** for a greenfield, multi-region platform recommendation. Use **LAB-27** for an offline hybrid-modernization simulation with migration waves and rollback gates. Compare the two: greenfield work optimizes a target state; modernization work must also preserve dependencies, coexistence, cutover, rollback, and organizational readiness.

Finish by checking the [permissions](../guides/permissions.md), [cost](../guides/cost.md), [evidence](../guidance/evidence.md), and [troubleshooting](../guides/troubleshooting.md) guides as if another engineer must execute your design.
