---
title: database_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - database_tables
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
<tr><td><b>Name</b></td><td><code>database_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.database_tables</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, resourceGroupName, schemaName, serverName, subscriptionId, tableName` | Get database table |
| `list_by_schema` | `SELECT` | `databaseName, resourceGroupName, schemaName, serverName, subscriptionId` | List database tables |
| `_list_by_schema` | `EXEC` | `databaseName, resourceGroupName, schemaName, serverName, subscriptionId` | List database tables |
