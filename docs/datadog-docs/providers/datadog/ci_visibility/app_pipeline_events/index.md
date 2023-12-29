---
title: app_pipeline_events
hide_title: false
hide_table_of_contents: false
keywords:
  - app_pipeline_events
  - ci_visibility
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
<tr><td><b>Name</b></td><td><code>app_pipeline_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.ci_visibility.app_pipeline_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID of the event. |
| `attributes` | `object` | JSON object containing all event attributes and their associated values. |
| `type` | `string` | Type of the event. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_ci_app_pipeline_events` | `SELECT` | `dd_site` | List endpoint returns CI Visibility pipeline events that match a [search query](https://docs.datadoghq.com/continuous_integration/explorer/search_syntax/).<br />[Results are paginated similarly to logs](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).<br /><br />Use this endpoint to see your latest pipeline events. |
| `create_ci_app_pipeline_event` | `INSERT` | `dd_site` | Send your pipeline event to your Datadog platform over HTTP. For details about how pipeline executions are modeled and what execution types we support, see [Pipeline Data Model And Execution Types](https://docs.datadoghq.com/continuous_integration/guides/pipeline_data_model/).<br /><br />Pipeline events can be submitted with a timestamp that is up to 18 hours in the past. |
| `_list_ci_app_pipeline_events` | `EXEC` | `dd_site` | List endpoint returns CI Visibility pipeline events that match a [search query](https://docs.datadoghq.com/continuous_integration/explorer/search_syntax/).<br />[Results are paginated similarly to logs](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).<br /><br />Use this endpoint to see your latest pipeline events. |
| `aggregate_ci_app_pipeline_events` | `EXEC` | `dd_site` | Use this API endpoint to aggregate CI Visibility pipeline events into buckets of computed metrics and timeseries. |
| `search_ci_app_pipeline_events` | `EXEC` | `dd_site` | List endpoint returns CI Visibility pipeline events that match a [search query](https://docs.datadoghq.com/continuous_integration/explorer/search_syntax/).<br />[Results are paginated similarly to logs](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).<br /><br />Use this endpoint to build complex events filtering and search. |
