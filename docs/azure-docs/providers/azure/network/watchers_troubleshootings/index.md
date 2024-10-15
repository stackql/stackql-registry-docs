---
title: watchers_troubleshootings
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers_troubleshootings
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

Creates, updates, deletes, gets or lists a <code>watchers_troubleshootings</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>watchers_troubleshootings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.network.watchers_troubleshootings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="code" /> | `string` | The result code of the troubleshooting. |
| <CopyableCode code="endTime" /> | `string` | The end time of the troubleshooting. |
| <CopyableCode code="results" /> | `array` | Information from troubleshooting. |
| <CopyableCode code="startTime" /> | `string` | The start time of the troubleshooting. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkWatcherName, resourceGroupName, subscriptionId, data__properties, data__targetResourceId" /> | Initiate troubleshooting on a specified resource. |

## `SELECT` examples

Initiate troubleshooting on a specified resource.


```sql
SELECT
code,
endTime,
results,
startTime
FROM azure.network.watchers_troubleshootings
WHERE networkWatcherName = '{{ networkWatcherName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND data__properties = '{{ data__properties }}'
AND data__targetResourceId = '{{ data__targetResourceId }}';
```