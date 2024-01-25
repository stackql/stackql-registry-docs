---
title: role_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - role_definitions
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
<tr><td><b>Name</b></td><td><code>role_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.role_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The role definition ID. |
| `name` | `string` | The role definition name. |
| `properties` | `object` | Role definition properties. |
| `type` | `string` | The role definition type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `roleDefinitionId, scope` | Get role definition by ID (GUID). |
| `list` | `SELECT` | `scope` | Get all role definitions that are applicable at scope and above. |
| `create_or_update` | `INSERT` | `roleDefinitionId, scope` | Creates or updates a role definition. |
| `delete` | `DELETE` | `roleDefinitionId, scope` | Deletes a role definition. |
| `_list` | `EXEC` | `scope` | Get all role definitions that are applicable at scope and above. |
