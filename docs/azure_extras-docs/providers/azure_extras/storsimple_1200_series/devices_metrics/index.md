---
title: devices_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_metrics
  - storsimple_1200_series
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

Creates, updates, deletes, gets or lists a <code>devices_metrics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>devices_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.devices_metrics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | The name of the metric |
| <CopyableCode code="dimensions" /> | `array` | The Metric dimension which indicates the source of the metric |
| <CopyableCode code="endTime" /> | `string` | The metric end time |
| <CopyableCode code="primaryAggregation" /> | `string` | The metric aggregation type |
| <CopyableCode code="resourceId" /> | `string` | The id of metric source |
| <CopyableCode code="startTime" /> | `string` | The metric start time |
| <CopyableCode code="timeGrain" /> | `string` | The time grain, time grain indicates frequency of the metric data |
| <CopyableCode code="type" /> | `string` | The Type of the metric data |
| <CopyableCode code="unit" /> | `string` | The unit of the metric data |
| <CopyableCode code="values" /> | `array` | The metric data |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> | Retrieves the device metrics. |

## `SELECT` examples

Retrieves the device metrics.


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
FROM azure_extras.storsimple_1200_series.devices_metrics
WHERE deviceName = '{{ deviceName }}'
AND managerName = '{{ managerName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```