---
title: virtual_network_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateways
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
<tr><td><b>Name</b></td><td><code>virtual_network_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_network_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `extendedLocation` | `object` | ExtendedLocation complex type. |
| `location` | `string` | Resource location. |
| `properties` | `object` | VirtualNetworkGateway properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Gets the specified virtual network gateway by resource group. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all virtual network gateways by resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName, data__properties` | Creates or updates a virtual network gateway in the specified resource group. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Deletes the specified virtual network gateway. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all virtual network gateways by resource group. |
| `disconnect_virtual_network_gateway_vpn_connections` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Disconnect vpn connections of virtual network gateway in the specified resource group. |
| `reset` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Resets the primary of the virtual network gateway in the specified resource group. |
| `reset_vpn_client_shared_key` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName` | Resets the VPN client shared key of the virtual network gateway in the specified resource group. |
| `set_vpnclient_ipsec_parameters` | `EXEC` | `resourceGroupName, subscriptionId, virtualNetworkGatewayName, data__dhGroup, data__ikeEncryption, data__ikeIntegrity, data__ipsecEncryption, data__ipsecIntegrity, data__pfsGroup, data__saDataSizeKilobytes, data__saLifeTimeSeconds` | The Set VpnclientIpsecParameters operation sets the vpnclient ipsec policy for P2S client of virtual network gateway in the specified resource group through Network resource provider. |
