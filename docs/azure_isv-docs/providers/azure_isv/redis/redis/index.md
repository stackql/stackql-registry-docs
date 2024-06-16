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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>redis</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure_isv.redis.redis" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="identity" /> | `object` | Managed service identity (system assigned and/or user assigned identities) |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Properties of the redis cache. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
| <CopyableCode code="zones" /> | `array` | A list of availability zones denoting where the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Gets a Redis cache (resource description). |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Lists all Redis caches in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Gets all Redis caches in the specified subscription. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__location, data__properties" /> | Create or replace (overwrite/recreate, with potential downtime) an existing Redis cache. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Deletes a Redis cache. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="subscriptionId, data__name, data__type" /> | Checks that the redis cache name is valid and is not already in use. |
| <CopyableCode code="export_data" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__container, data__prefix" /> | Export data from the redis cache to blobs in a container. |
| <CopyableCode code="flush_cache" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, subscriptionId" /> | Deletes all of the keys in a cache. |
| <CopyableCode code="force_reboot" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Reboot specified Redis node(s). This operation requires write permission to the cache resource. There can be potential data loss. |
| <CopyableCode code="import_data" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__files" /> | Import data into Redis cache. |
| <CopyableCode code="regenerate_key" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId, data__keyType" /> | Regenerate Redis cache's access keys. This operation requires write permission to the cache resource. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="name, resourceGroupName, subscriptionId" /> | Update an existing Redis cache. |
