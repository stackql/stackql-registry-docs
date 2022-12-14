---
title: backend
hide_title: false
hide_table_of_contents: false
keywords:
  - backend
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
<tr><td><b>Name</b></td><td><code>backend</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.backend</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | Parameters supplied to the Create Backend operation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Backend_Get` | `SELECT` | `backendId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the backend specified by its identifier. |
| `Backend_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of backends in the specified service instance. |
| `Backend_CreateOrUpdate` | `INSERT` | `backendId, resourceGroupName, serviceName, subscriptionId` | Creates or Updates a backend. |
| `Backend_Delete` | `DELETE` | `If-Match, backendId, resourceGroupName, serviceName, subscriptionId` | Deletes the specified backend. |
| `Backend_GetEntityTag` | `EXEC` | `backendId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the backend specified by its identifier. |
| `Backend_Reconnect` | `EXEC` | `backendId, resourceGroupName, serviceName, subscriptionId` | Notifies the APIM proxy to create a new connection to the backend after the specified timeout. If no timeout was specified, timeout of 2 minutes is used. |
| `Backend_Update` | `EXEC` | `If-Match, backendId, resourceGroupName, serviceName, subscriptionId` | Updates an existing backend. |
