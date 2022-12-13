---
title: diagnostic
hide_title: false
hide_table_of_contents: false
keywords:
  - diagnostic
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
<tr><td><b>Name</b></td><td><code>diagnostic</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.diagnostic</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | Diagnostic Entity Properties |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Diagnostic_Get` | `SELECT` | `diagnosticId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the Diagnostic specified by its identifier. |
| `Diagnostic_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists all diagnostics of the API Management service instance. |
| `Diagnostic_CreateOrUpdate` | `INSERT` | `diagnosticId, resourceGroupName, serviceName, subscriptionId` | Creates a new Diagnostic or updates an existing one. |
| `Diagnostic_Delete` | `DELETE` | `If-Match, diagnosticId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified Diagnostic. |
| `Diagnostic_GetEntityTag` | `EXEC` | `diagnosticId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the Diagnostic specified by its identifier. |
| `Diagnostic_Update` | `EXEC` | `If-Match, diagnosticId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the Diagnostic specified by its identifier. |
