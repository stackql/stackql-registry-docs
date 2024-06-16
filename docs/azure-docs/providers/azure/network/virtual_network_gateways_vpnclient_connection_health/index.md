---
title: virtual_network_gateways_vpnclient_connection_health
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateways_vpnclient_connection_health
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
<tr><td><b>Name</b></td><td><code>virtual_network_gateways_vpnclient_connection_health</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_gateways_vpnclient_connection_health" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="egressBytesTransferred" /> | `integer` | The egress bytes per second. |
| <CopyableCode code="egressPacketsTransferred" /> | `integer` | The egress packets per second. |
| <CopyableCode code="ingressBytesTransferred" /> | `integer` | The ingress bytes per second. |
| <CopyableCode code="ingressPacketsTransferred" /> | `integer` | The ingress packets per second. |
| <CopyableCode code="maxBandwidth" /> | `integer` | The max band width. |
| <CopyableCode code="maxPacketsPerSecond" /> | `integer` | The max packets transferred per second. |
| <CopyableCode code="privateIpAddress" /> | `string` | The assigned private Ip of a connected vpn client. |
| <CopyableCode code="publicIpAddress" /> | `string` | The public Ip of a connected vpn client. |
| <CopyableCode code="vpnConnectionDuration" /> | `integer` | The duration time of a connected vpn client. |
| <CopyableCode code="vpnConnectionId" /> | `string` | The vpn client Id. |
| <CopyableCode code="vpnConnectionTime" /> | `string` | The start time of a connected vpn client. |
| <CopyableCode code="vpnUserName" /> | `string` | The user name of a connected vpn client. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> |
