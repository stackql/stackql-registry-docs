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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>backup_instances</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.data_protection.backup_instances" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Proxy Resource Id represents the complete path to the resource. |
| <CopyableCode code="name" /> | `string` | Proxy Resource name associated with the resource. |
| <CopyableCode code="properties" /> | `object` | Backup Instance |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | Proxy Resource tags. |
| <CopyableCode code="type" /> | `string` | Proxy Resource type represents the complete path of the form Namespace/ResourceType/ResourceType/... |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | Gets a backup instance with name in a backup vault |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName" /> | Gets a backup instances belonging to a backup vault |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | Create or update a backup instance in a backup vault |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | Delete a backup instance in a backup vault |
| <CopyableCode code="adhoc_backup" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName, data__backupRuleOptions" /> | Trigger adhoc backup  |
| <CopyableCode code="resume_backups" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | This operation will resume backups for backup instance |
| <CopyableCode code="resume_protection" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | This operation will resume protection for a stopped backup instance |
| <CopyableCode code="stop_protection" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | This operation will stop protection of a backup instance and data will be held forever |
| <CopyableCode code="suspend_backups" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | This operation will stop backup for a backup instance and retains the backup data as per the policy (except latest Recovery point, which will be retained forever) |
| <CopyableCode code="sync_backup_instance" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName" /> | Sync backup instance again in case of failure<br />This action will retry last failed operation and will bring backup instance to valid state |
| <CopyableCode code="trigger_cross_region_restore" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId, data__crossRegionRestoreDetails, data__restoreRequestObject" /> | Triggers Cross Region Restore for BackupInstance. |
| <CopyableCode code="trigger_rehydrate" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName, data__recoveryPointId, data__rehydrationRetentionDuration" /> | rehydrate recovery point for restore for a BackupInstance |
| <CopyableCode code="trigger_restore" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName, data__objectType, data__restoreTargetInfo, data__sourceDataStoreType" /> | Triggers restore for a BackupInstance |
| <CopyableCode code="validate_cross_region_restore" /> | `EXEC` | <CopyableCode code="location, resourceGroupName, subscriptionId, data__crossRegionRestoreDetails, data__restoreRequestObject" /> | Validates whether Cross Region Restore can be triggered for DataSource. |
| <CopyableCode code="validate_for_backup" /> | `EXEC` | <CopyableCode code="resourceGroupName, subscriptionId, vaultName, data__backupInstance" /> | Validate whether adhoc backup will be successful or not |
| <CopyableCode code="validate_for_restore" /> | `EXEC` | <CopyableCode code="backupInstanceName, resourceGroupName, subscriptionId, vaultName, data__restoreRequestObject" /> | Validates if Restore can be triggered for a DataSource |
