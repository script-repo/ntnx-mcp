# Nutanix MCP Server Examples

This folder contains 20 example prompts demonstrating common operations with the Nutanix Prism Central MCP server. Each example includes detailed documentation and copy-paste ready prompts.

## Categories

### Virtual Machine Management
1. [List All VMs](01-list-all-vms.md) - Inventory of all virtual machines
2. [Find VMs by Name](02-find-vms-by-name.md) - Search VMs using filters
3. [Get VM Details](03-get-vm-details.md) - Detailed VM information
4. [Create a New VM](04-create-new-vm.md) - Provision a new virtual machine
5. [Power Operations](05-vm-power-operations.md) - Power on/off/reset VMs
6. [Delete a VM](06-delete-vm.md) - Remove a virtual machine

### Cluster Management
7. [List Clusters](07-list-clusters.md) - View all managed clusters
8. [Get Cluster Details](08-get-cluster-details.md) - Cluster health and capacity
9. [List Hosts](09-list-hosts.md) - View all hypervisor hosts

### Networking
10. [List Networks](10-list-networks.md) - View available subnets
11. [Create a Subnet](11-create-subnet.md) - Provision a new network

### Storage
12. [List Storage Containers](12-list-storage-containers.md) - View storage resources
13. [List Volume Groups](13-list-volume-groups.md) - View volume groups

### Monitoring & Alerts
14. [List Active Alerts](14-list-active-alerts.md) - View current alerts
15. [Acknowledge Alert](15-acknowledge-alert.md) - Mark alert as acknowledged
16. [View Recent Events](16-view-events.md) - Audit trail of events

### Images & Templates
17. [List Images](17-list-images.md) - View available disk images
18. [Find Image by Name](18-find-image-by-name.md) - Search for specific images

### Security & Compliance
19. [List Security Policies](19-list-security-policies.md) - Flow microsegmentation policies
20. [Check Licensing Status](20-check-licensing.md) - License compliance

---

## How to Use These Examples

1. **Connect the MCP server** to your AI client (Amp, Claude Desktop, etc.)
2. **Configure credentials** for your Prism Central environment
3. **Copy the prompt** from the example file
4. **Paste and modify** the prompt with your specific values (VM names, IDs, etc.)
5. **Verify the results** using the validation criteria provided

## Tips

- Replace placeholder values like `your-vm-name` with actual values
- Use the OData filter examples to narrow down large result sets
- Check task IDs for async operations (create, delete, power operations)
- Start with read-only operations (list, get) before modifying resources

## Quick Reference

| Operation | Example Prompt |
|-----------|----------------|
| List VMs | `List all virtual machines` |
| Find VM | `Find VMs with "prod" in the name` |
| VM Details | `Get details for VM "web-server-01"` |
| Power On | `Power on VM "web-server-01"` |
| List Clusters | `List all clusters` |
| List Networks | `List all networks` |
| List Alerts | `Show all critical alerts` |
| Check Storage | `List storage containers with utilization` |
