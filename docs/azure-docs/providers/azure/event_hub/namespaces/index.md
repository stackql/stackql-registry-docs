---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - event_hub
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
<tr><td><b>Id</b></td><td><code>azure.event_hub.namespaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `sku` | `object` | SKU parameters supplied to the create namespace operation |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Properties to configure Identity for Bring your Own Keys |
| `location` | `string` | Resource location. |
| `properties` | `` | Namespace properties supplied for create namespace operation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Namespaces_Get` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets the description of the specified namespace. |
| `Namespaces_List` | `SELECT` | `subscriptionId` | Lists all the available Namespaces within a subscription, irrespective of the resource groups. |
| `Namespaces_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists the available Namespaces within a resource group. |
| `Namespaces_CreateOrUpdate` | `INSERT` | `namespaceName, resourceGroupName, subscriptionId` | Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent. |
| `Namespaces_Delete` | `DELETE` | `namespaceName, resourceGroupName, subscriptionId` | Deletes an existing namespace. This operation also removes all associated resources under the namespace. |
| `Namespaces_CheckNameAvailability` | `EXEC` | `subscriptionId, data__name` | Check the give Namespace name availability. |
| `Namespaces_CreateOrUpdateAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Creates or updates an AuthorizationRule for a Namespace. |
| `Namespaces_CreateOrUpdateNetworkRuleSet` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Create or update NetworkRuleSet for a Namespace. |
| `Namespaces_DeleteAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Deletes an AuthorizationRule for a Namespace. |
| `Namespaces_GetAuthorizationRule` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Gets an AuthorizationRule for a Namespace by rule name. |
| `Namespaces_GetNetworkRuleSet` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Gets NetworkRuleSet for a Namespace. |
| `Namespaces_ListAuthorizationRules` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Gets a list of authorization rules for a Namespace. |
| `Namespaces_ListKeys` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId` | Gets the primary and secondary connection strings for the Namespace. |
| `Namespaces_ListNetworkRuleSet` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Gets NetworkRuleSet for a Namespace. |
| `Namespaces_RegenerateKeys` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the primary or secondary connection strings for the specified Namespace. |
| `Namespaces_Update` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent. |
