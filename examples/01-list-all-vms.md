# Example 01: List All Virtual Machines

## Brief Overview

Retrieve a complete inventory of all virtual machines managed by Prism Central. This is typically the first operation when exploring a Nutanix environment or performing infrastructure audits.

## Use Case

- **Infrastructure audits** - Get a complete list of VMs for documentation
- **Capacity planning** - Understand current VM footprint
- **Migration planning** - Inventory VMs before migration projects
- **Compliance reporting** - Generate VM lists for security reviews

## Desired Outcome

A JSON response containing all virtual machines with key properties including:
- VM name and ID
- Power state (ON/OFF)
- CPU and memory configuration
- Cluster assignment
- Creation timestamp

## Validation Criteria

- Response includes `data` array with VM objects
- Each VM has `extId`, `name`, and `powerState` fields
- Response includes pagination metadata
- No error messages in the response

---

## Prompt

### Basic - List All VMs

```
List all virtual machines in Prism Central
```

### With Limit - First 50 VMs

```
List the first 50 virtual machines in Prism Central, sorted by name
```

### Detailed - With Specific Fields

```
List all virtual machines in Prism Central. For each VM, show me:
- Name
- Power state
- Number of vCPUs
- Memory size
- Cluster it belongs to
- When it was created

Sort the results by name in ascending order and limit to 100 results.
```

### Power State Filter - Only Running VMs

```
List all virtual machines that are currently powered on
```

### Resource Filter - High Memory VMs

```
List all virtual machines that have more than 16 GB of memory allocated
```

---

## Expected Response Structure

```json
{
  "data": [
    {
      "extId": "abc123-def456-...",
      "name": "web-server-01",
      "powerState": "ON",
      "numSockets": 1,
      "numCoresPerSocket": 4,
      "memorySizeBytes": 8589934592,
      "cluster": {
        "extId": "cluster-uuid-..."
      },
      "createTime": "2024-01-15T10:30:00Z"
    }
  ]
}
```

## Related Operations

- [Find VMs by Name](02-find-vms-by-name.md)
- [Get VM Details](03-get-vm-details.md)
- [Power Operations](05-vm-power-operations.md)
