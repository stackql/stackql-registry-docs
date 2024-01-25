---
title: route_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - route_maps
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
<tr><td><b>Name</b></td><td><code>route_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.route_maps</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of RouteMap resource |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, routeMapName, subscriptionId, virtualHubName` | Retrieves the details of a RouteMap. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, virtualHubName` | Retrieves the details of all RouteMaps. |
| `create_or_update` | `INSERT` | `resourceGroupName, routeMapName, subscriptionId, virtualHubName` | Creates a RouteMap if it doesn't exist else updates the existing one. |
| `delete` | `DELETE` | `resourceGroupName, routeMapName, subscriptionId, virtualHubName` | Deletes a RouteMap. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, virtualHubName` | Retrieves the details of all RouteMaps. |
