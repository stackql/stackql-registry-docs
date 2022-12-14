---
title: express_route_circuit_authorizations
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuit_authorizations
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
<tr><td><b>Name</b></td><td><code>express_route_circuit_authorizations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.express_route_circuit_authorizations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `properties` | `object` | Properties of ExpressRouteCircuitAuthorization. |
| `type` | `string` | Type of the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ExpressRouteCircuitAuthorizations_Get` | `SELECT` | `authorizationName, circuitName, resourceGroupName, subscriptionId` | Gets the specified authorization from the specified express route circuit. |
| `ExpressRouteCircuitAuthorizations_List` | `SELECT` | `circuitName, resourceGroupName, subscriptionId` | Gets all authorizations in an express route circuit. |
| `ExpressRouteCircuitAuthorizations_CreateOrUpdate` | `INSERT` | `authorizationName, circuitName, resourceGroupName, subscriptionId` | Creates or updates an authorization in the specified express route circuit. |
| `ExpressRouteCircuitAuthorizations_Delete` | `DELETE` | `authorizationName, circuitName, resourceGroupName, subscriptionId` | Deletes the specified authorization from the specified express route circuit. |
