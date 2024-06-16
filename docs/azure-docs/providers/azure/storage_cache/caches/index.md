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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>caches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.caches" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | A fully qualified URL. |
| <CopyableCode code="name" /> | `string` | Schema for the name of resources served by this provider. Note that objects will contain an odata @id annotation as appropriate. This will contain the complete resource id of the object. These names are case-preserving, but not case sensitive. |
| <CopyableCode code="identity" /> | `object` | Cache identity properties. |
| <CopyableCode code="location" /> | `string` | Region name string. |
| <CopyableCode code="properties" /> | `object` | Properties of the cache. |
| <CopyableCode code="sku" /> | `object` | SKU for the cache. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="type" /> | `string` | Type of the cache; Microsoft.StorageCache/Cache |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Returns a cache. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Returns all caches the user has access to under a subscription. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Returns all caches the user has access to under a resource group. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Create or update a cache. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Schedules a cache for deletion. |
| <CopyableCode code="debug_info" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Tells a cache to write generate debug info for support to process. |
| <CopyableCode code="flush" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Tells a cache to write all dirty data to the Storage Target(s). During the flush, clients will see errors returned until the flush is complete. |
| <CopyableCode code="pause_priming_job" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId, data__primingJobId" /> | Schedule a priming job to be paused. |
| <CopyableCode code="resume_priming_job" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId, data__primingJobId" /> | Resumes a paused priming job. |
| <CopyableCode code="space_allocation" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Update cache space allocation. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Tells a Stopped state cache to transition to Active state. |
| <CopyableCode code="start_priming_job" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId, data__primingJobName, data__primingManifestUrl" /> | Create a priming job. This operation is only allowed when the cache is healthy. |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Tells an Active cache to transition to Stopped state. |
| <CopyableCode code="stop_priming_job" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId, data__primingJobId" /> | Schedule a priming job for deletion. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Update a cache instance. |
| <CopyableCode code="upgrade_firmware" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Upgrade a cache's firmware if a new version is available. Otherwise, this operation has no effect. |
