---
title: caches
hide_title: false
hide_table_of_contents: false
keywords:
  - caches
  - storage_cache
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
<tr><td><b>Name</b></td><td><code>caches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage_cache.caches</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | A fully qualified URL. |
| `name` | `string` | Schema for the name of resources served by this provider. Note that objects will contain an odata @id annotation as appropriate. This will contain the complete resource id of the object. These names are case-preserving, but not case sensitive. |
| `identity` | `object` | Cache identity properties. |
| `location` | `string` | Region name string. |
| `properties` | `object` | Properties of the cache. |
| `sku` | `object` | SKU for the cache. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Type of the cache; Microsoft.StorageCache/Cache |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `cacheName, resourceGroupName, subscriptionId` | Returns a cache. |
| `list` | `SELECT` | `subscriptionId` | Returns all caches the user has access to under a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Returns all caches the user has access to under a resource group. |
| `create_or_update` | `INSERT` | `cacheName, resourceGroupName, subscriptionId` | Create or update a cache. |
| `delete` | `DELETE` | `cacheName, resourceGroupName, subscriptionId` | Schedules a cache for deletion. |
| `_list` | `EXEC` | `subscriptionId` | Returns all caches the user has access to under a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns all caches the user has access to under a resource group. |
| `debug_info` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Tells a cache to write generate debug info for support to process. |
| `flush` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Tells a cache to write all dirty data to the Storage Target(s). During the flush, clients will see errors returned until the flush is complete. |
| `pause_priming_job` | `EXEC` | `cacheName, resourceGroupName, subscriptionId, data__primingJobId` | Schedule a priming job to be paused. |
| `resume_priming_job` | `EXEC` | `cacheName, resourceGroupName, subscriptionId, data__primingJobId` | Resumes a paused priming job. |
| `space_allocation` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Update cache space allocation. |
| `start` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Tells a Stopped state cache to transition to Active state. |
| `start_priming_job` | `EXEC` | `cacheName, resourceGroupName, subscriptionId, data__primingJobName, data__primingManifestUrl` | Create a priming job. This operation is only allowed when the cache is healthy. |
| `stop` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Tells an Active cache to transition to Stopped state. |
| `stop_priming_job` | `EXEC` | `cacheName, resourceGroupName, subscriptionId, data__primingJobId` | Schedule a priming job for deletion. |
| `update` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Update a cache instance. |
| `upgrade_firmware` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Upgrade a cache's firmware if a new version is available. Otherwise, this operation has no effect. |
