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
| `tags` | `object` | Resource tags. |
| `etag` | `string` | ETag of the resource. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of an API Management service resource description. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | Resource type for API Management resource is set to Microsoft.ApiManagement. |
| `sku` | `object` | API Management service resource SKU properties. |
| `identity` | `object` | Identity properties of the Api Management service resource. |
| `zones` | `array` | A list of availability zones denoting where the resource needs to come from. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiManagementService_Get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Gets an API Management service resource description. |
| `ApiManagementService_List` | `SELECT` | `subscriptionId` | Lists all API Management services within an Azure subscription. |
| `ApiManagementService_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | List all API Management services within a resource group. |
| `ApiManagementService_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, subscriptionId, data__location, data__properties, data__sku` | Creates or updates an API Management service. This is long running operation and could take several minutes to complete. |
| `ApiManagementService_Delete` | `DELETE` | `resourceGroupName, serviceName, subscriptionId` | Deletes an existing API Management service. |
| `ApiManagementService_ApplyNetworkConfigurationUpdates` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Updates the Microsoft.ApiManagement resource running in the Virtual network to pick the updated DNS changes. |
| `ApiManagementService_Backup` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, data__backupName, data__containerName, data__storageAccount` | Creates a backup of the API Management service to the given Azure Storage Account. This is long running operation and could take several minutes to complete. |
| `ApiManagementService_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name` | Checks availability and correctness of a name for an API Management service. |
| `ApiManagementService_GetDomainOwnershipIdentifier` | `EXEC` | `subscriptionId` | Get the custom domain ownership identifier for an API Management service. |
| `ApiManagementService_GetSsoToken` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Gets the Single-Sign-On token for the API Management Service which is valid for 5 Minutes. |
| `ApiManagementService_Restore` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, data__backupName, data__containerName, data__storageAccount` | Restores a backup of an API Management service created using the ApiManagementService_Backup operation on the current service. This is a long running operation and could take several minutes to complete. |
| `ApiManagementService_Update` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Updates an existing API Management service. |
