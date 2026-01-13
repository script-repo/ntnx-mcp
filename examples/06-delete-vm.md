# Example 06: Delete a Virtual Machine

## Brief Overview

Permanently remove a virtual machine and its associated virtual disks from the cluster. This operation is irreversible.

## Use Case

- **Decommissioning** - Remove end-of-life VMs
- **Cleanup** - Delete test or temporary VMs
- **Cost reduction** - Remove unused resources

## Desired Outcome

- VM is permanently deleted
- Associated virtual disks are removed
- Storage space is reclaimed

## Validation Criteria

- Task status shows "SUCCEEDED"
- VM no longer appears in VM list
- No orphaned disks remain

---

## Prompt

### Delete by ID

```
Delete the virtual machine with ID "abc123-def456-..."
```

### Delete by Name (Safe Approach)

```
I want to delete the VM named "old-test-server".

First, find the VM and show me its details so I can confirm it's the right one.
Then proceed with deletion only after I confirm.
```

### Delete with Verification

```
Delete the VM named "decom-web-01" but first:
1. Confirm the VM is powered off
2. Show me the VM's disk sizes
3. Check if there are any snapshots
4. Then proceed with deletion
```

---

## Pre-Deletion Checklist

| Check | Prompt |
|-------|--------|
| Power state | `Is VM "name" powered off?` |
| Snapshots | `Does VM "name" have any snapshots?` |
| Protection policy | `Is VM "name" protected?` |

> ⚠️ **Warning**: VM deletion cannot be undone. Ensure you have backups if needed.

## Related Operations

- [Get VM Details](03-get-vm-details.md)
- [Power Operations](05-vm-power-operations.md)
