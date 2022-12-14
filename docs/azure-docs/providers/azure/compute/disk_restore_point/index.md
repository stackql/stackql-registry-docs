---
title: disk_restore_point
hide_title: false
hide_table_of_contents: false
keywords:
  - disk_restore_point
  - compute
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
<tr><td><b>Name</b></td><td><code>disk_restore_point</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.compute.disk_restore_point</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id |
| `name` | `string` | Resource name |
| `properties` | `object` | Properties of an incremental disk restore point |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DiskRestorePoint_Get` | `SELECT` | `diskRestorePointName, resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName` | Get disk restorePoint resource |
| `DiskRestorePoint_ListByRestorePoint` | `SELECT` | `resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName` | Lists diskRestorePoints under a vmRestorePoint. |
| `DiskRestorePoint_GrantAccess` | `EXEC` | `diskRestorePointName, resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName, data__access, data__durationInSeconds` | Grants access to a diskRestorePoint. |
| `DiskRestorePoint_RevokeAccess` | `EXEC` | `diskRestorePointName, resourceGroupName, restorePointCollectionName, subscriptionId, vmRestorePointName` | Revokes access to a diskRestorePoint. |
