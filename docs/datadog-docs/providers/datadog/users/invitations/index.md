---
title: invitations
hide_title: false
hide_table_of_contents: false
keywords:
  - invitations
  - users
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>invitations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.users.invitations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the user invitation. |
| `attributes` | `object` | Attributes of a user invitation. |
| `relationships` | `object` | Relationships data for user invitation. |
| `type` | `string` | User invitations type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_invitation` | `SELECT` | `user_invitation_uuid, dd_site` | Returns a single user invitation by its UUID. |
| `_get_invitation` | `EXEC` | `user_invitation_uuid, dd_site` | Returns a single user invitation by its UUID. |
| `send_invitations` | `EXEC` | `data__data, dd_site` | Sends emails to one or more users inviting them to join the organization. |
