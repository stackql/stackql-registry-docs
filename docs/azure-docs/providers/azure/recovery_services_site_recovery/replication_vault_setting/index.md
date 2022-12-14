---
title: replication_vault_setting
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_vault_setting
  - recovery_services_site_recovery
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
<tr><td><b>Name</b></td><td><code>replication_vault_setting</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_site_recovery.replication_vault_setting</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `properties` | `object` | Vault setting properties. |
| `type` | `string` | Resource Type |
| `location` | `string` | Resource Location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ReplicationVaultSetting_Get` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId, vaultSettingName` | Gets the vault setting. This includes the Migration Hub connection settings. |
| `ReplicationVaultSetting_List` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Gets the list of vault setting. This includes the Migration Hub connection settings. |
| `ReplicationVaultSetting_Create` | `INSERT` | `api-version, resourceGroupName, resourceName, subscriptionId, vaultSettingName, data__properties` | The operation to configure vault setting. |
