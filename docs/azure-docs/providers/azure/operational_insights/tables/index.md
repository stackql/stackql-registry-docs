---
title: tables
hide_title: false
hide_table_of_contents: false
keywords:
  - tables
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
<tr><td><b>Name</b></td><td><code>tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.operational_insights.tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `properties` | `object` | Table properties. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Tables_Get` | `SELECT` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Gets a Log Analytics workspace table. |
| `Tables_ListByWorkspace` | `SELECT` | `resourceGroupName, subscriptionId, workspaceName` | Gets all the tables for the specified Log Analytics workspace. |
| `Tables_CreateOrUpdate` | `INSERT` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Update or Create a Log Analytics workspace table. |
| `Tables_Delete` | `DELETE` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Delete a Log Analytics workspace table. |
| `Tables_Migrate` | `EXEC` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Migrate a Log Analytics table from support of the Data Collector API and Custom Fields features to support of Data Collection Rule-based Custom Logs. |
| `Tables_Update` | `EXEC` | `resourceGroupName, subscriptionId, tableName, workspaceName` | Update a Log Analytics workspace table. |
