---
title: workspaces_notebook_access_token
hide_title: false
hide_table_of_contents: false
keywords:
  - workspaces_notebook_access_token
  - ml_services
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
<tr><td><b>Name</b></td><td><code>workspaces_notebook_access_token</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.ml_services.workspaces_notebook_access_token</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `accessToken` | `string` |
| `expiresIn` | `integer` |
| `hostName` | `string` |
| `notebookResourceId` | `string` |
| `publicDns` | `string` |
| `refreshToken` | `string` |
| `scope` | `string` |
| `tokenType` | `string` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` |
