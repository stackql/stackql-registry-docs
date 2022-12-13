---
title: managed_database_queries
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_queries
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
<tr><td><b>Name</b></td><td><code>managed_database_queries</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_database_queries</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `ManagedDatabaseQueries_ListByQuery` | `SELECT` | `databaseName, managedInstanceName, queryId, resourceGroupName, subscriptionId` | Get query execution statistics by query id. |
| `ManagedDatabaseQueries_Get` | `EXEC` | `databaseName, managedInstanceName, queryId, resourceGroupName, subscriptionId` | Get query by query id. |
