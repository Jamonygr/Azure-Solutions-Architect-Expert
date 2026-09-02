# Quick-start path

Use this route when you want a safe tour of the environment before committing to the full curriculum. Allow roughly six focused sessions.

## Session 1 — learn the contract

Complete **LAB-00**. Inspect the four lifecycle scripts, run preview-only preflight and setup, and explain why state must exist before a potential mutation. Confirm the three exit codes: `0` for success, `1` for failed assertions, and `2` for a gated or partial outcome requiring review.

Deliverable: a one-page note describing execution acknowledgements, state ownership, validation modes, and idempotent cleanup.

## Sessions 2–5 — sample every domain

| Session | Lab | Architecture muscle |
| ---: | --- | --- |
| 2 | LAB-03 | Identity boundaries, External ID, and tenant-scoped change control |
| 3 | LAB-12 | Storage economics, protection, durability, and measurable trade-offs |
| 4 | LAB-16 | RTO/RPO translation and relational continuity choices |
| 5 | LAB-24 | Internet and hybrid connectivity, routing, and negative-path evidence |

For each lab, complete all five checkpoints and write three sentences: the selected candidate, the strongest rejected candidate, and the requirement that separates them.

## Session 6 — integrate

Open **LAB-26** and complete the design pass without executing a deployment. Trace at least one objective from each domain to a requirement, checkpoint, evidence item, and WAF consequence.

## Ready for the full path?

Continue when you can do all of the following without referring to a command transcript:

- distinguish a requirement from an implementation preference;
- explain why a weighted winner can still be ineligible;
- name a positive and a negative assertion for the same design claim;
- describe why cleanup checks identity and ownership separately;
- state when the CLI lane, PowerShell lane, or Graph v1.0 commands are appropriate.

Move next to the [full-exam path](full-exam.md) or the [job-ready path](job-ready.md).
