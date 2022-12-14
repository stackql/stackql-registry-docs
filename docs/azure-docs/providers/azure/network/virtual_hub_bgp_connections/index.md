---
title: virtual_hub_bgp_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_hub_bgp_connections
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
<tr><td><b>Name</b></td><td><code>virtual_hub_bgp_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.virtual_hub_bgp_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Name of the connection. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of the bgp connection. |
| `type` | `string` | Connection type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `VirtualHubBgpConnections_List` | `SELECT` | `resourceGroupName, subscriptionId, virtualHubName` | Retrieves the details of all VirtualHubBgpConnections. |
| `VirtualHubBgpConnections_ListAdvertisedRoutes` | `EXEC` | `connectionName, hubName, resourceGroupName, subscriptionId` | Retrieves a list of routes the virtual hub bgp connection is advertising to the specified peer. |
| `VirtualHubBgpConnections_ListLearnedRoutes` | `EXEC` | `connectionName, hubName, resourceGroupName, subscriptionId` | Retrieves a list of routes the virtual hub bgp connection has learned. |
