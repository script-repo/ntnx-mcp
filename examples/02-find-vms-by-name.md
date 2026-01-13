# Example 02: Find Virtual Machines by Name

## Brief Overview

Search for virtual machines using name patterns or exact matches. Uses OData filtering to efficiently locate VMs without retrieving the entire inventory.

## Use Case

- **Locate specific VMs** - Find a VM when you know part of the name
- **Environment grouping** - Find all VMs for a specific environment (dev, prod, test)
- **Application discovery** - Find all VMs related to an application
- **Troubleshooting** - Quickly locate a problem VM

## Desired Outcome

A filtered list of VMs matching the search criteria, returning only relevant results instead of the full inventory.

## Validation Criteria

- Response contains only VMs matching the filter
- Filter syntax is correctly applied
- Results are returned quickly (< 2 seconds)
- Empty result set if no matches (not an error)

---

## Prompt

### Exact Name Match

```
Find the virtual machine named "web-server-01"
```

### Contains Search

```
Find all virtual machines with "prod" in their name
```

### Prefix Search

```
Find all virtual machines whose names start with "db-"
```

### Environment Pattern

```
Find all virtual machines that belong to the production environment. 
Look for VMs with names containing "prod" or "production"
```

### Multiple Conditions

```
Find all virtual machines that:
1. Have "app" in their name
2. Are currently powered on
3. Have at least 4 vCPUs
```

---

## OData Filter Examples

| Search Type | Filter Syntax |
|-------------|---------------|
| Exact match | `name eq 'web-server-01'` |
| Contains | `contains(name, 'prod')` |
| Starts with | `startswith(name, 'db-')` |
| Ends with | `endswith(name, '-backup')` |
| Multiple conditions | `contains(name, 'prod') and powerState eq 'ON'` |

## Related Operations

- [List All VMs](01-list-all-vms.md)
- [Get VM Details](03-get-vm-details.md)
