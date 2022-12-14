---
title: blob_inventory_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - blob_inventory_policies
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
<tr><td><b>Name</b></td><td><code>blob_inventory_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.blob_inventory_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | The storage account blob inventory policy properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BlobInventoryPolicies_Get` | `SELECT` | `accountName, blobInventoryPolicyName, resourceGroupName, subscriptionId` | Gets the blob inventory policy associated with the specified storage account. |
| `BlobInventoryPolicies_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Gets the blob inventory policy associated with the specified storage account. |
| `BlobInventoryPolicies_CreateOrUpdate` | `INSERT` | `accountName, blobInventoryPolicyName, resourceGroupName, subscriptionId` | Sets the blob inventory policy to the specified storage account. |
| `BlobInventoryPolicies_Delete` | `DELETE` | `accountName, blobInventoryPolicyName, resourceGroupName, subscriptionId` | Deletes the blob inventory policy associated with the specified storage account. |
