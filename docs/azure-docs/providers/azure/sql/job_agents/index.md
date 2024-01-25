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
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of a job agent. |
| `sku` | `object` | An ARM Resource SKU. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Gets a job agent. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of job agents in a server. |
| `create_or_update` | `INSERT` | `jobAgentName, resourceGroupName, serverName, subscriptionId, data__location` | Creates or updates a job agent. |
| `delete` | `DELETE` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Deletes a job agent. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets a list of job agents in a server. |
| `update` | `EXEC` | `jobAgentName, resourceGroupName, serverName, subscriptionId` | Updates a job agent. |
