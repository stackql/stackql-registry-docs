---
title: express_route_circuit_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuit_connections
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
<tr><td><b>Name</b></td><td><code>express_route_circuit_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_circuit_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `type` | `string` | Type of the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | Properties of the express route circuit connection. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExpressRouteCircuitConnections_Get` | `SELECT` | `circuitName, connectionName, peeringName, resourceGroupName, subscriptionId` | Gets the specified Express Route Circuit Connection from the specified express route circuit. |
| `ExpressRouteCircuitConnections_List` | `SELECT` | `circuitName, peeringName, resourceGroupName, subscriptionId` | Gets all global reach connections associated with a private peering in an express route circuit. |
| `ExpressRouteCircuitConnections_CreateOrUpdate` | `INSERT` | `circuitName, connectionName, peeringName, resourceGroupName, subscriptionId` | Creates or updates a Express Route Circuit Connection in the specified express route circuits. |
| `ExpressRouteCircuitConnections_Delete` | `DELETE` | `circuitName, connectionName, peeringName, resourceGroupName, subscriptionId` | Deletes the specified Express Route Circuit Connection from the specified express route circuit. |
