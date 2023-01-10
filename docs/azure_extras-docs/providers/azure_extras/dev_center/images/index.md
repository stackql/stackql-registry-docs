---
title: images
hide_title: false
hide_table_of_contents: false
keywords:
  - images
  - dev_center
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_center.images</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Images_Get` | `SELECT` | `devCenterName, galleryName, imageName, resourceGroupName, subscriptionId` | Gets a gallery image. |
| `Images_ListByDevCenter` | `SELECT` | `devCenterName, resourceGroupName, subscriptionId` | Lists images for a devcenter. |
| `Images_ListByGallery` | `SELECT` | `devCenterName, galleryName, resourceGroupName, subscriptionId` | Lists images for a gallery. |
