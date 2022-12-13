---
title: user
hide_title: false
hide_table_of_contents: false
keywords:
  - user
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
<tr><td><b>Name</b></td><td><code>user</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.user</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | User profile. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `User_Get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, userId` | Gets the details of the user specified by its identifier. |
| `User_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of registered users in the specified service instance. |
| `User_CreateOrUpdate` | `INSERT` | `resourceGroupName, serviceName, subscriptionId, userId` | Creates or Updates a user. |
| `User_Delete` | `DELETE` | `If-Match, resourceGroupName, serviceName, subscriptionId, userId` | Deletes specific user. |
| `User_GenerateSsoUrl` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, userId` | Retrieves a redirection URL containing an authentication token for signing a given user into the developer portal. |
| `User_GetEntityTag` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, userId` | Gets the entity state (Etag) version of the user specified by its identifier. |
| `User_GetSharedAccessToken` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, userId` | Gets the Shared Access Authorization Token for the User. |
| `User_Update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId, userId` | Updates the details of the user specified by its identifier. |
