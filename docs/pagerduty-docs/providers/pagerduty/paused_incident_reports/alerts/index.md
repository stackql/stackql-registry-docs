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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.paused_incident_reports.alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="resolved_after_pause_alerts" /> | `array` | An array of Alerts that were resolved after being paused. |
| <CopyableCode code="since" /> | `string` | The start of the date range over which the report data is represented. |
| <CopyableCode code="triggered_after_pause_alerts" /> | `array` | An array of Alerts that were triggered after being paused. |
| <CopyableCode code="until" /> | `string` | The end of the date range over which the report data is represented. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_paused_incident_report_alerts" /> | `SELECT` |  |
| <CopyableCode code="_get_paused_incident_report_alerts" /> | `EXEC` |  |
