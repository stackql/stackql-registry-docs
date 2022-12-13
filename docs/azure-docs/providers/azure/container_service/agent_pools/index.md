---
title: agent_pools
hide_title: false
hide_table_of_contents: false
keywords:
  - agent_pools
  - container_service
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
<tr><td><b>Id</b></td><td><code>azure.container_service.agent_pools</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | The name of the resource that is unique within a resource group. This name can be used to access the resource. |
| `properties` | `object` | Properties for the container service agent pool profile. |
| `type` | `string` | Resource type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AgentPools_Get` | `SELECT` | `agentPoolName, resourceGroupName, resourceName, subscriptionId` |  |
| `AgentPools_List` | `SELECT` | `resourceGroupName, resourceName, subscriptionId` |  |
| `AgentPools_CreateOrUpdate` | `INSERT` | `agentPoolName, resourceGroupName, resourceName, subscriptionId` |  |
| `AgentPools_Delete` | `DELETE` | `agentPoolName, resourceGroupName, resourceName, subscriptionId` |  |
| `AgentPools_AbortLatestOperation` | `EXEC` | `agentPoolName, resourceGroupName, resourceName, subscriptionId` | Aborting last running operation on agent pool. We return a 204 no content code here to indicate that the operation has been accepted and an abort will be attempted but is not guaranteed to complete successfully. Please look up the provisioning state of the agent pool to keep track of whether it changes to Canceled. A canceled provisioning state indicates that the abort was successful |
| `AgentPools_GetAvailableAgentPoolVersions` | `EXEC` | `resourceGroupName, resourceName, subscriptionId` | See [supported Kubernetes versions](https://docs.microsoft.com/azure/aks/supported-kubernetes-versions) for more details about the version lifecycle. |
| `AgentPools_GetUpgradeProfile` | `EXEC` | `agentPoolName, resourceGroupName, resourceName, subscriptionId` |  |
| `AgentPools_UpgradeNodeImageVersion` | `EXEC` | `agentPoolName, resourceGroupName, resourceName, subscriptionId` | Upgrading the node image version of an agent pool applies the newest OS and runtime updates to the nodes. AKS provides one new image per week with the latest updates. For more details on node image versions, see: https://docs.microsoft.com/azure/aks/node-image-upgrade |
