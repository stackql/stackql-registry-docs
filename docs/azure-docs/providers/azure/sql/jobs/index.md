---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.jobs</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobAgentName, jobName, resourceGroupName, serverName, subscriptionId` | Gets a job. |
| `list_by_agent` | `SELECT` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Gets a list of jobs. |
| `create_or_update` | `INSERT` | `jobAgentName, jobName, resourceGroupName, serverName, subscriptionId` | Creates or updates a job. |
| `delete` | `DELETE` | `jobAgentName, jobName, resourceGroupName, serverName, subscriptionId` | Deletes a job. |
| `_list_by_agent` | `EXEC` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Gets a list of jobs. |
