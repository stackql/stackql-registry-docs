---
title: vpn_link_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - vpn_link_connections
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
<tr><td><b>Name</b></td><td><code>vpn_link_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.vpn_link_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `properties` | `object` | Parameters for VpnConnection. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VpnLinkConnections_ListByVpnConnection` | `SELECT` | `connectionName, gatewayName, resourceGroupName, subscriptionId` | Retrieves all vpn site link connections for a particular virtual wan vpn gateway vpn connection. |
| `VpnLinkConnections_GetIkeSas` | `EXEC` | `connectionName, gatewayName, linkConnectionName, resourceGroupName, subscriptionId` | Lists IKE Security Associations for Vpn Site Link Connection in the specified resource group. |
| `VpnLinkConnections_ResetConnection` | `EXEC` | `connectionName, gatewayName, linkConnectionName, resourceGroupName, subscriptionId` | Resets the VpnLink connection specified. |
