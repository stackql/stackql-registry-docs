---
title: api_diagnostic
hide_title: false
hide_table_of_contents: false
keywords:
  - api_diagnostic
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
<tr><td><b>Name</b></td><td><code>api_diagnostic</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.api_diagnostic</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Diagnostic Entity Properties |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ApiDiagnostic_Get` | `SELECT` | `apiId, diagnosticId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the Diagnostic for an API specified by its identifier. |
| `ApiDiagnostic_ListByService` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId` | Lists all diagnostics of an API. |
| `ApiDiagnostic_CreateOrUpdate` | `INSERT` | `apiId, diagnosticId, resourceGroupName, serviceName, subscriptionId` | Creates a new Diagnostic for an API or updates an existing one. |
| `ApiDiagnostic_Delete` | `DELETE` | `If-Match, apiId, diagnosticId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified Diagnostic from an API. |
| `ApiDiagnostic_GetEntityTag` | `EXEC` | `apiId, diagnosticId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the Diagnostic for an API specified by its identifier. |
| `ApiDiagnostic_Update` | `EXEC` | `If-Match, apiId, diagnosticId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the Diagnostic for an API specified by its identifier. |
