---
title: vpn_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_gateways
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
<tr><td><b>Name</b></td><td><code>vpn_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.vpn_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Parameters for VpnGateway. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `gatewayName, resourceGroupName, subscriptionId` | Retrieves the details of a virtual wan vpn gateway. |
| `list` | `SELECT` | `subscriptionId` | Lists all the VpnGateways in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the VpnGateways in a resource group. |
| `create_or_update` | `INSERT` | `gatewayName, resourceGroupName, subscriptionId, data__location` | Creates a virtual wan vpn gateway if it doesn't exist else updates the existing gateway. |
| `delete` | `DELETE` | `gatewayName, resourceGroupName, subscriptionId` | Deletes a virtual wan vpn gateway. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the VpnGateways in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the VpnGateways in a resource group. |
| `reset` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Resets the primary of the vpn gateway in the specified resource group. |
