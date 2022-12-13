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
| `properties` | `object` | Route Filter Rule Resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RouteFilterRules_Get` | `SELECT` | `resourceGroupName, routeFilterName, ruleName, subscriptionId` | Gets the specified rule from a route filter. |
| `RouteFilterRules_ListByRouteFilter` | `SELECT` | `resourceGroupName, routeFilterName, subscriptionId` | Gets all RouteFilterRules in a route filter. |
| `RouteFilterRules_CreateOrUpdate` | `INSERT` | `resourceGroupName, routeFilterName, ruleName, subscriptionId` | Creates or updates a route in the specified route filter. |
| `RouteFilterRules_Delete` | `DELETE` | `resourceGroupName, routeFilterName, ruleName, subscriptionId` | Deletes the specified rule from a route filter. |
