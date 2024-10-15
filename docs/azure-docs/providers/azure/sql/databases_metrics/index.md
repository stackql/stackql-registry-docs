---
title: databases_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - databases_metrics
  - sql
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

Creates, updates, deletes, gets or lists a <code>databases_metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>databases_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.sql.databases_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | A database metric name. |
| <CopyableCode code="endTime" /> | `string` | The end time for the metric (ISO-8601 format). |
| <CopyableCode code="metricValues" /> | `array` | The metric values for the specified time window and timestep. |
| <CopyableCode code="startTime" /> | `string` | The start time for the metric (ISO-8601 format). |
| <CopyableCode code="timeGrain" /> | `string` | The time step to be used to summarize the metric values. |
| <CopyableCode code="unit" /> | `string` | The unit of the metric. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$filter, databaseName, resourceGroupName, serverName, subscriptionId" /> | Returns database metrics. |

## `SELECT` examples

Returns database metrics.


```sql
SELECT
name,
endTime,
metricValues,
startTime,
timeGrain,
unit
FROM azure.sql.databases_metrics
WHERE $filter = '{{ $filter }}'
AND databaseName = '{{ databaseName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND serverName = '{{ serverName }}'
AND subscriptionId = '{{ subscriptionId }}';
```