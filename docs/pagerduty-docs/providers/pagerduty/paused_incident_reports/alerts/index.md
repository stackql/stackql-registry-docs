---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.paused_incident_reports.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `resolved_after_pause_alerts` | `array` | An array of Alerts that were resolved after being paused. |
| `since` | `string` | The start of the date range over which the report data is represented. |
| `triggered_after_pause_alerts` | `array` | An array of Alerts that were triggered after being paused. |
| `until` | `string` | The end of the date range over which the report data is represented. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_paused_incident_report_alerts` | `SELECT` |  |
| `_get_paused_incident_report_alerts` | `EXEC` |  |
