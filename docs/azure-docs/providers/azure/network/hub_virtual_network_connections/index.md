---
title: hub_virtual_network_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - hub_virtual_network_connections
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
<tr><td><b>Name</b></td><td><code>hub_virtual_network_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.hub_virtual_network_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `properties` | `object` | Parameters for HubVirtualNetworkConnection. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `HubVirtualNetworkConnections_Get` | `SELECT` | `connectionName, resourceGroupName, subscriptionId, virtualHubName` | Retrieves the details of a HubVirtualNetworkConnection. |
| `HubVirtualNetworkConnections_List` | `SELECT` | `resourceGroupName, subscriptionId, virtualHubName` | Retrieves the details of all HubVirtualNetworkConnections. |
| `HubVirtualNetworkConnections_CreateOrUpdate` | `INSERT` | `connectionName, resourceGroupName, subscriptionId, virtualHubName` | Creates a hub virtual network connection if it doesn't exist else updates the existing one. |
| `HubVirtualNetworkConnections_Delete` | `DELETE` | `connectionName, resourceGroupName, subscriptionId, virtualHubName` | Deletes a HubVirtualNetworkConnection. |
