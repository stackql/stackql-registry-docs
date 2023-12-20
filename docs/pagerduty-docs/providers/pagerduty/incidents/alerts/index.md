---
title: alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - alerts
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
<tr><td><b>Name</b></td><td><code>alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.incidents.alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `_type` | `string` | The type of object being created. |
| `alert_key` | `string` | The alert's de-duplication key. |
| `body` | `object` | A JSON object containing data describing the alert. |
| `created_at` | `string` | The date/time the alert was first triggered. |
| `first_trigger_log_entry` | `object` |  |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `incident` | `object` |  |
| `integration` | `object` |  |
| `self` | `string` | the API show URL at which the object is accessible |
| `service` | `object` |  |
| `severity` | `string` | The magnitude of the problem as reported by the monitoring tool. |
| `status` | `string` | The current status of the alert. |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `suppressed` | `boolean` | Whether or not an alert is suppressed. Suppressed alerts are not created with a parent incident. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_incident_alert` | `SELECT` | `alert_id, id` | Show detailed information about an alert. Accepts an alert id.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />When a service sends an event to PagerDuty, an alert and corresponding incident is triggered in PagerDuty.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| `list_incident_alerts` | `SELECT` | `id` | List alerts for the specified incident.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| `_get_incident_alert` | `EXEC` | `alert_id, id` | Show detailed information about an alert. Accepts an alert id.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />When a service sends an event to PagerDuty, an alert and corresponding incident is triggered in PagerDuty.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| `_list_incident_alerts` | `EXEC` | `id` | List alerts for the specified incident.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.read`<br /> |
| `update_incident_alert` | `EXEC` | `From, alert_id, id, data__alert` | Resolve an alert or associate an alert with a new parent incident.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved.<br /><br />When a service sends an event to PagerDuty, an alert and corresponding incident is triggered in PagerDuty.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.write`<br /> |
| `update_incident_alerts` | `EXEC` | `From, id, data__alerts` | Resolve multiple alerts or associate them with different incidents.<br /><br />An incident represents a problem or an issue that needs to be addressed and resolved. An alert represents a digital signal that was emitted to PagerDuty by the monitoring systems that detected or identified the issue.<br /><br />A maximum of 500 alerts may be updated at a time. If more than this number of alerts are given, the API will respond with status 413 (Request Entity Too Large).<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#incidents)<br /><br />Scoped OAuth requires: `incidents.write`<br /> |
