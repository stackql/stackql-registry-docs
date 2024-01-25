---
title: vault
hide_title: false
hide_table_of_contents: false
keywords:
  - vault
  - data_replication
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
<tr><td><b>Name</b></td><td><code>vault</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_replication.vault</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Gets or sets the Id of the resource. |
| `name` | `string` | Gets or sets the name of the resource. |
| `location` | `string` | Gets or sets the location of the vault. |
| `properties` | `object` | Vault properties. |
| `systemData` | `object` | System data required to be defined for Azure resources. |
| `tags` | `object` | Gets or sets the resource tags. |
| `type` | `string` | Gets or sets the type of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | Gets the details of the vault. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the list of vaults in the given subscription and resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets the list of vaults in the given subscription. |
| `create` | `INSERT` | `resourceGroupName, subscriptionId, vaultName, data__location` | Creates the vault. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, vaultName` | Removes the vault. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Gets the list of vaults in the given subscription and resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets the list of vaults in the given subscription. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, vaultName` | Performs update on the vault. |
