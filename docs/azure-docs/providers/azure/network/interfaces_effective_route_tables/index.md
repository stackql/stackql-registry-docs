---
title: interfaces_effective_route_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - interfaces_effective_route_tables
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

Creates, updates, deletes, gets or lists a <code>interfaces_effective_route_tables</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>interfaces_effective_route_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.interfaces_effective_route_tables" /></td></tr>
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
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkInterfaceName, resourceGroupName, subscriptionId" /> | Gets all route tables applied to a network interface. |

## `SELECT` examples

Gets all route tables applied to a network interface.


```sql
SELECT
name,
addressPrefix,
disableBgpRoutePropagation,
nextHopIpAddress,
nextHopType,
source,
state
FROM azure.network.interfaces_effective_route_tables
WHERE networkInterfaceName = '{{ networkInterfaceName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```