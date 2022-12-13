---
title: platform_images
hide_title: false
hide_table_of_contents: false
keywords:
  - platform_images
  - compute_admin
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
<tr><td><b>Name</b></td><td><code>platform_images</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute_admin.platform_images</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the resource. |
| `name` | `string` | Name of the resource. |
| `properties` | `object` | Properties of platform image. |
| `type` | `string` | Type of Resource. |
| `location` | `string` | Location of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PlatformImages_Get` | `SELECT` | `location, offer, publisher, sku, subscriptionId, version` | Returns the specific platform image matching publisher, offer, skus and version. |
| `PlatformImages_List` | `SELECT` | `location, subscriptionId` | Returns a list of all platform images. |
| `PlatformImages_Create` | `INSERT` | `location, offer, publisher, sku, subscriptionId, version` | Creates a new platform image with given publisher, offer, skus and version. |
| `PlatformImages_Delete` | `DELETE` | `location, offer, publisher, sku, subscriptionId, version` | Delete a platform image |
