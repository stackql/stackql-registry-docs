---
title: workspace_policy_fragment
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_policy_fragment
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
<tr><td><b>Name</b></td><td><code>workspace_policy_fragment</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.workspace_policy_fragment</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `id, resourceGroupName, serviceName, subscriptionId, workspaceId` | Gets a policy fragment. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, workspaceId` | Gets all policy fragments defined within a workspace. |
| `create_or_update` | `INSERT` | `id, resourceGroupName, serviceName, subscriptionId, workspaceId` | Creates or updates a policy fragment. |
| `delete` | `DELETE` | `If-Match, id, resourceGroupName, serviceName, subscriptionId, workspaceId` | Deletes a policy fragment. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, workspaceId` | Gets all policy fragments defined within a workspace. |
