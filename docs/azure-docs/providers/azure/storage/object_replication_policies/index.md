---
title: object_replication_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - object_replication_policies
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
<tr><td><b>Name</b></td><td><code>object_replication_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.storage.object_replication_policies" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| <CopyableCode code="name" /> | `string` | The name of the resource |
| <CopyableCode code="properties" /> | `object` | The Storage Account ObjectReplicationPolicy properties. |
| <CopyableCode code="type" /> | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, objectReplicationPolicyId, resourceGroupName, subscriptionId" /> | Get the object replication policy of the storage account by policy ID. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List the object replication policies associated with the storage account. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, objectReplicationPolicyId, resourceGroupName, subscriptionId" /> | Create or update the object replication policy of the storage account. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, objectReplicationPolicyId, resourceGroupName, subscriptionId" /> | Deletes the object replication policy associated with the specified storage account. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | List the object replication policies associated with the storage account. |
