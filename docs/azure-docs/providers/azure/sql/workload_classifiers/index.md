---
title: workload_classifiers
hide_title: false
hide_table_of_contents: false
keywords:
  - workload_classifiers
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
<tr><td><b>Name</b></td><td><code>workload_classifiers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.workload_classifiers</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadClassifierName, workloadGroupName` | Gets a workload classifier |
| `list_by_workload_group` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName` | Gets the list of workload classifiers for a workload group |
| `create_or_update` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadClassifierName, workloadGroupName` | Creates or updates a workload classifier. |
| `delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadClassifierName, workloadGroupName` | Deletes a workload classifier. |
| `_list_by_workload_group` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName` | Gets the list of workload classifiers for a workload group |
