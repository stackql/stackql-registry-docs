---
title: redis
hide_title: false
hide_table_of_contents: false
keywords:
  - redis
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
<tr><td><b>Name</b></td><td><code>redis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.redis.redis</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `zones` | `array` | A list of availability zones denoting where the resource needs to come from. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the redis cache. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Redis_Get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Gets a Redis cache (resource description). |
| `Redis_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Redis caches in a resource group. |
| `Redis_ListBySubscription` | `SELECT` | `subscriptionId` | Gets all Redis caches in the specified subscription. |
| `Redis_Create` | `INSERT` | `name, resourceGroupName, subscriptionId, data__location, data__properties` | Create or replace (overwrite/recreate, with potential downtime) an existing Redis cache. |
| `Redis_Delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Deletes a Redis cache. |
| `Redis_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks that the redis cache name is valid and is not already in use. |
| `Redis_ExportData` | `EXEC` | `name, resourceGroupName, subscriptionId, data__container, data__prefix` | Export data from the redis cache to blobs in a container. |
| `Redis_ForceReboot` | `EXEC` | `name, resourceGroupName, subscriptionId` | Reboot specified Redis node(s). This operation requires write permission to the cache resource. There can be potential data loss. |
| `Redis_ImportData` | `EXEC` | `name, resourceGroupName, subscriptionId, data__files` | Import data into Redis cache. |
| `Redis_ListKeys` | `EXEC` | `name, resourceGroupName, subscriptionId` | Retrieve a Redis cache's access keys. This operation requires write permission to the cache resource. |
| `Redis_ListUpgradeNotifications` | `EXEC` | `history, name, resourceGroupName, subscriptionId` | Gets any upgrade notifications for a Redis cache. |
| `Redis_RegenerateKey` | `EXEC` | `name, resourceGroupName, subscriptionId, data__keyType` | Regenerate Redis cache's access keys. This operation requires write permission to the cache resource. |
| `Redis_Update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Update an existing Redis cache. |
