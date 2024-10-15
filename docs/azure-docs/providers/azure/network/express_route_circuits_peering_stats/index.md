---
title: express_route_circuits_peering_stats
hide_title: false
hide_table_of_contents: false
keywords:
  - express_route_circuits_peering_stats
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

Creates, updates, deletes, gets or lists a <code>express_route_circuits_peering_stats</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>express_route_circuits_peering_stats</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.express_route_circuits_peering_stats" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="primarybytesIn" /> | `integer` | The Primary BytesIn of the peering. |
| <CopyableCode code="primarybytesOut" /> | `integer` | The primary BytesOut of the peering. |
| <CopyableCode code="secondarybytesIn" /> | `integer` | The secondary BytesIn of the peering. |
| <CopyableCode code="secondarybytesOut" /> | `integer` | The secondary BytesOut of the peering. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="circuitName, peeringName, resourceGroupName, subscriptionId" /> | Gets all stats from an express route circuit in a resource group. |

## `SELECT` examples

Gets all stats from an express route circuit in a resource group.


```sql
SELECT
primarybytesIn,
primarybytesOut,
secondarybytesIn,
secondarybytesOut
FROM azure.network.express_route_circuits_peering_stats
WHERE circuitName = '{{ circuitName }}'
AND peeringName = '{{ peeringName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```