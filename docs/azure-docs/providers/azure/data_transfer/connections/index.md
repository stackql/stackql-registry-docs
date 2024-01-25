---
title: connections
hide_title: false
hide_table_of_contents: false
keywords:
  - connections
  - data_transfer
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
<tr><td><b>Name</b></td><td><code>connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_transfer.connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of connection |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectionName, resourceGroupName, subscriptionId` | Gets connection resource. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Gets connections in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Gets connections in a subscription. |
| `create_or_update` | `INSERT` | `connectionName, resourceGroupName, subscriptionId, data__location` | Creates or updates the connection resource. |
| `delete` | `DELETE` | `connectionName, resourceGroupName, subscriptionId` | Deletes the connection resource. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Gets connections in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Gets connections in a subscription. |
| `link` | `EXEC` | `connectionName, resourceGroupName, subscriptionId, data__id` | Links the connection to its pending connection. |
| `update` | `EXEC` | `connectionName, resourceGroupName, subscriptionId` | Updates the connection resource. |
