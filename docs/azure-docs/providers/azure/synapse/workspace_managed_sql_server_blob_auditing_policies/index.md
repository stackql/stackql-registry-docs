---
title: workspace_managed_sql_server_blob_auditing_policies
hide_title: false
hide_table_of_contents: false
keywords:
  - workspace_managed_sql_server_blob_auditing_policies
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
<tr><td><b>Name</b></td><td><code>workspace_managed_sql_server_blob_auditing_policies</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.workspace_managed_sql_server_blob_auditing_policies</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `blobAuditingPolicyName, resourceGroupName, subscriptionId, workspaceName` | Get a workspace managed sql server's blob auditing policy. |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | List workspace managed sql server's blob auditing policies. |
| `create_or_update` | `INSERT` | `blobAuditingPolicyName, resourceGroupName, subscriptionId, workspaceName` | Create or Update a workspace managed sql server's blob auditing policy. |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | List workspace managed sql server's blob auditing policies. |
