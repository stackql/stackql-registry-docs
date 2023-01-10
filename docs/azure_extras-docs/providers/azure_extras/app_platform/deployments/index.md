---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - app_platform
  - azure_extras    
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
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.app_platform.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Deployment resource properties payload |
| `sku` | `object` | Sku of Azure Spring Apps |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Deployments_Get` | `SELECT` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Get a Deployment and its properties. |
| `Deployments_List` | `SELECT` | `appName, resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in an App. |
| `Deployments_CreateOrUpdate` | `INSERT` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Create a new Deployment or update an exiting Deployment. |
| `Deployments_Delete` | `DELETE` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Operation to delete a Deployment. |
| `Deployments_DisableRemoteDebugging` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Disable remote debugging. |
| `Deployments_EnableRemoteDebugging` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Enable remote debugging. |
| `Deployments_GenerateHeapDump` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Generate Heap Dump |
| `Deployments_GenerateThreadDump` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Generate Thread Dump |
| `Deployments_GetLogFileUrl` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Get deployment log file URL |
| `Deployments_GetRemoteDebuggingConfig` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Get remote debugging config. |
| `Deployments_ListForCluster` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | List deployments for a certain service |
| `Deployments_Restart` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Restart the deployment. |
| `Deployments_Start` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Start the deployment. |
| `Deployments_StartJFR` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Start JFR |
| `Deployments_Stop` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Stop the deployment. |
| `Deployments_Update` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Operation to update an exiting Deployment. |
