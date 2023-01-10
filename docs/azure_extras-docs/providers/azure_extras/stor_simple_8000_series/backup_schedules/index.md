---
title: backup_schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_schedules
  - stor_simple_8000_series
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>backup_schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.stor_simple_8000_series.backup_schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `type` | `string` | The hierarchical type of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
| `properties` | `object` | The properties of the backup schedule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `BackupSchedules_Get` | `SELECT` | `backupPolicyName, backupScheduleName, deviceName, managerName, resourceGroupName, subscriptionId` | Gets the properties of the specified backup schedule name. |
| `BackupSchedules_ListByBackupPolicy` | `SELECT` | `backupPolicyName, deviceName, managerName, resourceGroupName, subscriptionId` | Gets all the backup schedules in a backup policy. |
| `BackupSchedules_CreateOrUpdate` | `INSERT` | `backupPolicyName, backupScheduleName, deviceName, managerName, resourceGroupName, subscriptionId, data__properties` | Creates or updates the backup schedule. |
| `BackupSchedules_Delete` | `DELETE` | `backupPolicyName, backupScheduleName, deviceName, managerName, resourceGroupName, subscriptionId` | Deletes the backup schedule. |
