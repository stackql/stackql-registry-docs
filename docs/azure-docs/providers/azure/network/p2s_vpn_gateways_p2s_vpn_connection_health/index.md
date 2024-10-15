---
title: p2s_vpn_gateways_p2s_vpn_connection_health
hide_title: false
hide_table_of_contents: false
keywords:
  - p2s_vpn_gateways_p2s_vpn_connection_health
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

Creates, updates, deletes, gets or lists a <code>p2s_vpn_gateways_p2s_vpn_connection_health</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>p2s_vpn_gateways_p2s_vpn_connection_health</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.p2s_vpn_gateways_p2s_vpn_connection_health" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID. |
| <CopyableCode code="name" /> | `string` | Resource name. |
| <CopyableCode code="etag" /> | `string` | A unique read-only string that changes whenever the resource is updated. |
| <CopyableCode code="location" /> | `string` | Resource location. |
| <CopyableCode code="properties" /> | `object` | Parameters for P2SVpnGateway. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Resource type. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="gatewayName, resourceGroupName, subscriptionId" /> | Gets the connection health of P2S clients of the virtual wan P2SVpnGateway in the specified resource group. |

## `SELECT` examples

Gets the connection health of P2S clients of the virtual wan P2SVpnGateway in the specified resource group.


```sql
SELECT
id,
name,
etag,
location,
properties,
tags,
type
FROM azure.network.p2s_vpn_gateways_p2s_vpn_connection_health
WHERE gatewayName = '{{ gatewayName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```