---
title: sql_pool_tables
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_pool_tables
  - synapse
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
<tr><td><b>Name</b></td><td><code>sql_pool_tables</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.sql_pool_tables</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextLink` | `string` | Link to retrieve next page of results. |
| `value` | `array` | Array of results. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `SqlPoolTables_ListBySchema` | `SELECT` | `resourceGroupName, schemaName, sqlPoolName, subscriptionId, workspaceName` | Gets tables of a given schema in a SQL pool. |
| `SqlPoolTables_Get` | `EXEC` | `resourceGroupName, schemaName, sqlPoolName, subscriptionId, tableName, workspaceName` | Get Sql pool table |
