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
| `get` | `SELECT` | `connectionName, gatewayName, resourceGroupName, subscriptionId` | Retrieves the details of a vpn connection. |
| `list_by_vpn_gateway` | `SELECT` | `gatewayName, resourceGroupName, subscriptionId` | Retrieves all vpn connections for a particular virtual wan vpn gateway. |
| `create_or_update` | `INSERT` | `connectionName, gatewayName, resourceGroupName, subscriptionId` | Creates a vpn connection to a scalable vpn gateway if it doesn't exist else updates the existing connection. |
| `delete` | `DELETE` | `connectionName, gatewayName, resourceGroupName, subscriptionId` | Deletes a vpn connection. |
| `_list_by_vpn_gateway` | `EXEC` | `gatewayName, resourceGroupName, subscriptionId` | Retrieves all vpn connections for a particular virtual wan vpn gateway. |
