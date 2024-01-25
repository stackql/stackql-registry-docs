---
title: workspace_managed_sql_server_recoverable_sql_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_recoverable_sql_pools
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
<tr><td><b>Name</b></td><td><code>workspace_managed_sql_server_recoverable_sql_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.workspace_managed_sql_server_recoverable_sql_pools</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, sqlPoolName, subscriptionId, workspaceName` | Get recoverable sql pools for workspace managed sql server. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Get list of recoverable sql pools for workspace managed sql server. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Get list of recoverable sql pools for workspace managed sql server. |
