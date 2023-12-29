---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.users.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the user. |
| `attributes` | `object` | Attributes of user object returned by the API. |
| `relationships` | `object` | Relationships of the user object returned by the API. |
| `type` | `string` | Users resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_user` | `SELECT` | `user_id, dd_site` | Get a user in the organization specified by the user’s `user_id`. |
| `list_users` | `SELECT` | `dd_site` | Get the list of all users in the organization. This list includes<br />all users even if they are deactivated or unverified. |
| `create_user` | `INSERT` | `data__data, dd_site` | Create a user for your organization. |
| `_get_user` | `EXEC` | `user_id, dd_site` | Get a user in the organization specified by the user’s `user_id`. |
| `_list_users` | `EXEC` | `dd_site` | Get the list of all users in the organization. This list includes<br />all users even if they are deactivated or unverified. |
| `disable_user` | `EXEC` | `user_id, dd_site` | Disable a user. Can only be used with an application key belonging<br />to an administrator user. |
| `update_user` | `EXEC` | `user_id, data__data, dd_site` | Edit a user. Can only be used with an application key belonging<br />to an administrator user. |
