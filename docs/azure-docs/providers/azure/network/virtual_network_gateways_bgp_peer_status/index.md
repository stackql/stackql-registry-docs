---
title: virtual_network_gateways_bgp_peer_status
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateways_bgp_peer_status
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
<tr><td><b>Name</b></td><td><code>virtual_network_gateways_bgp_peer_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_gateways_bgp_peer_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="asn" /> | `integer` | The autonomous system number of the remote BGP peer. |
| <CopyableCode code="connectedDuration" /> | `string` | For how long the peering has been up. |
| <CopyableCode code="localAddress" /> | `string` | The virtual network gateway's local address. |
| <CopyableCode code="messagesReceived" /> | `integer` | The number of BGP messages received. |
| <CopyableCode code="messagesSent" /> | `integer` | The number of BGP messages sent. |
| <CopyableCode code="neighbor" /> | `string` | The remote BGP peer. |
| <CopyableCode code="routesReceived" /> | `integer` | The number of routes learned from this peer. |
| <CopyableCode code="state" /> | `string` | The BGP peer state. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> |
