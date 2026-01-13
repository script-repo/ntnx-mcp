# Example 16: View Recent Events

## Brief Overview

Retrieve the event log showing system activities, changes, and occurrences. Events provide an audit trail of what happened in the environment.

## Use Case

- **Troubleshooting** - Trace what happened before an issue
- **Change tracking** - See what was modified and when
- **Security auditing** - Review system activities
- **Compliance** - Maintain audit trail for regulations
- **Root cause analysis** - Correlate events with issues

## Desired Outcome

List of events with timestamps, sources, and descriptions showing system activity history.

## Validation Criteria

- Events are returned in chronological order
- Event details include source entity
- Timestamps are accurate
- Event descriptions are meaningful

---

## Prompt

### Recent Events

```
Show me the last 50 events from the past 24 hours
```

### Events for Specific VM

```
Show all events related to VM "prod-database-01" in the past week
```

### Events by Type

```
Show all VM power state change events from today
```

### Events for Troubleshooting

```
A user reported issues with VM "app-server-01" around 2pm today.
Show me all events for that VM between 1pm and 4pm.
```

### Cluster Events

```
Show all events for cluster "Production-Cluster-01" in the last 4 hours
```

---

## Expected Response

```json
{
  "data": [
    {
      "extId": "event-uuid-...",
      "eventType": "VM_POWER_ON",
      "message": "VM 'web-server-01' was powered on",
      "createdTime": "2024-06-20T14:30:00Z",
      "sourceEntity": {
        "extId": "vm-uuid-...",
        "entityType": "VM",
        "name": "web-server-01"
      },
      "cluster": {
        "name": "Production-Cluster-01"
      }
    }
  ]
}
```

## Related Operations

- [List Active Alerts](14-list-active-alerts.md) - Current issues
- [Get VM Details](03-get-vm-details.md) - VM information
