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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>deployments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.spring_apps.deployments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="properties" /> | `object` | Deployment resource properties payload |
| <CopyableCode code="sku" /> | `object` | Sku of Azure Spring Apps |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Get a Deployment and its properties. |
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in an App. |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Create a new Deployment or update an exiting Deployment. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Operation to delete a Deployment. |
| <CopyableCode code="_list" /> | `EXEC` | <CopyableCode code="appName, resourceGroupName, serviceName, subscriptionId" /> | Handles requests to list all resources in an App. |
| <CopyableCode code="disable_remote_debugging" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Disable remote debugging. |
| <CopyableCode code="enable_remote_debugging" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Enable remote debugging. |
| <CopyableCode code="generate_heap_dump" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Generate Heap Dump |
| <CopyableCode code="generate_thread_dump" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Generate Thread Dump |
| <CopyableCode code="restart" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Restart the deployment. |
| <CopyableCode code="start" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Start the deployment. |
| <CopyableCode code="start_jfr" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Start JFR |
| <CopyableCode code="stop" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Stop the deployment. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="appName, deploymentName, resourceGroupName, serviceName, subscriptionId" /> | Operation to update an exiting Deployment. |
