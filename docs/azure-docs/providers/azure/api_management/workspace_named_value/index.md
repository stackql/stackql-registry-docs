---
title: workspace_named_value
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_named_value
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
<tr><td><b>Name</b></td><td><code>workspace_named_value</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.workspace_named_value</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `namedValueId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Gets the details of the named value specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, workspaceId` | Lists a collection of named values defined within a workspace in a service instance. |
| `create_or_update` | `INSERT` | `namedValueId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Creates or updates named value. |
| `delete` | `DELETE` | `If-Match, namedValueId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Deletes specific named value from the workspace in an API Management service instance. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, workspaceId` | Lists a collection of named values defined within a workspace in a service instance. |
| `refresh_secret` | `EXEC` | `namedValueId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Refresh the secret of the named value specified by its identifier. |
| `update` | `EXEC` | `If-Match, namedValueId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Updates the specific named value. |
