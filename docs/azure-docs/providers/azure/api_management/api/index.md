---
title: api
hide_title: false
hide_table_of_contents: false
keywords:
  - api
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
<tr><td><b>Name</b></td><td><code>api</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | API Entity Properties |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Api_Get` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the API specified by its identifier. |
| `Api_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists all APIs of the API Management service instance. |
| `Api_CreateOrUpdate` | `INSERT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Creates new or updates existing specified API of the API Management service instance. |
| `Api_Delete` | `DELETE` | `If-Match, apiId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified API of the API Management service instance. |
| `Api_GetEntityTag` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the API specified by its identifier. |
| `Api_ListByTags` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of apis associated with tags. |
| `Api_Update` | `EXEC` | `If-Match, apiId, resourceGroupName, serviceName, subscriptionId` | Updates the specified API of the API Management service instance. |
