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
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseColumns_Get` | `SELECT` | `columnName, databaseName, resourceGroupName, schemaName, serverName, subscriptionId, tableName` | Get database column |
| `DatabaseColumns_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | List database columns |
| `DatabaseColumns_ListByTable` | `SELECT` | `databaseName, resourceGroupName, schemaName, serverName, subscriptionId, tableName` | List database columns |
