---
title: volume_containers_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - volume_containers_metrics
  - storsimple_8000_series
  - azure_extras    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volume_containers_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_8000_series.volume_containers_metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | The metric name. |
| `dimensions` | `array` | The metric dimensions. |
| `endTime` | `string` | The end time of the metric data. |
| `primaryAggregation` | `string` | The metric aggregation type. |
| `resourceId` | `string` | The ID of metric source. |
| `startTime` | `string` | The start time of the metric data. |
| `timeGrain` | `string` | The time granularity of the metric data. |
| `type` | `string` | The type of the metric data. |
| `unit` | `string` | The unit of the metric data. |
| `values` | `array` | The list of the metric data. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `$filter, deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName` |
| `_list` | `EXEC` | `$filter, deviceName, managerName, resourceGroupName, subscriptionId, volumeContainerName` |
