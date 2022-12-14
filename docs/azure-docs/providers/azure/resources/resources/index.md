---
title: resources
hide_title: false
hide_table_of_contents: false
keywords:
  - resources
  - resources
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
<tr><td><b>Name</b></td><td><code>resources</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resources.resources</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID |
| `name` | `string` | Resource name |
| `sku` | `object` | SKU for the resource. |
| `type` | `string` | Resource type |
| `extendedLocation` | `object` | Resource extended location. |
| `identity` | `object` | Identity for the resource. |
| `kind` | `string` | The kind of the resource. |
| `tags` | `object` | Resource tags |
| `plan` | `object` | Plan for the resource. |
| `properties` | `object` | The resource properties. |
| `managedBy` | `string` | ID of the resource that manages this resource. |
| `location` | `string` | Resource location |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Resources_Get` | `SELECT` | `api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` | Gets a resource. |
| `Resources_List` | `SELECT` | `subscriptionId` | Get all the resources in a subscription. |
| `Resources_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the resources for a resource group. |
| `Resources_CreateOrUpdate` | `INSERT` | `api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` | Creates a resource. |
| `Resources_Delete` | `DELETE` | `api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` | Deletes a resource. |
| `Resources_DeleteById` | `DELETE` | `api-version, resourceId` | Deletes a resource by ID. |
| `Resources_CheckExistence` | `EXEC` | `api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` | Checks whether a resource exists. |
| `Resources_CheckExistenceById` | `EXEC` | `api-version, resourceId` | Checks by ID whether a resource exists. This API currently works only for a limited set of Resource providers. In the event that a Resource provider does not implement this API, ARM will respond with a 405. The alternative then is to use the GET API to check for the existence of the resource. |
| `Resources_CreateOrUpdateById` | `EXEC` | `api-version, resourceId` | Create a resource by ID. |
| `Resources_GetById` | `EXEC` | `api-version, resourceId` | Gets a resource by ID. |
| `Resources_MoveResources` | `EXEC` | `sourceResourceGroupName, subscriptionId` | The resources to be moved must be in the same source resource group in the source subscription being used. The target resource group may be in a different subscription. When moving resources, both the source group and the target group are locked for the duration of the operation. Write and delete operations are blocked on the groups until the move completes.  |
| `Resources_Update` | `EXEC` | `api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` | Updates a resource. |
| `Resources_UpdateById` | `EXEC` | `api-version, resourceId` | Updates a resource by ID. |
| `Resources_ValidateMoveResources` | `EXEC` | `sourceResourceGroupName, subscriptionId` | This operation checks whether the specified resources can be moved to the target. The resources to be moved must be in the same source resource group in the source subscription being used. The target resource group may be in a different subscription. If validation succeeds, it returns HTTP response code 204 (no content). If validation fails, it returns HTTP response code 409 (Conflict) with an error message. Retrieve the URL in the Location header value to check the result of the long-running operation. |
