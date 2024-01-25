---
title: azure_monitor_workspaces
hide_title: false
hide_table_of_contents: false
keywords:
  - azure_monitor_workspaces
  - monitor
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
<tr><td><b>Name</b></td><td><code>azure_monitor_workspaces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.monitor.azure_monitor_workspaces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `etag` | `string` | Resource entity tag (ETag) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Resource properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `azureMonitorWorkspaceName, resourceGroupName, subscriptionId` | Returns the specified Azure Monitor Workspace |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all Azure Monitor Workspaces in the specified resource group |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all Azure Monitor Workspaces in the specified subscription |
| `create` | `INSERT` | `azureMonitorWorkspaceName, resourceGroupName, subscriptionId, data__location` | Creates or updates an Azure Monitor Workspace |
| `delete` | `DELETE` | `azureMonitorWorkspaceName, resourceGroupName, subscriptionId` | Deletes an Azure Monitor Workspace |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all Azure Monitor Workspaces in the specified resource group |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all Azure Monitor Workspaces in the specified subscription |
| `update` | `EXEC` | `azureMonitorWorkspaceName, resourceGroupName, subscriptionId` | Updates part of an Azure Monitor Workspace |
