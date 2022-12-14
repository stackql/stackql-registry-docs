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
| `VirtualNetworkGatewayConnections_Get` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Gets the specified virtual network gateway connection by resource group. |
| `VirtualNetworkGatewayConnections_List` | `SELECT` | `resourceGroupName, subscriptionId` | The List VirtualNetworkGatewayConnections operation retrieves all the virtual network gateways connections created. |
| `VirtualNetworkGatewayConnections_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__properties` | Creates or updates a virtual network gateway connection in the specified resource group. |
| `VirtualNetworkGatewayConnections_Delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Deletes the specified virtual network Gateway connection. |
| `VirtualNetworkGatewayConnections_GetIkeSas` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Lists IKE Security Associations for the virtual network gateway connection in the specified resource group. |
| `VirtualNetworkGatewayConnections_GetSharedKey` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | The Get VirtualNetworkGatewayConnectionSharedKey operation retrieves information about the specified virtual network gateway connection shared key through Network resource provider. |
| `VirtualNetworkGatewayConnections_ResetConnection` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Resets the virtual network gateway connection specified. |
| `VirtualNetworkGatewayConnections_ResetSharedKey` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__keyLength` | The VirtualNetworkGatewayConnectionResetSharedKey operation resets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider. |
| `VirtualNetworkGatewayConnections_SetSharedKey` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName, data__value` | The Put VirtualNetworkGatewayConnectionSharedKey operation sets the virtual network gateway connection shared key for passed virtual network gateway connection in the specified resource group through Network resource provider. |
| `VirtualNetworkGatewayConnections_StartPacketCapture` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Starts packet capture on virtual network gateway connection in the specified resource group. |
| `VirtualNetworkGatewayConnections_StopPacketCapture` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Stops packet capture on virtual network gateway connection in the specified resource group. |
| `VirtualNetworkGatewayConnections_UpdateTags` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName` | Updates a virtual network gateway connection tags. |
