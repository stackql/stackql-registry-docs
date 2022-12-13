---
title: job_executions
hide_title: false
hide_table_of_contents: false
keywords:
  - job_executions
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
<tr><td><b>Name</b></td><td><code>job_executions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.job_executions</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobExecutions_Get` | `SELECT` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId` | Gets a job execution. |
| `JobExecutions_ListByAgent` | `SELECT` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Lists all executions in a job agent. |
| `JobExecutions_ListByJob` | `SELECT` | `jobAgentName, jobName, resourceGroupName, serverName, subscriptionId` | Lists a job's executions. |
| `JobExecutions_Create` | `INSERT` | `jobAgentName, jobName, resourceGroupName, serverName, subscriptionId` | Starts an elastic job execution. |
| `JobExecutions_CreateOrUpdate` | `INSERT` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId` | Creates or updates a job execution. |
| `JobExecutions_Cancel` | `EXEC` | `jobAgentName, jobExecutionId, jobName, resourceGroupName, serverName, subscriptionId` | Requests cancellation of a job execution. |
