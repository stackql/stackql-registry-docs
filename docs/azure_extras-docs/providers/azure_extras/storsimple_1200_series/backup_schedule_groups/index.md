---
title: backup_schedule_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_schedule_groups
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
<tr><td><b>Name</b></td><td><code>backup_schedule_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.backup_schedule_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier. |
| `name` | `string` | The name. |
| `properties` | `object` | The Backup Schedule Group Properties |
| `type` | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, managerName, resourceGroupName, scheduleGroupName, subscriptionId` | Returns the properties of the specified backup schedule group name. |
| `list_by_device` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the backup schedule groups in a device. |
| `create_or_update` | `INSERT` | `deviceName, managerName, resourceGroupName, scheduleGroupName, subscriptionId, data__properties` | Creates or Updates the backup schedule Group. |
| `delete` | `DELETE` | `deviceName, managerName, resourceGroupName, scheduleGroupName, subscriptionId` | Deletes the backup schedule group. |
| `_list_by_device` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the backup schedule groups in a device. |
