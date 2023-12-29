---
title: role_permissions
hide_title: false
hide_table_of_contents: false
keywords:
  - role_permissions
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
<tr><td><b>Name</b></td><td><code>role_permissions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.roles.role_permissions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the permission. |
| `attributes` | `object` | Attributes of a permission. |
| `type` | `string` | Permissions resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_role_permissions` | `SELECT` | `role_id, dd_site` | Returns a list of all permissions for a single role. |
| `remove_permission_from_role` | `DELETE` | `role_id, dd_site` | Removes a permission from a role. |
| `_list_role_permissions` | `EXEC` | `role_id, dd_site` | Returns a list of all permissions for a single role. |
| `add_permission_to_role` | `EXEC` | `role_id, dd_site` | Adds a permission to a role. |
