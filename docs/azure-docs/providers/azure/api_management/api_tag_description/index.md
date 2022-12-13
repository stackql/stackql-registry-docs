---
title: api_tag_description
hide_title: false
hide_table_of_contents: false
keywords:
  - api_tag_description
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
<tr><td><b>Name</b></td><td><code>api_tag_description</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_tag_description</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | TagDescription contract Properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiTagDescription_Get` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId, tagDescriptionId` | Get Tag description in scope of API |
| `ApiTagDescription_ListByService` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists all Tags descriptions in scope of API. Model similar to swagger - tagDescription is defined on API level but tag may be assigned to the Operations |
| `ApiTagDescription_CreateOrUpdate` | `INSERT` | `apiId, resourceGroupName, serviceName, subscriptionId, tagDescriptionId` | Create/Update tag description in scope of the Api. |
| `ApiTagDescription_Delete` | `DELETE` | `If-Match, apiId, resourceGroupName, serviceName, subscriptionId, tagDescriptionId` | Delete tag description for the Api. |
| `ApiTagDescription_GetEntityTag` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId, tagDescriptionId` | Gets the entity state version of the tag specified by its identifier. |
