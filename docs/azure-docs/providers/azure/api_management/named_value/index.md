---
title: named_value
hide_title: false
hide_table_of_contents: false
keywords:
  - named_value
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
<tr><td><b>Name</b></td><td><code>named_value</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.named_value</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | NamedValue Contract properties. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `NamedValue_Get` | `SELECT` | `namedValueId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the named value specified by its identifier. |
| `NamedValue_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of named values defined within a service instance. |
| `NamedValue_CreateOrUpdate` | `INSERT` | `namedValueId, resourceGroupName, serviceName, subscriptionId` | Creates or updates named value. |
| `NamedValue_Delete` | `DELETE` | `If-Match, namedValueId, resourceGroupName, serviceName, subscriptionId` | Deletes specific named value from the API Management service instance. |
| `NamedValue_GetEntityTag` | `EXEC` | `namedValueId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the named value specified by its identifier. |
| `NamedValue_ListValue` | `EXEC` | `namedValueId, resourceGroupName, serviceName, subscriptionId` | Gets the secret of the named value specified by its identifier. |
| `NamedValue_RefreshSecret` | `EXEC` | `namedValueId, resourceGroupName, serviceName, subscriptionId` | Refresh the secret of the named value specified by its identifier. |
| `NamedValue_Update` | `EXEC` | `If-Match, namedValueId, resourceGroupName, serviceName, subscriptionId` | Updates the specific named value. |
