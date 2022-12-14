---
title: job_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - job_agents
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
<tr><td><b>Name</b></td><td><code>job_agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.job_agents</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a job agent. |
| `sku` | `object` | An ARM Resource SKU. |
| `tags` | `object` | Resource tags. |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `JobAgents_Get` | `SELECT` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Gets a job agent. |
| `JobAgents_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of job agents in a server. |
| `JobAgents_CreateOrUpdate` | `INSERT` | `jobAgentName, resourceGroupName, serverName, subscriptionId, data__location` | Creates or updates a job agent. |
| `JobAgents_Delete` | `DELETE` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Deletes a job agent. |
| `JobAgents_Update` | `EXEC` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Updates a job agent. |
