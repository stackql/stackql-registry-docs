---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
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
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.log_analytics.tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Table properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Gets a Log Analytics workspace table. |
| `list_by_workspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all the tables for the specified Log Analytics workspace. |
| `create_or_update` | `INSERT` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Update or Create a Log Analytics workspace table. |
| `delete` | `DELETE` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Delete a Log Analytics workspace table. |
| `_list_by_workspace` | `EXEC` | `resourceGroupName, subscriptionId, workspaceName` | Gets all the tables for the specified Log Analytics workspace. |
| `cancel_search` | `EXEC` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Cancel a log analytics workspace search results table query run. |
| `migrate` | `EXEC` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Migrate a Log Analytics table from support of the Data Collector API and Custom Fields features to support of Data Collection Rule-based Custom Logs. |
| `update` | `EXEC` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Update a Log Analytics workspace table. |
