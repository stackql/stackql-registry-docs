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
| `ScopeAccessReviewScheduleDefinitions_List` | `SELECT` | `scope` | Get access review schedule definitions |
| `ScopeAccessReviewScheduleDefinitions_DeleteById` | `DELETE` | `scheduleDefinitionId, scope` | Delete access review schedule definition |
| `ScopeAccessReviewScheduleDefinitions_CreateOrUpdateById` | `EXEC` | `scheduleDefinitionId, scope` | Create or Update access review schedule definition. |
| `ScopeAccessReviewScheduleDefinitions_GetById` | `EXEC` | `scheduleDefinitionId, scope` | Get single access review definition |
| `ScopeAccessReviewScheduleDefinitions_Stop` | `EXEC` | `scheduleDefinitionId, scope` | Stop access review definition |
