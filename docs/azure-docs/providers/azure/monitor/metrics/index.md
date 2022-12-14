---
title: metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics
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
<tr><td><b>Name</b></td><td><code>metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | the metric Id. |
| `name` | `object` | The localizable string class. |
| `errorCode` | `string` | 'Success' or the error details on query failures for this metric. |
| `errorMessage` | `string` | Error message encountered querying this specific metric. |
| `timeseries` | `array` | the time series returned when a data query is performed. |
| `type` | `string` | the resource type of the metric resource. |
| `unit` | `string` | The unit of the metric. |
| `displayDescription` | `string` | Detailed description of this metric. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `Metrics_List` | `SELECT` | `resourceUri` |
