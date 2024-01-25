---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
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
<tr><td><b>Name</b></td><td><code>namespaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.relay.namespaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the namespace. |
| `sku` | `object` | The resource model definition representing SKU |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Returns the description for the specified namespace. |
| `list` | `SELECT` | `subscriptionId` | Lists all the available namespaces within the subscription regardless of the resourceGroups. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the available namespaces within the ResourceGroup. |
| `create_or_update` | `INSERT` | `namespaceName, resourceGroupName, subscriptionId` | Create Azure Relay namespace. |
| `delete` | `DELETE` | `namespaceName, resourceGroupName, subscriptionId` | Deletes an existing namespace. This operation also removes all associated resources under the namespace. |
| `_list` | `EXEC` | `subscriptionId` | Lists all the available namespaces within the subscription regardless of the resourceGroups. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the available namespaces within the ResourceGroup. |
| `check_name_availability` | `EXEC` | `subscriptionId, data__name` | Check the specified namespace name availability. |
| `regenerate_keys` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the primary or secondary connection strings to the namespace. |
| `update` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Creates or updates a namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent. |
