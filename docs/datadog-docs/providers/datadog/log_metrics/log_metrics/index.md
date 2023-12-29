---
title: log_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - log_metrics
  - log_metrics
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
<tr><td><b>Name</b></td><td><code>log_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.log_metrics.log_metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The name of the log-based metric. |
| `attributes` | `object` | The object describing a Datadog log-based metric. |
| `type` | `string` | The type of the resource. The value should always be logs_metrics. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_logs_metric` | `SELECT` | `metric_id, dd_site` | Get a specific log-based metric from your organization. |
| `list_logs_metrics` | `SELECT` | `dd_site` | Get the list of configured log-based metrics with their definitions. |
| `create_logs_metric` | `INSERT` | `data__data, dd_site` | Create a metric based on your ingested logs in your organization.<br />Returns the log-based metric object from the request body when the request is successful. |
| `delete_logs_metric` | `DELETE` | `metric_id, dd_site` | Delete a specific log-based metric from your organization. |
| `_get_logs_metric` | `EXEC` | `metric_id, dd_site` | Get a specific log-based metric from your organization. |
| `_list_logs_metrics` | `EXEC` | `dd_site` | Get the list of configured log-based metrics with their definitions. |
| `update_logs_metric` | `EXEC` | `metric_id, data__data, dd_site` | Update a specific log-based metric from your organization.<br />Returns the log-based metric object from the request body when the request is successful. |
