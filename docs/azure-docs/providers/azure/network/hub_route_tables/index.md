---
title: hub_route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - hub_route_tables
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
<tr><td><b>Name</b></td><td><code>hub_route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.hub_route_tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `properties` | `object` | Parameters for RouteTable. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `HubRouteTables_Get` | `SELECT` | `resourceGroupName, routeTableName, subscriptionId, virtualHubName` | Retrieves the details of a RouteTable. |
| `HubRouteTables_List` | `SELECT` | `resourceGroupName, subscriptionId, virtualHubName` | Retrieves the details of all RouteTables. |
| `HubRouteTables_CreateOrUpdate` | `INSERT` | `resourceGroupName, routeTableName, subscriptionId, virtualHubName` | Creates a RouteTable resource if it doesn't exist else updates the existing RouteTable. |
| `HubRouteTables_Delete` | `DELETE` | `resourceGroupName, routeTableName, subscriptionId, virtualHubName` | Deletes a RouteTable. |
