# Example 14: List Active Alerts

## Brief Overview

Retrieve all active alerts in Prism Central to monitor infrastructure health. Alerts indicate issues requiring attention.

## Use Case

- **Daily health checks** - Morning review of infrastructure
- **Incident response** - Investigate reported issues
- **Proactive monitoring** - Catch problems early
- **SLA compliance** - Track and resolve alerts

## Desired Outcome

List of active alerts with severity, description, and affected entities.

## Validation Criteria

- All active alerts are returned
- Severity levels are categorized
- Affected entities are identified

---

## Prompt

### List All Active Alerts

```
List all active alerts in Prism Central
```

### Alerts by Severity

```
List all active alerts, sorted by severity (critical first)
```

### Critical Alerts Only

```
Show me only critical alerts that need immediate attention
```

### Alerts for Specific Cluster

```
Show all active alerts for cluster "Production-Cluster-01"
```

### Alert Summary

```
Give me an alert summary:
1. Total number of active alerts
2. Count by severity (critical, warning, info)
3. Top 5 most common alert types
```

---

## Alert Severity Levels

| Severity | Description | Response Time |
|----------|-------------|---------------|
| `CRITICAL` | Immediate impact | Immediate |
| `WARNING` | Potential issue | Within hours |
| `INFO` | Informational | Review periodically |

## Related Operations

- [Acknowledge Alert](15-acknowledge-alert.md)
- [View Recent Events](16-view-events.md)
