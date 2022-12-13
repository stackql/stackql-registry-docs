---
title: api_version_set
hide_title: false
hide_table_of_contents: false
keywords:
  - api_version_set
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
<tr><td><b>Name</b></td><td><code>api_version_set</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_version_set</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of an API Version Set. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiVersionSet_Get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, versionSetId` | Gets the details of the Api Version Set specified by its identifier. |
| `ApiVersionSet_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of API Version Sets in the specified service instance. |
| `ApiVersionSet_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, subscriptionId, versionSetId` | Creates or Updates a Api Version Set. |
| `ApiVersionSet_Delete` | `DELETE` | `If-Match, resourceGroupName, serviceName, subscriptionId, versionSetId` | Deletes specific Api Version Set. |
| `ApiVersionSet_GetEntityTag` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, versionSetId` | Gets the entity state (Etag) version of the Api Version Set specified by its identifier. |
| `ApiVersionSet_Update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId, versionSetId` | Updates the details of the Api VersionSet specified by its identifier. |
