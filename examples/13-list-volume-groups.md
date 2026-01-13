# Example 13: List Volume Groups

## Brief Overview

Retrieve all volume groups (VGs) in the environment. Volume groups provide block storage attachable to VMs or external hosts via iSCSI.

## Use Case

- **Shared storage** - View shared disk configurations
- **Database clusters** - Manage Oracle RAC or SQL FCI storage
- **External host storage** - Track iSCSI volumes
- **Capacity management** - Monitor volume group usage

## Desired Outcome

List of volume groups with capacity, attachments, and iSCSI information.

## Validation Criteria

- All volume groups are listed
- Capacity information is present
- Attachment details are shown

---

## Prompt

### List All Volume Groups

```
List all volume groups
```

### Volume Groups with Details

```
List all volume groups with:
- Volume group name and ID
- Total capacity
- Number of virtual disks
- Which VMs or clients are attached
- iSCSI target information
```

### Attached vs Unattached

```
List all volume groups and indicate:
1. Which have VMs attached
2. Which have iSCSI initiators connected
3. Which are not attached to anything
```

---

## Common Use Cases

| Use Case | Configuration |
|----------|---------------|
| Oracle RAC | Shared VG with multiple VMs |
| SQL Server FCI | Shared VG for cluster storage |
| External backup | iSCSI target for physical server |

## Related Operations

- [List Storage Containers](12-list-storage-containers.md)
- [List All VMs](01-list-all-vms.md)
