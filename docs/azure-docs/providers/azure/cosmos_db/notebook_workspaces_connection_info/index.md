---
title: notebook_workspaces_connection_info
hide_title: false
hide_table_of_contents: false
keywords:
  - notebook_workspaces_connection_info
  - cosmos_db
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
<tr><td><b>Name</b></td><td><code>notebook_workspaces_connection_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.cosmos_db.notebook_workspaces_connection_info</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `authToken` | `string` | Specifies auth token used for connecting to Notebook server (uses token-based auth). |
| `notebookServerEndpoint` | `string` | Specifies the endpoint of Notebook server. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `accountName, notebookWorkspaceName, resourceGroupName, subscriptionId` |
