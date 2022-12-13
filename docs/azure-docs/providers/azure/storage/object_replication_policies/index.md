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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>object_replication_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.object_replication_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | The Storage Account ObjectReplicationPolicy properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ObjectReplicationPolicies_Get` | `SELECT` | `accountName, objectReplicationPolicyId, resourceGroupName, subscriptionId` | Get the object replication policy of the storage account by policy ID. |
| `ObjectReplicationPolicies_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List the object replication policies associated with the storage account. |
| `ObjectReplicationPolicies_CreateOrUpdate` | `INSERT` | `accountName, objectReplicationPolicyId, resourceGroupName, subscriptionId` | Create or update the object replication policy of the storage account. |
| `ObjectReplicationPolicies_Delete` | `DELETE` | `accountName, objectReplicationPolicyId, resourceGroupName, subscriptionId` | Deletes the object replication policy associated with the specified storage account. |
