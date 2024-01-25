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
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `identity` | `object` | Identity for the resource. |
| `kind` | `string` | The kind of the resource. |
| `managedBy` | `string` | ID of the resource that manages this resource. |
| `plan` | `object` | Plan for the resource. |
| `properties` | `object` | The resource properties. |
| `sku` | `object` | The resource model definition representing SKU |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` | Gets a resource. |
| `list` | `SELECT` | `subscriptionId` | Get all the resources in a subscription. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Get all the resources for a resource group. |
| `create_or_update` | `INSERT` | `api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` | Creates a resource. |
| `delete` | `DELETE` | `api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` | Deletes a resource. |
| `delete_by_id` | `DELETE` | `api-version, resourceId` | Deletes a resource by ID. |
| `_list` | `EXEC` | `subscriptionId` | Get all the resources in a subscription. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Get all the resources for a resource group. |
| `check_existence` | `EXEC` | `api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` | Checks whether a resource exists. |
| `check_existence_by_id` | `EXEC` | `api-version, resourceId` | Checks by ID whether a resource exists. This API currently works only for a limited set of Resource providers. In the event that a Resource provider does not implement this API, ARM will respond with a 405. The alternative then is to use the GET API to check for the existence of the resource. |
| `create_or_update_by_id` | `EXEC` | `api-version, resourceId` | Create a resource by ID. |
| `get_by_id` | `EXEC` | `api-version, resourceId` | Gets a resource by ID. |
| `move_resources` | `EXEC` | `sourceResourceGroupName, subscriptionId` | The resources to be moved must be in the same source resource group in the source subscription being used. The target resource group may be in a different subscription. When moving resources, both the source group and the target group are locked for the duration of the operation. Write and delete operations are blocked on the groups until the move completes.  |
| `update` | `EXEC` | `api-version, parentResourcePath, resourceGroupName, resourceName, resourceProviderNamespace, resourceType, subscriptionId` | Updates a resource. |
| `update_by_id` | `EXEC` | `api-version, resourceId` | Updates a resource by ID. |
| `validate_move_resources` | `EXEC` | `sourceResourceGroupName, subscriptionId` | This operation checks whether the specified resources can be moved to the target. The resources to be moved must be in the same source resource group in the source subscription being used. The target resource group may be in a different subscription. If validation succeeds, it returns HTTP response code 204 (no content). If validation fails, it returns HTTP response code 409 (Conflict) with an error message. Retrieve the URL in the Location header value to check the result of the long-running operation. |
