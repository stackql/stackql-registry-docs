---
title: span_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - span_metrics
  - span_metrics
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
<tr><td><b>Name</b></td><td><code>span_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.span_metrics.span_metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The name of the span-based metric. |
| `attributes` | `object` | The object describing a Datadog span-based metric. |
| `type` | `string` | The type of resource. The value should always be spans_metrics. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_spans_metric` | `SELECT` | `metric_id, dd_site` | Get a specific span-based metric from your organization. |
| `list_spans_metrics` | `SELECT` | `dd_site` | Get the list of configured span-based metrics with their definitions. |
| `create_spans_metric` | `INSERT` | `data__data, dd_site` | Create a metric based on your ingested spans in your organization.<br />Returns the span-based metric object from the request body when the request is successful. |
| `delete_spans_metric` | `DELETE` | `metric_id, dd_site` | Delete a specific span-based metric from your organization. |
| `_get_spans_metric` | `EXEC` | `metric_id, dd_site` | Get a specific span-based metric from your organization. |
| `_list_spans_metrics` | `EXEC` | `dd_site` | Get the list of configured span-based metrics with their definitions. |
| `update_spans_metric` | `EXEC` | `metric_id, data__data, dd_site` | Update a specific span-based metric from your organization.<br />Returns the span-based metric object from the request body when the request is successful. |
