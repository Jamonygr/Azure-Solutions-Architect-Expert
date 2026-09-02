# Assessment dashboard

Track the five checkpoints for all 28 labs and an optional score for each 50-question bank in Labs 01–25. Foundation Lab 00 and Capstones 26–27 are intentionally unscored.

!!! warning "Private, local, and explicit"
    Progress is stored only in this browser under `az305LearnerProgress.v1`. It is never sent to analytics, a server, Azure, Microsoft Graph, or the CLI. Browser and CLI progress do not synchronize. Use the explicit JSON export and import buttons to move progress yourself.

<div id="az305-progress-app">
JavaScript is required for the private progress controls. The lab content and assessment pages remain readable without it.
</div>

## Import contract

An import must be valid JSON no larger than 256 KiB, contain exactly LAB-00 through LAB-27, and give each lab exactly five boolean checkpoint values. A completion flag must agree with those five values. Only LAB-01 through LAB-25 may contain an integer score from 0 through 50 or `null`.

The importer recursively rejects fields whose names indicate credentials, secrets, tokens, connection strings, private keys, account identifiers, or prototype-pollution keys. Invalid input never replaces the saved record.

## Interpreting results

Use a score to choose remediation, not as a badge. Review the mapped checkpoint for each miss, state why every option is right or wrong under the scenario, and retry after a delay. The learner page does not contain answers; answer keys are intentionally excluded from the staged site and its search index.
