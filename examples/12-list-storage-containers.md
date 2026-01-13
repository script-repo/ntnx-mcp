# Example 12: List Storage Containers

## Brief Overview

Retrieve all storage containers across clusters. Storage containers are the logical storage pools where VM disks are stored.

## Use Case

- **Storage capacity planning** - Review available storage
- **VM provisioning** - Choose storage for new VMs
- **Performance analysis** - Check container utilization

## Desired Outcome

List of storage containers with capacity, utilization, and configuration.

## Validation Criteria

- All containers are listed
- Capacity metrics are present
- Cluster associations are correct

---

## Prompt

### List All Storage Containers

```
List all storage containers across all clusters
```

### Containers with Capacity Details

```
List all storage containers with:
- Container name
- Cluster it belongs to
- Total capacity
- Used space
- Free space
- Utilization percentage
```

### Capacity Report

```
Generate a storage capacity report:
1. List all storage containers
2. Total capacity across all containers
3. Total used space
4. Containers over 80% utilization
```

---

## Storage Container Properties

| Property | Description |
|----------|-------------|
| `capacityBytes` | Total raw capacity |
| `usedBytes` | Space currently used |
| `freeBytes` | Available space |
| `compressionEnabled` | Inline compression |

## Related Operations

- [List Volume Groups](13-list-volume-groups.md)
- [List Clusters](07-list-clusters.md)
