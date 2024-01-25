---
title: workspace_api_policy
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_api_policy
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
<tr><td><b>Name</b></td><td><code>workspace_api_policy</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.api_management.workspace_api_policy</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `apiId, policyId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Get the policy configuration at the API level. |
| `list_by_api` | `SELECT` | `apiId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Get the policy configuration at the API level. |
| `create_or_update` | `INSERT` | `apiId, policyId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Creates or updates policy configuration for the API. |
| `delete` | `DELETE` | `If-Match, apiId, policyId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Deletes the policy configuration at the Api. |
| `_list_by_api` | `EXEC` | `apiId, resourceGroupName, serviceName, subscriptionId, workspaceId` | Get the policy configuration at the API level. |
