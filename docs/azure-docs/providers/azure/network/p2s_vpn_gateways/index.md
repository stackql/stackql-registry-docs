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
| `get` | `SELECT` | `gatewayName, resourceGroupName, subscriptionId` | Retrieves the details of a virtual wan p2s vpn gateway. |
| `list` | `SELECT` | `subscriptionId` | Lists all the P2SVpnGateways in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the P2SVpnGateways in a resource group. |
| `create_or_update` | `INSERT` | `gatewayName, resourceGroupName, subscriptionId, data__location` | Creates a virtual wan p2s vpn gateway if it doesn't exist else updates the existing gateway. |
| `delete` | `DELETE` | `gatewayName, resourceGroupName, subscriptionId` | Deletes a virtual wan p2s vpn gateway. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the P2SVpnGateways in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the P2SVpnGateways in a resource group. |
| `disconnect_p2s_vpn_connections` | `EXEC` | `p2sVpnGatewayName, resourceGroupName, subscriptionId` | Disconnect P2S vpn connections of the virtual wan P2SVpnGateway in the specified resource group. |
| `generate_vpn_profile` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Generates VPN profile for P2S client of the P2SVpnGateway in the specified resource group. |
| `reset` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Resets the primary of the p2s vpn gateway in the specified resource group. |
