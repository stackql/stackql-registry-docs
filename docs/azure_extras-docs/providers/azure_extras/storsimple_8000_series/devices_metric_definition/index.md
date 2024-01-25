---
title: devices_metric_definition
hide_title: false
hide_table_of_contents: false
keywords:
  - devices_metric_definition
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
<tr><td><b>Name</b></td><td><code>devices_metric_definition</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_8000_series.devices_metric_definition</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `object` | The metric name. |
| `category` | `string` | The category of the metric. |
| `dimensions` | `array` | The available metric dimensions. |
| `metricAvailabilities` | `array` | The available metric granularities. |
| `primaryAggregationType` | `string` | The metric aggregation type. |
| `resourceId` | `string` | The metric source ID. |
| `type` | `string` | The metric definition type. |
| `unit` | `string` | The metric unit. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` |
| `_list` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` |
