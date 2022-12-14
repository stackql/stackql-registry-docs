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
| `location` | `string` | Resource location. |
| `properties` | `object` | Virtual Router definition. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualRouters_Get` | `SELECT` | `resourceGroupName, subscriptionId, virtualRouterName` | Gets the specified Virtual Router. |
| `VirtualRouters_List` | `SELECT` | `subscriptionId` | Gets all the Virtual Routers in a subscription. |
| `VirtualRouters_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Virtual Routers in a resource group. |
| `VirtualRouters_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualRouterName` | Creates or updates the specified Virtual Router. |
| `VirtualRouters_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualRouterName` | Deletes the specified Virtual Router. |
