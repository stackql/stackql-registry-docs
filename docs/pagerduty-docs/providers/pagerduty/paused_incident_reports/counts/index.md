---
title: counts
hide_title: false
hide_table_of_contents: false
keywords:
  - counts
  - paused_incident_reports
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
<tr><td><b>Name</b></td><td><code>counts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.paused_incident_reports.counts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `paused_count` | `number` | The total number of paused Alerts for the Account or Servce. |
| `resolved_after_pause_count` | `number` | The total number of paused Alerts for the Account or Service that were resolved after being paused and not triggered (transient Alerts). |
| `since` | `string` | The start of the date range over which the report data is represented. |
| `triggered_after_pause_count` | `number` | The total number of paused Alerts for the Account or Service that were triggerd after being paused (non-transient Alerts). |
| `until` | `string` | The end of the date range over which the report data is represented. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_paused_incident_report_counts` | `SELECT` |  |
| `_get_paused_incident_report_counts` | `EXEC` |  |
