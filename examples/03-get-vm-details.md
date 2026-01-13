# Example 03: Get Virtual Machine Details

## Brief Overview

Retrieve comprehensive details for a specific virtual machine using its ID. This provides complete configuration information including disks, NICs, guest tools status, and more.

## Use Case

- **Troubleshooting** - Investigate VM configuration issues
- **Documentation** - Record VM specifications
- **Change verification** - Confirm VM changes were applied
- **Capacity analysis** - Review resource allocation for a specific VM

## Desired Outcome

Complete VM configuration including:
- Hardware configuration (CPU, memory, disks, NICs)
- Power state and boot configuration
- Guest OS information
- Protection policy status
- Categories/tags applied

## Validation Criteria

- Response contains the requested VM's full configuration
- `extId` matches the requested ID
- Disk and NIC arrays are populated (if configured)
- No error response (404 if VM doesn't exist)

---

## Prompt

### By VM ID

```
Get the details for virtual machine with ID "abc123-def456-789-xyz"
```

### By VM Name (Two-Step)

```
Find the VM named "prod-database-01" and show me its complete configuration including:
- CPU and memory settings
- All attached disks with sizes
- Network interfaces and IP addresses
- Guest tools status
- Protection policy
- Any categories or tags applied
```

### Specific Information

```
For the VM with ID "abc123-def456-789-xyz", show me:
1. The current power state
2. CPU configuration (sockets, cores)
3. Memory allocation
4. All disk sizes
5. Network configuration
```

---

## Expected Response Structure

```json
{
  "data": {
    "extId": "abc123-def456-...",
    "name": "prod-database-01",
    "powerState": "ON",
    "numSockets": 2,
    "numCoresPerSocket": 4,
    "memorySizeBytes": 34359738368,
    "nics": [...],
    "disks": [...],
    "guestTools": {
      "isInstalled": true
    }
  }
}
```

## Related Operations

- [Find VMs by Name](02-find-vms-by-name.md)
- [Power Operations](05-vm-power-operations.md)
