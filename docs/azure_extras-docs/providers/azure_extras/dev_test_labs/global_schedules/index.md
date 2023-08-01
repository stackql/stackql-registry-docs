---
title: global_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - global_schedules
  - dev_test_labs
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>global_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.dev_test_labs.global_schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `type` | `string` | The type of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a schedule. |
| `tags` | `object` | The tags of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GlobalSchedules_Get` | `SELECT` | `api-version, name, resourceGroupName, subscriptionId` | Get schedule. |
| `GlobalSchedules_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List schedules in a resource group. |
| `GlobalSchedules_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | List schedules in a subscription. |
| `GlobalSchedules_CreateOrUpdate` | `INSERT` | `api-version, name, resourceGroupName, subscriptionId, data__properties` | Create or replace an existing schedule. |
| `GlobalSchedules_Delete` | `DELETE` | `api-version, name, resourceGroupName, subscriptionId` | Delete schedule. |
| `GlobalSchedules_Execute` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Execute a schedule. This operation can take a while to complete. |
| `GlobalSchedules_Retarget` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Updates a schedule's target resource Id. This operation can take a while to complete. |
| `GlobalSchedules_Update` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Allows modifying tags of schedules. All other properties will be ignored. |
