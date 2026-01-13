# Example 04: Create a New Virtual Machine

## Brief Overview

Provision a new virtual machine on Nutanix with specified CPU, memory, disk, and network configuration. This is an async operation that returns a task ID.

## Use Case

- **New application deployment** - Create VMs for new applications
- **Development environments** - Spin up dev/test VMs
- **Disaster recovery** - Recreate VMs from specifications
- **Scaling** - Add capacity for existing applications

## Desired Outcome

- A new VM is created with the specified configuration
- VM is placed on the designated cluster
- Network interface is connected to the specified subnet
- Task completes successfully

## Validation Criteria

- Response includes a `taskId` for tracking
- Task status eventually shows "SUCCEEDED"
- VM appears in VM list with correct name
- VM configuration matches requested specs

---

## Prompt

### Basic VM Creation

```
Create a new virtual machine with the following specifications:
- Name: test-web-server
- vCPUs: 4
- Memory: 8 GB
- Cluster: [your-cluster-id]
```

### Complete VM with All Options

```
Create a new virtual machine with these specifications:

Name: prod-app-server-01
Description: Production application server

Hardware:
- vCPUs: 8
- Memory: 32 GB
- Boot disk: 100 GB

Network:
- Connect to subnet ID: [your-subnet-id]

Deployment:
- Cluster ID: [your-cluster-id]
- Boot from image ID: [your-image-id]
```

### Get Prerequisites First

```
Before creating the VM, I need to gather some information:
1. List all clusters so I can choose where to deploy
2. List all subnets so I can select a network
3. List available images if I want to boot from a template
```

---

## Required Information

| Requirement | How to Get It |
|-------------|---------------|
| Cluster ID | `List all clusters` |
| Subnet ID | `List all networks/subnets` |
| Image ID | `List all images` |

## Related Operations

- [List Clusters](07-list-clusters.md)
- [List Networks](10-list-networks.md)
- [List Images](17-list-images.md)
