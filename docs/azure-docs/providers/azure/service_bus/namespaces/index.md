---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - service_bus
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
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.service_bus.namespaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
| `identity` | `object` | Properties to configure User Assigned Identities for Bring your Own Keys |
| `location` | `string` | The Geo-location where the resource lives |
| `properties` | `object` | Properties of the namespace. |
| `sku` | `object` | SKU of the namespace. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Namespaces_Get` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets a description for the specified namespace. |
| `Namespaces_List` | `SELECT` | `subscriptionId` | Gets all the available namespaces within the subscription, irrespective of the resource groups. |
| `Namespaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the available namespaces within a resource group. |
| `Namespaces_CreateOrUpdate` | `INSERT` | `namespaceName, resourceGroupName, subscriptionId` | Creates or updates a service namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent. |
| `Namespaces_Delete` | `DELETE` | `namespaceName, resourceGroupName, subscriptionId` | Deletes an existing namespace. This operation also removes all associated resources under the namespace. |
| `Namespaces_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name` | Check the give namespace name availability. |
| `Namespaces_CreateOrUpdateAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Creates or updates an authorization rule for a namespace. |
| `Namespaces_CreateOrUpdateNetworkRuleSet` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Create or update NetworkRuleSet for a Namespace. |
| `Namespaces_DeleteAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Deletes a namespace authorization rule. |
| `Namespaces_GetAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Gets an authorization rule for a namespace by rule name. |
| `Namespaces_GetNetworkRuleSet` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Gets NetworkRuleSet for a Namespace. |
| `Namespaces_ListAuthorizationRules` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Gets the authorization rules for a namespace. |
| `Namespaces_ListKeys` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Gets the primary and secondary connection strings for the namespace. |
| `Namespaces_ListNetworkRuleSets` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Gets list of NetworkRuleSet for a Namespace. |
| `Namespaces_RegenerateKeys` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the primary or secondary connection strings for the namespace. |
| `Namespaces_Update` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Updates a service namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent. |
