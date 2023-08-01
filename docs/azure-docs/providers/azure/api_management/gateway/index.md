---
title: gateway
hide_title: false
hide_table_of_contents: false
keywords:
  - gateway
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
<tr><td><b>Name</b></td><td><code>gateway</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.gateway</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Fully qualified resource ID for the resource. Ex - /subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125; |
| `name` | `string` | The name of the resource |
| `properties` | `object` | Properties of the Gateway contract. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Gateway_Get` | `SELECT` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Gets the details of the Gateway specified by its identifier. |
| `Gateway_ListByService` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists a collection of gateways registered with service instance. |
| `Gateway_CreateOrUpdate` | `INSERT` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Creates or updates a Gateway to be used in Api Management instance. |
| `Gateway_Delete` | `DELETE` | `If-Match, gatewayId, resourceGroupName, serviceName, subscriptionId` | Deletes specific Gateway. |
| `Gateway_GenerateToken` | `EXEC` | `gatewayId, resourceGroupName, serviceName, subscriptionId, data__expiry, data__keyType` | Gets the Shared Access Authorization Token for the gateway. |
| `Gateway_GetEntityTag` | `EXEC` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Gets the entity state (Etag) version of the Gateway specified by its identifier. |
| `Gateway_ListKeys` | `EXEC` | `gatewayId, resourceGroupName, serviceName, subscriptionId` | Retrieves gateway keys. |
| `Gateway_RegenerateKey` | `EXEC` | `gatewayId, resourceGroupName, serviceName, subscriptionId, data__keyType` | Regenerates specified gateway key invalidating any tokens created with it. |
| `Gateway_Update` | `EXEC` | `If-Match, gatewayId, resourceGroupName, serviceName, subscriptionId` | Updates the details of the gateway specified by its identifier. |
