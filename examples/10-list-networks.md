# Example 10: List Networks (Subnets)

## Brief Overview

Retrieve all network subnets configured in Prism Central. Networks are required for VM NIC configuration.

## Use Case

- **VM provisioning** - Find network for new VM deployment
- **Network documentation** - Inventory all configured networks
- **Troubleshooting** - Verify network configuration
- **IPAM management** - Check IP pool availability

## Desired Outcome

List of all subnets with names, VLAN IDs, IP configuration, and cluster association.

## Validation Criteria

- All subnets are returned
- Each subnet has `extId` and `name`
- Network configuration is populated

---

## Prompt

### List All Networks

```
List all networks (subnets) in Prism Central
```

### Networks with Full Details

```
List all networks with:
- Network name and ID
- VLAN ID
- Network address and prefix
- Gateway IP
- DHCP configuration
- IP pool ranges
```

### Networks for Specific Cluster

```
List all networks available on cluster "Production-Cluster-01"
```

### Find Network by Name

```
Find the network named "Production-VLAN100"
```

---

## Subnet Types

| Type | Description |
|------|-------------|
| `VLAN` | Traditional VLAN-backed network |
| `OVERLAY` | Software-defined overlay network |

## Related Operations

- [Create a Subnet](11-create-subnet.md)
- [Create a New VM](04-create-new-vm.md)
