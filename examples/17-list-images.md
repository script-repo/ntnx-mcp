# Example 17: List Images

## Brief Overview

Retrieve all disk images stored in Prism Central. Images are templates used to create VM boot disks, including OS installations and golden images.

## Use Case

- **VM provisioning** - Find image for new VM deployment
- **Image management** - Inventory available templates
- **Version tracking** - Check OS versions available
- **Cleanup** - Identify old or unused images
- **Compliance** - Verify approved images are available

## Desired Outcome

List of images with names, sizes, types, and status.

## Validation Criteria

- All images are listed
- Image sizes are shown
- Image types are identified (ISO, DISK)
- Active/inactive status is clear

---

## Prompt

### List All Images

```
List all disk images in Prism Central
```

### Images with Details

```
List all images with:
- Image name
- Size (in GB)
- Image type (ISO or DISK)
- Creation date
- Description
```

### Find OS Images

```
Find all Windows Server images available for deployment
```

### Find Linux Images

```
Find all Ubuntu or CentOS images
```

### Large Images

```
List all images larger than 50 GB, sorted by size
```

---

## Expected Response

```json
{
  "data": [
    {
      "extId": "image-uuid-...",
      "name": "ubuntu-22.04-server",
      "description": "Ubuntu 22.04 LTS Server",
      "type": "DISK_IMAGE",
      "sizeBytes": 5368709120,
      "sourceUri": "https://...",
      "createdTime": "2024-01-15T10:00:00Z"
    }
  ]
}
```

## Related Operations

- [Find Image by Name](18-find-image-by-name.md) - Search for specific image
- [Create a New VM](04-create-new-vm.md) - Use image for VM
