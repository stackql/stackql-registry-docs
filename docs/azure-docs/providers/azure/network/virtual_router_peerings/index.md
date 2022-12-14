---
title: virtual_router_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_router_peerings
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
<tr><td><b>Name</b></td><td><code>virtual_router_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_router_peerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of the virtual router peering that is unique within a virtual router. |
| `properties` | `object` | Properties of the rule group. |
| `type` | `string` | Peering type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualRouterPeerings_Get` | `SELECT` | `peeringName, resourceGroupName, subscriptionId, virtualRouterName` | Gets the specified Virtual Router Peering. |
| `VirtualRouterPeerings_List` | `SELECT` | `resourceGroupName, subscriptionId, virtualRouterName` | Lists all Virtual Router Peerings in a Virtual Router resource. |
| `VirtualRouterPeerings_CreateOrUpdate` | `INSERT` | `peeringName, resourceGroupName, subscriptionId, virtualRouterName` | Creates or updates the specified Virtual Router Peering. |
| `VirtualRouterPeerings_Delete` | `DELETE` | `peeringName, resourceGroupName, subscriptionId, virtualRouterName` | Deletes the specified peering from a Virtual Router. |
