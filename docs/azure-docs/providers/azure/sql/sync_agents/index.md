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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serverName, subscriptionId, syncAgentName` | Gets a sync agent. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Lists sync agents in a server. |
| `create_or_update` | `INSERT` | `resourceGroupName, serverName, subscriptionId, syncAgentName` | Creates or updates a sync agent. |
| `delete` | `DELETE` | `resourceGroupName, serverName, subscriptionId, syncAgentName` | Deletes a sync agent. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Lists sync agents in a server. |
| `generate_key` | `EXEC` | `resourceGroupName, serverName, subscriptionId, syncAgentName` | Generates a sync agent key. |
