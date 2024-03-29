---
title: linked_storage_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_storage_accounts
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
<tr><td><b>Name</b></td><td><code>linked_storage_accounts</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.log_analytics.linked_storage_accounts</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataSourceType, resourceGroupName, subscriptionId, workspaceName` | Gets all linked storage account of a specific data source type associated with the specified workspace. |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all linked storage accounts associated with the specified workspace, storage accounts will be sorted by their data source type. |
| `create_or_update` | `INSERT` | `dataSourceType, resourceGroupName, subscriptionId, workspaceName, data__properties` | Create or Update a link relation between current workspace and a group of storage accounts of a specific data source type. |
| `delete` | `DELETE` | `dataSourceType, resourceGroupName, subscriptionId, workspaceName` | Deletes all linked storage accounts of a specific data source type associated with the specified workspace. |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets all linked storage accounts associated with the specified workspace, storage accounts will be sorted by their data source type. |
