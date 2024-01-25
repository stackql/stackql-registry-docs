---
title: sql_pool_workload_group
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_workload_group
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
<tr><td><b>Name</b></td><td><code>sql_pool_workload_group</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_workload_group</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workloadGroupName, workspaceName` | Get a Sql pool's workload group. |
| `list` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get list of  Sql pool's workload groups. |
| `create_or_update` | `INSERT` | `resourceGroupName, sqlPoolName, subscriptionId, workloadGroupName, workspaceName` | Create Or Update a Sql pool's workload group. |
| `delete` | `DELETE` | `resourceGroupName, sqlPoolName, subscriptionId, workloadGroupName, workspaceName` | Remove Sql pool's workload group. |
| `_list` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get list of  Sql pool's workload groups. |
