---
title: routes
hide_title: false
hide_table_of_contents: false
keywords:
  - routes
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
<tr><td><b>Name</b></td><td><code>routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.routes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Route resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Routes_Get` | `SELECT` | `resourceGroupName, routeName, routeTableName, subscriptionId` | Gets the specified route from a route table. |
| `Routes_List` | `SELECT` | `resourceGroupName, routeTableName, subscriptionId` | Gets all routes in a route table. |
| `Routes_CreateOrUpdate` | `INSERT` | `resourceGroupName, routeName, routeTableName, subscriptionId` | Creates or updates a route in the specified route table. |
| `Routes_Delete` | `DELETE` | `resourceGroupName, routeName, routeTableName, subscriptionId` | Deletes the specified route from a route table. |
