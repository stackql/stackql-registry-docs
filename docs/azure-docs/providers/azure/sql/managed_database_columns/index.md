---
title: managed_database_columns
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_columns
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
<tr><td><b>Name</b></td><td><code>managed_database_columns</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_database_columns</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedDatabaseColumns_Get` | `SELECT` | `columnName, databaseName, managedInstanceName, resourceGroupName, schemaName, subscriptionId, tableName` | Get managed database column |
| `ManagedDatabaseColumns_ListByDatabase` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, subscriptionId` | List managed database columns |
| `ManagedDatabaseColumns_ListByTable` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, schemaName, subscriptionId, tableName` | List managed database columns |
