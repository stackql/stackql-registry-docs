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
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | ExpressRoute gateway resource properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExpressRouteGateways_Get` | `SELECT` | `expressRouteGatewayName, resourceGroupName, subscriptionId` | Fetches the details of a ExpressRoute gateway in a resource group. |
| `ExpressRouteGateways_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists ExpressRoute gateways in a given resource group. |
| `ExpressRouteGateways_ListBySubscription` | `SELECT` | `subscriptionId` | Lists ExpressRoute gateways under a given subscription. |
| `ExpressRouteGateways_CreateOrUpdate` | `INSERT` | `expressRouteGatewayName, resourceGroupName, subscriptionId` | Creates or updates a ExpressRoute gateway in a specified resource group. |
| `ExpressRouteGateways_Delete` | `DELETE` | `expressRouteGatewayName, resourceGroupName, subscriptionId` | Deletes the specified ExpressRoute gateway in a resource group. An ExpressRoute gateway resource can only be deleted when there are no connection subresources. |
| `ExpressRouteGateways_UpdateTags` | `EXEC` | `expressRouteGatewayName, resourceGroupName, subscriptionId` | Updates express route gateway tags. |
