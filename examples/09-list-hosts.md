# Example 09: List Hosts

## Brief Overview

Retrieve all hypervisor hosts (nodes) across all clusters or for a specific cluster. Provides visibility into the physical infrastructure layer.

## Use Case

- **Hardware inventory** - Track all physical servers
- **Capacity planning** - Understand per-node resources
- **Maintenance planning** - Identify nodes for maintenance
- **Troubleshooting** - Check host health status

## Desired Outcome

List of all hosts with names, cluster membership, capacity, and versions.

## Validation Criteria

- All hosts are returned
- Each host has cluster association
- Hardware details are populated

---

## Prompt

### List All Hosts

```
List all hosts across all clusters
```

### Hosts with Full Details

```
List all hosts with the following details:
- Host name
- Cluster it belongs to
- Number of CPU cores
- Total memory
- Hypervisor version
- Hardware model
```

### Hosts in Specific Cluster

```
List all hosts in the cluster named "Production-Cluster-01"
```

### Host Health Status

```
Show me all hosts and their current status. Flag any hosts that are:
- In maintenance mode
- Degraded
- Have recent hardware alerts
```

---

## Host States

| State | Description |
|-------|-------------|
| `NORMAL` | Host is operational |
| `IN_MAINTENANCE` | Host in maintenance mode |
| `DEGRADED` | Host has issues |

## Related Operations

- [List Clusters](07-list-clusters.md)
- [Get Cluster Details](08-get-cluster-details.md)
