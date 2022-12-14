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
| `type` | `string` | Resource type |
| `location` | `string` | Resource location |
| `properties` | `object` | Describes the properties of a gallery image version. |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GalleryApplicationVersions_Get` | `SELECT` | `galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId` | Retrieves information about a gallery Application Version. |
| `GalleryApplicationVersions_ListByGalleryApplication` | `SELECT` | `galleryApplicationName, galleryName, resourceGroupName, subscriptionId` | List gallery Application Versions in a gallery Application Definition. |
| `GalleryApplicationVersions_CreateOrUpdate` | `INSERT` | `galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId` | Create or update a gallery Application Version. |
| `GalleryApplicationVersions_Delete` | `DELETE` | `galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId` | Delete a gallery Application Version. |
| `GalleryApplicationVersions_Update` | `EXEC` | `galleryApplicationName, galleryApplicationVersionName, galleryName, resourceGroupName, subscriptionId` | Update a gallery Application Version. |
