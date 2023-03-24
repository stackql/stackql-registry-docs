---
title: check_alerts
hide_title: false
hide_table_of_contents: false
keywords:
  - check_alerts
  - uptime
  - digitalocean    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/digitalocean/stackql-digitalocean-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>check_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.uptime.check_alerts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A unique ID that can be used to identify and reference the alert. |
| `name` | `string` | A human-friendly display name. |
| `notifications` | `object` | The notification settings for a trigger alert. |
| `period` | `string` | Period of time the threshold must be exceeded to trigger the alert. |
| `threshold` | `integer` | The threshold at which the alert will enter a trigger state. The specific threshold is dependent on the alert type. |
| `type` | `string` | The type of alert. |
| `comparison` | `string` | The comparison operator used against the alert's threshold. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `alert_get` | `SELECT` | `alert_id, check_id` | To show information about an existing alert, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts/$ALERT_ID`. |
| `list` | `SELECT` | `check_id` | To list all of the alerts for an Uptime check, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts`. |
| `alert_create` | `INSERT` | `check_id` | To create an Uptime alert, send a POST request to `/v2/uptime/checks/$CHECK_ID/alerts` specifying the attributes<br />in the table below in the JSON body.<br /> |
| `alert_delete` | `DELETE` | `alert_id, check_id` | To delete an Uptime alert, send a DELETE request to `/v2/uptime/checks/$CHECK_ID/alerts/$ALERT_ID`. A 204 status<br />code with no body will be returned in response to a successful request.<br /> |
| `_alert_get` | `EXEC` | `alert_id, check_id` | To show information about an existing alert, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts/$ALERT_ID`. |
| `_list` | `EXEC` | `check_id` | To list all of the alerts for an Uptime check, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts`. |
| `alert_update` | `EXEC` | `alert_id, check_id` | To update the settings of an Uptime alert, send a PUT request to `/v2/uptime/checks/$CHECK_ID/alerts/$ALERT_ID`.<br /> |
