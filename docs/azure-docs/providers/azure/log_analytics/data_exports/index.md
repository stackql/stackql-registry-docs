---
title: data_exports
hide_title: false
hide_table_of_contents: false
keywords:
  - data_exports
  - log_analytics
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
<tr><td><b>Name</b></td><td><code>data_exports</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.log_analytics.data_exports</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataExportName, resourceGroupName, subscriptionId, workspaceName` | Gets a data export instance. |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Lists the data export instances within a workspace. |
| `create_or_update` | `INSERT` | `dataExportName, resourceGroupName, subscriptionId, workspaceName` | Create or update a data export. |
| `delete` | `DELETE` | `dataExportName, resourceGroupName, subscriptionId, workspaceName` | Deletes the specified data export in a given workspace.. |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Lists the data export instances within a workspace. |
