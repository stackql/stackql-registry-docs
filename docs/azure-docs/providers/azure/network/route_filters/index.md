---
title: route_filters
hide_title: false
hide_table_of_contents: false
keywords:
  - route_filters
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
<tr><td><b>Name</b></td><td><code>route_filters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.route_filters</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Route Filter Resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, routeFilterName, subscriptionId` | Gets the specified route filter. |
| `list` | `SELECT` | `subscriptionId` | Gets all route filters in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all route filters in a resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, routeFilterName, subscriptionId, data__location` | Creates or updates a route filter in a specified resource group. |
| `delete` | `DELETE` | `resourceGroupName, routeFilterName, subscriptionId` | Deletes the specified route filter. |
| `_list` | `EXEC` | `subscriptionId` | Gets all route filters in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all route filters in a resource group. |
