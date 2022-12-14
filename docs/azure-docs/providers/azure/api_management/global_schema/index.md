---
title: global_schema
hide_title: false
hide_table_of_contents: false
keywords:
  - global_schema
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
<tr><td><b>Name</b></td><td><code>global_schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.global_schema</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Schema create or update contract Properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `GlobalSchema_Get` | `SELECT` | `resourceGroupName, schemaId, serviceName, subscriptionId` | Gets the details of the Schema specified by its identifier. |
| `GlobalSchema_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of schemas registered with service instance. |
| `GlobalSchema_CreateOrUpdate` | `INSERT` | `resourceGroupName, schemaId, serviceName, subscriptionId` | Creates new or updates existing specified Schema of the API Management service instance. |
| `GlobalSchema_Delete` | `DELETE` | `If-Match, resourceGroupName, schemaId, serviceName, subscriptionId` | Deletes specific Schema. |
| `GlobalSchema_GetEntityTag` | `EXEC` | `resourceGroupName, schemaId, serviceName, subscriptionId` | Gets the entity state (Etag) version of the Schema specified by its identifier. |
