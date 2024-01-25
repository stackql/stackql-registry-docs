---
title: route_filter_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - route_filter_rules
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
<tr><td><b>Name</b></td><td><code>route_filter_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.route_filter_rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Route Filter Rule Resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, routeFilterName, ruleName, subscriptionId` | Gets the specified rule from a route filter. |
| `list_by_route_filter` | `SELECT` | `resourceGroupName, routeFilterName, subscriptionId` | Gets all RouteFilterRules in a route filter. |
| `create_or_update` | `INSERT` | `resourceGroupName, routeFilterName, ruleName, subscriptionId` | Creates or updates a route in the specified route filter. |
| `delete` | `DELETE` | `resourceGroupName, routeFilterName, ruleName, subscriptionId` | Deletes the specified rule from a route filter. |
| `_list_by_route_filter` | `EXEC` | `resourceGroupName, routeFilterName, subscriptionId` | Gets all RouteFilterRules in a route filter. |
