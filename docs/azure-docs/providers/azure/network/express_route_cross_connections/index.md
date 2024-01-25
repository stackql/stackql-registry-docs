---
title: express_route_cross_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_cross_connections
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
<tr><td><b>Name</b></td><td><code>express_route_cross_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_cross_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of ExpressRouteCrossConnection. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `crossConnectionName, resourceGroupName, subscriptionId` | Gets details about the specified ExpressRouteCrossConnection. |
| `list` | `SELECT` | `subscriptionId` | Retrieves all the ExpressRouteCrossConnections in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Retrieves all the ExpressRouteCrossConnections in a resource group. |
| `create_or_update` | `INSERT` | `crossConnectionName, resourceGroupName, subscriptionId` | Update the specified ExpressRouteCrossConnection. |
| `_list` | `EXEC` | `subscriptionId` | Retrieves all the ExpressRouteCrossConnections in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Retrieves all the ExpressRouteCrossConnections in a resource group. |
