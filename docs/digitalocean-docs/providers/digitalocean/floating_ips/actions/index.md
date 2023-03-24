---
title: actions
hide_title: false
hide_table_of_contents: false
keywords:
  - actions
  - floating_ips
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
<tr><td><b>Id</b></td><td><code>digitalocean.floating_ips.actions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | A unique numeric ID that can be used to identify and reference an action. |
| `type` | `string` | This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action. |
| `resource_id` | `integer` | A unique identifier for the resource that the action is associated with. |
| `resource_type` | `string` | The type of resource that the action is associated with. |
| `status` | `string` | The current status of the action. This can be "in-progress", "completed", or "errored". |
| `started_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the action was initiated. |
| `completed_at` | `string` | A time value given in ISO8601 combined date and time format that represents when the action was completed. |
| `region` | `object` |  |
| `region_slug` | `string` | A human-readable string that is used as a unique identifier for each region. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `floatingIPsAction_get` | `SELECT` | `action_id, floating_ip` | To retrieve the status of a floating IP action, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions/$ACTION_ID`. |
| `floatingIPsAction_list` | `SELECT` | `floating_ip` | To retrieve all actions that have been executed on a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions`. |
| `floatingIPsAction_post` | `INSERT` | `floating_ip` | To initiate an action on a floating IP send a POST request to<br />`/v2/floating_ips/$FLOATING_IP/actions`. In the JSON body to the request,<br />set the `type` attribute to on of the supported action types:<br /><br />\| Action     \| Details<br />\|------------\|--------<br />\| `assign`   \| Assigns a floating IP to a Droplet<br />\| `unassign` \| Unassign a floating IP from a Droplet<br /> |
| `_floatingIPsAction_get` | `EXEC` | `action_id, floating_ip` | To retrieve the status of a floating IP action, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions/$ACTION_ID`. |
| `_floatingIPsAction_list` | `EXEC` | `floating_ip` | To retrieve all actions that have been executed on a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions`. |
