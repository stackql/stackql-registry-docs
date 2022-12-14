---
title: device_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - device_groups
  - iot_security
  - azure    
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
<tr><td><b>Name</b></td><td><code>device_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_security.device_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Device group properties |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DeviceGroups_Get` | `SELECT` | `deviceGroupName, iotDefenderLocation, subscriptionId` | Get device group |
| `DeviceGroups_List` | `SELECT` | `iotDefenderLocation, subscriptionId` | List device groups |
| `DeviceGroups_CreateOrUpdate` | `INSERT` | `deviceGroupName, iotDefenderLocation, subscriptionId` | Create or update device group |
| `DeviceGroups_Delete` | `DELETE` | `deviceGroupName, iotDefenderLocation, subscriptionId` | Delete device group |
