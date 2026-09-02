# Permissions guide

Architecture work separates the identity that designs a change, the identity that deploys it, and the identity that validates or approves it. Granting broad rights to make a lab convenient defeats the authorization learning outcome.

## Plan by control plane

| Plane | Typical concern | Design question |
| --- | --- | --- |
| Azure Resource Manager | Resource creation, configuration, policy, and RBAC | What is the narrowest scope and action set for deployment? |
| Microsoft Graph | Directory objects, applications, groups, and governance | Is a tenant-wide directory permission truly required? |
| Data plane | Secrets, blobs, queues, databases, logs, and messages | Does the workload need data access, management access, or both? |
| CI/CD | Federated identity, deployment approvals, and artifact integrity | Can a short-lived workload identity replace a stored credential? |
| Operations | Monitoring, incident response, backup, and recovery | Who can observe, restore, and break glass, and how is use reviewed? |

## Permission worksheet

For each checkpoint, record the operation, plane, target scope, built-in role or Graph scope, whether it is read or write, approval owner, and removal condition. If the exact least-privilege role is uncertain, treat it as an assumption to validate rather than defaulting to Owner or a broad directory role.

## Separation and escalation

- Keep policy definition, policy assignment, and exemption approval distinguishable.
- Separate Key Vault management rights from secret, key, and certificate data access.
- Separate backup configuration from restore approval when the recovery path is sensitive.
- Prefer eligible, time-bound privileged access where organizational controls support it.
- Record Graph consent type and approval ownership before requesting a scope.
- Make emergency access explicit, monitored, and tested; it is not a normal deployment identity.

The repository never signs in, grants a role, requests Graph consent, or tests a live permission. A future operator must verify current role actions, deny assignments, policy effects, privileged access controls, and service-specific data-plane rules before execution.
