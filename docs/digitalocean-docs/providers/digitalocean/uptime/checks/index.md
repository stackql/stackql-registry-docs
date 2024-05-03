---
title: checks
hide_title: false
hide_table_of_contents: false
keywords:
  - checks
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
<tr><td><b>Name</b></td><td><code>checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.uptime.checks" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A unique ID that can be used to identify and reference the check. |
| <CopyableCode code="name" /> | `string` | A human-friendly display name. |
| <CopyableCode code="enabled" /> | `boolean` | A boolean value indicating whether the check is enabled/disabled. |
| <CopyableCode code="regions" /> | `array` | An array containing the selected regions to perform healthchecks from. |
| <CopyableCode code="target" /> | `string` | The endpoint to perform healthchecks on. |
| <CopyableCode code="type" /> | `string` | The type of health check to perform. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="check_get" /> | `SELECT` | <CopyableCode code="check_id" /> | To show information about an existing check, send a GET request to `/v2/uptime/checks/$CHECK_ID`. |
| <CopyableCode code="list" /> | `SELECT` |  | To list all of the Uptime checks on your account, send a GET request to `/v2/uptime/checks`. |
| <CopyableCode code="check_create" /> | `INSERT` | <CopyableCode code="data__enabled, data__name, data__regions, data__target, data__type" /> | To create an Uptime check, send a POST request to `/v2/uptime/checks` specifying the attributes<br />in the table below in the JSON body.<br /> |
| <CopyableCode code="check_delete" /> | `DELETE` | <CopyableCode code="check_id" /> | To delete an Uptime check, send a DELETE request to `/v2/uptime/checks/$CHECK_ID`. A 204 status<br />code with no body will be returned in response to a successful request.<br /><br /><br />Deleting a check will also delete alerts associated with the check.<br /> |
| <CopyableCode code="_check_get" /> | `EXEC` | <CopyableCode code="check_id" /> | To show information about an existing check, send a GET request to `/v2/uptime/checks/$CHECK_ID`. |
| <CopyableCode code="_list" /> | `EXEC` |  | To list all of the Uptime checks on your account, send a GET request to `/v2/uptime/checks`. |
| <CopyableCode code="check_update" /> | `EXEC` | <CopyableCode code="check_id" /> | To update the settings of an Uptime check, send a PUT request to `/v2/uptime/checks/$CHECK_ID`.<br /> |
