---
title: iot_dps_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_dps_resource
  - devices
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
<tr><td><b>Name</b></td><td><code>iot_dps_resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.devices.iot_dps_resource</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource identifier. |
| `name` | `string` | The resource name. |
| `tags` | `object` | The resource tags. |
| `properties` | `object` | the service specific properties of a provisioning service, including keys, linked iot hubs, current state, and system generated properties such as hostname and idScope |
| `location` | `string` | The resource location. |
| `sku` | `object` | List of possible provisioning service SKUs. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The resource type. |
| `etag` | `string` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IotDpsResource_Get` | `SELECT` | `api-version, provisioningServiceName, resourceGroupName, subscriptionId` | Get the metadata of the provisioning service without SAS keys. |
| `IotDpsResource_ListByResourceGroup` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Get a list of all provisioning services in the given resource group. |
| `IotDpsResource_ListBySubscription` | `SELECT` | `api-version, subscriptionId` | List all the provisioning services for a given subscription id. |
| `IotDpsResource_CreateOrUpdate` | `INSERT` | `api-version, provisioningServiceName, resourceGroupName, subscriptionId, data__properties, data__sku` | Create or update the metadata of the provisioning service. The usual pattern to modify a property is to retrieve the provisioning service metadata and security metadata, and then combine them with the modified values in a new body to update the provisioning service. |
| `IotDpsResource_Delete` | `DELETE` | `api-version, provisioningServiceName, resourceGroupName, subscriptionId` | Deletes the Provisioning Service. |
| `IotDpsResource_CheckProvisioningServiceNameAvailability` | `EXEC` | `api-version, subscriptionId, data__name` | Check if a provisioning service name is available. This will validate if the name is syntactically valid and if the name is usable |
| `IotDpsResource_CreateOrUpdatePrivateEndpointConnection` | `EXEC` | `api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId, data__properties` | Create or update the status of a private endpoint connection with the specified name |
| `IotDpsResource_DeletePrivateEndpointConnection` | `EXEC` | `api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Delete private endpoint connection with the specified name |
| `IotDpsResource_GetOperationResult` | `EXEC` | `api-version, asyncinfo, operationId, provisioningServiceName, resourceGroupName, subscriptionId` | Gets the status of a long running operation, such as create, update or delete a provisioning service. |
| `IotDpsResource_GetPrivateEndpointConnection` | `EXEC` | `api-version, privateEndpointConnectionName, resourceGroupName, resourceName, subscriptionId` | Get private endpoint connection properties |
| `IotDpsResource_GetPrivateLinkResources` | `EXEC` | `api-version, groupId, resourceGroupName, resourceName, subscriptionId` | Get the specified private link resource for the given provisioning service |
| `IotDpsResource_ListKeys` | `EXEC` | `api-version, provisioningServiceName, resourceGroupName, subscriptionId` | List the primary and secondary keys for a provisioning service. |
| `IotDpsResource_ListKeysForKeyName` | `EXEC` | `api-version, keyName, provisioningServiceName, resourceGroupName, subscriptionId` | List primary and secondary keys for a specific key name |
| `IotDpsResource_ListPrivateEndpointConnections` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | List private endpoint connection properties |
| `IotDpsResource_ListPrivateLinkResources` | `EXEC` | `api-version, resourceGroupName, resourceName, subscriptionId` | List private link resources for the given provisioning service |
| `IotDpsResource_Update` | `EXEC` | `api-version, provisioningServiceName, resourceGroupName, subscriptionId` | Update an existing provisioning service's tags. to update other fields use the CreateOrUpdate method |
| `IotDpsResource_listValidSkus` | `EXEC` | `api-version, provisioningServiceName, resourceGroupName, subscriptionId` | Gets the list of valid SKUs and tiers for a provisioning service. |
