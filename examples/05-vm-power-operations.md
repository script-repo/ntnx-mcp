# Example 05: VM Power Operations

## Brief Overview

Control the power state of virtual machines including power on, power off, graceful shutdown, reset, and reboot.

## Use Case

- **Maintenance windows** - Gracefully shut down VMs for updates
- **Troubleshooting** - Reset hung VMs
- **Cost management** - Power off unused VMs
- **Deployment** - Start newly created VMs

## Desired Outcome

- VM power state changes as requested
- Graceful operations allow guest OS to shut down properly
- Task ID returned for tracking

## Validation Criteria

- Task status shows "SUCCEEDED"
- VM power state reflects the requested change
- For graceful operations, guest OS shuts down cleanly

---

## Prompt

### Power On a VM

```
Power on the virtual machine named "prod-web-server-01"
```

### Power Off (Hard)

```
Power off the VM named "test-server" immediately
```

### Graceful Shutdown

```
Gracefully shut down the VM named "prod-database-01"
```

### Graceful Reboot

```
Gracefully reboot the VM named "web-server-02"
```

### Reset (Hard Reboot)

```
Reset the VM named "hung-application-server"
```

---

## Power Operation Types

| Operation | Method | Description |
|-----------|--------|-------------|
| Power On | `vmm_power_on` | Start a powered-off VM |
| Power Off | `vmm_power_off` | Hard power off (immediate) |
| Guest Shutdown | `vmm_guest_shutdown` | Graceful OS shutdown via NGT |
| Guest Reboot | `vmm_guest_reboot` | Graceful OS reboot via NGT |
| Reset | `vmm_reset` | Hard reset |

## Related Operations

- [Get VM Details](03-get-vm-details.md)
- [List Active Alerts](14-list-active-alerts.md)
