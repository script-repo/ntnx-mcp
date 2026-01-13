# Example 19: List Security Policies (Flow)

## Brief Overview

Retrieve Flow microsegmentation security policies. These policies control network traffic between VMs based on categories and rules.

## Use Case

- **Security audit** - Review network security rules
- **Compliance** - Verify segmentation policies
- **Troubleshooting** - Check why traffic is blocked
- **Policy planning** - Understand current security posture
- **Change management** - Review before modifications

## Desired Outcome

List of security policies with rules, categories, and enforcement status.

## Validation Criteria

- All policies are listed
- Policy rules are visible
- Enforcement mode is shown
- Category associations are clear

---

## Prompt

### List All Policies

```
List all Flow microsegmentation security policies
```

### Policies with Details

```
List all security policies with:
- Policy name
- Enforcement mode (monitor/enforce)
- Number of rules
- Categories it applies to
- Last modified date
```

### Enforced Policies Only

```
Show only security policies that are actively enforcing rules 
(not in monitor mode)
```

### Policies for Specific App

```
Find security policies that apply to VMs with category "AppType:WebServer"
```

### Policy Audit

```
Generate a security policy audit report:
1. Total number of policies
2. Policies in enforce mode vs monitor mode
3. Any policies with no rules defined
4. Policies modified in the last 30 days
```

---

## Expected Response

```json
{
  "data": [
    {
      "extId": "policy-uuid-...",
      "name": "Web-Tier-Isolation",
      "description": "Isolate web tier from database tier",
      "mode": "ENFORCE",
      "rules": [
        {
          "action": "ALLOW",
          "srcCategory": "AppTier:Web",
          "dstCategory": "AppTier:App",
          "protocol": "TCP",
          "port": 8080
        }
      ],
      "appliedTo": [
        {"category": "AppTier:Web"}
      ]
    }
  ]
}
```

## Related Operations

- [List All VMs](01-list-all-vms.md) - VMs affected by policies
- [List Active Alerts](14-list-active-alerts.md) - Security alerts
