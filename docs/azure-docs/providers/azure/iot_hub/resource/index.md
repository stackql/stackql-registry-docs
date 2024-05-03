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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_hub.resource" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The resource identifier. |
| <CopyableCode code="name" /> | `string` | The resource name. |
| <CopyableCode code="etag" /> | `string` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
| <CopyableCode code="identity" /> | `object` |  |
| <CopyableCode code="location" /> | `string` | The resource location. |
| <CopyableCode code="properties" /> | `object` | The properties of an IoT hub. |
| <CopyableCode code="sku" /> | `object` | Information about the SKU of the IoT hub. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="tags" /> | `object` | The resource tags. |
| <CopyableCode code="type" /> | `string` | The resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Get the non-security related metadata of an IoT hub. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Get all the IoT hubs in a resource group. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="api-version, subscriptionId" /> | Get all the IoT hubs in a subscription. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId, data__sku" /> | Create or update the metadata of an Iot hub. The usual pattern to modify a property is to retrieve the IoT hub metadata and security metadata, and then combine them with the modified values in a new body to update the IoT hub. If certain properties are missing in the JSON, updating IoT Hub may cause these values to fallback to default, which may lead to unexpected behavior. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Delete an IoT hub. |
| <CopyableCode code="_list_by_resource_group" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, subscriptionId" /> | Get all the IoT hubs in a resource group. |
| <CopyableCode code="_list_by_subscription" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId" /> | Get all the IoT hubs in a subscription. |
| <CopyableCode code="check_name_availability" /> | `EXEC` | <CopyableCode code="api-version, subscriptionId, data__name" /> | Check if an IoT hub name is available. |
| <CopyableCode code="export_devices" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId, data__excludeKeys, data__exportBlobContainerUri" /> | Exports all the device identities in the IoT hub identity registry to an Azure Storage blob container. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities. |
| <CopyableCode code="import_devices" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId, data__inputBlobContainerUri, data__outputBlobContainerUri" /> | Import, update, or delete device identities in the IoT hub identity registry from a blob. For more information, see: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-identity-registry#import-and-export-device-identities. |
| <CopyableCode code="test_all_routes" /> | `EXEC` | <CopyableCode code="api-version, iotHubName, resourceGroupName, subscriptionId" /> | Test all routes configured in this Iot Hub |
| <CopyableCode code="test_route" /> | `EXEC` | <CopyableCode code="api-version, iotHubName, resourceGroupName, subscriptionId, data__route" /> | Test the new route for this Iot Hub |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="api-version, resourceGroupName, resourceName, subscriptionId" /> | Update an existing IoT Hub tags. to update other fields use the CreateOrUpdate method |
