---
title: device_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - device_settings
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
<tr><td><b>Name</b></td><td><code>device_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.stor_simple_8000_series.device_settings</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DeviceSettings_CreateOrUpdateAlertSettings` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId, data__properties` | Creates or updates the alert settings of the specified device. |
| `DeviceSettings_CreateOrUpdateTimeSettings` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId, data__properties` | Creates or updates the time settings of the specified device. |
| `DeviceSettings_GetAlertSettings` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Gets the alert settings of the specified device. |
| `DeviceSettings_GetNetworkSettings` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Gets the network settings of the specified device. |
| `DeviceSettings_GetSecuritySettings` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Returns the Security properties of the specified device name. |
| `DeviceSettings_GetTimeSettings` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | Gets the time settings of the specified device. |
| `DeviceSettings_SyncRemotemanagementCertificate` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId` | sync Remote management Certificate between appliance and Service |
| `DeviceSettings_UpdateNetworkSettings` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId, data__properties` | Updates the network settings on the specified device. |
| `DeviceSettings_UpdateSecuritySettings` | `EXEC` | `deviceName, managerName, resourceGroupName, subscriptionId, data__properties` | Patch Security properties of the specified device name. |
