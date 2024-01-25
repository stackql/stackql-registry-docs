---
title: local_users
hide_title: false
hide_table_of_contents: false
keywords:
  - local_users
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
<tr><td><b>Name</b></td><td><code>local_users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.storage.local_users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | The Storage Account Local User properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `accountName, resourceGroupName, subscriptionId, username` | Get the local user of the storage account by username. |
| `list` | `SELECT` | `accountName, resourceGroupName, subscriptionId` | List the local users associated with the storage account. |
| `create_or_update` | `INSERT` | `accountName, resourceGroupName, subscriptionId, username` | Create or update the properties of a local user associated with the storage account |
| `delete` | `DELETE` | `accountName, resourceGroupName, subscriptionId, username` | Deletes the local user associated with the specified storage account. |
| `_list` | `EXEC` | `accountName, resourceGroupName, subscriptionId` | List the local users associated with the storage account. |
| `regenerate_password` | `EXEC` | `accountName, resourceGroupName, subscriptionId, username` | Regenerate the local user SSH password. |
