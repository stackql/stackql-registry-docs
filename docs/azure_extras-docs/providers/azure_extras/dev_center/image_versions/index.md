---
title: image_versions
hide_title: false
hide_table_of_contents: false
keywords:
  - image_versions
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
<tr><td><b>Name</b></td><td><code>image_versions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_center.image_versions</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ImageVersions_Get` | `SELECT` | `devCenterName, galleryName, imageName, resourceGroupName, subscriptionId, versionName` | Gets an image version. |
| `ImageVersions_ListByImage` | `SELECT` | `devCenterName, galleryName, imageName, resourceGroupName, subscriptionId` | Lists versions for an image. |
