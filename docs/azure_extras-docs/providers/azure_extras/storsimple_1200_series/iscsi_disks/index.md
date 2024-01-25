---
title: iscsi_disks
hide_title: false
hide_table_of_contents: false
keywords:
  - iscsi_disks
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
<tr><td><b>Name</b></td><td><code>iscsi_disks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.iscsi_disks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier. |
| `name` | `string` | The name. |
| `properties` | `object` | The iSCSI disk properties. |
| `type` | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, diskName, iscsiServerName, managerName, resourceGroupName, subscriptionId` | Returns the properties of the specified iSCSI disk name. |
| `list_by_device` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the iSCSI disks in a device. |
| `list_by_iscsi_server` | `SELECT` | `deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId` | Retrieves all the disks in a iSCSI server. |
| `create_or_update` | `INSERT` | `deviceName, diskName, iscsiServerName, managerName, resourceGroupName, subscriptionId, data__properties` | Creates or updates the iSCSI disk. |
| `delete` | `DELETE` | `deviceName, diskName, iscsiServerName, managerName, resourceGroupName, subscriptionId` | Deletes the iSCSI disk. |
| `_list_by_device` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the iSCSI disks in a device. |
| `_list_by_iscsi_server` | `EXEC` | `deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId` | Retrieves all the disks in a iSCSI server. |
