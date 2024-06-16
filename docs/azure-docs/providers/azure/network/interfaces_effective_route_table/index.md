---
title: interfaces_effective_route_table
hide_title: false
hide_table_of_contents: false
keywords:
  - interfaces_effective_route_table
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>interfaces_effective_route_table</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.interfaces_effective_route_table" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of the user defined route. This is optional. |
| <CopyableCode code="addressPrefix" /> | `array` | The address prefixes of the effective routes in CIDR notation. |
| <CopyableCode code="disableBgpRoutePropagation" /> | `boolean` | If true, on-premises routes are not propagated to the network interfaces in the subnet. |
| <CopyableCode code="nextHopIpAddress" /> | `array` | The IP address of the next hop of the effective route. |
| <CopyableCode code="nextHopType" /> | `string` | The type of Azure hop the packet should be sent to. |
| <CopyableCode code="source" /> | `string` | Who created the route. |
| <CopyableCode code="state" /> | `string` | The value of effective route. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId" /> |
