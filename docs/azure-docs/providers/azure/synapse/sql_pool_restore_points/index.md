---
title: sql_pool_restore_points
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_restore_points
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
<tr><td><b>Name</b></td><td><code>sql_pool_restore_points</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_restore_points</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of a database restore point |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlPoolRestorePoints_Get` | `SELECT` | `resourceGroupName, restorePointName, sqlPoolName, subscriptionId, workspaceName` | Gets a restore point. |
| `SqlPoolRestorePoints_List` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get SQL pool backup information |
| `SqlPoolRestorePoints_Create` | `INSERT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName, data__restorePointLabel` | Creates a restore point for a data warehouse. |
| `SqlPoolRestorePoints_Delete` | `DELETE` | `resourceGroupName, restorePointName, sqlPoolName, subscriptionId, workspaceName` | Deletes a restore point. |
