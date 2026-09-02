# Licensing guide

Licensing is an architecture constraint when a control exists only in a particular service tier, identity plan, support plan, or commercial offer. Do not infer entitlement from a product name in a scenario.

<figure class="az305-visual">
  <img src="../assets/infographics/licensing-boundary.svg" alt="Licensing boundary connecting required capability, covered population, service tier, availability, evidence date, and fallback design">
  <figcaption>Treat entitlement as a dated, testable architecture input with a fallback.</figcaption>
</figure>

## Licensing decision record

Capture these facts before scoring candidates:

1. required capability and the user, workload, or resource population it covers;
2. service tier or license that enables the capability;
3. unit and counting rule, including guests, administrators, replicas, or protected instances;
4. regional or sovereign-cloud availability;
5. trial, preview, retirement, or migration status;
6. procurement owner and evidence date;
7. fallback design if the entitlement is unavailable.

## Avoid common category errors

- A role assignment is not a product license.
- An Azure resource SKU is not the same as a Microsoft Entra user entitlement.
- A security recommendation being available in documentation does not prove it is enabled in the tenant’s plan.
- A free or development tier may not support the resilience, networking, retention, or SLA requirement used in production.
- A bundled benefit can have activation, scope, or consumption conditions.

## Evidence and freshness

Use the source registry as the offline baseline, then verify the current official product terms, pricing page, and service documentation before a real recommendation. Record the date and the specific capability checked. Because licensing can change independently of code, a repository gate cannot validate entitlement.

For lab work, prefer a design simulation or safe analogue when validating licensing would require purchasing, tenant-wide configuration, or exposing organization data.
