---
title: encryption_scopes
hide_title: false
hide_table_of_contents: false
keywords:
  - encryption_scopes
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
<tr><td><b>Name</b></td><td><code>encryption_scopes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.encryption_scopes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of the encryption scope. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `EncryptionScopes_Get` | `SELECT` | `accountName, encryptionScopeName, resourceGroupName, subscriptionId` | Returns the properties for the specified encryption scope. |
| `EncryptionScopes_List` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | Lists all the encryption scopes available under the specified storage account. |
| `EncryptionScopes_Patch` | `EXEC` | `accountName, encryptionScopeName, resourceGroupName, subscriptionId` | Update encryption scope properties as specified in the request body. Update fails if the specified encryption scope does not already exist. |
| `EncryptionScopes_Put` | `EXEC` | `accountName, encryptionScopeName, resourceGroupName, subscriptionId` | Synchronously creates or updates an encryption scope under the specified storage account. If an encryption scope is already created and a subsequent request is issued with different properties, the encryption scope properties will be updated per the specified request. |
