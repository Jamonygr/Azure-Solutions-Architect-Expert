# AZ-305 architecture practice, offline first

<p class="az305-lede">Turn the 49 measured skills into repeatable architecture decisions, evidence, and explanations. The environment contains 28 portable labs, 25 assessment banks, two capstones, and one safety-first execution contract.</p>

!!! important "Offline validation is not live verification"
    Repository status proves structure, arithmetic, safety behavior, and fixture results. It does not prove that a command succeeded against an Azure tenant. Every lab begins in preview mode, and `lastLiveVerified` remains `null` until a future owner performs and records an authorized live verification.

<div class="az305-card-grid" markdown>
<div class="az305-card" markdown>

## Get oriented

Use the [quick-start path](paths/quick-start.md) to learn the lifecycle contract in Lab 00, then complete one representative lab from each domain.

</div>
<div class="az305-card" markdown>

## Cover the blueprint

Use the [full-exam path](paths/full-exam.md), [objective map](objective-map.md), and 1,250-question assessment set to close measured-skill gaps.

</div>
<div class="az305-card" markdown>

## Practice the role

Use the [job-ready path](paths/job-ready.md) to produce requirements, a decision matrix, an ADR, evidence, and a change response for both capstones.

</div>
</div>

## The learning loop

1. Translate the scenario into measurable requirements and mandatory constraints.
2. Disqualify candidates that cannot satisfy a mandatory requirement.
3. Score eligible candidates with the published criteria and inspect the trade-offs.
4. Walk the five checkpoints using the lab’s assigned command lane.
5. Prove a desired condition and the absence of an unsafe condition independently.
6. Respond to the material change request and revise the ADR when the decision changes.
7. Review cleanup ownership and residual state, then record local progress explicitly.

## Safety boundaries

- No script signs in on your behalf.
- Preview is the default; `-Execute` is the explicit mutation boundary.
- Cost-bearing and tenant-wide changes require separate acknowledgements.
- Cleanup requires exact managed IDs and all four ownership tags.
- The site uses no analytics or external active assets.
- Learner progress stays under one browser-local key and never synchronizes with CLI records.

Start with [Lab 00](labs/00-safe-architect-bootstrap/README.md) or choose a lab from the [searchable catalog](catalog.md).
