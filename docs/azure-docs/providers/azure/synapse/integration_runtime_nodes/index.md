---
title: integration_runtime_nodes
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtime_nodes
  - synapse
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
<tr><td><b>Name</b></td><td><code>integration_runtime_nodes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.integration_runtime_nodes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `status` | `string` | Status of the integration runtime node. |
| `expiryTime` | `string` | The time at which the integration runtime will expire in ISO8601 format. |
| `registerTime` | `string` | The time at which the integration runtime node was registered in ISO8601 format. |
| `isActiveDispatcher` | `boolean` | Indicates whether this node is the active dispatcher for integration runtime requests. |
| `machineName` | `string` | Machine name of the integration runtime node. |
| `version` | `string` | Version of the integration runtime node. |
| `lastUpdateResult` | `string` | The result of the last integration runtime node update. |
| `nodeName` | `string` | Name of the integration runtime node. |
| `lastConnectTime` | `string` | The most recent time at which the integration runtime was connected in ISO8601 format. |
| `lastEndUpdateTime` | `string` | The last time for the integration runtime node update end. |
| `capabilities` | `object` | The integration runtime capabilities dictionary |
| `hostServiceUri` | `string` | URI for the host machine of the integration runtime. |
| `concurrentJobsLimit` | `integer` | Maximum concurrent jobs on the integration runtime node. |
| `versionStatus` | `string` | Status of the integration runtime node version. |
| `lastStartTime` | `string` | The time the node last started up. |
| `lastStartUpdateTime` | `string` | The last time for the integration runtime node update start. |
| `lastStopTime` | `string` | The integration runtime node last stop time. |
| `maxConcurrentJobs` | `integer` | The maximum concurrent jobs in this integration runtime. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationRuntimeNodes_Get` | `SELECT` | `integrationRuntimeName, nodeName, resourceGroupName, subscriptionId, workspaceName` | Get an integration runtime node |
| `IntegrationRuntimeNodes_Delete` | `DELETE` | `integrationRuntimeName, nodeName, resourceGroupName, subscriptionId, workspaceName` | Delete an integration runtime node |
| `IntegrationRuntimeNodes_Update` | `EXEC` | `integrationRuntimeName, nodeName, resourceGroupName, subscriptionId, workspaceName` | Create an integration runtime node |
