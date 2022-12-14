---
title: tag
hide_title: false
hide_table_of_contents: false
keywords:
  - tag
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
<tr><td><b>Name</b></td><td><code>tag</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.tag</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Tag contract Properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Tag_Get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, tagId` | Gets the details of the tag specified by its identifier. |
| `Tag_ListByApi` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists all Tags associated with the API. |
| `Tag_ListByOperation` | `SELECT` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Lists all Tags associated with the Operation. |
| `Tag_ListByProduct` | `SELECT` | `productId, resourceGroupName, serviceName, subscriptionId` | Lists all Tags associated with the Product. |
| `Tag_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of tags defined within a service instance. |
| `Tag_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, subscriptionId, tagId` | Creates a tag. |
| `Tag_Delete` | `DELETE` | `If-Match, resourceGroupName, serviceName, subscriptionId, tagId` | Deletes specific tag of the API Management service instance. |
| `Tag_AssignToApi` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId, tagId` | Assign tag to the Api. |
| `Tag_AssignToOperation` | `EXEC` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId, tagId` | Assign tag to the Operation. |
| `Tag_AssignToProduct` | `EXEC` | `productId, resourceGroupName, serviceName, subscriptionId, tagId` | Assign tag to the Product. |
| `Tag_DetachFromApi` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId, tagId` | Detach the tag from the Api. |
| `Tag_DetachFromOperation` | `EXEC` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId, tagId` | Detach the tag from the Operation. |
| `Tag_DetachFromProduct` | `EXEC` | `productId, resourceGroupName, serviceName, subscriptionId, tagId` | Detach the tag from the Product. |
| `Tag_GetByApi` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId, tagId` | Get tag associated with the API. |
| `Tag_GetByOperation` | `EXEC` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId, tagId` | Get tag associated with the Operation. |
| `Tag_GetByProduct` | `EXEC` | `productId, resourceGroupName, serviceName, subscriptionId, tagId` | Get tag associated with the Product. |
| `Tag_GetEntityState` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, tagId` | Gets the entity state version of the tag specified by its identifier. |
| `Tag_GetEntityStateByApi` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId, tagId` | Gets the entity state version of the tag specified by its identifier. |
| `Tag_GetEntityStateByOperation` | `EXEC` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId, tagId` | Gets the entity state version of the tag specified by its identifier. |
| `Tag_GetEntityStateByProduct` | `EXEC` | `productId, resourceGroupName, serviceName, subscriptionId, tagId` | Gets the entity state version of the tag specified by its identifier. |
| `Tag_Update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId, tagId` | Updates the details of the tag specified by its identifier. |
