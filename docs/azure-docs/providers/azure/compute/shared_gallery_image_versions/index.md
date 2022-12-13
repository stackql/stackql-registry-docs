---
title: shared_gallery_image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_gallery_image_versions
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
<tr><td><b>Name</b></td><td><code>shared_gallery_image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.shared_gallery_image_versions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identifier` | `object` | The identifier information of shared gallery. |
| `properties` | `object` | Describes the properties of a gallery image version. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SharedGalleryImageVersions_Get` | `SELECT` | `galleryImageName, galleryImageVersionName, galleryUniqueName, location, subscriptionId` | Get a shared gallery image version by subscription id or tenant id. |
| `SharedGalleryImageVersions_List` | `SELECT` | `galleryImageName, galleryUniqueName, location, subscriptionId` | List shared gallery image versions by subscription id or tenant id. |
