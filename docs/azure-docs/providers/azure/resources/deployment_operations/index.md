---
title: deployment_operations
hide_title: false
hide_table_of_contents: false
keywords:
  - deployment_operations
  - resources
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
<tr><td><b>Name</b></td><td><code>deployment_operations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.resources.deployment_operations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Full deployment operation ID. |
| `operationId` | `string` | Deployment operation ID. |
| `properties` | `object` | Deployment operation properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DeploymentOperations_Get` | `SELECT` | `deploymentName, operationId, resourceGroupName, subscriptionId` | Gets a deployments operation. |
| `DeploymentOperations_List` | `SELECT` | `deploymentName, resourceGroupName, subscriptionId` | Gets all deployments operations for a deployment. |
| `DeploymentOperations_GetAtManagementGroupScope` | `EXEC` | `deploymentName, groupId, operationId` | Gets a deployments operation. |
| `DeploymentOperations_GetAtScope` | `EXEC` | `deploymentName, operationId, scope` | Gets a deployments operation. |
| `DeploymentOperations_GetAtSubscriptionScope` | `EXEC` | `deploymentName, operationId, subscriptionId` | Gets a deployments operation. |
| `DeploymentOperations_GetAtTenantScope` | `EXEC` | `deploymentName, operationId` | Gets a deployments operation. |
| `DeploymentOperations_ListAtManagementGroupScope` | `EXEC` | `deploymentName, groupId` | Gets all deployments operations for a deployment. |
| `DeploymentOperations_ListAtScope` | `EXEC` | `deploymentName, scope` | Gets all deployments operations for a deployment. |
| `DeploymentOperations_ListAtSubscriptionScope` | `EXEC` | `deploymentName, subscriptionId` | Gets all deployments operations for a deployment. |
| `DeploymentOperations_ListAtTenantScope` | `EXEC` | `deploymentName` | Gets all deployments operations for a deployment. |
