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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>counts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.paused_incident_reports.counts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="paused_count" /> | `number` | The total number of paused Alerts for the Account or Servce. |
| <CopyableCode code="resolved_after_pause_count" /> | `number` | The total number of paused Alerts for the Account or Service that were resolved after being paused and not triggered (transient Alerts). |
| <CopyableCode code="since" /> | `string` | The start of the date range over which the report data is represented. |
| <CopyableCode code="triggered_after_pause_count" /> | `number` | The total number of paused Alerts for the Account or Service that were triggerd after being paused (non-transient Alerts). |
| <CopyableCode code="until" /> | `string` | The end of the date range over which the report data is represented. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_paused_incident_report_counts" /> | `SELECT` |  |
| <CopyableCode code="_get_paused_incident_report_counts" /> | `EXEC` |  |
