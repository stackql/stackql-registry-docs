---
title: backup_instances
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_instances
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
<tr><td><b>Name</b></td><td><code>backup_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_protection.backup_instances</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Proxy Resource Id represents the complete path to the resource. |
| `name` | `string` | Proxy Resource name associated with the resource. |
| `properties` | `object` | Backup Instance |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Proxy Resource tags. |
| `type` | `string` | Proxy Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName` | Gets a backup instance with name in a backup vault |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, vaultName` | Gets a backup instances belonging to a backup vault |
| `create_or_update` | `INSERT` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName` | Create or update a backup instance in a backup vault |
| `delete` | `DELETE` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName` | Delete a backup instance in a backup vault |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, vaultName` | Gets a backup instances belonging to a backup vault |
| `adhoc_backup` | `EXEC` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName, data__backupRuleOptions` | Trigger adhoc backup  |
| `resume_backups` | `EXEC` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName` | This operation will resume backups for backup instance |
| `resume_protection` | `EXEC` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName` | This operation will resume protection for a stopped backup instance |
| `stop_protection` | `EXEC` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName` | This operation will stop protection of a backup instance and data will be held forever |
| `suspend_backups` | `EXEC` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName` | This operation will stop backup for a backup instance and retains the backup data as per the policy (except latest Recovery point, which will be retained forever) |
| `sync_backup_instance` | `EXEC` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName` | Sync backup instance again in case of failure<br />This action will retry last failed operation and will bring backup instance to valid state |
| `trigger_cross_region_restore` | `EXEC` | `location, resourceGroupName, subscriptionId, data__crossRegionRestoreDetails, data__restoreRequestObject` | Triggers Cross Region Restore for BackupInstance. |
| `trigger_rehydrate` | `EXEC` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName, data__recoveryPointId, data__rehydrationRetentionDuration` | rehydrate recovery point for restore for a BackupInstance |
| `trigger_restore` | `EXEC` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName, data__objectType, data__restoreTargetInfo, data__sourceDataStoreType` | Triggers restore for a BackupInstance |
| `validate_cross_region_restore` | `EXEC` | `location, resourceGroupName, subscriptionId, data__crossRegionRestoreDetails, data__restoreRequestObject` | Validates whether Cross Region Restore can be triggered for DataSource. |
| `validate_for_backup` | `EXEC` | `resourceGroupName, subscriptionId, vaultName, data__backupInstance` | Validate whether adhoc backup will be successful or not |
| `validate_for_restore` | `EXEC` | `backupInstanceName, resourceGroupName, subscriptionId, vaultName, data__restoreRequestObject` | Validates if Restore can be triggered for a DataSource |
