---
title: integration_runtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - integration_runtimes
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
<tr><td><b>Name</b></td><td><code>integration_runtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.integration_runtimes</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `IntegrationRuntimes_Get` | `SELECT` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Get an integration runtime |
| `IntegrationRuntimes_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List all integration runtimes |
| `IntegrationRuntimes_Create` | `INSERT` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName, data__properties` | Create an integration runtime |
| `IntegrationRuntimes_Delete` | `DELETE` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Delete an integration runtime |
| `IntegrationRuntimes_DisableInteractiveQuery` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Disable interactive query in integration runtime |
| `IntegrationRuntimes_EnableInteractiveQuery` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Enable interactive query in integration runtime |
| `IntegrationRuntimes_ListOutboundNetworkDependenciesEndpoints` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Gets the list of outbound network dependencies for a given Azure-SSIS integration runtime. |
| `IntegrationRuntimes_Start` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Start an integration runtime |
| `IntegrationRuntimes_Stop` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Stop an integration runtime |
| `IntegrationRuntimes_Update` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Update an integration runtime |
| `IntegrationRuntimes_Upgrade` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Upgrade an integration runtime |
