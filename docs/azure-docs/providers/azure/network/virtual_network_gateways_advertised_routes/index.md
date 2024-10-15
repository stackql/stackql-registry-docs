---
title: virtual_network_gateways_advertised_routes
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateways_advertised_routes
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

Creates, updates, deletes, gets or lists a <code>virtual_network_gateways_advertised_routes</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_network_gateways_advertised_routes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_gateways_advertised_routes" /></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="peer, resourceGroupName, subscriptionId, virtualNetworkGatewayName" /> | This operation retrieves a list of routes the virtual network gateway is advertising to the specified peer. |

## `SELECT` examples

This operation retrieves a list of routes the virtual network gateway is advertising to the specified peer.


```sql
SELECT
asPath,
localAddress,
network,
nextHop,
origin,
sourcePeer,
weight
FROM azure.network.virtual_network_gateways_advertised_routes
WHERE peer = '{{ peer }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkGatewayName = '{{ virtualNetworkGatewayName }}';
```