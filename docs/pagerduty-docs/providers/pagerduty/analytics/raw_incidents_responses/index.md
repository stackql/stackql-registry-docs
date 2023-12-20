---
title: raw_incidents_responses
hide_title: false
hide_table_of_contents: false
keywords:
  - raw_incidents_responses
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
<tr><td><b>Name</b></td><td><code>raw_incidents_responses</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.analytics.raw_incidents_responses</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `requested_at` | `string` | Timestamp of when the user was requested. |
| `responded_at` | `string` | Timestamp of when the user responded to the request. |
| `responder_id` | `string` | ID of the user associated with the Incident Response. |
| `responder_name` | `string` | Name of the user associated with the Incident Response. |
| `responder_type` | `string` | Type of responder, where `assigned` means the user was added to the Incident via Assignment at Incident creation,<br />`reassigned` means the user was added to the Incident via Reassignment, `escalated` means the user was added via Escalation,<br />and `added_responder` means the user was added via Responder Reqeuest. |
| `response_status` | `string` | Status of the user's interaction with the Incident notification. |
| `time_to_respond_seconds` | `integer` | Measures the time it took for the user to respond to the Incident request. In other words, `responded_at - requested_at`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_analytics_incident_responses_by_id` | `SELECT` | `id` |
| `_get_analytics_incident_responses_by_id` | `EXEC` | `id` |
