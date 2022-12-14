---
title: p2s_vpn_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - p2s_vpn_gateways
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
<tr><td><b>Name</b></td><td><code>p2s_vpn_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.p2s_vpn_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Parameters for P2SVpnGateway. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `P2sVpnGateways_Get` | `SELECT` | `gatewayName, resourceGroupName, subscriptionId` | Retrieves the details of a virtual wan p2s vpn gateway. |
| `P2sVpnGateways_List` | `SELECT` | `subscriptionId` | Lists all the P2SVpnGateways in a subscription. |
| `P2sVpnGateways_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the P2SVpnGateways in a resource group. |
| `P2sVpnGateways_CreateOrUpdate` | `INSERT` | `gatewayName, resourceGroupName, subscriptionId, data__location` | Creates a virtual wan p2s vpn gateway if it doesn't exist else updates the existing gateway. |
| `P2sVpnGateways_Delete` | `DELETE` | `gatewayName, resourceGroupName, subscriptionId` | Deletes a virtual wan p2s vpn gateway. |
| `P2SVpnGateways_Reset` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Resets the primary of the p2s vpn gateway in the specified resource group. |
| `P2sVpnGateways_DisconnectP2sVpnConnections` | `EXEC` | `p2sVpnGatewayName, resourceGroupName, subscriptionId` | Disconnect P2S vpn connections of the virtual wan P2SVpnGateway in the specified resource group. |
| `P2sVpnGateways_GenerateVpnProfile` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Generates VPN profile for P2S client of the P2SVpnGateway in the specified resource group. |
| `P2sVpnGateways_GetP2sVpnConnectionHealth` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Gets the connection health of P2S clients of the virtual wan P2SVpnGateway in the specified resource group. |
| `P2sVpnGateways_GetP2sVpnConnectionHealthDetailed` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Gets the sas url to get the connection health detail of P2S clients of the virtual wan P2SVpnGateway in the specified resource group. |
| `P2sVpnGateways_UpdateTags` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Updates virtual wan p2s vpn gateway tags. |
