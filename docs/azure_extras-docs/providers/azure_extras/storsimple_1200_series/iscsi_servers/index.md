---
title: iscsi_servers
hide_title: false
hide_table_of_contents: false
keywords:
  - iscsi_servers
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
<tr><td><b>Name</b></td><td><code>iscsi_servers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.iscsi_servers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier. |
| `name` | `string` | The name. |
| `properties` | `object` | The iSCSI server properties. |
| `type` | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId` | Returns the properties of the specified iSCSI server name. |
| `list_by_device` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the iSCSI in a device. |
| `list_by_manager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the iSCSI servers in a manager. |
| `create_or_update` | `INSERT` | `deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId, data__properties` | Creates or updates the iSCSI server. |
| `delete` | `DELETE` | `deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId` | Deletes the iSCSI server. |
| `_list_by_device` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the iSCSI in a device. |
| `_list_by_manager` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the iSCSI servers in a manager. |
| `backup_now` | `EXEC` | `deviceName, iscsiServerName, managerName, resourceGroupName, subscriptionId` | Backup the iSCSI server now. |
