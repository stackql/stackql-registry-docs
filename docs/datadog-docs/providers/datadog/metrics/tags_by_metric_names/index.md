---
title: tags_by_metric_names
hide_title: false
hide_table_of_contents: false
keywords:
  - tags_by_metric_names
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
<tr><td><b>Name</b></td><td><code>tags_by_metric_names</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.metrics.tags_by_metric_names</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The metric name for this resource. |
| `attributes` | `object` | Object containing the definition of a metric's tags. |
| `type` | `string` | The metric resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_tags_by_metric_name` | `SELECT` | `metric_name, dd_site` |
| `_list_tags_by_metric_name` | `EXEC` | `metric_name, dd_site` |
