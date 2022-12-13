---
title: api_release
hide_title: false
hide_table_of_contents: false
keywords:
  - api_release
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
<tr><td><b>Name</b></td><td><code>api_release</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_release</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | API Release details |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiRelease_Get` | `SELECT` | `apiId, releaseId, resourceGroupName, serviceName, subscriptionId` | Returns the details of an API release. |
| `ApiRelease_ListByService` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists all releases of an API. An API release is created when making an API Revision current. Releases are also used to rollback to previous revisions. Results will be paged and can be constrained by the $top and $skip parameters. |
| `ApiRelease_CreateOrUpdate` | `INSERT` | `apiId, releaseId, resourceGroupName, serviceName, subscriptionId` | Creates a new Release for the API. |
| `ApiRelease_Delete` | `DELETE` | `If-Match, apiId, releaseId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified release in the API. |
| `ApiRelease_GetEntityTag` | `EXEC` | `apiId, releaseId, resourceGroupName, serviceName, subscriptionId` | Returns the etag of an API release. |
| `ApiRelease_Update` | `EXEC` | `If-Match, apiId, releaseId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the release of the API specified by its identifier. |
