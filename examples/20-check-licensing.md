# Example 20: Check Licensing Status

## Brief Overview

Retrieve licensing information including license compliance, feature entitlements, and expiration dates.

## Use Case

- **License compliance** - Verify proper licensing
- **Capacity planning** - Check licensed vs used capacity
- **Renewal planning** - Track expiration dates
- **Feature availability** - Verify entitled features
- **Audit preparation** - Generate license reports

## Desired Outcome

Licensing summary showing compliance status, entitlements, and expiration information.

## Validation Criteria

- License status is reported
- Compliance state is clear
- Expiration dates are visible
- Feature entitlements are listed

---

## Prompt

### License Summary

```
Show me the licensing summary for this Prism Central environment
```

### Detailed License Status

```
Show licensing details including:
- License type (Starter, Pro, Ultimate)
- Compliance status
- Licensed capacity
- Used capacity
- Expiration date
- Enabled features
```

### Compliance Check

```
Check if we are in compliance with our Nutanix licensing.
Show any over-utilization or upcoming expirations.
```

### Feature Entitlements

```
What features are we entitled to with our current license?
Show which premium features are enabled vs disabled.
```

### Expiration Warning

```
Are any licenses expiring in the next 90 days?
If so, show which ones and their expiration dates.
```

---

## Expected Response

```json
{
  "data": {
    "licenseType": "PRISM_PRO",
    "complianceStatus": "COMPLIANT",
    "expirationDate": "2025-12-31T00:00:00Z",
    "licensedCapacity": {
      "nodes": 50,
      "capacityTiB": 500
    },
    "usedCapacity": {
      "nodes": 12,
      "capacityTiB": 150
    },
    "features": {
      "flowMicrosegmentation": true,
      "prismPro": true,
      "disasterRecovery": true,
      "filesStorage": false
    }
  }
}
```

## License Types

| Type | Features |
|------|----------|
| Starter | Basic monitoring, VM management |
| Pro | Prism Pro analytics, Flow microseg |
| Ultimate | All features including DR |

## Related Operations

- [List Clusters](07-list-clusters.md) - Nodes being licensed
- [List Storage Containers](12-list-storage-containers.md) - Capacity being licensed
