---
title: galleries
hide_title: false
hide_table_of_contents: false
keywords:
  - galleries
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
<tr><td><b>Name</b></td><td><code>galleries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.galleries</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `location` | `string` | Resource location |
| `properties` | `object` | Describes the properties of a Shared Image Gallery. |
| `tags` | `object` | Resource tags |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `galleryName, resourceGroupName, subscriptionId` | Retrieves information about a Shared Image Gallery. |
| `list` | `SELECT` | `subscriptionId` | List galleries under a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List galleries under a resource group. |
| `create_or_update` | `INSERT` | `galleryName, resourceGroupName, subscriptionId` | Create or update a Shared Image Gallery. |
| `delete` | `DELETE` | `galleryName, resourceGroupName, subscriptionId` | Delete a Shared Image Gallery. |
| `_list` | `EXEC` | `subscriptionId` | List galleries under a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List galleries under a resource group. |
| `update` | `EXEC` | `galleryName, resourceGroupName, subscriptionId` | Update a Shared Image Gallery. |
