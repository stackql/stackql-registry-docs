---
title: devices_metric_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_metric_definition
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
<tr><td><b>Name</b></td><td><code>devices_metric_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_extras.storsimple_1200_series.devices_metric_definition" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `object` | The name of the metric |
| <CopyableCode code="dimensions" /> | `array` | The supported dimensions |
| <CopyableCode code="metricAvailabilities" /> | `array` | The available metric granularities |
| <CopyableCode code="primaryAggregationType" /> | `string` | The metric aggregation type |
| <CopyableCode code="resourceId" /> | `string` | The metric source id |
| <CopyableCode code="type" /> | `string` | The metric definition type |
| <CopyableCode code="unit" /> | `string` | The metric unit |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="deviceName, managerName, resourceGroupName, subscriptionId" /> |
