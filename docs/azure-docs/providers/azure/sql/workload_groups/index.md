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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkloadGroups_Get` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName` | Gets a workload group |
| `WorkloadGroups_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets the list of workload groups |
| `WorkloadGroups_CreateOrUpdate` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName` | Creates or updates a workload group. |
| `WorkloadGroups_Delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId, workloadGroupName` | Deletes a workload group. |
