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
| `id` | `string` | Fully qualified resource ID for the resource. E.g. "/subscriptions/&#123;subscriptionId&#125;/resourceGroups/&#123;resourceGroupName&#125;/providers/&#123;resourceProviderNamespace&#125;/&#123;resourceType&#125;/&#123;resourceName&#125;" |
| `name` | `string` | The name of the resource |
| `properties` | `object` | The properties of agent pool. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `type` | `string` | The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts" |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `agentPoolName, registryName, resourceGroupName, subscriptionId` | Gets the detailed information for a given agent pool. |
| `list` | `SELECT` | `registryName, resourceGroupName, subscriptionId` | Lists all the agent pools for a specified container registry. |
| `create` | `INSERT` | `agentPoolName, registryName, resourceGroupName, subscriptionId` | Creates an agent pool for a container registry with the specified parameters. |
| `delete` | `DELETE` | `agentPoolName, registryName, resourceGroupName, subscriptionId` | Deletes a specified agent pool resource. |
| `_list` | `EXEC` | `registryName, resourceGroupName, subscriptionId` | Lists all the agent pools for a specified container registry. |
| `update` | `EXEC` | `agentPoolName, registryName, resourceGroupName, subscriptionId` | Updates an agent pool with the specified parameters. |
