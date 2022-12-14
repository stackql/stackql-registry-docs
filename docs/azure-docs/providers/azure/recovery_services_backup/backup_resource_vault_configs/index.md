---
title: backup_resource_vault_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_resource_vault_configs
  - recovery_services_backup
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
<tr><td><b>Name</b></td><td><code>backup_resource_vault_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.recovery_services_backup.backup_resource_vault_configs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id represents the complete path to the resource. |
| `name` | `string` | Resource name associated with the resource. |
| `properties` | `object` | Backup resource vault config details. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
| `eTag` | `string` | Optional ETag. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BackupResourceVaultConfigs_Get` | `SELECT` | `api-version, resourceGroupName, subscriptionId, vaultName` | Fetches resource vault config. |
| `BackupResourceVaultConfigs_Put` | `EXEC` | `api-version, resourceGroupName, subscriptionId, vaultName` | Updates vault security config.  |
| `BackupResourceVaultConfigs_Update` | `EXEC` | `api-version, resourceGroupName, subscriptionId, vaultName` | Updates vault security config. |
