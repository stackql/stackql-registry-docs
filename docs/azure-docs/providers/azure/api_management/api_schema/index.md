---
title: api_schema
hide_title: false
hide_table_of_contents: false
keywords:
  - api_schema
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
<tr><td><b>Name</b></td><td><code>api_schema</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_schema</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | API Schema create or update contract Properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiSchema_Get` | `SELECT` | `apiId, resourceGroupName, schemaId, serviceName, subscriptionId` | Get the schema configuration at the API level. |
| `ApiSchema_ListByApi` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Get the schema configuration at the API level. |
| `ApiSchema_CreateOrUpdate` | `INSERT` | `apiId, resourceGroupName, schemaId, serviceName, subscriptionId` | Creates or updates schema configuration for the API. |
| `ApiSchema_Delete` | `DELETE` | `If-Match, apiId, resourceGroupName, schemaId, serviceName, subscriptionId` | Deletes the schema configuration at the Api. |
| `ApiSchema_GetEntityTag` | `EXEC` | `apiId, resourceGroupName, schemaId, serviceName, subscriptionId` | Gets the entity state (Etag) version of the schema specified by its identifier. |
