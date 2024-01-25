---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - sphere
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
<tr><td><b>Id</b></td><td><code>azure.sphere.devices</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId` | Get a Device. Use '.unassigned' or '.default' for the device group and product names when a device does not belong to a device group and product. |
| `list_by_device_group` | `SELECT` | `catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId` | List Device resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| `create_or_update` | `INSERT` | `catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId` | Create a Device. Use '.unassigned' or '.default' for the device group and product names to claim a device to the catalog only. |
| `delete` | `DELETE` | `catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId` | Delete a Device |
| `_list_by_device_group` | `EXEC` | `catalogName, deviceGroupName, productName, resourceGroupName, subscriptionId` | List Device resources by DeviceGroup. '.default' and '.unassigned' are system defined values and cannot be used for product or device group name. |
| `generate_capability_image` | `EXEC` | `catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId, data__capabilities` | Generates the capability image for the device. Use '.unassigned' or '.default' for the device group and product names to generate the image for a device that does not belong to a specific device group and product. |
| `update` | `EXEC` | `catalogName, deviceGroupName, deviceName, productName, resourceGroupName, subscriptionId` | Update a Device. Use '.unassigned' or '.default' for the device group and product names to move a device to the catalog level. |
