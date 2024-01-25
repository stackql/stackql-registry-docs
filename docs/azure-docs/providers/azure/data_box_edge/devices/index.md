---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - data_box_edge
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
<tr><td><b>Id</b></td><td><code>azure.data_box_edge.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `etag` | `string` | The etag for the devices. |
| `identity` | `object` | Msi identity details of the resource |
| `kind` | `string` | The kind of the device. |
| `location` | `string` | The location of the device. This is a supported and registered Azure geographical region (for example, West US, East US, or Southeast Asia). The geographical region of a device cannot be changed once it is created, but if an identical geographical region is specified on update, the request will succeed. |
| `properties` | `object` | The properties of the Data Box Edge/Gateway device. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | The list of tags that describe the device. These tags can be used to view and group this device (across resource groups). |
| `type` | `string` | The hierarchical type of the object. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` | Gets the properties of the Data Box Edge/Data Box Gateway device. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the Data Box Edge/Data Box Gateway devices in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets all the Data Box Edge/Data Box Gateway devices in a subscription. |
| `create_or_update` | `INSERT` | `deviceName, resourceGroupName, subscriptionId, data__location` | Creates or updates a Data Box Edge/Data Box Gateway resource. |
| `delete` | `DELETE` | `deviceName, resourceGroupName, subscriptionId` | Deletes the Data Box Edge/Data Box Gateway device. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all the Data Box Edge/Data Box Gateway devices in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets all the Data Box Edge/Data Box Gateway devices in a subscription. |
| `download_updates` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` |  |
| `generate_certificate` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | Generates certificate for activation key. |
| `install_updates` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` |  |
| `scan_for_updates` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` |  |
| `update` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | Modifies a Data Box Edge/Data Box Gateway resource. |
| `upload_certificate` | `EXEC` | `deviceName, resourceGroupName, subscriptionId, data__properties` | Uploads registration certificate for the device. |
