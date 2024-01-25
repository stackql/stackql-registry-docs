---
title: service
hide_title: false
hide_table_of_contents: false
keywords:
  - service
  - api_management
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
<tr><td><b>Name</b></td><td><code>service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.service</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | ETag of the resource. |
| `identity` | `object` | Identity properties of the Api Management service resource. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of an API Management service resource description. |
| `sku` | `object` | API Management service resource SKU properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type for API Management resource is set to Microsoft.ApiManagement. |
| `zones` | `array` | A list of availability zones denoting where the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Gets an API Management service resource description. |
| `list` | `SELECT` | `subscriptionId` | Lists all API Management services within an Azure subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all API Management services within a resource group. |
| `create_or_update` | `INSERT` | `resourceGroupName, serviceName, subscriptionId, data__location, data__properties, data__sku` | Creates or updates an API Management service. This is long running operation and could take several minutes to complete. |
| `delete` | `DELETE` | `resourceGroupName, serviceName, subscriptionId` | Deletes an existing API Management service. |
| `_list` | `EXEC` | `subscriptionId` | Lists all API Management services within an Azure subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all API Management services within a resource group. |
| `apply_network_configuration_updates` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Updates the Microsoft.ApiManagement resource running in the Virtual network to pick the updated DNS changes. |
| `backup` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, data__backupName, data__containerName, data__storageAccount` | Creates a backup of the API Management service to the given Azure Storage Account. This is long running operation and could take several minutes to complete. |
| `check_name_availability` | `EXEC` | `subscriptionId, data__name` | Checks availability and correctness of a name for an API Management service. |
| `migrate_to_stv2` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Upgrades an API Management service to the Stv2 platform. For details refer to https://aka.ms/apim-migrate-stv2. This change is not reversible. This is long running operation and could take several minutes to complete. |
| `restore` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, data__backupName, data__containerName, data__storageAccount` | Restores a backup of an API Management service created using the ApiManagementService_Backup operation on the current service. This is a long running operation and could take several minutes to complete. |
| `update` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Updates an existing API Management service. |
