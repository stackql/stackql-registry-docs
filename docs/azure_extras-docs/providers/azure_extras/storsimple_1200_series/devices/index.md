---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
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
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_1200_series.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The identifier. |
| `name` | `string` | The name. |
| `properties` | `object` | Encases all the properties of the Device |
| `type` | `string` | The type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Returns the properties of the specified device name. |
| `list_by_manager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the devices in a manager. |
| `delete` | `DELETE` | `deviceName, managerName, resourceGroupName, subscriptionId` | Deletes the device. |
| `_list_by_manager` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Retrieves all the devices in a manager. |
| `deactivate` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Deactivates the device. |
| `download_updates` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Downloads updates on the device. |
| `failover` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Fails over the device to another device. |
| `install_updates` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Installs the updates on the device. |
| `patch` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Patches the device. |
| `scan_for_updates` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Scans for updates on the device. |
