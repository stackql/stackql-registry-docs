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
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | The resource tags. |
| `location` | `string` | The resource location. |
| `sku` | `object` | Information about the SKU of the IoT hub. |
| `type` | `string` | The resource type. |
| `identity` | `object` |  |
| `properties` | `object` | The properties of an IoT hub. |
| `etag` | `string` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IotHubResource_Get` | `SELECT` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get the non-security related metadata of an IoT hub. |
| `IotHubResource_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Get all the IoT hubs in a resource group. |
| `IotHubResource_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | Get all the IoT hubs in a subscription. |
| `IotHubResource_CreateOrUpdate` | `INSERT` | `api-version, resourceGroupName, resourceName, subscriptionId, data__sku` | Create or update the metadata of an Iot hub. The usual pattern to modify a property is to retrieve the IoT hub metadata and security metadata, and then combine them with the modified values in a new body to update the IoT hub. |
| `IotHubResource_Delete` | `DELETE` | `api-version, resourceGroupName, resourceName, subscriptionId` | Delete an IoT hub. |
| `IotHubResource_CheckNameAvailability` | `EXEC` | `api-version, subscriptionId, data__name` | Check if an IoT hub name is available. |
| `IotHubResource_CreateEventHubConsumerGroup` | `EXEC` | `api-version, eventHubEndpointName, name, resourceGroupName, resourceName, subscriptionId, data__properties` | Add a consumer group to an Event Hub-compatible endpoint in an IoT hub. |
| `IotHubResource_DeleteEventHubConsumerGroup` | `EXEC` | `api-version, eventHubEndpointName, name, resourceGroupName, resourceName, subscriptionId` | Delete a consumer group from an Event Hub-compatible endpoint in an IoT hub. |
| `IotHubResource_ExportDevices` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId, data__excludeKeys, data__exportBlobContainerUri` | Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities. |
| `IotHubResource_GetEndpointHealth` | `EXEC` | `api-version, iotHubName, resourceGroupName, subscriptionId` | Get the health for routing endpoints. |
| `IotHubResource_GetEventHubConsumerGroup` | `EXEC` | `api-version, eventHubEndpointName, name, resourceGroupName, resourceName, subscriptionId` | Get a consumer group from the Event Hub-compatible device-to-cloud endpoint for an IoT hub. |
| `IotHubResource_GetJob` | `EXEC` | `api-version, jobId, resourceGroupName, resourceName, subscriptionId` | Get the details of a job from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry. |
| `IotHubResource_GetKeysForKeyName` | `EXEC` | `api-version, keyName, resourceGroupName, resourceName, subscriptionId` | Get a shared access policy by name from an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security. |
| `IotHubResource_GetQuotaMetrics` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get the quota metrics for an IoT hub. |
| `IotHubResource_GetStats` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get the statistics from an IoT hub. |
| `IotHubResource_GetValidSkus` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get the list of valid SKUs for an IoT hub. |
| `IotHubResource_ImportDevices` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId, data__inputBlobContainerUri, data__outputBlobContainerUri` | Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities. |
| `IotHubResource_ListEventHubConsumerGroups` | `EXEC` | `api-version, eventHubEndpointName, resourceGroupName, resourceName, subscriptionId` | Get a list of the consumer groups in the Event Hub-compatible device-to-cloud endpoint in an IoT hub. |
| `IotHubResource_ListJobs` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get a list of all the jobs in an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry. |
| `IotHubResource_ListKeys` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Get the security metadata for an IoT hub. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-security. |
| `IotHubResource_TestAllRoutes` | `EXEC` | `api-version, iotHubName, resourceGroupName, subscriptionId` | Test all routes configured in this Iot Hub |
| `IotHubResource_TestRoute` | `EXEC` | `api-version, iotHubName, resourceGroupName, subscriptionId, data__route` | Test the new route for this Iot Hub |
| `IotHubResource_Update` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | Update an existing IoT Hub tags. to update other fields use the CreateOrUpdate method |
