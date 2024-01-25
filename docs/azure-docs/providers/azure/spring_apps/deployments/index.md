---
title: deployments
hide_title: false
hide_table_of_contents: false
keywords:
  - deployments
  - spring_apps
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
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.spring_apps.deployments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Deployment resource properties payload |
| `sku` | `object` | Sku of Azure Spring Apps |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Get a Deployment and its properties. |
| `list` | `SELECT` | `appName, resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in an App. |
| `create_or_update` | `INSERT` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Create a new Deployment or update an exiting Deployment. |
| `delete` | `DELETE` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Operation to delete a Deployment. |
| `_list` | `EXEC` | `appName, resourceGroupName, serviceName, subscriptionId` | Handles requests to list all resources in an App. |
| `disable_remote_debugging` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Disable remote debugging. |
| `enable_remote_debugging` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Enable remote debugging. |
| `generate_heap_dump` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Generate Heap Dump |
| `generate_thread_dump` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Generate Thread Dump |
| `restart` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Restart the deployment. |
| `start` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Start the deployment. |
| `start_jfr` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Start JFR |
| `stop` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Stop the deployment. |
| `update` | `EXEC` | `appName, deploymentName, resourceGroupName, serviceName, subscriptionId` | Operation to update an exiting Deployment. |
