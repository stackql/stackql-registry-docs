---
title: role_assignments
hide_title: false
hide_table_of_contents: false
keywords:
  - role_assignments
  - authorization
  - azure    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Azure resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>role_assignments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.role_assignments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The role assignment ID. |
| `name` | `string` | The role assignment name. |
| `properties` | `object` | Role assignment properties. |
| `type` | `string` | The role assignment type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `roleAssignmentName, scope` | Get a role assignment by scope and name. |
| `create` | `INSERT` | `roleAssignmentName, scope, data__properties` | Create or update a role assignment by scope and name. |
| `delete` | `DELETE` | `roleAssignmentName, scope` | Delete a role assignment by scope and name. |
| `delete_by_id` | `DELETE` | `roleAssignmentId` | Delete a role assignment by ID. |
| `create_by_id` | `EXEC` | `roleAssignmentId, data__properties` | Create or update a role assignment by ID. |
| `get_by_id` | `EXEC` | `roleAssignmentId` | Get a role assignment by ID. |
