---
title: redis
hide_title: false
hide_table_of_contents: false
keywords:
  - redis
  - redis
  - azure_isv    
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
<tr><td><b>Id</b></td><td><code>azure_isv.redis.redis</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the redis cache. |
| `tags` | `object` | Resource tags. |
| `zones` | `array` | A list of availability zones denoting where the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `name, resourceGroupName, subscriptionId` | Gets a Redis cache (resource description). |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Redis caches in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets all Redis caches in the specified subscription. |
| `create` | `INSERT` | `name, resourceGroupName, subscriptionId, data__location, data__properties` | Create or replace (overwrite/recreate, with potential downtime) an existing Redis cache. |
| `delete` | `DELETE` | `name, resourceGroupName, subscriptionId` | Deletes a Redis cache. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all Redis caches in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets all Redis caches in the specified subscription. |
| `check_name_availability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks that the redis cache name is valid and is not already in use. |
| `export_data` | `EXEC` | `name, resourceGroupName, subscriptionId, data__container, data__prefix` | Export data from the redis cache to blobs in a container. |
| `flush_cache` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Deletes all of the keys in a cache. |
| `force_reboot` | `EXEC` | `name, resourceGroupName, subscriptionId` | Reboot specified Redis node(s). This operation requires write permission to the cache resource. There can be potential data loss. |
| `import_data` | `EXEC` | `name, resourceGroupName, subscriptionId, data__files` | Import data into Redis cache. |
| `regenerate_key` | `EXEC` | `name, resourceGroupName, subscriptionId, data__keyType` | Regenerate Redis cache's access keys. This operation requires write permission to the cache resource. |
| `update` | `EXEC` | `name, resourceGroupName, subscriptionId` | Update an existing Redis cache. |
