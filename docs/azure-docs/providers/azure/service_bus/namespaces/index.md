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
| `identity` | `object` | Properties to configure User Assigned Identities for Bring your Own Keys |
| `location` | `string` | The Geo-location where the resource lives |
| `properties` | `object` | Properties of the namespace. |
| `sku` | `object` | SKU of the namespace. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Gets a description for the specified namespace. |
| `list` | `SELECT` | `subscriptionId` | Gets all the available namespaces within the subscription, irrespective of the resource groups. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets the available namespaces within a resource group. |
| `create_or_update` | `INSERT` | `namespaceName, resourceGroupName, subscriptionId` | Creates or updates a service namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent. |
| `delete` | `DELETE` | `namespaceName, resourceGroupName, subscriptionId` | Deletes an existing namespace. This operation also removes all associated resources under the namespace. |
| `_list` | `EXEC` | `subscriptionId` | Gets all the available namespaces within the subscription, irrespective of the resource groups. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets the available namespaces within a resource group. |
| `check_name_availability` | `EXEC` | `subscriptionId, data__name` | Check the give namespace name availability. |
| `regenerate_keys` | `EXEC` | `authorizationRuleName, namespaceName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the primary or secondary connection strings for the namespace. |
| `update` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Updates a service namespace. Once created, this namespace's resource manifest is immutable. This operation is idempotent. |
