---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
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
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.storsimple_8000_series.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
| `properties` | `object` | The properties of the StorSimple device. |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Returns the properties of the specified device. |
| `list_by_manager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Returns the list of devices for the specified manager. |
| `delete` | `DELETE` | `deviceName, managerName, resourceGroupName, subscriptionId` | Deletes the device. |
| `_list_by_manager` | `EXEC` | `managerName, resourceGroupName, subscriptionId` | Returns the list of devices for the specified manager. |
| `authorize_for_service_encryption_key_rollover` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Authorizes the specified device for service data encryption key rollover. |
| `configure` | `EXEC` | `managerName, resourceGroupName, subscriptionId, data__properties` | Complete minimal setup before using the device. |
| `deactivate` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Deactivates the device. |
| `failover` | `EXEC` | `managerName, resourceGroupName, sourceDeviceName, subscriptionId` | Failovers a set of volume containers from a specified source device to a target device. |
| `install_updates` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Downloads and installs the updates on the device. |
| `scan_for_updates` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Scans for updates on the device. |
| `update` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId, data__properties` | Patches the device. |
