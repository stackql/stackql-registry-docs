---
title: community_gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - community_gallery_images
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
<tr><td><b>Name</b></td><td><code>community_gallery_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.community_gallery_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Resource name |
| `identifier` | `object` | The identifier information of community gallery. |
| `location` | `string` | Resource location |
| `properties` | `object` | Describes the properties of a gallery image definition. |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `galleryImageName, location, publicGalleryName, subscriptionId` | Get a community gallery image. |
| `list` | `SELECT` | `location, publicGalleryName, subscriptionId` | List community gallery images inside a gallery. |
| `_list` | `EXEC` | `location, publicGalleryName, subscriptionId` | List community gallery images inside a gallery. |
