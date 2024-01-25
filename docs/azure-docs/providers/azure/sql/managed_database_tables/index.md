---
title: managed_database_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - managed_database_tables
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
<tr><td><b>Name</b></td><td><code>managed_database_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.managed_database_tables</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, schemaName, subscriptionId, tableName` | Get managed database table |
| `list_by_schema` | `SELECT` | `databaseName, managedInstanceName, resourceGroupName, schemaName, subscriptionId` | List managed database tables |
| `_list_by_schema` | `EXEC` | `databaseName, managedInstanceName, resourceGroupName, schemaName, subscriptionId` | List managed database tables |
