---
title: blob_containers
hide_title: false
hide_table_of_contents: false
keywords:
  - blob_containers
  - storage
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
<tr><td><b>Name</b></td><td><code>blob_containers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.blob_containers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="etag" /> | `string` | Resource Etag. |
| <CopyableCode code="properties" /> | `object` | The properties of a container. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId" /> | Gets properties of a specified container.  |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all containers and does not support a prefix like data plane. Also SRP today does not return continuation token. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId" /> | Creates a new container under the specified account as described by request body. The container resource includes metadata and properties for that container. It does not include a list of the blobs contained by the container.  |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId" /> | Deletes specified container under its account. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists all containers and does not support a prefix like data plane. Also SRP today does not return continuation token. |
| <CopyableCode code="clear_legal_hold" /> | `EXEC` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId, data__tags" /> | Clears legal hold tags. Clearing the same or non-existent tag results in an idempotent operation. ClearLegalHold clears out only the specified tags in the request. |
| <CopyableCode code="extend_immutability_policy" /> | `EXEC` | <CopyableCode code="If-Match, accountName, containerName, resourceGroupName, subscriptionId, data__properties" /> | Extends the immutabilityPeriodSinceCreationInDays of a locked immutabilityPolicy. The only action allowed on a Locked policy will be this action. ETag in If-Match is required for this operation. |
| <CopyableCode code="lease" /> | `EXEC` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId, data__action" /> | The Lease Container operation establishes and manages a lock on a container for delete operations. The lock duration can be 15 to 60 seconds, or can be infinite. |
| <CopyableCode code="lock_immutability_policy" /> | `EXEC` | <CopyableCode code="If-Match, accountName, containerName, resourceGroupName, subscriptionId" /> | Sets the ImmutabilityPolicy to Locked state. The only action allowed on a Locked policy is ExtendImmutabilityPolicy action. ETag in If-Match is required for this operation. |
| <CopyableCode code="object_level_worm" /> | `EXEC` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId" /> | This operation migrates a blob container from container level WORM to object level immutability enabled container. Prerequisites require a container level immutability policy either in locked or unlocked state, Account level versioning must be enabled and there should be no Legal hold on the container. |
| <CopyableCode code="set_legal_hold" /> | `EXEC` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId, data__tags" /> | Sets legal hold tags. Setting the same tag results in an idempotent operation. SetLegalHold follows an append pattern and does not clear out the existing tags that are not specified in the request. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="accountName, containerName, resourceGroupName, subscriptionId" /> | Updates container properties as specified in request body. Properties not mentioned in the request will be unchanged. Update fails if the specified container doesn't already exist.  |
