---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
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
<tr><td><b>Name</b></td><td><code>backups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.stor_simple_8000_series.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `properties` | `object` | The properties of the backup. |
| `type` | `string` | The hierarchical type of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Backups_ListByDevice` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the backups in a device. |
| `Backups_Delete` | `DELETE` | `backupName, deviceName, managerName, resourceGroupName, subscriptionId` | Deletes the backup. |
| `Backups_Clone` | `EXEC` | `backupElementName, backupName, deviceName, managerName, resourceGroupName, subscriptionId, data__backupElement, data__targetAccessControlRecordIds, data__targetDeviceId, data__targetVolumeName` | Clones the backup element as a new volume. |
| `Backups_Restore` | `EXEC` | `backupName, deviceName, managerName, resourceGroupName, subscriptionId` | Restores the backup on the device. |
