---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
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
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.stor_simple_8000_series.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The name of the object. |
| `properties` | `object` | The properties of the StorSimple device. |
| `type` | `string` | The hierarchical type of the object. |
| `kind` | `string` | The Kind of the object. Currently only Series8000 is supported |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Devices_Get` | `SELECT` | `deviceName, managerName, resourceGroupName, subscriptionId` | Returns the properties of the specified device. |
| `Devices_ListByManager` | `SELECT` | `managerName, resourceGroupName, subscriptionId` | Returns the list of devices for the specified manager. |
| `Devices_Delete` | `DELETE` | `deviceName, managerName, resourceGroupName, subscriptionId` | Deletes the device. |
| `Devices_AuthorizeForServiceEncryptionKeyRollover` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Authorizes the specified device for service data encryption key rollover. |
| `Devices_Configure` | `EXEC` | `managerName, resourceGroupName, subscriptionId, data__properties` | Complete minimal setup before using the device. |
| `Devices_Deactivate` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Deactivates the device. |
| `Devices_Failover` | `EXEC` | `managerName, resourceGroupName, sourceDeviceName, subscriptionId` | Failovers a set of volume containers from a specified source device to a target device. |
| `Devices_GetUpdateSummary` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Returns the update summary of the specified device name. |
| `Devices_InstallUpdates` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Downloads and installs the updates on the device. |
| `Devices_ListFailoverSets` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Returns all failover sets for a given device and their eligibility for participating in a failover. A failover set refers to a set of volume containers that need to be failed-over as a single unit to maintain data integrity. |
| `Devices_ListFailoverTargets` | `EXEC` | `managerName, resourceGroupName, sourceDeviceName, subscriptionId` | Given a list of volume containers to be failed over from a source device, this method returns the eligibility result, as a failover target, for all devices under that resource. |
| `Devices_ListMetricDefinition` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Gets the metric definitions for the specified device. |
| `Devices_ListMetrics` | `EXEC` | `$filter, deviceName, managerName, resourceGroupName, subscriptionId` | Gets the metrics for the specified device. |
| `Devices_ScanForUpdates` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Scans for updates on the device. |
| `Devices_Update` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId, data__properties` | Patches the device. |
