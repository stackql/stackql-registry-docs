---
title: patch_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - patch_schedules
  - redis
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
<tr><td><b>Name</b></td><td><code>patch_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.redis.patch_schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | List of patch schedules for a Redis cache. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PatchSchedules_Get` | `SELECT` | `default, name, resourceGroupName, subscriptionId` | Gets the patching schedule of a redis cache. |
| `PatchSchedules_ListByRedisResource` | `SELECT` | `cacheName, resourceGroupName, subscriptionId` | Gets all patch schedules in the specified redis cache (there is only one). |
| `PatchSchedules_CreateOrUpdate` | `INSERT` | `default, name, resourceGroupName, subscriptionId, data__properties` | Create or replace the patching schedule for Redis cache. |
| `PatchSchedules_Delete` | `DELETE` | `default, name, resourceGroupName, subscriptionId` | Deletes the patching schedule of a redis cache. |
