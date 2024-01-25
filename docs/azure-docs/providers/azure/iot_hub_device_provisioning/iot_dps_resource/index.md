---
title: iot_dps_resource
hide_title: false
hide_table_of_contents: false
keywords:
  - iot_dps_resource
  - iot_hub_device_provisioning
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
<tr><td><b>Name</b></td><td><code>iot_dps_resource</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_hub_device_provisioning.iot_dps_resource</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `etag` | `string` | The Etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal ETag convention. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `properties` | `object` | the service specific properties of a provisioning service, including keys, linked iot hubs, current state, and system generated properties such as hostname and idScope |
| `sku` | `object` | List of possible provisioning service SKUs. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, provisioningServiceName, resourceGroupName, subscriptionId` | Get the metadata of the provisioning service without SAS keys. |
| `list_by_resource_group` | `SELECT` | `api-version, resourceGroupName, subscriptionId` | Get a list of all provisioning services in the given resource group. |
| `list_by_subscription` | `SELECT` | `api-version, subscriptionId` | List all the provisioning services for a given subscription id. |
| `create_or_update` | `INSERT` | `api-version, provisioningServiceName, resourceGroupName, subscriptionId, data__properties, data__sku` | Create or update the metadata of the provisioning service. The usual pattern to modify a property is to retrieve the provisioning service metadata and security metadata, and then combine them with the modified values in a new body to update the provisioning service. |
| `delete` | `DELETE` | `api-version, provisioningServiceName, resourceGroupName, subscriptionId` | Deletes the Provisioning Service. |
| `_list_by_resource_group` | `EXEC` | `api-version, resourceGroupName, subscriptionId` | Get a list of all provisioning services in the given resource group. |
| `_list_by_subscription` | `EXEC` | `api-version, subscriptionId` | List all the provisioning services for a given subscription id. |
| `check_provisioning_service_name_availability` | `EXEC` | `api-version, subscriptionId, data__name` | Check if a provisioning service name is available. This will validate if the name is syntactically valid and if the name is usable |
| `update` | `EXEC` | `api-version, provisioningServiceName, resourceGroupName, subscriptionId` | Update an existing provisioning service's tags. to update other fields use the CreateOrUpdate method |
