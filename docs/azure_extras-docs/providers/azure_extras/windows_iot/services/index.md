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
| `etag` | `string` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
| `location` | `string` | The Azure Region where the resource lives |
| `properties` | `object` | The properties of a Windows IoT Device Service. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `deviceName, resourceGroupName, subscriptionId` | Get the non-security related metadata of a Windows IoT Device Service. |
| `list` | `SELECT` | `subscriptionId` | Get all the IoT hubs in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the IoT hubs in a resource group. |
| `create_or_update` | `INSERT` | `deviceName, resourceGroupName, subscriptionId` | Create or update the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values in a new body to update the Windows IoT Device Service. |
| `delete` | `DELETE` | `deviceName, resourceGroupName, subscriptionId` | Delete a Windows IoT Device Service. |
| `_list` | `EXEC` | `subscriptionId` | Get all the IoT hubs in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get all the IoT hubs in a resource group. |
| `check_device_service_name_availability` | `EXEC` | `subscriptionId, data__name` | Check if a Windows IoT Device Service name is available. |
| `update` | `EXEC` | `deviceName, resourceGroupName, subscriptionId` | Updates the metadata of a Windows IoT Device Service. The usual pattern to modify a property is to retrieve the Windows IoT Device Service metadata and security metadata, and then combine them with the modified values in a new body to update the Windows IoT Device Service. |
