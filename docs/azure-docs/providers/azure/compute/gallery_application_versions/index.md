---
title: gallery_application_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - gallery_application_versions
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
<tr><td><b>Name</b></td><td><code>gallery_application_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.gallery_application_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | Describes the properties of a gallery image version. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId` | Retrieves information about a gallery Application Version. |
| `list_by_gallery_application` | `SELECT` | `galleryApplicationName, galleryName, resourceGroupName, subscriptionId` | List gallery Application Versions in a gallery Application Definition. |
| `create_or_update` | `INSERT` | `galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId` | Create or update a gallery Application Version. |
| `delete` | `DELETE` | `galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId` | Delete a gallery Application Version. |
| `_list_by_gallery_application` | `EXEC` | `galleryApplicationName, galleryName, resourceGroupName, subscriptionId` | List gallery Application Versions in a gallery Application Definition. |
| `update` | `EXEC` | `galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId` | Update a gallery Application Version. |
