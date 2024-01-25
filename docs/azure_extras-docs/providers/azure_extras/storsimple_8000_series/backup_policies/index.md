---
title: backup_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - backup_policies
  - storsimple_8000_series
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
<tr><td><b>Name</b></td><td><code>backup_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_8000_series.backup_policies</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
| `properties` | `object` | The properties of the backup policy. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `backupPolicyName, deviceName, managerName, resourceGroupName, subscriptionId` | Gets the properties of the specified backup policy name. |
| `list_by_device` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Gets all the backup policies in a device. |
| `create_or_update` | `INSERT` | `backupPolicyName, deviceName, managerName, resourceGroupName, subscriptionId, data__properties` | Creates or updates the backup policy. |
| `delete` | `DELETE` | `backupPolicyName, deviceName, managerName, resourceGroupName, subscriptionId` | Deletes the backup policy. |
| `_list_by_device` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Gets all the backup policies in a device. |
| `backup_now` | `EXEC` | `backupPolicyName, backupType, deviceName, managerName, resourceGroupName, subscriptionId` | Backup the backup policy now. |
