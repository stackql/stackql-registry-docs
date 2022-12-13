---
title: keys
hide_title: false
hide_table_of_contents: false
keywords:
  - keys
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
<tr><td><b>Name</b></td><td><code>keys</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.key_vault.keys</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the key vault resource. |
| `name` | `string` | Name of the key vault resource. |
| `properties` | `object` | The properties of the key. |
| `tags` | `object` | Tags assigned to the key vault resource. |
| `type` | `string` | Resource type of the key vault resource. |
| `location` | `string` | Azure location of the key vault resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Keys_Get` | `SELECT` | `keyName, resourceGroupName, subscriptionId, vaultName` | Gets the current version of the specified key from the specified key vault. |
| `Keys_List` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | Lists the keys in the specified key vault. |
| `Keys_CreateIfNotExist` | `EXEC` | `keyName, resourceGroupName, subscriptionId, vaultName, data__properties` | Creates the first version of a new key if it does not exist. If it already exists, then the existing key is returned without any write operations being performed. This API does not create subsequent versions, and does not update existing keys. |
| `Keys_GetVersion` | `EXEC` | `keyName, keyVersion, resourceGroupName, subscriptionId, vaultName` | Gets the specified version of the specified key in the specified key vault. |
| `Keys_ListVersions` | `EXEC` | `keyName, resourceGroupName, subscriptionId, vaultName` | Lists the versions of the specified key in the specified key vault. |
