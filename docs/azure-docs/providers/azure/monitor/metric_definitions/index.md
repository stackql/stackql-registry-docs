---
title: metric_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - metric_definitions
  - monitor
  - azure    
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
<tr><td><b>Name</b></td><td><code>metric_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.metric_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier of the metric definition. |
| `name` | `object` | The localizable string class. |
| `category` | `string` | Custom category name for this metric. |
| `dimensions` | `array` | The name and the display name of the dimension, i.e. it is a localizable string. |
| `displayDescription` | `string` | Detailed description of this metric. |
| `isDimensionRequired` | `boolean` | Flag to indicate whether the dimension is required. |
| `metricAvailabilities` | `array` | The collection of what aggregation intervals are available to be queried. |
| `metricClass` | `string` | The class of the metric. |
| `namespace` | `string` | The namespace the metric belongs to. |
| `primaryAggregationType` | `string` | The aggregation type of the metric. |
| `resourceId` | `string` | The resource identifier of the resource that emitted the metric. |
| `supportedAggregationTypes` | `array` | The collection of what aggregation types are supported. |
| `unit` | `string` | The unit of the metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceUri` |
| `_list` | `EXEC` | `resourceUri` |
