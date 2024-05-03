---
title: storage_targets
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_targets
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
<tr><td><b>Name</b></td><td><code>storage_targets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.storage_targets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Resource ID of the Storage Target. |
| <CopyableCode code="name" /> | `string` | Schema for the name of resources served by this provider. Note that objects will contain an odata @id annotation as appropriate. This will contain the complete resource id of the object. These names are case-preserving, but not case sensitive. |
| <CopyableCode code="location" /> | `string` | Region name string. |
| <CopyableCode code="properties" /> | `object` | Properties of the Storage Target. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Type of the Storage Target; Microsoft.StorageCache/Cache/StorageTarget |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Returns a Storage Target from a cache. |
| <CopyableCode code="list_by_cache" /> | `SELECT` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Returns a list of Storage Targets for the specified cache. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Create or update a Storage Target. This operation is allowed at any time, but if the cache is down or unhealthy, the actual creation/modification of the Storage Target may be delayed until the cache is healthy again. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Removes a Storage Target from a cache. This operation is allowed at any time, but if the cache is down or unhealthy, the actual removal of the Storage Target may be delayed until the cache is healthy again. Note that if the cache has data to flush to the Storage Target, the data will be flushed before the Storage Target will be deleted. |
| <CopyableCode code="_list_by_cache" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Returns a list of Storage Targets for the specified cache. |
| <CopyableCode code="dns_refresh" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Tells a storage target to refresh its DNS information. |
| <CopyableCode code="restore_defaults" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Tells a storage target to restore its settings to their default values. |
