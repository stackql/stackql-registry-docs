---
title: peer_express_route_circuit_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - peer_express_route_circuit_connections
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
<tr><td><b>Name</b></td><td><code>peer_express_route_circuit_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.peer_express_route_circuit_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `properties` | `object` | Properties of the peer express route circuit connection. |
| `type` | `string` | Type of the resource. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PeerExpressRouteCircuitConnections_Get` | `SELECT` | `circuitName, connectionName, peeringName, resourceGroupName, subscriptionId` | Gets the specified Peer Express Route Circuit Connection from the specified express route circuit. |
| `PeerExpressRouteCircuitConnections_List` | `SELECT` | `circuitName, peeringName, resourceGroupName, subscriptionId` | Gets all global reach peer connections associated with a private peering in an express route circuit. |
