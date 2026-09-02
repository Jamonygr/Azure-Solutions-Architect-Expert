# Architecture decisions and ADRs

An architecture recommendation is a traceable response to requirements, not a preferred product list. Every lab uses the same decision chain:

<figure class="az305-visual">
  <img src="../assets/infographics/decision-workflow.svg" alt="Architecture decision workflow from requirements and eligibility through weighted analysis, ADR, evidence, and revision">
  <figcaption>A defensible decision keeps constraints, scoring, alternatives, and change history visible.</figcaption>
</figure>

`objective → requirement → candidate eligibility → weighted analysis → ADR → checkpoint → evidence`

## Start with discriminating requirements

A useful requirement can change the choice. Record who needs the outcome, the metric or boundary, and how acceptance will be tested. Separate these categories:

- **functional** — a capability the system must provide;
- **nonfunctional** — reliability, security, performance, operating, or cost quality;
- **constraint** — a boundary such as region, identity, skill, regulatory, or coexistence limits;
- **assumption** — a fact that needs validation and may change the decision.

Mark a requirement mandatory only when failure makes a candidate unacceptable. A mandatory requirement is the only valid basis for overriding the weighted winner in this curriculum.

## Eliminate before scoring

Evaluate disqualifiers first. A candidate that cannot meet a mandatory data-residency, recovery, network, identity, or operating constraint is ineligible even if its feature or cost score is attractive. Record the reason so a later reviewer can distinguish deliberate rejection from omission.

## Use the common scoring model

Each decision uses five criteria whose weights total 100. Scores are integers from 1 through 5. The normalized total is:

`sum(weight × score) / 5`

A total communicates relative fit under the stated facts. It does not erase uncertainty, make an ineligible design eligible, or replace professional judgment. Sensitivity-check the most important criterion: if a one-point change reverses the result, call out that fragility.

## Write the ADR

The ADR records context, decision, selected candidate, rejected alternatives, risks, mitigations, evidence expectations, and consequences across all five WAF pillars. Keep the original decision legible. When the material change request introduces a mandatory requirement, record a revised decision and cite that requirement rather than silently rewriting history.

## Review questions

1. Which requirement most strongly separates the top two eligible candidates?
2. Is any assumption masquerading as a verified fact?
3. Does each disqualifier point to a mandatory requirement?
4. Can each checkpoint produce both positive and negative evidence?
5. Who owns the operating model, cost review, and recovery test after handoff?
