---
title: hybrid_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_connections
  - relay
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>hybrid_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.relay.hybrid_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `` | Properties of the HybridConnection. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `HybridConnections_Get` | `SELECT` | `hybridConnectionName, namespaceName, resourceGroupName, subscriptionId` | Returns the description for the specified hybrid connection. |
| `HybridConnections_ListByNamespace` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Lists the hybrid connection within the namespace. |
| `HybridConnections_CreateOrUpdate` | `INSERT` | `hybridConnectionName, namespaceName, resourceGroupName, subscriptionId` | Creates or updates a service hybrid connection. This operation is idempotent. |
| `HybridConnections_Delete` | `DELETE` | `hybridConnectionName, namespaceName, resourceGroupName, subscriptionId` | Deletes a hybrid connection. |
| `HybridConnections_CreateOrUpdateAuthorizationRule` | `EXEC` | `authorizationRuleName, hybridConnectionName, namespaceName, resourceGroupName, subscriptionId` | Creates or updates an authorization rule for a hybrid connection. |
| `HybridConnections_DeleteAuthorizationRule` | `EXEC` | `authorizationRuleName, hybridConnectionName, namespaceName, resourceGroupName, subscriptionId` | Deletes a hybrid connection authorization rule. |
| `HybridConnections_GetAuthorizationRule` | `EXEC` | `authorizationRuleName, hybridConnectionName, namespaceName, resourceGroupName, subscriptionId` | Hybrid connection authorization rule for a hybrid connection by name. |
| `HybridConnections_ListAuthorizationRules` | `EXEC` | `hybridConnectionName, namespaceName, resourceGroupName, subscriptionId` | Authorization rules for a hybrid connection. |
| `HybridConnections_ListKeys` | `EXEC` | `authorizationRuleName, hybridConnectionName, namespaceName, resourceGroupName, subscriptionId` | Primary and secondary connection strings to the hybrid connection. |
| `HybridConnections_RegenerateKeys` | `EXEC` | `authorizationRuleName, hybridConnectionName, namespaceName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the primary or secondary connection strings to the hybrid connection. |
