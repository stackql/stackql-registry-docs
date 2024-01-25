---
title: agent_pool
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pool
  - hybrid_aks
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
<tr><td><b>Name</b></td><td><code>agent_pool</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.hybrid_aks.agent_pool</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | Extended location pointing to the underlying infrastructure |
| `properties` | `object` | Properties of the agent pool resource |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `agentPoolName, connectedClusterResourceUri` | Gets the specified agent pool in the provisioned cluster |
| `list_by_provisioned_cluster` | `SELECT` | `connectedClusterResourceUri` | Gets the list of agent pools in the specified provisioned cluster |
| `create_or_update` | `INSERT` | `agentPoolName, connectedClusterResourceUri` | Creates or updates the agent pool in the provisioned cluster |
| `delete` | `DELETE` | `agentPoolName, connectedClusterResourceUri` | Deletes the specified agent pool in the provisioned cluster |
| `_list_by_provisioned_cluster` | `EXEC` | `connectedClusterResourceUri` | Gets the list of agent pools in the specified provisioned cluster |
