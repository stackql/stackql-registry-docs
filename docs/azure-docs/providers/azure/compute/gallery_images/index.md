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
| `location` | `string` | Resource location |
| `properties` | `object` | Describes the properties of a gallery image definition. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `galleryImageName, galleryName, resourceGroupName, subscriptionId` | Retrieves information about a gallery image definition. |
| `list_by_gallery` | `SELECT` | `galleryName, resourceGroupName, subscriptionId` | List gallery image definitions in a gallery. |
| `create_or_update` | `INSERT` | `galleryImageName, galleryName, resourceGroupName, subscriptionId` | Create or update a gallery image definition. |
| `delete` | `DELETE` | `galleryImageName, galleryName, resourceGroupName, subscriptionId` | Delete a gallery image. |
| `_list_by_gallery` | `EXEC` | `galleryName, resourceGroupName, subscriptionId` | List gallery image definitions in a gallery. |
| `update` | `EXEC` | `galleryImageName, galleryName, resourceGroupName, subscriptionId` | Update a gallery image definition. |
