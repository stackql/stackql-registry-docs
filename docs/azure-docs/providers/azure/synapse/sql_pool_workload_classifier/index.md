---
title: sql_pool_workload_classifier
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_workload_classifier
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
<tr><td><b>Name</b></td><td><code>sql_pool_workload_classifier</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_workload_classifier</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workloadClassifierName, workloadGroupName, workspaceName` | Get a workload classifier of Sql pool's workload group. |
| `list` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workloadGroupName, workspaceName` | Get list of  Sql pool's workload classifier for workload groups. |
| `create_or_update` | `INSERT` | `resourceGroupName, sqlPoolName, subscriptionId, workloadClassifierName, workloadGroupName, workspaceName` | Create Or Update workload classifier for a Sql pool's workload group. |
| `delete` | `DELETE` | `resourceGroupName, sqlPoolName, subscriptionId, workloadClassifierName, workloadGroupName, workspaceName` | Remove workload classifier of a Sql pool's workload group. |
| `_list` | `EXEC` | `resourceGroupName, sqlPoolName, subscriptionId, workloadGroupName, workspaceName` | Get list of  Sql pool's workload classifier for workload groups. |
