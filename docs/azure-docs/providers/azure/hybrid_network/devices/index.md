---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - hybrid_network
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
<tr><td><b>Name</b></td><td><code>devices</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_network.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Device properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Devices_Get` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` | Gets information about the specified device. |
| `Devices_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the device resource in a resource group. |
| `Devices_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all the devices in a subscription. |
| `Devices_CreateOrUpdate` | `INSERT` | `deviceName, resourceGroupName, subscriptionId` | Creates or updates a device. |
| `Devices_Delete` | `DELETE` | `deviceName, resourceGroupName, subscriptionId` | Deletes the specified device. |
| `Devices_ListRegistrationKey` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | List the registration key for the device. |
| `Devices_UpdateTags` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | Updates device tags. |
