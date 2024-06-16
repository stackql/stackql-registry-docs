---
title: virtual_network_gateways_learned_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateways_learned_routes
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
<tr><td><b>Name</b></td><td><code>virtual_network_gateways_learned_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_gateways_learned_routes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="asPath" /> | `string` | The route's AS path sequence. |
| <CopyableCode code="localAddress" /> | `string` | The gateway's local address. |
| <CopyableCode code="network" /> | `string` | The route's network prefix. |
| <CopyableCode code="nextHop" /> | `string` | The route's next hop. |
| <CopyableCode code="origin" /> | `string` | The source this route was learned from. |
| <CopyableCode code="sourcePeer" /> | `string` | The peer this route was learned from. |
| <CopyableCode code="weight" /> | `integer` | The route's weight. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> |
