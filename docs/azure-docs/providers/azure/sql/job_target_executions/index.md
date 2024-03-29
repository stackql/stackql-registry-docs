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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, stepName, subscriptionId, targetId` | Gets a target execution. |
| `list_by_job_execution` | `SELECT` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId` | Lists target executions for all steps of a job execution. |
| `list_by_step` | `SELECT` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, stepName, subscriptionId` | Lists the target executions of a job step execution. |
| `_list_by_job_execution` | `EXEC` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId` | Lists target executions for all steps of a job execution. |
| `_list_by_step` | `EXEC` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, stepName, subscriptionId` | Lists the target executions of a job step execution. |
