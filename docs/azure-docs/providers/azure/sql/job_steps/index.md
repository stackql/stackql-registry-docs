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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobAgentName, jobName, resourceGroupName, serverName, stepName, subscriptionId` | Gets a job step in a job's current version. |
| `list_by_job` | `SELECT` | `jobAgentName, jobName, resourceGroupName, serverName, subscriptionId` | Gets all job steps for a job's current version. |
| `list_by_version` | `SELECT` | `jobAgentName, jobName, jobVersion, resourceGroupName, serverName, subscriptionId` | Gets all job steps in the specified job version. |
| `create_or_update` | `INSERT` | `jobAgentName, jobName, resourceGroupName, serverName, stepName, subscriptionId` | Creates or updates a job step. This will implicitly create a new job version. |
| `delete` | `DELETE` | `jobAgentName, jobName, resourceGroupName, serverName, stepName, subscriptionId` | Deletes a job step. This will implicitly create a new job version. |
| `_list_by_job` | `EXEC` | `jobAgentName, jobName, resourceGroupName, serverName, subscriptionId` | Gets all job steps for a job's current version. |
| `_list_by_version` | `EXEC` | `jobAgentName, jobName, jobVersion, resourceGroupName, serverName, subscriptionId` | Gets all job steps in the specified job version. |
| `get_by_version` | `EXEC` | `jobAgentName, jobName, jobVersion, resourceGroupName, serverName, stepName, subscriptionId` | Gets the specified version of a job step. |
