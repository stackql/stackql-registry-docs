---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
  - events
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.events.events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | the unique ID of the event. |
| `attributes` | `object` | The object description of an event response attribute. |
| `type` | `string` | Type of the event. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_events` | `SELECT` | `dd_site` | List endpoint returns events that match an events search query.<br />[Results are paginated similarly to logs](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).<br /><br />Use this endpoint to see your latest events. |
| `_list_events` | `EXEC` | `dd_site` | List endpoint returns events that match an events search query.<br />[Results are paginated similarly to logs](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).<br /><br />Use this endpoint to see your latest events. |
| `search_events` | `EXEC` | `dd_site` | List endpoint returns events that match an events search query.<br />[Results are paginated similarly to logs](https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination).<br /><br />Use this endpoint to build complex events filtering and search. |
