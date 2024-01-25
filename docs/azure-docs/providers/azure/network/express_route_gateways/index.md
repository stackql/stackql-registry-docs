---
title: express_route_gateways
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_gateways
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
<tr><td><b>Name</b></td><td><code>express_route_gateways</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_gateways</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | ExpressRoute gateway resource properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `expressRouteGatewayName, resourceGroupName, subscriptionId` | Fetches the details of a ExpressRoute gateway in a resource group. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists ExpressRoute gateways in a given resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists ExpressRoute gateways under a given subscription. |
| `create_or_update` | `INSERT` | `expressRouteGatewayName, resourceGroupName, subscriptionId` | Creates or updates a ExpressRoute gateway in a specified resource group. |
| `delete` | `DELETE` | `expressRouteGatewayName, resourceGroupName, subscriptionId` | Deletes the specified ExpressRoute gateway in a resource group. An ExpressRoute gateway resource can only be deleted when there are no connection subresources. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists ExpressRoute gateways in a given resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists ExpressRoute gateways under a given subscription. |
