---
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
  - container_registry
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
<tr><td><b>Name</b></td><td><code>agent_pools</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.container_registry.agent_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The resource ID. |
| `name` | `string` | The name of the resource. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | The tags of the resource. |
| `type` | `string` | The type of the resource. |
| `location` | `string` | The location of the resource. This cannot be changed after the resource is created. |
| `properties` | `object` | The properties of agent pool. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AgentPools_Get` | `SELECT` | `agentPoolName, registryName, resourceGroupName, subscriptionId` | Gets the detailed information for a given agent pool. |
| `AgentPools_List` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all the agent pools for a specified container registry. |
| `AgentPools_Create` | `INSERT` | `agentPoolName, registryName, resourceGroupName, subscriptionId` | Creates an agent pool for a container registry with the specified parameters. |
| `AgentPools_Delete` | `DELETE` | `agentPoolName, registryName, resourceGroupName, subscriptionId` | Deletes a specified agent pool resource. |
| `AgentPools_GetQueueStatus` | `EXEC` | `agentPoolName, registryName, resourceGroupName, subscriptionId` | Gets the count of queued runs for a given agent pool. |
| `AgentPools_Update` | `EXEC` | `agentPoolName, registryName, resourceGroupName, subscriptionId` | Updates an agent pool with the specified parameters. |
