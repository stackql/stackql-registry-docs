---
title: job_target_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_target_executions
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
<tr><td><b>Name</b></td><td><code>job_target_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.job_target_executions</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobTargetExecutions_Get` | `SELECT` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, stepName, subscriptionId, targetId` | Gets a target execution. |
| `JobTargetExecutions_ListByJobExecution` | `SELECT` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId` | Lists target executions for all steps of a job execution. |
| `JobTargetExecutions_ListByStep` | `SELECT` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, stepName, subscriptionId` | Lists the target executions of a job step execution. |
