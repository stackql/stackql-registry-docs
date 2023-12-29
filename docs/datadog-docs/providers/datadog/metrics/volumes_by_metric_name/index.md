---
title: volumes_by_metric_name
hide_title: false
hide_table_of_contents: false
keywords:
  - volumes_by_metric_name
  - metrics
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>volumes_by_metric_name</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.metrics.volumes_by_metric_name</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The metric name for this resource. |
| `MetricIngestedIndexedVolume_attributes` | `object` | Object containing the definition of a metric's ingested and indexed volume. |
| `MetricIngestedIndexedVolume_id` | `string` | The metric name for this resource. |
| `MetricIngestedIndexedVolume_type` | `string` | The metric ingested and indexed volume type. |
| `attributes` | `object` | Object containing the definition of a metric's distinct volume. |
| `type` | `string` | The metric distinct volume type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_volumes_by_metric_name` | `SELECT` | `metric_name, dd_site` |
| `_list_volumes_by_metric_name` | `EXEC` | `metric_name, dd_site` |
