---
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
  - nexus
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
<tr><td><b>Id</b></td><td><code>azure.nexus.agent_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` |  |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` |  |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `agentPoolName, kubernetesClusterName, resourceGroupName, subscriptionId` | Get properties of the provided Kubernetes cluster agent pool. |
| `list_by_kubernetes_cluster` | `SELECT` | `kubernetesClusterName, resourceGroupName, subscriptionId` | Get a list of agent pools for the provided Kubernetes cluster. |
| `create_or_update` | `INSERT` | `agentPoolName, kubernetesClusterName, resourceGroupName, subscriptionId, data__properties` | Create a new Kubernetes cluster agent pool or update the properties of the existing one. |
| `delete` | `DELETE` | `agentPoolName, kubernetesClusterName, resourceGroupName, subscriptionId` | Delete the provided Kubernetes cluster agent pool. |
| `_list_by_kubernetes_cluster` | `EXEC` | `kubernetesClusterName, resourceGroupName, subscriptionId` | Get a list of agent pools for the provided Kubernetes cluster. |
| `update` | `EXEC` | `agentPoolName, kubernetesClusterName, resourceGroupName, subscriptionId` | Patch the properties of the provided Kubernetes cluster agent pool, or update the tags associated with the Kubernetes cluster agent pool. Properties and tag updates can be done independently. |
