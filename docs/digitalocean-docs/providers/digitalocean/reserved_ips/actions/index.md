---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - reserved_ips
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
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>digitalocean.reserved_ips.actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique numeric ID that can be used to identify and reference an action. |
| `region_slug` | `string` | A human-readable string that is used as a unique identifier for each region. |
| `resource_type` | `string` | The type of resource that the action is associated with. |
| `resource_id` | `integer` | A unique identifier for the resource that the action is associated with. |
| `completed_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the action was completed. |
| `type` | `string` | This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action. |
| `region` | `object` |  |
| `started_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the action was initiated. |
| `status` | `string` | The current status of the action. This can be "in-progress", "completed", or "errored". |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `reservedIPsActions_get` | `SELECT` | `action_id, reserved_ip` | To retrieve the status of a reserved IP action, send a GET request to `/v2/reserved_ips/$RESERVED_IP/actions/$ACTION_ID`. |
| `reservedIPsActions_list` | `SELECT` | `reserved_ip` | To retrieve all actions that have been executed on a reserved IP, send a GET request to `/v2/reserved_ips/$RESERVED_IP/actions`. |
| `reservedIPsActions_post` | `INSERT` | `reserved_ip` | To initiate an action on a reserved IP send a POST request to<br />`/v2/reserved_ips/$RESERVED_IP/actions`. In the JSON body to the request,<br />set the `type` attribute to on of the supported action types:<br /><br />\| Action     \| Details<br />\|------------\|--------<br />\| `assign`   \| Assigns a reserved IP to a Droplet<br />\| `unassign` \| Unassign a reserved IP from a Droplet<br /> |
| `_reservedIPsActions_get` | `EXEC` | `action_id, reserved_ip` | To retrieve the status of a reserved IP action, send a GET request to `/v2/reserved_ips/$RESERVED_IP/actions/$ACTION_ID`. |
| `_reservedIPsActions_list` | `EXEC` | `reserved_ip` | To retrieve all actions that have been executed on a reserved IP, send a GET request to `/v2/reserved_ips/$RESERVED_IP/actions`. |
