---
title: nodebalancers
hide_title: false
hide_table_of_contents: false
keywords:
  - nodebalancers
  - instances
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
<tr><td><b>Id</b></td><td><code>linode.instances.nodebalancers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | This NodeBalancer's unique ID.<br /> |
| `ipv4` | `string` | This NodeBalancer's public IPv4 address.<br /> |
| `transfer` | `object` | Information about the amount of transfer this NodeBalancer has had so far this month.<br /> |
| `ipv6` | `string` | This NodeBalancer's public IPv6 address.<br /> |
| `label` | `string` | This NodeBalancer's label. These must be unique on your Account.<br /> |
| `region` | `string` | The Region where this NodeBalancer is located. NodeBalancers only support backends in the same Region.<br /> |
| `created` | `string` | When this NodeBalancer was created.<br /> |
| `client_conn_throttle` | `integer` | Throttle connections per second.  Set to 0 (zero) to disable throttling.<br /> |
| `updated` | `string` | When this NodeBalancer was last updated.<br /> |
| `hostname` | `string` | This NodeBalancer's hostname, beginning with its IP address and ending with _.ip.linodeusercontent.com_.<br /> |
| `tags` | `array` | An array of Tags applied to this object.  Tags are for organizational purposes only.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getLinodeNodeBalancers` | `SELECT` | `linodeId` |
| `_getLinodeNodeBalancers` | `EXEC` | `linodeId` |
