---
title: backups
hide_title: false
hide_table_of_contents: false
keywords:
  - backups
  - storsimple_1200_series
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
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.backups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier. |
| `name` | `string` | The name. |
| `properties` | `object` | Class represents Backup properties |
| `type` | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_by_device` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the backups in a device. Can be used to get the backups for failover also. |
| `list_by_manager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the backups in a manager. |
| `delete` | `DELETE` | `backupName, deviceName, managerName, resourceGroupName, subscriptionId` | Deletes the backup. |
| `_list_by_device` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the backups in a device. Can be used to get the backups for failover also. |
| `_list_by_manager` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the backups in a manager. |
| `clone` | `EXEC` | `backupName, deviceName, elementName, managerName, resourceGroupName, subscriptionId, data__properties` | Clones the given backup element to a new disk or share with given details. |
