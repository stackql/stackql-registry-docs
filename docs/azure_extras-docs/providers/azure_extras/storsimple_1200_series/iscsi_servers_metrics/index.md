---
title: iscsi_servers_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - iscsi_servers_metrics
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>iscsi_servers_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.iscsi_servers_metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | The name of the metric |
| `dimensions` | `array` | The Metric dimension which indicates the source of the metric |
| `endTime` | `string` | The metric end time |
| `primaryAggregation` | `string` | The metric aggregation type |
| `resourceId` | `string` | The id of metric source |
| `startTime` | `string` | The metric start time |
| `timeGrain` | `string` | The time grain, time grain indicates frequency of the metric data |
| `type` | `string` | The Type of the metric data |
| `unit` | `string` | The unit of the metric data |
| `values` | `array` | The metric data |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId` |
