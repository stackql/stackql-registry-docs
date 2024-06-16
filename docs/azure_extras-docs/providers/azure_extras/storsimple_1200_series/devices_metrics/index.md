---
title: devices_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_metrics
  - storsimple_1200_series
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




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
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> |
