---
title: accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - accounts
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
<tr><td><b>Name</b></td><td><code>accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.accounts</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Gets the Kind. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the storage account. |
| `sku` | `object` | The SKU of the storage account. |
| `tags` | `object` | Resource tags. |
| `extendedLocation` | `object` | The complex type of the extended location. |
| `identity` | `object` | Identity for the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `StorageAccounts_List` | `SELECT` | `subscriptionId` | Lists all the storage accounts available under the subscription. Note that storage keys are not returned; use the ListKeys operation for this. |
| `StorageAccounts_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the storage accounts available under the given resource group. Note that storage keys are not returned; use the ListKeys operation for this. |
| `StorageAccounts_Create` | `INSERT` | `accountName, resourceGroupName, subscriptionId, data__kind, data__location, data__sku` | Asynchronously creates a new storage account with the specified parameters. If an account is already created and a subsequent create request is issued with different properties, the account properties will be updated. If an account is already created and a subsequent create or update request is issued with the exact same set of properties, the request will succeed. |
| `StorageAccounts_Delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId` | Deletes a storage account in Microsoft Azure. |
| `StorageAccounts_AbortHierarchicalNamespaceMigration` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Abort live Migration of storage account to enable Hns |
| `StorageAccounts_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks that the storage account name is valid and is not already in use. |
| `StorageAccounts_Failover` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Failover request can be triggered for a storage account in case of availability issues. The failover occurs from the storage account's primary cluster to secondary cluster for RA-GRS accounts. The secondary cluster will become primary after failover. |
| `StorageAccounts_GetProperties` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Returns the properties for the specified storage account including but not limited to name, SKU name, location, and account status. The ListKeys operation should be used to retrieve storage keys. |
| `StorageAccounts_HierarchicalNamespaceMigration` | `EXEC` | `accountName, requestType, resourceGroupName, subscriptionId` | Live Migration of storage account to enable Hns |
| `StorageAccounts_ListAccountSAS` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__signedExpiry, data__signedPermission, data__signedResourceTypes, data__signedServices` | List SAS credentials of a storage account. |
| `StorageAccounts_ListKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Lists the access keys or Kerberos keys (if active directory enabled) for the specified storage account. |
| `StorageAccounts_ListServiceSAS` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__canonicalizedResource` | List service SAS credentials of a specific resource. |
| `StorageAccounts_RegenerateKey` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__keyName` | Regenerates one of the access keys or Kerberos keys for the specified storage account. |
| `StorageAccounts_RestoreBlobRanges` | `EXEC` | `accountName, resourceGroupName, subscriptionId, data__blobRanges, data__timeToRestore` | Restore blobs in the specified blob ranges |
| `StorageAccounts_RevokeUserDelegationKeys` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | Revoke user delegation keys. |
| `StorageAccounts_Update` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | The update operation can be used to update the SKU, encryption, access tier, or tags for a storage account. It can also be used to map the account to a custom domain. Only one custom domain is supported per storage account; the replacement/change of custom domain is not supported. In order to replace an old custom domain, the old value must be cleared/unregistered before a new value can be set. The update of multiple properties is supported. This call does not change the storage keys for the account. If you want to change the storage account keys, use the regenerate keys operation. The location and name of the storage account cannot be changed after creation. |
