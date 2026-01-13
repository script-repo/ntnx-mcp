# Example 15: Acknowledge Alert

## Brief Overview

Mark an alert as acknowledged to indicate someone is aware of the issue and working on it. This helps teams track alert ownership and response.

## Use Case

- **Incident management** - Track who is handling an issue
- **Team coordination** - Prevent duplicate investigation efforts
- **SLA tracking** - Record response time to alerts
- **Shift handoffs** - Document which alerts are being worked

## Desired Outcome

- Alert is marked as acknowledged
- Acknowledgment timestamp is recorded
- Alert remains visible until resolved
- Other team members know it's being handled

## Validation Criteria

- Alert status shows "ACKNOWLEDGED"
- Acknowledgment time is recorded
- Alert still appears in active alert list
- Operation completes without error

---

## Prompt

### Acknowledge Single Alert

```
Acknowledge the alert with ID "alert-uuid-123..."
```

### Acknowledge by Finding Alert First

```
Find the critical alert about disk space on Production-Cluster-01 
and acknowledge it. I'm working on adding storage.
```

### Acknowledge Multiple Alerts

```
Acknowledge all warning alerts related to storage capacity - 
I'm aware of the issue and have a storage expansion scheduled.
```

### Acknowledge with Context

```
Acknowledge the alert "Host memory utilization high" for host ahv-node-03.
Note: This is expected due to month-end batch processing.
```

---

## Expected Response

```json
{
  "data": {
    "extId": "alert-uuid-...",
    "status": "ACKNOWLEDGED",
    "acknowledgedTime": "2024-06-20T14:30:00Z"
  }
}
```

## Related Operations

- [List Active Alerts](14-list-active-alerts.md) - Find alerts to acknowledge
- [View Recent Events](16-view-events.md) - See related events
