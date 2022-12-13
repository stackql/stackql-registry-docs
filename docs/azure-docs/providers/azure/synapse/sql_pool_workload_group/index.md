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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlPoolWorkloadGroup_Get` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workloadGroupName, workspaceName` | Get a Sql pool's workload group. |
| `SqlPoolWorkloadGroup_List` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get list of  Sql pool's workload groups. |
| `SqlPoolWorkloadGroup_CreateOrUpdate` | `INSERT` | `resourceGroupName, sqlPoolName, subscriptionId, workloadGroupName, workspaceName` | Create Or Update a Sql pool's workload group. |
| `SqlPoolWorkloadGroup_Delete` | `DELETE` | `resourceGroupName, sqlPoolName, subscriptionId, workloadGroupName, workspaceName` | Remove Sql pool's workload group. |
