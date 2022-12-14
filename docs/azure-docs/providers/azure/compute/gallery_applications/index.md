---
title: gallery_applications
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_applications
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
<tr><td><b>Name</b></td><td><code>gallery_applications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.gallery_applications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
| `location` | `string` | Resource location |
| `properties` | `object` | Describes the properties of a gallery Application Definition. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GalleryApplications_Get` | `SELECT` | `galleryApplicationName, galleryName, resourceGroupName, subscriptionId` | Retrieves information about a gallery Application Definition. |
| `GalleryApplications_ListByGallery` | `SELECT` | `galleryName, resourceGroupName, subscriptionId` | List gallery Application Definitions in a gallery. |
| `GalleryApplications_CreateOrUpdate` | `INSERT` | `galleryApplicationName, galleryName, resourceGroupName, subscriptionId` | Create or update a gallery Application Definition. |
| `GalleryApplications_Delete` | `DELETE` | `galleryApplicationName, galleryName, resourceGroupName, subscriptionId` | Delete a gallery Application. |
| `GalleryApplications_Update` | `EXEC` | `galleryApplicationName, galleryName, resourceGroupName, subscriptionId` | Update a gallery Application Definition. |
