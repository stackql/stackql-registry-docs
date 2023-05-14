---
title: configs_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - configs_nodes
  - nodebalancers
  - linode    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Linode resources using SQL
custom_edit_url: null
image: /img/providers/linode/stackql-linode-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>configs_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.nodebalancers.configs_nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | This node's unique ID. |
| `label` | `string` | The label for this node.  This is for display purposes only.<br /> |
| `mode` | `string` | The mode this NodeBalancer should use when sending traffic to this backend.<br />* If set to `accept` this backend is accepting traffic.<br />* If set to `reject` this backend will not receive traffic.<br />* If set to `drain` this backend will not receive _new_ traffic, but connections already<br />  pinned to it will continue to be routed to it.<br /><br />* If set to `backup`, this backend will only receive traffic if all `accept` nodes<br />  are down.<br /> |
| `nodebalancer_id` | `integer` | The NodeBalancer ID that this Node belongs to.<br /> |
| `status` | `string` | The current status of this node, based on the configured checks of its NodeBalancer Config.<br /> |
| `weight` | `integer` | Used when picking a backend to serve a request and is not pinned to a single backend yet.  Nodes with a higher weight will receive more traffic.<br /> |
| `address` | `string` | The private IP Address where this backend can be reached. This _must_ be a private IP address.<br /> |
| `config_id` | `integer` | The NodeBalancer Config ID that this Node belongs to.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getNodeBalancerConfigNodes` | `SELECT` | `configId, nodeBalancerId` | Returns a paginated list of NodeBalancer nodes associated with this Config. These are the backends that will be sent traffic for this port.<br /> |
| `getNodeBalancerNode` | `SELECT` | `configId, nodeBalancerId, nodeId` | Returns information about a single Node, a backend for this NodeBalancer's configured port.<br /> |
| `createNodeBalancerNode` | `INSERT` | `configId, nodeBalancerId, data__address, data__label` | Creates a NodeBalancer Node, a backend that can accept traffic for this NodeBalancer Config. Nodes are routed requests on the configured port based on their status.<br /> |
| `deleteNodeBalancerConfigNode` | `DELETE` | `configId, nodeBalancerId, nodeId` | Deletes a Node from this Config. This backend will no longer receive traffic for the configured port of this NodeBalancer.<br /><br />This does not change or remove the Linode whose address was used in the creation of this Node.<br /> |
| `_getNodeBalancerConfigNodes` | `EXEC` | `configId, nodeBalancerId` | Returns a paginated list of NodeBalancer nodes associated with this Config. These are the backends that will be sent traffic for this port.<br /> |
| `_getNodeBalancerNode` | `EXEC` | `configId, nodeBalancerId, nodeId` | Returns information about a single Node, a backend for this NodeBalancer's configured port.<br /> |
| `updateNodeBalancerNode` | `EXEC` | `configId, nodeBalancerId, nodeId` | Updates information about a Node, a backend for this NodeBalancer's configured port.<br /> |
