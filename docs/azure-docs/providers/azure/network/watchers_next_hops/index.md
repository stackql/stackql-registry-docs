---
title: watchers_next_hops
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers_next_hops
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

Creates, updates, deletes, gets or lists a <code>watchers_next_hops</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>watchers_next_hops</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.watchers_next_hops" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="nextHopIpAddress" /> | `string` | Next hop IP Address. |
| <CopyableCode code="nextHopType" /> | `string` | Next hop type. |
| <CopyableCode code="routeTableId" /> | `string` | The resource identifier for the route table associated with the route being returned. If the route being returned does not correspond to any user created routes then this field will be the string 'System Route'. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId, data__destinationIPAddress, data__sourceIPAddress, data__targetResourceId" /> | Gets the next hop from the specified VM. |

## `SELECT` examples

Gets the next hop from the specified VM.


```sql
SELECT
nextHopIpAddress,
nextHopType,
routeTableId
FROM azure.network.watchers_next_hops
WHERE networkWatcherName = '{{ networkWatcherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__destinationIPAddress = '{{ data__destinationIPAddress }}'
AND data__sourceIPAddress = '{{ data__sourceIPAddress }}'
AND data__targetResourceId = '{{ data__targetResourceId }}';
```