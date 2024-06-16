---
title: storage_target
hide_title: false
hide_table_of_contents: false
keywords:
  - storage_target
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
<tr><td><b>Name</b></td><td><code>storage_target</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage_cache.storage_target" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="flush" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Tells the cache to write all dirty data to the Storage Target's backend storage. Client requests to this storage target's namespace will return errors until the flush operation completes. |
| <CopyableCode code="invalidate" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Invalidate all cached data for a storage target. Cached files are discarded and fetched from the back end on the next request. |
| <CopyableCode code="resume" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Resumes client access to a previously suspended storage target. |
| <CopyableCode code="suspend" /> | `EXEC` | <CopyableCode code="cacheName, resourceGroupName, storageTargetName, subscriptionId" /> | Suspends client access to a storage target. |
