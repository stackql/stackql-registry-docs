---
title: backup_vaults
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_vaults
  - data_protection
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
<tr><td><b>Name</b></td><td><code>backup_vaults</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_protection.backup_vaults</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Identity details |
| `properties` | `object` | Backup Vault |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | Returns a resource belonging to a resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, vaultName, data__properties` | Creates or updates a BackupVault resource belonging to a resource group. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, vaultName` | Deletes a BackupVault resource from the resource group. |
| `_get_in_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns resource collection belonging to a resource group. |
| `_get_in_subscription` | `EXEC` | `subscriptionId` | Returns resource collection belonging to a subscription. |
| `check_name_availability` | `EXEC` | `location, resourceGroupName, subscriptionId` |  |
| `get_in_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Returns resource collection belonging to a resource group. |
| `get_in_subscription` | `EXEC` | `subscriptionId` | Returns resource collection belonging to a subscription. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, vaultName` | Updates a BackupVault resource belonging to a resource group. For example, updating tags for a resource. |
