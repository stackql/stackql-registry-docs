---
title: scope_access_review_schedule_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - scope_access_review_schedule_definitions
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
<tr><td><b>Name</b></td><td><code>scope_access_review_schedule_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.scope_access_review_schedule_definitions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The access review schedule definition id. |
| `name` | `string` | The access review schedule definition unique id. |
| `properties` | `object` | Access Review. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list` | `SELECT` | `scope` | Get access review schedule definitions |
| `delete_by_id` | `DELETE` | `scheduleDefinitionId, scope` | Delete access review schedule definition |
| `_list` | `EXEC` | `scope` | Get access review schedule definitions |
| `create_or_update_by_id` | `EXEC` | `scheduleDefinitionId, scope` | Create or Update access review schedule definition. |
| `get_by_id` | `EXEC` | `scheduleDefinitionId, scope` | Get single access review definition |
| `stop` | `EXEC` | `scheduleDefinitionId, scope` | Stop access review definition |
