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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>nodebalancers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.instances.nodebalancers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | This NodeBalancer's unique ID.<br /> |
| <CopyableCode code="client_conn_throttle" /> | `integer` | Throttle connections per second.  Set to 0 (zero) to disable throttling.<br /> |
| <CopyableCode code="created" /> | `string` | When this NodeBalancer was created.<br /> |
| <CopyableCode code="hostname" /> | `string` | This NodeBalancer's hostname, beginning with its IP address and ending with _.ip.linodeusercontent.com_.<br /> |
| <CopyableCode code="ipv4" /> | `string` | This NodeBalancer's public IPv4 address.<br /> |
| <CopyableCode code="ipv6" /> | `string` | This NodeBalancer's public IPv6 address.<br /> |
| <CopyableCode code="label" /> | `string` | This NodeBalancer's label. These must be unique on your Account.<br /> |
| <CopyableCode code="region" /> | `string` | The Region where this NodeBalancer is located. NodeBalancers only support backends in the same Region.<br /> |
| <CopyableCode code="tags" /> | `array` | An array of Tags applied to this object.  Tags are for organizational purposes only.<br /> |
| <CopyableCode code="transfer" /> | `object` | Information about the amount of transfer this NodeBalancer has had so far this month.<br /> |
| <CopyableCode code="updated" /> | `string` | When this NodeBalancer was last updated.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getLinodeNodeBalancers" /> | `SELECT` | <CopyableCode code="linodeId" /> |
| <CopyableCode code="_getLinodeNodeBalancers" /> | `EXEC` | <CopyableCode code="linodeId" /> |
