---
title: file_shares
hide_title: false
hide_table_of_contents: false
keywords:
  - file_shares
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
<tr><td><b>Name</b></td><td><code>file_shares</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.file_shares</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier. |
| `name` | `string` | The name. |
| `properties` | `object` | The File Share. |
| `type` | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, fileServerName, managerName, resourceGroupName, shareName, subscriptionId` | Returns the properties of the specified file share name. |
| `list_by_device` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the file shares in a device. |
| `list_by_file_server` | `SELECT` | `deviceName, fileServerName, managerName, resourceGroupName, subscriptionId` | Retrieves all the file shares in a file server. |
| `create_or_update` | `INSERT` | `deviceName, fileServerName, managerName, resourceGroupName, shareName, subscriptionId, data__properties` | Creates or updates the file share. |
| `delete` | `DELETE` | `deviceName, fileServerName, managerName, resourceGroupName, shareName, subscriptionId` | Deletes the file share. |
| `_list_by_device` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Retrieves all the file shares in a device. |
| `_list_by_file_server` | `EXEC` | `deviceName, fileServerName, managerName, resourceGroupName, subscriptionId` | Retrieves all the file shares in a file server. |
