---
title: sql_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pools
  - synapse
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
<tr><td><b>Name</b></td><td><code>sql_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Properties of a SQL Analytics pool |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get SQL pool properties |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List all SQL pools |
| `create` | `INSERT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Create a SQL pool |
| `delete` | `DELETE` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Delete a SQL pool |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | List all SQL pools |
| `pause` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Pause a SQL pool |
| `resume` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Resume a SQL pool |
| `update` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Apply a partial update to a SQL pool |
