---
title: database_schemas
hide_title: false
hide_table_of_contents: false
keywords:
  - database_schemas
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
<tr><td><b>Name</b></td><td><code>database_schemas</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.database_schemas</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | Link to retrieve next page of results. |
| `value` | `array` | Array of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `DatabaseSchemas_ListByDatabase` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | List database schemas |
| `DatabaseSchemas_Get` | `EXEC` | `databaseName, resourceGroupName, schemaName, serverName, subscriptionId` | Get database schema |
