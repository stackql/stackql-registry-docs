---
title: vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - vaults
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
<tr><td><b>Name</b></td><td><code>vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.key_vault.vaults</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified identifier of the key vault resource. |
| `name` | `string` | Name of the key vault resource. |
| `location` | `string` | Azure location of the key vault resource. |
| `properties` | `object` | Properties of the vault |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the key vault resource. |
| `tags` | `object` | Tags assigned to the key vault resource. |
| `type` | `string` | Resource type of the key vault resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | Gets the specified Azure key vault. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | The List operation gets information about the vaults associated with the subscription and within the specified resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | The List operation gets information about the vaults associated with the subscription. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, vaultName, data__location, data__properties` | Create or update a key vault in the specified subscription. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, vaultName` | Deletes the specified Azure key vault. |
| `_exec_list` | `EXEC` | `$filter, api-version, subscriptionId` | The List operation gets information about the vaults associated with the subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | The List operation gets information about the vaults associated with the subscription and within the specified resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | The List operation gets information about the vaults associated with the subscription. |
| `check_name_availability` | `EXEC` | `subscriptionId, data__name, data__type` | Checks that the vault name is valid and is not already in use. |
| `exec_list` | `EXEC` | `$filter, api-version, subscriptionId` | The List operation gets information about the vaults associated with the subscription. |
| `purge_deleted` | `EXEC` | `location, subscriptionId, vaultName` | Permanently deletes the specified vault. aka Purges the deleted Azure key vault. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, vaultName` | Update a key vault in the specified subscription. |
