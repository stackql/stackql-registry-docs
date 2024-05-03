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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>check_alerts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.uptime.check_alerts" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference the alert. |
| <CopyableCode code="name" /> | `string` | A human-friendly display name. |
| <CopyableCode code="comparison" /> | `string` | The comparison operator used against the alert's threshold. |
| <CopyableCode code="notifications" /> | `object` | The notification settings for a trigger alert. |
| <CopyableCode code="period" /> | `string` | Period of time the threshold must be exceeded to trigger the alert. |
| <CopyableCode code="threshold" /> | `integer` | The threshold at which the alert will enter a trigger state. The specific threshold is dependent on the alert type. |
| <CopyableCode code="type" /> | `string` | The type of alert. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="alert_get" /> | `SELECT` | <CopyableCode code="alert_id, check_id" /> | To show information about an existing alert, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts/$ALERT_ID`. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="check_id" /> | To list all of the alerts for an Uptime check, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts`. |
| <CopyableCode code="alert_create" /> | `INSERT` | <CopyableCode code="check_id, data__name, data__notifications, data__type" /> | To create an Uptime alert, send a POST request to `/v2/uptime/checks/$CHECK_ID/alerts` specifying the attributes<br />in the table below in the JSON body.<br /> |
| <CopyableCode code="alert_delete" /> | `DELETE` | <CopyableCode code="alert_id, check_id" /> | To delete an Uptime alert, send a DELETE request to `/v2/uptime/checks/$CHECK_ID/alerts/$ALERT_ID`. A 204 status<br />code with no body will be returned in response to a successful request.<br /> |
| <CopyableCode code="_alert_get" /> | `EXEC` | <CopyableCode code="alert_id, check_id" /> | To show information about an existing alert, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts/$ALERT_ID`. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="check_id" /> | To list all of the alerts for an Uptime check, send a GET request to `/v2/uptime/checks/$CHECK_ID/alerts`. |
| <CopyableCode code="alert_update" /> | `EXEC` | <CopyableCode code="alert_id, check_id" /> | To update the settings of an Uptime alert, send a PUT request to `/v2/uptime/checks/$CHECK_ID/alerts/$ALERT_ID`.<br /> |
