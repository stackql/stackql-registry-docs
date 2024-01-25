---
title: global_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - global_schedules
  - dev_test_labs
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
<tr><td><b>Name</b></td><td><code>global_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.dev_test_labs.global_schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier of the resource. |
| `name` | `string` | The name of the resource. |
| `location` | `string` | The location of the resource. |
| `properties` | `object` | Properties of a schedule. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, name, resourceGroupName, subscriptionId` | Get schedule. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | List schedules in a resource group. |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | List schedules in a subscription. |
| `create_or_update` | `INSERT` | `api-version, name, resourceGroupName, subscriptionId, data__properties` | Create or replace an existing schedule. |
| `delete` | `DELETE` | `api-version, name, resourceGroupName, subscriptionId` | Delete schedule. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | List schedules in a resource group. |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | List schedules in a subscription. |
| `execute` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Execute a schedule. This operation can take a while to complete. |
| `retarget` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Updates a schedule's target resource Id. This operation can take a while to complete. |
| `update` | `EXEC` | `api-version, name, resourceGroupName, subscriptionId` | Allows modifying tags of schedules. All other properties will be ignored. |
