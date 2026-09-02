<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-24 solution rationale

The recommended architecture is **Front Door Premium with dual ExpressRoute connectivity, VPN failover, and Virtual WAN transit** with a weighted total of 91/100. Premium edge security, redundant private circuits, scaled VPN fallback, and managed transit form explicit customer and private failure paths. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Regional Application Gateway with internet VPN tunnels and manual branch routing:** It lacks the selected design's global edge and predictable automated transit behavior.
- **Front Door Standard with provider-managed SD-WAN and direct spoke connections:** Split provider and spoke controls make end-to-end private path evidence harder to establish.
- **One ExpressRoute circuit with unencrypted private traffic and undersized VPN:** It is ineligible because both encryption and backup-capacity requirements are mandatory.

## Risks and mitigations

- **Encryption overhead can reduce effective throughput below the four-hour peak requirement.** — Load-test encrypted circuit and VPN paths with production packet sizes and reserve measured headroom.
- **Advertised routes can prefer an unintended path and bypass inspection during failover.** — Capture effective routes and next hops for normal, circuit-loss, and recovery states before approval.

## Initial Well-Architected consequences

- **reliability:** Independent edge, dual-circuit, VPN, gateway, and route tests expose each connectivity failure domain.
- **security:** Premium edge controls and encrypted private transport protect both public entry and regulated transactions.
- **costOptimization:** Redundant circuits and full VPN capacity are tied to regulatory continuity instead of duplicated indiscriminately.
- **operationalExcellence:** Route, encryption, health, failover, and restoration evidence provide a deterministic network runbook.
- **performanceEfficiency:** Measured encrypted throughput sizes gateways and tunnels for the full four-hour peak.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: The payment regulator requires all private transaction traffic to remain encrypted in transit even over ExpressRoute, and the backup VPN must carry the full peak load for four hours.

The revised decision is **Front Door Premium with dual ExpressRoute connectivity, VPN failover, and Virtual WAN transit**. LAB24-REQ-02 requires explicit private-circuit and VPN failover design, so the selected path adds ExpressRoute encryption and a load-tested full-peak VPN capacity floor. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Full-capacity VPN prevents regulatory traffic from becoming a partial service during circuit loss.
- **security:** Transaction traffic remains encrypted on primary and fallback private paths.
- **costOptimization:** Higher gateway and encryption cost is attributed to the four-hour compliance objective.
- **operationalExcellence:** Normal, failure, and restoration route captures prove the intended path.
- **performanceEfficiency:** Gateway selection follows encrypted throughput measurements rather than nominal SKU bandwidth.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
