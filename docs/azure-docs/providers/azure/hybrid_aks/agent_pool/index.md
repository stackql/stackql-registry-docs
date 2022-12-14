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
| `id` | `string` | Resource Id |
| `name` | `string` | Resource Name |
| `type` | `string` | Resource Type |
| `extendedLocation` | `object` |  |
| `location` | `string` | The resource location |
| `properties` | `object` |  |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `agentPool_Get` | `SELECT` | `agentPoolName, provisionedClustersName, resourceGroupName, subscriptionId` | Gets the agent pool in the Hybrid AKS provisioned cluster |
| `agentPool_ListByProvisionedCluster` | `SELECT` | `provisionedClustersName, resourceGroupName, subscriptionId` | Gets the agent pools in the Hybrid AKS provisioned cluster |
| `agentPool_CreateOrUpdate` | `INSERT` | `agentPoolName, provisionedClustersName, resourceGroupName, subscriptionId` | Creates the agent pool in the Hybrid AKS provisioned cluster |
| `agentPool_Delete` | `DELETE` | `agentPoolName, provisionedClustersName, resourceGroupName, subscriptionId` | Deletes the agent pool in the Hybrid AKS provisioned cluster |
| `agentPool_Update` | `EXEC` | `agentPoolName, provisionedClustersName, resourceGroupName, subscriptionId` | Updates the agent pool in the Hybrid AKS provisioned cluster |
