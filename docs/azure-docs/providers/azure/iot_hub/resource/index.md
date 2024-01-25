---
title: resource
hide_title: false
hide_table_of_contents: false
keywords:
  - resource
  - iot_hub
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
<tr><td><b>Name</b></td><td><code>resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub.resource</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `etag` | `string` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
| `identity` | `object` |  |
| `location` | `string` | The resource location. |
| `properties` | `object` | The properties of an IoT hub. |
| `sku` | `object` | Information about the SKU of the IoT hub. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | The resource tags. |
| `type` | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get the non-security related metadata of an IoT hub. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Get all the IoT hubs in a resource group. |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | Get all the IoT hubs in a subscription. |
| `create_or_update` | `INSERT` | `api-version, resourceGroupName, resourceName, subscriptionId, data__sku` | Create or update the metadata of an Iot hub. The usual pattern to modify a property is to retrieve the IoT hub metadata and security metadata, and then combine them with the modified values in a new body to update the IoT hub. If certain properties are missing in the JSON, updating IoT Hub may cause these values to fallback to default, which may lead to unexpected behavior. |
| `delete` | `DELETE` | `api-version, resourceGroupName, resourceName, subscriptionId` | Delete an IoT hub. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Get all the IoT hubs in a resource group. |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | Get all the IoT hubs in a subscription. |
| `check_name_availability` | `EXEC` | `api-version, subscriptionId, data__name` | Check if an IoT hub name is available. |
| `export_devices` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId, data__excludeKeys, data__exportBlobContainerUri` | Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities. |
| `import_devices` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId, data__inputBlobContainerUri, data__outputBlobContainerUri` | Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities. |
| `test_all_routes` | `EXEC` | `api-version, iotHubName, resourceGroupName, subscriptionId` | Test all routes configured in this Iot Hub |
| `test_route` | `EXEC` | `api-version, iotHubName, resourceGroupName, subscriptionId, data__route` | Test the new route for this Iot Hub |
| `update` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Update an existing IoT Hub tags. to update other fields use the CreateOrUpdate method |
