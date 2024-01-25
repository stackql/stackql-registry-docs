---
title: namespaces
hide_title: false
hide_table_of_contents: false
keywords:
  - namespaces
  - event_grid
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
<tr><td><b>Id</b></td><td><code>azure.event_grid.namespaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | The identity information for the resource. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of the namespace resource. |
| `sku` | `object` | Represents available Sku pricing tiers. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `namespaceName, resourceGroupName, subscriptionId` | Get properties of a namespace. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | List all the namespaces under a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | List all the namespaces under an Azure subscription. |
| `create_or_update` | `INSERT` | `namespaceName, resourceGroupName, subscriptionId` | Asynchronously creates or updates a new namespace with the specified parameters. |
| `delete` | `DELETE` | `namespaceName, resourceGroupName, subscriptionId` | Delete existing namespace. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | List all the namespaces under a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | List all the namespaces under an Azure subscription. |
| `regenerate_key` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId, data__keyName` | Regenerate a shared access key for a namespace. |
| `update` | `EXEC` | `namespaceName, resourceGroupName, subscriptionId` | Asynchronously updates a namespace with the specified parameters. |
