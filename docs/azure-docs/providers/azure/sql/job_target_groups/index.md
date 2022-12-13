---
title: job_target_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - job_target_groups
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
<tr><td><b>Name</b></td><td><code>job_target_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.job_target_groups</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobTargetGroups_Get` | `SELECT` | `jobAgentName, resourceGroupName, serverName, subscriptionId, targetGroupName` | Gets a target group. |
| `JobTargetGroups_ListByAgent` | `SELECT` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Gets all target groups in an agent. |
| `JobTargetGroups_CreateOrUpdate` | `INSERT` | `jobAgentName, resourceGroupName, serverName, subscriptionId, targetGroupName` | Creates or updates a target group. |
| `JobTargetGroups_Delete` | `DELETE` | `jobAgentName, resourceGroupName, serverName, subscriptionId, targetGroupName` | Deletes a target group. |
