---
title: job_steps
hide_title: false
hide_table_of_contents: false
keywords:
  - job_steps
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
<tr><td><b>Name</b></td><td><code>job_steps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.job_steps</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobSteps_Get` | `SELECT` | `jobAgentName, jobName, resourceGroupName, serverName, stepName, subscriptionId` | Gets a job step in a job's current version. |
| `JobSteps_ListByJob` | `SELECT` | `jobAgentName, jobName, resourceGroupName, serverName, subscriptionId` | Gets all job steps for a job's current version. |
| `JobSteps_ListByVersion` | `SELECT` | `jobAgentName, jobName, jobVersion, resourceGroupName, serverName, subscriptionId` | Gets all job steps in the specified job version. |
| `JobSteps_CreateOrUpdate` | `INSERT` | `jobAgentName, jobName, resourceGroupName, serverName, stepName, subscriptionId` | Creates or updates a job step. This will implicitly create a new job version. |
| `JobSteps_Delete` | `DELETE` | `jobAgentName, jobName, resourceGroupName, serverName, stepName, subscriptionId` | Deletes a job step. This will implicitly create a new job version. |
| `JobSteps_GetByVersion` | `EXEC` | `jobAgentName, jobName, jobVersion, resourceGroupName, serverName, stepName, subscriptionId` | Gets the specified version of a job step. |
