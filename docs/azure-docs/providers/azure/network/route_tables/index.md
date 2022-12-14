---
title: route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - route_tables
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
<tr><td><b>Name</b></td><td><code>route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.route_tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Route Table resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `RouteTables_Get` | `SELECT` | `resourceGroupName, routeTableName, subscriptionId` | Gets the specified route table. |
| `RouteTables_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all route tables in a resource group. |
| `RouteTables_ListAll` | `SELECT` | `subscriptionId` | Gets all route tables in a subscription. |
| `RouteTables_CreateOrUpdate` | `INSERT` | `resourceGroupName, routeTableName, subscriptionId` | Create or updates a route table in a specified resource group. |
| `RouteTables_Delete` | `DELETE` | `resourceGroupName, routeTableName, subscriptionId` | Deletes the specified route table. |
| `RouteTables_UpdateTags` | `EXEC` | `resourceGroupName, routeTableName, subscriptionId` | Updates a route table tags. |
