---
title: tenant_access
hide_title: false
hide_table_of_contents: false
keywords:
  - tenant_access
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
<tr><td><b>Name</b></td><td><code>tenant_access</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.tenant_access</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Tenant access information contract of the API Management service. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `TenantAccess_Get` | `SELECT` | `accessName, resourceGroupName, serviceName, subscriptionId` | Get tenant access information details without secrets. |
| `TenantAccess_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Returns list of access infos - for Git and Management endpoints. |
| `TenantAccess_Create` | `INSERT` | `If-Match, accessName, resourceGroupName, serviceName, subscriptionId` | Update tenant access information details. |
| `TenantAccess_GetEntityTag` | `EXEC` | `accessName, resourceGroupName, serviceName, subscriptionId` | Tenant access metadata |
| `TenantAccess_ListSecrets` | `EXEC` | `accessName, resourceGroupName, serviceName, subscriptionId` | Get tenant access information details. |
| `TenantAccess_RegeneratePrimaryKey` | `EXEC` | `accessName, resourceGroupName, serviceName, subscriptionId` | Regenerate primary access key |
| `TenantAccess_RegenerateSecondaryKey` | `EXEC` | `accessName, resourceGroupName, serviceName, subscriptionId` | Regenerate secondary access key |
| `TenantAccess_Update` | `EXEC` | `If-Match, accessName, resourceGroupName, serviceName, subscriptionId` | Update tenant access information details. |
