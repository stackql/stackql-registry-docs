---
title: managers_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - managers_metrics
  - storsimple_8000_series
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

Creates, updates, deletes, gets or lists a <code>managers_metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>managers_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_8000_series.managers_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | The metric name. |
| <CopyableCode code="dimensions" /> | `array` | The metric dimensions. |
| <CopyableCode code="endTime" /> | `string` | The end time of the metric data. |
| <CopyableCode code="primaryAggregation" /> | `string` | The metric aggregation type. |
| <CopyableCode code="resourceId" /> | `string` | The ID of metric source. |
| <CopyableCode code="startTime" /> | `string` | The start time of the metric data. |
| <CopyableCode code="timeGrain" /> | `string` | The time granularity of the metric data. |
| <CopyableCode code="type" /> | `string` | The type of the metric data. |
| <CopyableCode code="unit" /> | `string` | The unit of the metric data. |
| <CopyableCode code="values" /> | `array` | The list of the metric data. |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="$filter, managerName, resourceGroupName, subscriptionId" /> | Gets the metrics for the specified manager. |

## `SELECT` examples

Gets the metrics for the specified manager.


```sql
SELECT
name,
dimensions,
endTime,
primaryAggregation,
resourceId,
startTime,
timeGrain,
type,
unit,
values
FROM azure_extras.storsimple_8000_series.managers_metrics
WHERE $filter = '{{ $filter }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```