---
title: virtual_network_gateway_connections_ike_sas
hide_title: false
hide_table_of_contents: false
keywords:
  - virtual_network_gateway_connections_ike_sas
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

Creates, updates, deletes, gets or lists a <code>virtual_network_gateway_connections_ike_sas</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>virtual_network_gateway_connections_ike_sas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.virtual_network_gateway_connections_ike_sas" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource.


## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, virtualNetworkGatewayConnectionName" /> | Lists IKE Security Associations for the virtual network gateway connection in the specified resource group. |

## `SELECT` examples

Lists IKE Security Associations for the virtual network gateway connection in the specified resource group.


```sql
SELECT

FROM azure.network.virtual_network_gateway_connections_ike_sas
WHERE resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND virtualNetworkGatewayConnectionName = '{{ virtualNetworkGatewayConnectionName }}';
```