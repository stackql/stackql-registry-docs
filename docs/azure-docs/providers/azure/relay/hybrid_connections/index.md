---
title: hybrid_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - hybrid_connections
  - relay
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
<tr><td><b>Name</b></td><td><code>hybrid_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.relay.hybrid_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `` | Properties of the HybridConnection. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `hybridConnectionName, namespaceName, resourceGroupName, subscriptionId` | Returns the description for the specified hybrid connection. |
| `list_by_namespace` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Lists the hybrid connection within the namespace. |
| `create_or_update` | `INSERT` | `hybridConnectionName, namespaceName, resourceGroupName, subscriptionId` | Creates or updates a service hybrid connection. This operation is idempotent. |
| `delete` | `DELETE` | `hybridConnectionName, namespaceName, resourceGroupName, subscriptionId` | Deletes a hybrid connection. |
| `_list_by_namespace` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Lists the hybrid connection within the namespace. |
| `regenerate_keys` | `EXEC` | `authorizationRuleName, hybridConnectionName, namespaceName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the primary or secondary connection strings to the hybrid connection. |
