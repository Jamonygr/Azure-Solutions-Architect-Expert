# Evidence discipline

Evidence connects a design claim to an observable result. It must be sufficient for a reviewer, safe to retain, and honest about whether it is synthetic, offline, or live.

<figure class="az305-visual">
  <img src="../assets/infographics/evidence-chain.svg" alt="Evidence chain pairing each checkpoint with independent positive and negative assertions and a sanitized result record">
  <figcaption>Evidence is useful when it is independent, attributable, minimal, and traceable.</figcaption>
</figure>

## Pair every assertion

For each checkpoint, keep two independent assertions:

- a **positive assertion** proves the intended object, relationship, policy, route, or behavior exists;
- a **negative assertion** proves a prohibited path, overly broad grant, unsafe setting, or residual object does not exist.

One command returning an object rarely proves both. Separate commands and separate result records prevent a false positive from hiding an unsafe condition.

## Evidence envelope

Record only the minimum fields needed to interpret the assertion:

| Field | Purpose |
| --- | --- |
| Lab and checkpoint ID | Trace to the learning and requirement contract |
| Run ID | Separate independent attempts |
| Assertion kind | Distinguish positive from negative proof |
| Result and timestamp | Show the observation and when it occurred |
| Sanitized subject | Identify the design object without exposing an account |
| Interpretation | State what the result proves and what it does not prove |

## Never retain

Do not commit or import tokens, secrets, passwords, cookies, private keys, connection strings, SAS values, tenant or subscription identifiers, account information, real resource IDs, unsanitized command output, or live screenshots. Use unmistakably synthetic reserved UUIDs and `.invalid` names in fixtures.

## Evidence levels

- **offline contract evidence** — schema, generated-file, arithmetic, safety, or fixture result;
- **simulation evidence** — deterministic reasoning or a local model of the intended architecture;
- **live verification evidence** — an authorized observation from a real environment, sanitized before retention.

Never relabel the first two as live verification. A built site and green test suite prove consistency of this repository, not current Azure behavior, quota, permissions, regional availability, or price.

## Cleanup evidence

Cleanup first proves exact ID and ownership through `purpose=az305-lab`, `labId`, `runId`, and `expiresOn`. It then processes dependencies in reverse order and records each result. The final negative assertion requires zero active managed objects. Uncertain ownership is a refusal condition, not a reason to widen deletion scope.
