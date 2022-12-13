---
title: sync_agents
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_agents
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
<tr><td><b>Name</b></td><td><code>sync_agents</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.sync_agents</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SyncAgents_Get` | `SELECT` | `resourceGroupName, serverName, subscriptionId, syncAgentName` | Gets a sync agent. |
| `SyncAgents_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Lists sync agents in a server. |
| `SyncAgents_CreateOrUpdate` | `INSERT` | `resourceGroupName, serverName, subscriptionId, syncAgentName` | Creates or updates a sync agent. |
| `SyncAgents_Delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId, syncAgentName` | Deletes a sync agent. |
| `SyncAgents_GenerateKey` | `EXEC` | `resourceGroupName, serverName, subscriptionId, syncAgentName` | Generates a sync agent key. |
| `SyncAgents_ListLinkedDatabases` | `EXEC` | `resourceGroupName, serverName, subscriptionId, syncAgentName` | Lists databases linked to a sync agent. |
