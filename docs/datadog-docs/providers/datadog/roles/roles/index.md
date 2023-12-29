---
title: roles
hide_title: false
hide_table_of_contents: false
keywords:
  - roles
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
<tr><td><b>Name</b></td><td><code>roles</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.roles.roles</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The unique identifier of the role. |
| `attributes` | `object` | Attributes of the role. |
| `relationships` | `object` | Relationships of the role object returned by the API. |
| `type` | `string` | Roles type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_role` | `SELECT` | `role_id, dd_site` | Get a role in the organization specified by the role’s `role_id`. |
| `list_roles` | `SELECT` | `dd_site` | Returns all roles, including their names and their unique identifiers. |
| `create_role` | `INSERT` | `data__data, dd_site` | Create a new role for your organization. |
| `delete_role` | `DELETE` | `role_id, dd_site` | Disables a role. |
| `_get_role` | `EXEC` | `role_id, dd_site` | Get a role in the organization specified by the role’s `role_id`. |
| `_list_roles` | `EXEC` | `dd_site` | Returns all roles, including their names and their unique identifiers. |
| `clone_role` | `EXEC` | `role_id, data__data, dd_site` | Clone an existing role |
| `update_role` | `EXEC` | `role_id, data__data, dd_site` | Edit a role. Can only be used with application keys belonging to administrators. |
