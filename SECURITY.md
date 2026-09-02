# Security and privacy

Do not report Azure service vulnerabilities here; use the Microsoft Security Response Center. For repository issues, open a private security advisory in the future owner’s GitHub project.

This learning environment never stores credentials. Lifecycle state may contain only resource IDs, non-secret input values, original non-secret settings, and ownership tags. It is excluded by `.gitignore`. Scripts never request or persist tokens and never sign in automatically.

The browser dashboard stores progress only under `az305LearnerProgress.v1`. JSON import and export are explicit user actions; nothing is transmitted automatically. Import is limited to 256 KiB, schema-checked, and recursively rejects keys associated with secrets, credentials, tokens, tenants, subscriptions, accounts, and personal data. Browser and CLI progress are intentionally separate and never synchronize silently.

Cleanup is deny-by-default. A managed object must match its exact recorded ID and all four tags: `purpose=az305-lab`, `labId`, `runId`, and `expiresOn`. Purge operations are never automated.
