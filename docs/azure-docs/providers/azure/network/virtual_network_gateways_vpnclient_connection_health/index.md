---
title: virtual_network_gateways_vpnclient_connection_health
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateways_vpnclient_connection_health
  - network
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>virtual_network_gateways_vpnclient_connection_health</code> resource.

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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | Get VPN client connection health detail per P2S client connection of the virtual network gateway in the specified resource group. |

## `SELECT` examples

Get VPN client connection health detail per P2S client connection of the virtual network gateway in the specified resource group.


```sql
SELECT
egressBytesTransferred,
egressPacketsTransferred,
ingressBytesTransferred,
ingressPacketsTransferred,
maxBandwidth,
maxPacketsPerSecond,
privateIpAddress,
publicIpAddress,
vpnConnectionDuration,
vpnConnectionId,
vpnConnectionTime,
vpnUserName
FROM azure.network.virtual_network_gateways_vpnclient_connection_health
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkGatewayName = '{{ virtualNetworkGatewayName }}';
```