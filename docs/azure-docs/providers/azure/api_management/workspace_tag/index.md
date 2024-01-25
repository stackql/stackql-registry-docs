---
title: workspace_tag
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_tag
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
<tr><td><b>Name</b></td><td><code>workspace_tag</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.workspace_tag</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, tagId, workspaceId` | Gets the details of the tag specified by its identifier. |
| `list_by_service` | `SELECT` | `resourceGroupName, serviceName, subscriptionId, workspaceId` | Lists a collection of tags defined within a workspace in a service instance. |
| `create_or_update` | `INSERT` | `resourceGroupName, serviceName, subscriptionId, tagId, workspaceId` | Creates a tag. |
| `delete` | `DELETE` | `If-Match, resourceGroupName, serviceName, subscriptionId, tagId, workspaceId` | Deletes specific tag of the workspace in an API Management service instance. |
| `_list_by_service` | `EXEC` | `resourceGroupName, serviceName, subscriptionId, workspaceId` | Lists a collection of tags defined within a workspace in a service instance. |
| `update` | `EXEC` | `If-Match, resourceGroupName, serviceName, subscriptionId, tagId, workspaceId` | Updates the details of the tag specified by its identifier. |
