<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-20 solution rationale

The recommended architecture is **Service Bus for commands, Event Grid for state events, Event Hubs for telemetry, and API Management for partners** with a weighted total of 94/100. Purpose-specific services map ordered commands, routed events, high-throughput telemetry, and governed partner APIs to their native semantics. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Event Hubs as the transport for all commands, events, telemetry, and partner requests:** Uniform transport simplifies inventory at the cost of weak command and partner semantics.
- **Storage queues and direct partner webhooks with application-owned routing:** Custom routing and direct partner exposure produce the weakest security and operating fit.
- **Synchronous depot-to-carrier call chain with no durable broker:** It is ineligible because a downstream outage can lose or reject an accepted shipment command.

## Risks and mitigations

- **A shipment session can block behind one poison command and delay all later updates for that shipment.** — Bound delivery attempts, dead-letter with full correlation, and require an idempotent repair and replay procedure.
- **Tenfold telemetry can consume shared namespace or network capacity needed by commands.** — Isolate telemetry units and quotas from Service Bus, then load-test each path independently.

## Initial Well-Architected consequences

- **reliability:** Durable sessions, dead letters, isolated subscriptions, and idempotent consumers preserve shipment processing.
- **security:** APIM policy, managed identities, and recipient-specific subscriptions constrain partner and event access.
- **costOptimization:** Broker features and capacity are purchased per message class instead of overengineering telemetry or commands.
- **operationalExcellence:** Correlation IDs join API acceptance, command settlement, state events, telemetry, and repair actions.
- **performanceEfficiency:** Event Hubs absorbs tenfold telemetry while Service Bus session capacity scales on ordered shipment demand.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: A carrier contract now requires commands for each shipment to remain ordered while also sustaining ten times the telemetry volume during peak season.

The revised decision is **Service Bus for commands, Event Grid for state events, Event Hubs for telemetry, and API Management for partners**. LAB20-REQ-05 makes per-shipment ordering and tenfold telemetry isolation mandatory, so the selected split-service design adds Service Bus sessions while scaling Event Hubs separately. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Session ordering and durable settlement protect shipment state through retries.
- **security:** Partner APIs and event subscribers retain separate authorization boundaries.
- **costOptimization:** Only telemetry processing units rise for the seasonal peak.
- **operationalExcellence:** Correlation and dead-letter evidence expose stalled sessions without hiding later failures.
- **performanceEfficiency:** Commands and telemetry scale on different units and cannot consume the same broker ceiling.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
