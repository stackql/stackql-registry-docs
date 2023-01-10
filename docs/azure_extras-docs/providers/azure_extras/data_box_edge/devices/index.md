---
title: devices
hide_title: false
hide_table_of_contents: false
keywords:
  - devices
  - data_box_edge
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
<tr><td><b>Id</b></td><td><code>azure_extras.data_box_edge.devices</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The path ID that uniquely identifies the object. |
| `name` | `string` | The object name. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | The list of tags that describe the device. These tags can be used to view and group this device (across resource groups). |
| `type` | `string` | The hierarchical type of the object. |
| `properties` | `object` | The properties of the Data Box Edge/Gateway device. |
| `location` | `string` | The location of the device. This is a supported and registered Azure geographical region (for example, West US, East US, or Southeast Asia). The geographical region of a device cannot be changed once it is created, but if an identical geographical region is specified on update, the request will succeed. |
| `etag` | `string` | The etag for the devices. |
| `identity` | `object` | Msi identity details of the resource |
| `kind` | `string` | The kind of the device. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Devices_Get` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` | Gets the properties of the Data Box Edge/Data Box Gateway device. |
| `Devices_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all the Data Box Edge/Data Box Gateway devices in a resource group. |
| `Devices_ListBySubscription` | `SELECT` | `subscriptionId` | Gets all the Data Box Edge/Data Box Gateway devices in a subscription. |
| `Devices_CreateOrUpdate` | `INSERT` | `deviceName, resourceGroupName, subscriptionId, data__location` | Creates or updates a Data Box Edge/Data Box Gateway resource. |
| `Devices_Delete` | `DELETE` | `deviceName, resourceGroupName, subscriptionId` | Deletes the Data Box Edge/Data Box Gateway device. |
| `Devices_CreateOrUpdateSecuritySettings` | `EXEC` | `deviceName, resourceGroupName, subscriptionId, data__properties` | Updates the security settings on a Data Box Edge/Data Box Gateway device. |
| `Devices_DownloadUpdates` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` |  |
| `Devices_GenerateCertificate` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | Generates certificate for activation key. |
| `Devices_GetExtendedInformation` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | Gets additional information for the specified Azure Stack Edge/Data Box Gateway device. |
| `Devices_GetNetworkSettings` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | Gets the network settings of the specified Data Box Edge/Data Box Gateway device. |
| `Devices_GetUpdateSummary` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` |  |
| `Devices_InstallUpdates` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` |  |
| `Devices_ScanForUpdates` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` |  |
| `Devices_Update` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | Modifies a Data Box Edge/Data Box Gateway resource. |
| `Devices_UpdateExtendedInformation` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | Gets additional information for the specified Data Box Edge/Data Box Gateway device. |
| `Devices_UploadCertificate` | `EXEC` | `deviceName, resourceGroupName, subscriptionId, data__properties` | Uploads registration certificate for the device. |
