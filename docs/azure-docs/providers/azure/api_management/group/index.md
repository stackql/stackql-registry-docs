---
title: group
hide_title: false
hide_table_of_contents: false
keywords:
  - group
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
<tr><td><b>Name</b></td><td><code>group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.group</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
| `properties` | `object` | Group contract Properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Group_Get` | `SELECT` | `groupId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the group specified by its identifier. |
| `Group_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of groups defined within a service instance. |
| `Group_CreateOrUpdate` | `INSERT` | `groupId, resourceGroupName, serviceName, subscriptionId` | Creates or Updates a group. |
| `Group_Delete` | `DELETE` | `If-Match, groupId, resourceGroupName, serviceName, subscriptionId` | Deletes specific group of the API Management service instance. |
| `Group_GetEntityTag` | `EXEC` | `groupId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the group specified by its identifier. |
| `Group_Update` | `EXEC` | `If-Match, groupId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the group specified by its identifier. |
