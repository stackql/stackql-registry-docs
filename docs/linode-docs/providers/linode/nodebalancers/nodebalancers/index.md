---
title: nodebalancers
hide_title: false
hide_table_of_contents: false
keywords:
  - nodebalancers
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
<tr><td><b>Name</b></td><td><code>nodebalancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>linode.nodebalancers.nodebalancers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | This NodeBalancer's unique ID.<br /> |
| `client_conn_throttle` | `integer` | Throttle connections per second.  Set to 0 (zero) to disable throttling.<br /> |
| `tags` | `array` | An array of Tags applied to this object.  Tags are for organizational purposes only.<br /> |
| `region` | `string` | The Region where this NodeBalancer is located. NodeBalancers only support backends in the same Region.<br /> |
| `updated` | `string` | When this NodeBalancer was last updated.<br /> |
| `hostname` | `string` | This NodeBalancer's hostname, beginning with its IP address and ending with _.ip.linodeusercontent.com_.<br /> |
| `ipv6` | `string` | This NodeBalancer's public IPv6 address.<br /> |
| `created` | `string` | When this NodeBalancer was created.<br /> |
| `transfer` | `object` | Information about the amount of transfer this NodeBalancer has had so far this month.<br /> |
| `ipv4` | `string` | This NodeBalancer's public IPv4 address.<br /> |
| `label` | `string` | This NodeBalancer's label. These must be unique on your Account.<br /> |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getNodeBalancer` | `SELECT` | `nodeBalancerId` | Returns a single NodeBalancer you can access.<br /> |
| `getNodeBalancers` | `SELECT` |  | Returns a paginated list of NodeBalancers you have access to.<br /> |
| `createNodeBalancer` | `INSERT` | `data__region` | Creates a NodeBalancer in the requested Region.<br /><br />NodeBalancers require a port Config with at least one backend Node to start serving requests.<br /><br />When using the Linode CLI to create a NodeBalancer, first create a NodeBalancer without any Configs. Then, create Configs and Nodes for that NodeBalancer with the respective [Config Create](/docs/api/nodebalancers/#config-create) and [Node Create](/docs/api/nodebalancers/#node-create) commands.<br /> |
| `deleteNodeBalancer` | `DELETE` | `nodeBalancerId` | Deletes a NodeBalancer.<br /><br />**This is a destructive action and cannot be undone.**<br /><br />Deleting a NodeBalancer will also delete all associated Configs and Nodes, although the backend servers represented by the Nodes will not be changed or removed. Deleting a NodeBalancer will cause you to lose access to the IP Addresses assigned to this NodeBalancer.<br /> |
| `_getNodeBalancer` | `EXEC` | `nodeBalancerId` | Returns a single NodeBalancer you can access.<br /> |
| `_getNodeBalancers` | `EXEC` |  | Returns a paginated list of NodeBalancers you have access to.<br /> |
| `updateNodeBalancer` | `EXEC` | `nodeBalancerId` | Updates information about a NodeBalancer you can access.<br /> |
