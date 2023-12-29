---
title: role_users
hide_title: false
hide_table_of_contents: false
keywords:
  - role_users
  - roles
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
<tr><td><b>Name</b></td><td><code>role_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.roles.role_users</code></td></tr>
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
| `list_role_users` | `SELECT` | `role_id, dd_site` | Gets all users of a role. |
| `remove_user_from_role` | `DELETE` | `role_id, data__data, dd_site` | Removes a user from a role. |
| `_list_role_users` | `EXEC` | `role_id, dd_site` | Gets all users of a role. |
| `add_user_to_role` | `EXEC` | `role_id, data__data, dd_site` | Adds a user to a role. |
