---
title: gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_images
  - compute
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>gallery_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.gallery_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `location` | `string` | Resource location |
| `properties` | `object` | Describes the properties of a gallery image definition. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GalleryImages_Get` | `SELECT` | `galleryImageName, galleryName, resourceGroupName, subscriptionId` | Retrieves information about a gallery image definition. |
| `GalleryImages_ListByGallery` | `SELECT` | `galleryName, resourceGroupName, subscriptionId` | List gallery image definitions in a gallery. |
| `GalleryImages_CreateOrUpdate` | `INSERT` | `galleryImageName, galleryName, resourceGroupName, subscriptionId` | Create or update a gallery image definition. |
| `GalleryImages_Delete` | `DELETE` | `galleryImageName, galleryName, resourceGroupName, subscriptionId` | Delete a gallery image. |
| `GalleryImages_Update` | `EXEC` | `galleryImageName, galleryName, resourceGroupName, subscriptionId` | Update a gallery image definition. |
