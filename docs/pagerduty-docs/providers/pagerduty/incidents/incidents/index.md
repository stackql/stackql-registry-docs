---
title: incidents
hide_title: false
hide_table_of_contents: false
keywords:
  - incidents
  - incidents
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
<tr><td><b>Name</b></td><td><code>incidents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.incidents.incidents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `acknowledgements` | `array` | List of all acknowledgements for this incident. This list will be empty if the `Incident.status` is `resolved` or `triggered`. |
| `alert_counts` | `object` |  |
| `assigned_via` | `string` | How the current incident assignments were decided.  Note that `direct_assignment` incidents will not escalate up the attached `escalation_policy` |
| `assignments` | `array` | List of all assignments for this incident. This list will be empty if the `Incident.status` is `resolved`. |
| `body` | `object` |  |
| `conference_bridge` | `object` |  |
| `created_at` | `string` | The date/time the incident was first triggered. |
| `escalation_policy` | `object` |  |
| `first_trigger_log_entry` | `object` |  |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `incident_key` | `string` | The incident's de-duplication key. |
| `incident_number` | `integer` | The number of the incident. This is unique across your account. |
| `incidents_responders` | `array` |  |
| `last_status_change_at` | `string` | The time at which the status of the incident last changed. |
| `last_status_change_by` | `object` | The agent (user, service or integration) that created or modified the Incident Log Entry. |
| `pending_actions` | `array` | The list of pending_actions on the incident. A pending_action object contains a type of action which can be escalate, unacknowledge, resolve or urgency_change. A pending_action object contains at, the time at which the action will take place. An urgency_change pending_action will contain to, the urgency that the incident will change to. |
| `priority` | `object` |  |
| `resolve_reason` | `object` |  |
| `responder_requests` | `array` |  |
| `self` | `string` | the API show URL at which the object is accessible |
| `service` | `object` |  |
| `status` | `string` | The current status of the incident. |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `teams` | `array` | The teams involved in the incident’s lifecycle. |
| `title` | `string` | A succinct description of the nature, symptoms, cause, or effect of the incident. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `urgency` | `string` | The current urgency of the incident. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_incident` | `SELECT` | `X-EARLY-ACCESS, id` | Show detailed information about an incident. Accepts either an incident id, or an incident number.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; The `include[]=field_values` part of this endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| `list_incidents` | `SELECT` |  | List existing incidents.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| `create_incident` | `INSERT` | `From, data__incident` | Create an incident synchronously without a corresponding event from a monitoring service.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.write`<br /> |
| `_get_incident` | `EXEC` | `X-EARLY-ACCESS, id` | Show detailed information about an incident. Accepts either an incident id, or an incident number.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; The `include[]=field_values` part of this endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| `_list_incidents` | `EXEC` |  | List existing incidents.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| `create_incident_responder_request` | `EXEC` | `From, id, data__message, data__requester_id, data__responder_request_targets` | Send a new responder request for the specified incident.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.write`<br /> |
| `create_incident_snooze` | `EXEC` | `From, id, data__duration` | Snooze an incident.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.write`<br /> |
| `create_incident_status_update` | `EXEC` | `From, id, data__message` | Create a new status update for the specified incident. Optionally pass `subject` and `html_message` properties in the request body to override the email notification that gets sent.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.write`<br /> |
| `merge_incidents` | `EXEC` | `From, id, data__source_incidents` | Merge a list of source incidents into this incident.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.write`<br /> |
| `remove_incident_notification_subscribers` | `EXEC` | `id, data__subscribers` | Unsubscribes the matching Subscribers from Incident Status Update Notifications.<br /><br />Scoped OAuth requires: `subscribers.write`<br /> |
| `update_incident` | `EXEC` | `From, id, data__incident` | Acknowledge, resolve, escalate or reassign an incident.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.write`<br /> |
| `update_incidents` | `EXEC` | `From, data__incidents` | Acknowledge, resolve, escalate or reassign one or more incidents.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />A maximum of 250 incidents may be updated at a time. If more than this number of incidents are given, the API will respond with status 413 (Request Entity Too Large).<br /><br />Note: the manage incidents API endpoint is rate limited to 500 requests per minute.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.write`<br /> |
