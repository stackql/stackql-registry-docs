---
title: metrics_incidents_teams
hide_title: false
hide_table_of_contents: false
keywords:
  - metrics_incidents_teams
  - analytics
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>metrics_incidents_teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.analytics.metrics_incidents_teams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `aggregate_unit` | `string` | The time unit to aggregate metrics by.  If no value is provided, the metrics will be aggregated for the entire period. |
| `data` | `array` |  |
| `filters` | `object` | Accepts a set of filters to apply to the Incidents before aggregating.  Any incidents that do not match the included filters will be omitted from the results |
| `time_zone` | `string` | The time zone to use for the results and grouping. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_analytics_metrics_incidents_team` | `SELECT` |  |
