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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>checks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.uptime.checks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A unique ID that can be used to identify and reference the check. |
| `name` | `string` | A human-friendly display name. |
| `regions` | `array` | An array containing the selected regions to perform healthchecks from. |
| `target` | `string` | The endpoint to perform healthchecks on. |
| `type` | `string` | The type of health check to perform. |
| `enabled` | `boolean` | A boolean value indicating whether the check is enabled/disabled. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `check_get` | `SELECT` | `check_id` | To show information about an existing check, send a GET request to `/v2/uptime/checks/$CHECK_ID`. |
| `list` | `SELECT` |  | To list all of the Uptime checks on your account, send a GET request to `/v2/uptime/checks`. |
| `check_create` | `INSERT` | `data__enabled, data__name, data__regions, data__target, data__type` | To create an Uptime check, send a POST request to `/v2/uptime/checks` specifying the attributes<br />in the table below in the JSON body.<br /> |
| `check_delete` | `DELETE` | `check_id` | To delete an Uptime check, send a DELETE request to `/v2/uptime/checks/$CHECK_ID`. A 204 status<br />code with no body will be returned in response to a successful request.<br /><br /><br />Deleting a check will also delete alerts associated with the check.<br /> |
| `_check_get` | `EXEC` | `check_id` | To show information about an existing check, send a GET request to `/v2/uptime/checks/$CHECK_ID`. |
| `_list` | `EXEC` |  | To list all of the Uptime checks on your account, send a GET request to `/v2/uptime/checks`. |
| `check_update` | `EXEC` | `check_id` | To update the settings of an Uptime check, send a PUT request to `/v2/uptime/checks/$CHECK_ID`.<br /> |
