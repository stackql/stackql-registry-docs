---
title: shared_gallery_images
hide_title: false
hide_table_of_contents: false
keywords:
  - shared_gallery_images
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
<tr><td><b>Name</b></td><td><code>shared_gallery_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.shared_gallery_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Describes the properties of a gallery image definition. |
| `identifier` | `object` | The identifier information of shared gallery. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SharedGalleryImages_Get` | `SELECT` | `galleryImageName, galleryUniqueName, location, subscriptionId` | Get a shared gallery image by subscription id or tenant id. |
| `SharedGalleryImages_List` | `SELECT` | `galleryUniqueName, location, subscriptionId` | List shared gallery images by subscription id or tenant id. |
