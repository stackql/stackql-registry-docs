---
title: workload_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_groups
  - sql
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
<tr><td><b>Name</b></td><td><code>workload_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.workload_groups</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName` | Gets a workload group |
| `list_by_database` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets the list of workload groups |
| `create_or_update` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName` | Creates or updates a workload group. |
| `delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName` | Deletes a workload group. |
| `_list_by_database` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets the list of workload groups |
