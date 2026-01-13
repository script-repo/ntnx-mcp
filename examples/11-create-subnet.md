# Example 11: Create a Subnet (Network)

## Brief Overview

Create a new network subnet for VM connectivity. This configures a VLAN-backed or overlay network with optional IPAM.

## Use Case

- **New environment setup** - Create networks for new projects
- **Network segmentation** - Isolate workloads
- **Application deployment** - Create dedicated app networks

## Desired Outcome

- New subnet is created on the specified cluster
- VLAN tagging is configured correctly
- IP configuration is set up (if specified)

## Validation Criteria

- Task completes successfully
- Subnet appears in network list
- Configuration matches requested specs

---

## Prompt

### Basic VLAN Network

```
Create a new VLAN network with these settings:
- Name: Development-VLAN200
- VLAN ID: 200
- Cluster: Production-Cluster-01
```

### Network with IP Configuration

```
Create a new network with full IP configuration:

Name: App-Network-VLAN150
VLAN ID: 150
Cluster: Production-Cluster-01

IP Configuration:
- Network: 10.150.0.0/24
- Gateway: 10.150.0.1
- IP Pool: 10.150.0.100 to 10.150.0.200
```

---

## Required Information

| Requirement | How to Get It |
|-------------|---------------|
| Cluster ID | `List all clusters` |
| Available VLAN ID | Check with network team |
| IP Subnet | Assign from your IP plan |

## Related Operations

- [List Networks](10-list-networks.md)
- [List Clusters](07-list-clusters.md)
