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
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Get an integration runtime |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List all integration runtimes |
| `create` | `INSERT` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName, data__properties` | Create an integration runtime |
| `delete` | `DELETE` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Delete an integration runtime |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | List all integration runtimes |
| `disable_interactive_query` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Disable interactive query in integration runtime |
| `enable_interactive_query` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Enable interactive query in integration runtime |
| `start` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Start an integration runtime |
| `stop` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Stop an integration runtime |
| `update` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Update an integration runtime |
| `upgrade` | `EXEC` | `integrationRuntimeName, resourceGroupName, subscriptionId, workspaceName` | Upgrade an integration runtime |
