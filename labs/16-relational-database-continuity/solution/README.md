<!-- BEGIN GENERATED AZ305 V1 -->
# LAB-16 solution rationale

The recommended architecture is **Azure SQL Database failover group with zone-redundant primary and secondary databases** with a weighted total of 92/100. Failover groups provide listener-based application continuity and managed regional database relationships with zonal protection. The matrix is an aid to judgment; a disqualifier always overrides a numerical score.

## Rejected alternatives

- **Active geo-replication with application-managed endpoints and failover:** Application-managed endpoint and database coordination adds recovery steps that threaten the shorter RTO.
- **SQL Server on Azure Virtual Machines with an Always On availability group:** The extra infrastructure operations are unnecessary for the managed-database workload and increase recovery complexity.
- **Backups with manual DNS switching and no continuously replicated secondary:** It is ineligible because backup restore cannot prove the mandatory RTO and RPO combination.

## Risks and mitigations

- **Doubled log generation can increase replication lag beyond the five-minute data-loss window.** — Load-test the peak write profile, monitor lag, and size both databases and network dependencies for the observed rate.
- **The database listener can fail over while application configuration or secrets remain region-bound.** — Test the API transaction through all regional dependencies and treat any failed business assertion as recovery failure.

## Initial Well-Architected consequences

- **reliability:** Zonal databases, regional replication, listener failover, and application checks cover layered failure domains.
- **security:** Encrypted connections, private access, identity, and audit controls apply in both primary and secondary regions.
- **costOptimization:** Secondary capacity is a funded RPO/RTO control and can serve approved reads rather than remain entirely idle.
- **operationalExcellence:** Lag, failover, DNS, API transaction, and failback timestamps form the recovery scorecard.
- **performanceEfficiency:** Both regions are sized and tested for doubled write throughput instead of assuming replication keeps pace.

## Evidence interpretation

Each checkpoint has an independent positive assertion and negative assertion. A resource existing does not prove that an unintended route, trust path, region, tier, or residual object is absent. Preserve only the sanitized evidence named by the checkpoint.

## Change response

The deterministic change request is: A new flash-sale contract doubles peak write volume and requires the reservation API to recover within fifteen minutes rather than one hour.

The revised decision is **Azure SQL Database failover group with zone-redundant primary and secondary databases**. LAB16-REQ-05 now requires fifteen-minute application recovery under doubled writes, so the failover group is retained with peak-tested secondary capacity and prevalidated dependency routing. Update the ADR rather than editing the original evidence trail.

### Revised Well-Architected consequences

- **reliability:** Peak-tested lag and application failover protect both the five-minute RPO and fifteen-minute RTO.
- **security:** Secondary-region identities, private paths, and auditing are validated before an incident.
- **costOptimization:** Higher standby capacity is explicitly tied to the contracted flash-sale continuity target.
- **operationalExcellence:** Automated connection and business checks replace manual endpoint edits.
- **performanceEfficiency:** Capacity evidence covers doubled writes and the replication work they generate.

## Live-verification boundary

This solution is offline-validated. It contains no live evidence and does not claim that an Azure or Microsoft Graph request succeeded. `lastLiveVerified` remains `null`.
<!-- END GENERATED AZ305 V1 -->
