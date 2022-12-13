---
title: express_route_circuits
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuits
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
<tr><td><b>Name</b></td><td><code>express_route_circuits</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_circuits</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `properties` | `object` | Properties of ExpressRouteCircuit. |
| `sku` | `object` | Contains SKU in an ExpressRouteCircuit. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExpressRouteCircuits_Get` | `SELECT` | `circuitName, resourceGroupName, subscriptionId` | Gets information about the specified express route circuit. |
| `ExpressRouteCircuits_List` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the express route circuits in a resource group. |
| `ExpressRouteCircuits_ListAll` | `SELECT` | `subscriptionId` | Gets all the express route circuits in a subscription. |
| `ExpressRouteCircuits_CreateOrUpdate` | `INSERT` | `circuitName, resourceGroupName, subscriptionId` | Creates or updates an express route circuit. |
| `ExpressRouteCircuits_Delete` | `DELETE` | `circuitName, resourceGroupName, subscriptionId` | Deletes the specified express route circuit. |
| `ExpressRouteCircuits_GetPeeringStats` | `EXEC` | `circuitName, peeringName, resourceGroupName, subscriptionId` | Gets all stats from an express route circuit in a resource group. |
| `ExpressRouteCircuits_GetStats` | `EXEC` | `circuitName, resourceGroupName, subscriptionId` | Gets all the stats from an express route circuit in a resource group. |
| `ExpressRouteCircuits_ListArpTable` | `EXEC` | `circuitName, devicePath, peeringName, resourceGroupName, subscriptionId` | Gets the currently advertised ARP table associated with the express route circuit in a resource group. |
| `ExpressRouteCircuits_ListRoutesTable` | `EXEC` | `circuitName, devicePath, peeringName, resourceGroupName, subscriptionId` | Gets the currently advertised routes table associated with the express route circuit in a resource group. |
| `ExpressRouteCircuits_ListRoutesTableSummary` | `EXEC` | `circuitName, devicePath, peeringName, resourceGroupName, subscriptionId` | Gets the currently advertised routes table summary associated with the express route circuit in a resource group. |
| `ExpressRouteCircuits_UpdateTags` | `EXEC` | `circuitName, resourceGroupName, subscriptionId` | Updates an express route circuit tags. |
