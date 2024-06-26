---
title: raw_incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - raw_incidents
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>raw_incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.analytics.raw_incidents" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Incident ID |
| <CopyableCode code="description" /> | `string` | The incident description |
| <CopyableCode code="assignment_count" /> | `integer` | Total count of instances where responders were assigned an incident (including through reassignment or escalation) or accepted a responder request. |
| <CopyableCode code="business_hour_interruptions" /> | `integer` | Total number of unique interruptions during business hour.<br />Business hour: 8am-6pm Mon-Fri, based on the user’s time zone.   |
| <CopyableCode code="created_at" /> | `string` | Timestamp of when the incident was created. |
| <CopyableCode code="engaged_seconds" /> | `integer` | Total engaged time across all responders for this incident.  Engaged time is measured from the time a user engages with an incident (by acknowledging or accepting a responder request) until the incident is resolved.  This may include periods in which the incident was snoozed. |
| <CopyableCode code="engaged_user_count" /> | `integer` | Total number of users who engaged (acknowledged, accepted responder request) in the incident. |
| <CopyableCode code="escalation_count" /> | `integer` | Total count of instances where an incident is escalated between responders assigned to an escalation policy. |
| <CopyableCode code="incident_number" /> | `integer` | The PagerDuty incident number |
| <CopyableCode code="major" /> | `boolean` | An incident is classified as a [major incident](https://support.pagerduty.com/docs/operational-reviews#major-incidents) if it has one of the two highest priorities, or if multiple responders are added and acknowledge the incident. |
| <CopyableCode code="off_hour_interruptions" /> | `integer` | Total number of unique interruptions during off hour.<br />Off hour: 6pm-10pm Mon-Fri and all day Sat-Sun, based on the user’s time zone.       |
| <CopyableCode code="priority_id" /> | `string` | ID of the incident's priority level. |
| <CopyableCode code="priority_name" /> | `string` | The user-provided short name of the priority. |
| <CopyableCode code="resolved_at" /> | `string` | Timestamp of when the incident was resolved. |
| <CopyableCode code="seconds_to_engage" /> | `integer` | A measure of *people response time*. This metric measures the time from<br />the first user engagement (acknowledge or responder accept) to the last.<br />This metric is only used for incidents with **multiple responders**;<br />for incidents with one or no engaged users, this value is null. |
| <CopyableCode code="seconds_to_first_ack" /> | `integer` | Time between start of an incident, and the first responder to acknowledge. |
| <CopyableCode code="seconds_to_mobilize" /> | `integer` | Time between start of an incident, and the last additional responder to acknowledge.  If an incident has one or less responders, the value will be null. |
| <CopyableCode code="seconds_to_resolve" /> | `integer` | Time from when incident triggered until it was resolved. |
| <CopyableCode code="service_id" /> | `string` | ID of the service that the incident triggered on. |
| <CopyableCode code="service_name" /> | `string` | Name of the service that the incident triggered on. |
| <CopyableCode code="sleep_hour_interruptions" /> | `integer` | Total number of unique interruptions during sleep hour.<br />Sleep hour: 10pm-8am every day, based on the user’s time zone. |
| <CopyableCode code="snoozed_seconds" /> | `integer` | Total seconds the incident has been snoozed for. |
| <CopyableCode code="team_id" /> | `string` | ID of the team the incident was assigned to. |
| <CopyableCode code="team_name" /> | `string` | Name of the team the incident was assigned to. |
| <CopyableCode code="urgency" /> | `string` | Notification level |
| <CopyableCode code="user_defined_effort_seconds" /> | `integer` | The total response effort in seconds,<br />[as defined by the user](https://support.pagerduty.com/docs/editing-incidents#edit-incident-duration). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_analytics_incidents" /> | `SELECT` |  | Provides enriched incident data and metrics for multiple incidents.<br /><br />Example metrics include Seconds to Resolve, Seconds to Engage, Snoozed Seconds, and Sleep Hour Interruptions. Some metric definitions can be found in our [Knowledge Base](https://support.pagerduty.com/docs/pagerduty-analytics).<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br />&lt;!-- theme: info --&gt;<br />&gt; A `team_ids` or `service_ids` filter is required for [user-level API keys](https://support.pagerduty.com/docs/using-the-api#section-generating-a-personal-rest-api-key) or keys generated through an OAuth flow. Account-level API keys do not have this requirement.<br />&lt;!-- theme: info --&gt;<br />&gt; **Note:** Analytics data is updated once per day. It takes up to 24 hours before new incidents appear in the Analytics API.<br /><br />Scoped OAuth requires: `analytics.read`<br /> |
| <CopyableCode code="get_analytics_incidents_by_id" /> | `SELECT` | <CopyableCode code="id" /> | Provides enriched incident data and metrics for a single incident.<br /><br />Example metrics include Seconds to Resolve, Seconds to Engage, Snoozed Seconds, and Sleep Hour Interruptions. Some metric definitions can be found in our [Knowledge Base](https://support.pagerduty.com/docs/pagerduty-analytics).<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br />&lt;!-- theme: info --&gt;<br />&gt; **Note:** Analytics data is updated once per day. It takes up to 24 hours before new incidents appear in the Analytics API.<br /><br />Scoped OAuth requires: `analytics.read`<br /> |
| <CopyableCode code="_get_analytics_incidents_by_id" /> | `EXEC` | <CopyableCode code="id" /> | Provides enriched incident data and metrics for a single incident.<br /><br />Example metrics include Seconds to Resolve, Seconds to Engage, Snoozed Seconds, and Sleep Hour Interruptions. Some metric definitions can be found in our [Knowledge Base](https://support.pagerduty.com/docs/pagerduty-analytics).<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br />&lt;!-- theme: info --&gt;<br />&gt; **Note:** Analytics data is updated once per day. It takes up to 24 hours before new incidents appear in the Analytics API.<br /><br />Scoped OAuth requires: `analytics.read`<br /> |
