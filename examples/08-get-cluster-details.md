# Example 08: Get Cluster Details

## Brief Overview

Retrieve comprehensive details for a specific Nutanix cluster including capacity, configuration, network settings, and health status.

## Use Case

- **Capacity analysis** - Detailed resource utilization
- **Troubleshooting** - Investigate cluster issues
- **Upgrade planning** - Check current versions
- **Documentation** - Record cluster specifications

## Desired Outcome

Complete cluster information including hardware, software versions, network config, and capacity.

## Validation Criteria

- Response contains the requested cluster
- All major configuration sections are populated
- Network configuration is complete
- Version information is present

---

## Prompt

### By Cluster ID

```
Get the complete details for cluster ID "abc123-def456-..."
```

### By Cluster Name

```
Find the cluster named "Production-Cluster-01" and show me all its details including:
- Number of hosts
- Total and available CPU capacity
- Total and available memory
- Total and available storage
- AOS and hypervisor versions
- Network configuration
```

### Capacity Deep Dive

```
For cluster "Main-Datacenter-Cluster", show me:
1. Current CPU utilization percentage
2. Current memory utilization percentage  
3. Current storage utilization percentage
4. How much room for new VMs
```

---

## Key Metrics

| Metric | Formula |
|--------|---------|
| CPU Utilization | (used / total) × 100 |
| Memory Utilization | (used / total) × 100 |
| Storage Utilization | (used / total) × 100 |

## Related Operations

- [List Clusters](07-list-clusters.md)
- [List Hosts](09-list-hosts.md)
