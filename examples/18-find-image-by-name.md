# Example 18: Find Image by Name

## Brief Overview

Search for a specific disk image by name to get its ID for VM deployment or to verify image availability.

## Use Case

- **VM deployment prep** - Get image ID for VM creation
- **Verification** - Confirm an image exists before automation
- **Version selection** - Find the right version of an OS image
- **Troubleshooting** - Verify image is available for failed deployments

## Desired Outcome

Find the specific image and retrieve its ID and details for use in VM creation.

## Validation Criteria

- Image is found by name/pattern
- Image ID (extId) is returned
- Image details match expectations
- Image is in usable state

---

## Prompt

### Exact Name Match

```
Find the image named "ubuntu-22.04-template"
```

### Partial Name Search

```
Find all images with "windows" in the name
```

### Find and Get ID

```
Find the image "rhel-9-golden" and give me its ID so I can use it to create a VM
```

### Version Search

```
Find all Ubuntu images and show which versions are available
```

### Find for VM Creation

```
I need to create a new Windows Server 2022 VM.
Find the appropriate image and show me its ID.
```

---

## Expected Response

```json
{
  "data": [
    {
      "extId": "image-uuid-abc123...",
      "name": "ubuntu-22.04-template",
      "type": "DISK_IMAGE",
      "sizeBytes": 5368709120,
      "description": "Ubuntu 22.04 LTS - Updated June 2024"
    }
  ]
}
```

## Using the Image ID

After finding the image:

```
Now create a VM using image ID "image-uuid-abc123...":
- Name: new-ubuntu-server
- 4 vCPUs, 8 GB RAM
- Cluster: Production-Cluster-01
```

## Related Operations

- [List Images](17-list-images.md) - View all images
- [Create a New VM](04-create-new-vm.md) - Deploy using image
