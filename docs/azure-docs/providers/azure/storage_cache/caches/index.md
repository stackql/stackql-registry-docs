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
| `name` | `string` | Schema for the name of resources served by this provider. Note that objects will contain an odata @id annotation as appropriate. This will contain the complete URL of the object. These names are case-preserving, but not case sensitive. |
| `identity` | `object` | Cache identity properties. |
| `sku` | `object` | SKU for the Cache. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Type of the Cache; Microsoft.StorageCache/Cache |
| `location` | `string` | Region name string. |
| `tags` | `object` | Resource tags. |
| `properties` | `object` | Properties of the Cache. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Caches_Get` | `SELECT` | `cacheName, resourceGroupName, subscriptionId` | Returns a Cache. |
| `Caches_List` | `SELECT` | `subscriptionId` | Returns all Caches the user has access to under a subscription. |
| `Caches_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Returns all Caches the user has access to under a resource group. |
| `Caches_CreateOrUpdate` | `INSERT` | `cacheName, resourceGroupName, subscriptionId` | Create or update a Cache. |
| `Caches_Delete` | `DELETE` | `cacheName, resourceGroupName, subscriptionId` | Schedules a Cache for deletion. |
| `Caches_DebugInfo` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Tells a Cache to write generate debug info for support to process. |
| `Caches_Flush` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Tells a Cache to write all dirty data to the Storage Target(s). During the flush, clients will see errors returned until the flush is complete. |
| `Caches_PausePrimingJob` | `EXEC` | `cacheName, resourceGroupName, subscriptionId, data__primingJobId` | Schedule a priming job to be paused. |
| `Caches_ResumePrimingJob` | `EXEC` | `cacheName, resourceGroupName, subscriptionId, data__primingJobId` | Resumes a paused priming job. |
| `Caches_SpaceAllocation` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Update cache space allocation. |
| `Caches_Start` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Tells a Stopped state Cache to transition to Active state. |
| `Caches_StartPrimingJob` | `EXEC` | `cacheName, resourceGroupName, subscriptionId, data__primingJobName, data__primingManifestUrl` | Create a priming job. This operation is only allowed when the cache is healthy. |
| `Caches_Stop` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Tells an Active Cache to transition to Stopped state. |
| `Caches_StopPrimingJob` | `EXEC` | `cacheName, resourceGroupName, subscriptionId, data__primingJobId` | Schedule a priming job for deletion. |
| `Caches_Update` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Update a Cache instance. |
| `Caches_UpgradeFirmware` | `EXEC` | `cacheName, resourceGroupName, subscriptionId` | Upgrade a Cache's firmware if a new version is available. Otherwise, this operation has no effect. |
