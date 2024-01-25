---
title: virtual_network_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_peerings
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
<tr><td><b>Name</b></td><td><code>virtual_network_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_network_peerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of the virtual network peering. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName, virtualNetworkPeeringName` | Gets the specified virtual network peering. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkName` | Gets all virtual network peerings in a virtual network. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkName, virtualNetworkPeeringName` | Creates or updates a peering in the specified virtual network. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkName, virtualNetworkPeeringName` | Deletes the specified virtual network peering. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkName` | Gets all virtual network peerings in a virtual network. |
