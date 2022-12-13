---
title: linked_storage_accounts
hide_title: false
hide_table_of_contents: false
keywords:
  - linked_storage_accounts
  - operational_insights
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
<tr><td><b>Id</b></td><td><code>azure.operational_insights.linked_storage_accounts</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `LinkedStorageAccounts_Get` | `SELECT` | `dataSourceType, resourceGroupName, subscriptionId, workspaceName` | Gets all linked storage account of a specific data source type associated with the specified workspace. |
| `LinkedStorageAccounts_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all linked storage accounts associated with the specified workspace, storage accounts will be sorted by their data source type. |
| `LinkedStorageAccounts_CreateOrUpdate` | `INSERT` | `dataSourceType, resourceGroupName, subscriptionId, workspaceName, data__properties` | Create or Update a link relation between current workspace and a group of storage accounts of a specific data source type. |
| `LinkedStorageAccounts_Delete` | `DELETE` | `dataSourceType, resourceGroupName, subscriptionId, workspaceName` | Deletes all linked storage accounts of a specific data source type associated with the specified workspace. |
