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
| `AccessReviewScheduleDefinitions_List` | `SELECT` | `subscriptionId` | Get access review schedule definitions |
| `AccessReviewScheduleDefinitions_DeleteById` | `DELETE` | `scheduleDefinitionId, subscriptionId` | Delete access review schedule definition |
| `AccessReviewScheduleDefinitions_CreateOrUpdateById` | `EXEC` | `scheduleDefinitionId, subscriptionId` | Create or Update access review schedule definition. |
| `AccessReviewScheduleDefinitions_GetById` | `EXEC` | `scheduleDefinitionId, subscriptionId` | Get single access review definition |
| `AccessReviewScheduleDefinitions_Stop` | `EXEC` | `scheduleDefinitionId, subscriptionId` | Stop access review definition |
