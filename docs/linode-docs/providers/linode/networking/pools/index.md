---
title: pools
hide_title: false
hide_table_of_contents: false
keywords:
  - pools
  - networking
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
<tr><td><b>Name</b></td><td><code>pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="linode.networking.pools" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="prefix" /> | `integer` | The prefix length of the address, denoting how many addresses can be assigned from this pool calculated as 2 &lt;sup&gt;128-prefix&lt;/sup&gt;.<br /> |
| <CopyableCode code="range" /> | `string` | The IPv6 range of addresses in this pool.<br /> |
| <CopyableCode code="region" /> | `string` | The region for this pool of IPv6 addresses.<br /> |
| <CopyableCode code="route_target" /> | `string` | The last address in this block of IPv6 addresses.<br /> |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="getIPv6Pools" /> | `SELECT` |  |
| <CopyableCode code="_getIPv6Pools" /> | `EXEC` |  |
