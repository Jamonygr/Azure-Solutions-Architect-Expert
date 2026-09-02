# Project plan and maintenance rhythm

The April 17, 2026 AZ-305 blueprint is frozen in `curriculum/blueprint.yml`. Maintainers should recheck the official study guide before changing an objective, lab ownership, source verification date, or tested tool version.

The release sequence is foundation, Lab 00, identity/governance/monitoring, data, business continuity, infrastructure, capstones and documentation, then the complete offline gate. A wave is releasable only when its authored content, generated artifacts, assessment bank, diagrams, fixtures, safety tests, and source mappings pass together.

Live verification is a separate, opt-in activity performed by a future owner in an authorized disposable environment. It must never be inferred from offline validation or recorded by hand-editing generated `lab.yml` files. A future live-verification release must update the authoritative catalog, generator, schema, and validator policy consistently, regenerate every affected artifact, and retain independently reviewed, redacted evidence containing no identifiers or credentials.
