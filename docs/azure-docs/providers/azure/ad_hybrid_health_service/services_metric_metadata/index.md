---
title: services_metric_metadata
hide_title: false
hide_table_of_contents: false
keywords:
  - services_metric_metadata
  - ad_hybrid_health_service
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
<tr><td><b>Name</b></td><td><code>services_metric_metadata</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ad_hybrid_health_service.services_metric_metadata</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `displayName` | `string` | The display name for the metric. |
| `groupings` | `array` | The groupings for the metrics. |
| `isDefault` | `boolean` | Indicates if the metric is a default metric or not. |
| `isDevOps` | `boolean` | Indicates if the metric is visible to DevOps or not. |
| `isPerfCounter` | `boolean` | Indicates if the metric is a performance counter metric or not. |
| `kind` | `string` | Indicates whether the dashboard to represent the metric is a line, bar,pie, area or donut chart. |
| `maxValue` | `integer` | The maximum value. |
| `metricName` | `string` | The metric name |
| `metricsProcessorClassName` | `string` | The name of the class which retrieve and process the metric. |
| `minValue` | `integer` | The minimum value. |
| `valueKind` | `string` | Indicates if the metrics is a rate,value, percent or duration type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get` | `SELECT` | `metricName, serviceName` |
| `list` | `SELECT` | `serviceName` |
| `_list` | `EXEC` | `serviceName` |
