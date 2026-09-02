# Azure Solutions Architect Expert — AZ-305

A visual, architecture-first learning environment for the Microsoft AZ-305 blueprint effective April 17, 2026.

![Isometric overview of the AZ-305 learning environment, connecting identity, data, continuity, and infrastructure architecture](docs/site-assets/visuals/home-hero.png)

It contains 28 portable labs, maps every one of the 49 measured skills to one primary lab, and provides 1,250 original questions across Labs 01–25.

## Start here

1. Open the repository in its pinned development container.
2. Run `pwsh ./tools/Invoke-OfflineReleaseGate.ps1`.
3. Read [Lab 00](labs/00-safe-architect-bootstrap/README.md) before any lab that can deploy resources.
4. Start the documentation site with `mkdocs serve` for the catalog, maps, study plan, and private progress dashboard.

All lifecycle scripts are previews unless `-Execute` is supplied. Acknowledgement switches are also required for cost-bearing or tenant-scoped changes. No script signs in for you, no learner data is transmitted automatically, and cleanup refuses resources whose exact identity and ownership tags cannot be proven. Progress import and export are explicit JSON operations; browser and CLI progress never synchronize silently.

## Authoritative inputs

- `curriculum/blueprint.yml`: official objective wording, weights, and ownership.
- `curriculum/lab-catalog.yml`: fixed lab order, lane, mode, and navigation.
- `curriculum/content/*.yml`: authored scenarios, checkpoints, decisions, and architecture analysis.
- `curriculum/lab-content.yml`: deterministic aggregate generated from the authored content fragments.
- `curriculum/sources.yml`: frozen Microsoft source registry.
- `curriculum/commands.yml`: supported command families by lane.

Everything under a lab’s generated markers is reproducible. The pipeline assembles authored content, generates assessment banks and labs, renders diagrams and assessment pages, and stages the answer-free site. Run `pwsh ./tools/Invoke-OfflineReleaseGate.ps1` in the development container to check every generated surface. Content outside lab markers is preserved.

## Safety boundary

The repository’s release gate is entirely offline. Live Azure and Microsoft Graph verification is intentionally excluded from this implementation. Fixture identifiers are synthetic; generated evidence is never represented as live evidence. See [SECURITY.md](SECURITY.md) and [IMPLEMENTATION-REPORT.md](IMPLEMENTATION-REPORT.md).

## License

MIT © 2026 Jamon.
