---
title: database_columns
hide_title: false
hide_table_of_contents: false
keywords:
  - database_columns
  - sql
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
<tr><td><b>Name</b></td><td><code>database_columns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.database_columns</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `columnName, databaseName, resourceGroupName, schemaName, serverName, subscriptionId, tableName` | Get database column |
| `list_by_database` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | List database columns |
| `list_by_table` | `SELECT` | `databaseName, resourceGroupName, schemaName, serverName, subscriptionId, tableName` | List database columns |
| `_list_by_database` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | List database columns |
| `_list_by_table` | `EXEC` | `databaseName, resourceGroupName, schemaName, serverName, subscriptionId, tableName` | List database columns |
