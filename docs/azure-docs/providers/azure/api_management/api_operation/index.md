---
title: api_operation
hide_title: false
hide_table_of_contents: false
keywords:
  - api_operation
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
<tr><td><b>Name</b></td><td><code>api_operation</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_operation</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Operation Contract Properties |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiOperation_Get` | `SELECT` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the API Operation specified by its identifier. |
| `ApiOperation_ListByApi` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists a collection of the operations for the specified API. |
| `ApiOperation_CreateOrUpdate` | `INSERT` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Creates a new operation in the API or updates an existing one. |
| `ApiOperation_Delete` | `DELETE` | `If-Match, apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified operation in the API. |
| `ApiOperation_GetEntityTag` | `EXEC` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the API operation specified by its identifier. |
| `ApiOperation_Update` | `EXEC` | `If-Match, apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the operation in the API specified by its identifier. |
