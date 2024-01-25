---
title: managed_hsm_keys
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_hsm_keys
  - key_vault
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
<tr><td><b>Name</b></td><td><code>managed_hsm_keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.key_vault.managed_hsm_keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | The properties of the key. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `keyName, name, resourceGroupName, subscriptionId` | Gets the current version of the specified key from the specified managed HSM. |
| `list` | `SELECT` | `name, resourceGroupName, subscriptionId` | Lists the keys in the specified managed HSM. |
| `_list` | `EXEC` | `name, resourceGroupName, subscriptionId` | Lists the keys in the specified managed HSM. |
| `create_if_not_exist` | `EXEC` | `keyName, name, resourceGroupName, subscriptionId, data__properties` | Creates the first version of a new key if it does not exist. If it already exists, then the existing key is returned without any write operations being performed. This API does not create subsequent versions, and does not update existing keys. |
