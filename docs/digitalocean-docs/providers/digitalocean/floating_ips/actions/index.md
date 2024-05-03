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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>actions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="digitalocean.floating_ips.actions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | A unique numeric ID that can be used to identify and reference an action. |
| <CopyableCode code="completed_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the action was completed. |
| <CopyableCode code="region" /> | `object` |  |
| <CopyableCode code="region_slug" /> | `string` | A human-readable string that is used as a unique identifier for each region. |
| <CopyableCode code="resource_id" /> | `integer` | A unique identifier for the resource that the action is associated with. |
| <CopyableCode code="resource_type" /> | `string` | The type of resource that the action is associated with. |
| <CopyableCode code="started_at" /> | `string` | A time value given in ISO8601 combined date and time format that represents when the action was initiated. |
| <CopyableCode code="status" /> | `string` | The current status of the action. This can be "in-progress", "completed", or "errored". |
| <CopyableCode code="type" /> | `string` | This is the type of action that the object represents. For example, this could be "transfer" to represent the state of an image transfer action. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="floatingIPsAction_get" /> | `SELECT` | <CopyableCode code="action_id, floating_ip" /> | To retrieve the status of a floating IP action, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions/$ACTION_ID`. |
| <CopyableCode code="floatingIPsAction_list" /> | `SELECT` | <CopyableCode code="floating_ip" /> | To retrieve all actions that have been executed on a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions`. |
| <CopyableCode code="floatingIPsAction_post" /> | `INSERT` | <CopyableCode code="floating_ip" /> | To initiate an action on a floating IP send a POST request to<br />`/v2/floating_ips/$FLOATING_IP/actions`. In the JSON body to the request,<br />set the `type` attribute to on of the supported action types:<br /><br />\| Action     \| Details<br />\|------------\|--------<br />\| `assign`   \| Assigns a floating IP to a Droplet<br />\| `unassign` \| Unassign a floating IP from a Droplet<br /> |
| <CopyableCode code="_floatingIPsAction_get" /> | `EXEC` | <CopyableCode code="action_id, floating_ip" /> | To retrieve the status of a floating IP action, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions/$ACTION_ID`. |
| <CopyableCode code="_floatingIPsAction_list" /> | `EXEC` | <CopyableCode code="floating_ip" /> | To retrieve all actions that have been executed on a floating IP, send a GET request to `/v2/floating_ips/$FLOATING_IP/actions`. |
