---
title: local_network_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - local_network_gateways
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
<tr><td><b>Name</b></td><td><code>local_network_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.local_network_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | LocalNetworkGateway properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LocalNetworkGateways_Get` | `SELECT` | `localNetworkGatewayName, resourceGroupName, subscriptionId` | Gets the specified local network gateway in a resource group. |
| `LocalNetworkGateways_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the local network gateways in a resource group. |
| `LocalNetworkGateways_CreateOrUpdate` | `INSERT` | `localNetworkGatewayName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a local network gateway in the specified resource group. |
| `LocalNetworkGateways_Delete` | `DELETE` | `localNetworkGatewayName, resourceGroupName, subscriptionId` | Deletes the specified local network gateway. |
| `LocalNetworkGateways_UpdateTags` | `EXEC` | `localNetworkGatewayName, resourceGroupName, subscriptionId` | Updates a local network gateway tags. |
