---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - netapp
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.netapp.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `type` | `string` | Resource type |
| `location` | `string` | Resource location |
| `properties` | `object` | Backup properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Backups_Get` | `SELECT` | `accountName, backupName, poolName, resourceGroupName, subscriptionId, volumeName` | Gets the specified backup of the volume |
| `Backups_List` | `SELECT` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | List all backups for a volume |
| `Backups_Create` | `INSERT` | `accountName, backupName, poolName, resourceGroupName, subscriptionId, volumeName, data__location, data__properties` | Create a backup for the volume |
| `Backups_Delete` | `DELETE` | `accountName, backupName, poolName, resourceGroupName, subscriptionId, volumeName` | Delete a backup of the volume |
| `Backups_GetStatus` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Get the status of the backup for a volume |
| `Backups_GetVolumeRestoreStatus` | `EXEC` | `accountName, poolName, resourceGroupName, subscriptionId, volumeName` | Get the status of the restore for a volume |
| `Backups_Update` | `EXEC` | `accountName, backupName, poolName, resourceGroupName, subscriptionId, volumeName` | Patch a backup for the volume |
