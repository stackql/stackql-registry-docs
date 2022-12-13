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
| `properties` | `object` | Properties of a SQL Analytics pool |
| `sku` | `object` | The resource model definition representing SKU |
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlPools_Get` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get SQL pool properties |
| `SqlPools_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List all SQL pools |
| `SqlPools_Create` | `INSERT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Create a SQL pool |
| `SqlPools_Delete` | `DELETE` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Delete a SQL pool |
| `SqlPools_Pause` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Pause a SQL pool |
| `SqlPools_Rename` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName, data__id` | Rename a SQL pool. |
| `SqlPools_Resume` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Resume a SQL pool |
| `SqlPools_Update` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Apply a partial update to a SQL pool |
