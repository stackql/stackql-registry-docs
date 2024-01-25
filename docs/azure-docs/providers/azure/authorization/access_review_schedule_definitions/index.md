---
title: access_review_schedule_definitions
hide_title: false
hide_table_of_contents: false
keywords:
  - access_review_schedule_definitions
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
<tr><td><b>Name</b></td><td><code>access_review_schedule_definitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.authorization.access_review_schedule_definitions</code></td></tr>
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
| `list` | `SELECT` | `subscriptionId` | Get access review schedule definitions |
| `delete_by_id` | `DELETE` | `scheduleDefinitionId, subscriptionId` | Delete access review schedule definition |
| `_list` | `EXEC` | `subscriptionId` | Get access review schedule definitions |
| `create_or_update_by_id` | `EXEC` | `scheduleDefinitionId, subscriptionId` | Create or Update access review schedule definition. |
| `get_by_id` | `EXEC` | `scheduleDefinitionId, subscriptionId` | Get single access review definition |
| `stop` | `EXEC` | `scheduleDefinitionId, subscriptionId` | Stop access review definition |
