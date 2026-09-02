# Searchable lab catalog

Filter by lab ID, title, domain, command lane, or implementation mode. The catalog is staged from `curriculum/lab-catalog.yml`; it is not maintained by hand.

<figure class="az305-visual">
  <img src="assets/infographics/exam-domains.svg" alt="AZ-305 lab catalog organized into foundation, four blueprint domains, and capstones">
  <figcaption>Navigate from foundation through four domain waves and two synthesis capstones.</figcaption>
</figure>

<div class="az305-domain-gallery" aria-label="Four AZ-305 design domains">
  <figure class="az305-visual"><img src="assets/visuals/domain-identity-governance-monitoring.png" alt="Isometric identity, governance, and monitoring architecture"><figcaption>Identity, governance, and monitoring</figcaption></figure>
  <figure class="az305-visual"><img src="assets/visuals/domain-data.png" alt="Isometric data storage, integration, protection, and analytics architecture"><figcaption>Data storage and integration</figcaption></figure>
  <figure class="az305-visual"><img src="assets/visuals/domain-continuity.png" alt="Isometric dual-region availability, backup, replication, and recovery architecture"><figcaption>Business continuity</figcaption></figure>
  <figure class="az305-visual"><img src="assets/visuals/domain-infrastructure.png" alt="Isometric network, compute, application, and hybrid infrastructure architecture"><figcaption>Infrastructure</figcaption></figure>
</div>

<label for="az305-catalog-filter"><strong>Filter labs</strong></label><br>
<input id="az305-catalog-filter" class="az305-filter" data-az305-catalog-filter type="search" autocomplete="off" placeholder="Try networking, PowerShell, or safe-analogue">
<p class="az305-muted" data-az305-catalog-count aria-live="polite">28 labs shown</p>

<!-- BEGIN GENERATED AZ305 DOCS CATALOG -->
Catalog rows are inserted by the deterministic documentation staging tool.
<!-- END GENERATED AZ305 DOCS CATALOG -->

## Mode legend

- **reference-deployable** — a bounded reference implementation is available; preview remains the default.
- **safe-analogue** — the lab exercises the architecture contract through a deliberately constrained substitute.
- **design-simulation** — the learning outcome is achieved offline through design, evidence, and change analysis.

The catalog status `offline-validated` does not imply live tenant verification.
