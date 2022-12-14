---
title: workspace_aad_admins
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_aad_admins
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
<tr><td><b>Name</b></td><td><code>workspace_aad_admins</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.workspace_aad_admins</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `WorkspaceAadAdmins_Get` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets a workspace active directory admin |
| `WorkspaceAadAdmins_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, workspaceName` | Creates or updates a workspace active directory admin |
| `WorkspaceAadAdmins_Delete` | `DELETE` | `resourceGroupName, subscriptionId, workspaceName` | Deletes a workspace active directory admin |
