# Example 07: List Clusters

## Brief Overview

Retrieve all Nutanix clusters managed by Prism Central. This provides visibility into the entire infrastructure across multiple sites.

## Use Case

- **Infrastructure overview** - See all managed clusters
- **Capacity planning** - Review cluster resources
- **VM placement decisions** - Choose the right cluster for new VMs
- **Health monitoring** - Quick check on cluster status

## Desired Outcome

A list of all clusters with names, IDs, node counts, and versions.

## Validation Criteria

- Response includes all expected clusters
- Each cluster has `extId` and `name`
- Configuration details are populated

---

## Prompt

### Basic Cluster List

```
List all clusters managed by this Prism Central
```

### Detailed Cluster Information

```
List all clusters with the following details:
- Cluster name and ID
- Number of hosts/nodes
- Hypervisor type and version
- AOS version
- Total CPU and memory capacity
```

### Find Specific Cluster

```
Find the cluster named "Production-Cluster-01" and show me its configuration
```

### Cluster Comparison

```
List all clusters and compare their:
- Total vs used CPU capacity
- Total vs used memory capacity
- Total vs used storage capacity
```

---

## Expected Response Structure

```json
{
  "data": [
    {
      "extId": "cluster-uuid-...",
      "name": "Production-Cluster-01",
      "nodes": {
        "numberOfNodes": 4
      },
      "build": {
        "fullVersion": "7.0.0.1"
      }
    }
  ]
}
```

## Related Operations

- [Get Cluster Details](08-get-cluster-details.md)
- [List Hosts](09-list-hosts.md)
- [Create a New VM](04-create-new-vm.md)
