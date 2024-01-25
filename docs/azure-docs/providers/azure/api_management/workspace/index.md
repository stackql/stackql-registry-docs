---
title: workspace
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace
  - api_management
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
<tr><td><b>Name</b></td><td><code>workspace</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.workspace</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, workspaceId` | Gets the details of the workspace specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId` | Lists all workspaces of the API Management service instance. |
| `create_or_update` | `INSERT` | `resourceGroupName, serviceName, subscriptionId, workspaceId` | Creates a new workspace or updates an existing one. |
| `delete` | `DELETE` | `If-Match, resourceGroupName, serviceName, subscriptionId, workspaceId` | Deletes the specified workspace. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId` | Lists all workspaces of the API Management service instance. |
| `update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId, workspaceId` | Updates the details of the workspace specified by its identifier. |
