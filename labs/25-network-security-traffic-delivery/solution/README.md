<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-25 solution rationale

The recommended architecture is **Front Door Premium, Application Gateway WAF v2, Azure Firewall Premium, Standard Load Balancer, and NAT Gateway** with a weighted total of 94/100. Layered global, regional, east-west, and explicit outbound services provide native WAF, TLS inspection, FQDN policy, and failure-domain controls. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Traffic Manager, regional WAF gateways, NSG-only inspection, Standard Load Balancer, and NAT Gateway:** The model cannot meet the new outbound inspection requirement without adding another control plane.
- **Front Door Standard, third-party NVAs behind Gateway Load Balancer, and centralized proxy egress:** Equivalent controls carry greater lifecycle and routing complexity than the managed-service design.
- **Basic Load Balancer implicit outbound with unrestricted internet egress:** It is ineligible because current-service and mandatory outbound requirements are unmet.

## Risks and mitigations

- **A broad TLS bypass for the pinned vendor can become an unmonitored exfiltration route.** — Scope bypass to exact FQDN and flow identity, retain SNI and connection logs, and review vendor certificate changes.
- **Centralized inspection can exhaust SNAT ports or throughput during a regional event.** — Calculate peak concurrent flows, distribute NAT capacity, and load-test the surviving zone and regional path.

## Initial Well-Architected consequences

- **reliability:** Layered health probes, zonal capacity, regional routing, and explicit outbound remove implicit traffic dependencies.
- **security:** Premium WAF, firewall FQDN policy, TLS inspection, and a narrow pinned-certificate exception enforce flow intent.
- **costOptimization:** Premium controls apply to classified clinical paths and capacity follows measured throughput and connection demand.
- **operationalExcellence:** Effective routes, rule hits, certificates, probes, NAT ports, and exception ownership form the network evidence set.
- **performanceEfficiency:** Each hop and inspection stage is measured so security does not silently consume the clinical latency budget.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: Clinical security now requires outbound allowlisting by FQDN and TLS inspection for update traffic, but one vendor uses certificate pinning and cannot tolerate interception.

The revised decision is **Front Door Premium, Application Gateway WAF v2, Azure Firewall Premium, Standard Load Balancer, and NAT Gateway**. LAB25-REQ-02 requires owned FQDN and TLS inspection policy, so the selected design adds an exact pinned-vendor bypass with independent logging and expiry review. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** The vendor exception remains reachable through explicit redundant outbound paths.
- **security:** All other update traffic is inspected and the bypass is constrained to the exact destination.
- **costOptimization:** Premium inspection spend remains tied to clinical flows instead of a blanket enterprise rollout.
- **operationalExcellence:** Rule hits, certificates, owner, and review date make the exceptional path auditable.
- **performanceEfficiency:** Inspection and bypass latency are tested independently against clinical response needs.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
