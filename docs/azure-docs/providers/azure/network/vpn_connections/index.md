---
title: vpn_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_connections
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
<tr><td><b>Name</b></td><td><code>vpn_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.vpn_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Parameters for VpnConnection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VpnConnections_Get` | `SELECT` | `connectionName, gatewayName, resourceGroupName, subscriptionId` | Retrieves the details of a vpn connection. |
| `VpnConnections_ListByVpnGateway` | `SELECT` | `gatewayName, resourceGroupName, subscriptionId` | Retrieves all vpn connections for a particular virtual wan vpn gateway. |
| `VpnConnections_CreateOrUpdate` | `INSERT` | `connectionName, gatewayName, resourceGroupName, subscriptionId` | Creates a vpn connection to a scalable vpn gateway if it doesn't exist else updates the existing connection. |
| `VpnConnections_Delete` | `DELETE` | `connectionName, gatewayName, resourceGroupName, subscriptionId` | Deletes a vpn connection. |
| `VpnConnections_StartPacketCapture` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId, vpnConnectionName` | Starts packet capture on Vpn connection in the specified resource group. |
| `VpnConnections_StopPacketCapture` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId, vpnConnectionName` | Stops packet capture on Vpn connection in the specified resource group. |
