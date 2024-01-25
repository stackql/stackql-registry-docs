---
title: virtual_routers
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_routers
  - network
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
<tr><td><b>Name</b></td><td><code>virtual_routers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_routers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Virtual Router definition. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, virtualRouterName` | Gets the specified Virtual Router. |
| `list` | `SELECT` | `subscriptionId` | Gets all the Virtual Routers in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Virtual Routers in a resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, virtualRouterName` | Creates or updates the specified Virtual Router. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualRouterName` | Deletes the specified Virtual Router. |
| `_list` | `EXEC` | `subscriptionId` | Gets all the Virtual Routers in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all Virtual Routers in a resource group. |
