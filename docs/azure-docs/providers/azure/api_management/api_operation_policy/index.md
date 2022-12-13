---
title: api_operation_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - api_operation_policy
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
<tr><td><b>Name</b></td><td><code>api_operation_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_operation_policy</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Policy contract Properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiOperationPolicy_Get` | `SELECT` | `apiId, operationId, policyId, resourceGroupName, serviceName, subscriptionId` | Get the policy configuration at the API Operation level. |
| `ApiOperationPolicy_ListByOperation` | `SELECT` | `apiId, operationId, resourceGroupName, serviceName, subscriptionId` | Get the list of policy configuration at the API Operation level. |
| `ApiOperationPolicy_CreateOrUpdate` | `INSERT` | `apiId, operationId, policyId, resourceGroupName, serviceName, subscriptionId` | Creates or updates policy configuration for the API Operation level. |
| `ApiOperationPolicy_Delete` | `DELETE` | `If-Match, apiId, operationId, policyId, resourceGroupName, serviceName, subscriptionId` | Deletes the policy configuration at the Api Operation. |
| `ApiOperationPolicy_GetEntityTag` | `EXEC` | `apiId, operationId, policyId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the API operation policy specified by its identifier. |
