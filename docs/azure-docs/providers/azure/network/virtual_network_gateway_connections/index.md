---
title: virtual_network_gateway_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateway_connections
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
<tr><td><b>Name</b></td><td><code>virtual_network_gateway_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_network_gateway_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | VirtualNetworkGatewayConnection properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Gets the specified virtual network gateway connection by resource group. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways connections created. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__properties` | Creates or updates a virtual network gateway connection in the specified resource group. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Deletes the specified virtual network Gateway connection. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways connections created. |
| `reset_connection` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Resets the virtual network gateway connection specified. |
| `reset_shared_key` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__keyLength` | The VirtualNetworkGatewayConnectionResetSharedKey operation resets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider. |
| `set_shared_key` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__value` | The Put VirtualNetworkGatewayConnectionSharedKey operation sets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider. |
