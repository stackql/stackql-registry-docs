---
title: express_route_circuit_peerings
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuit_peerings
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
<tr><td><b>Name</b></td><td><code>express_route_circuit_peerings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_circuit_peerings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `properties` | `object` | Properties of the express route circuit peering. |
| `type` | `string` | Type of the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExpressRouteCircuitPeerings_Get` | `SELECT` | `circuitName, peeringName, resourceGroupName, subscriptionId` | Gets the specified peering for the express route circuit. |
| `ExpressRouteCircuitPeerings_List` | `SELECT` | `circuitName, resourceGroupName, subscriptionId` | Gets all peerings in a specified express route circuit. |
| `ExpressRouteCircuitPeerings_CreateOrUpdate` | `INSERT` | `circuitName, peeringName, resourceGroupName, subscriptionId` | Creates or updates a peering in the specified express route circuits. |
| `ExpressRouteCircuitPeerings_Delete` | `DELETE` | `circuitName, peeringName, resourceGroupName, subscriptionId` | Deletes the specified peering from the specified express route circuit. |
