---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
  - windows_iot
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.windows_iot.services</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `etag` | `string` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
| `location` | `string` | The Azure Region where the resource lives |
| `properties` | `object` | The properties of a Windows IoT Device Service. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Services_Get` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` | Get the non-security related metadata of a Windows IoT Device Service. |
| `Services_List` | `SELECT` | `subscriptionId` | Get all the IoT hubs in a subscription. |
| `Services_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the IoT hubs in a resource group. |
| `Services_CreateOrUpdate` | `INSERT` | `deviceName, resourceGroupName, subscriptionId` | Create or update the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values in a new body to update the Windows IoT Device Service. |
| `Services_Delete` | `DELETE` | `deviceName, resourceGroupName, subscriptionId` | Delete a Windows IoT Device Service. |
| `Services_CheckDeviceServiceNameAvailability` | `EXEC` | `subscriptionId, data__name` | Check if a Windows IoT Device Service name is available. |
| `Services_Update` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | Updates the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values in a new body to update the Windows IoT Device Service. |
