---
title: sql_server_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - sql_server_databases
  - azure_arc_data
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
<tr><td><b>Name</b></td><td><code>sql_server_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.azure_arc_data.sql_server_databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | The properties of Arc Sql Server database resource |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `api-version, databaseName, resourceGroupName, sqlServerInstanceName, subscriptionId` | Retrieves an Arc Sql Server database. |
| `list` | `SELECT` | `api-version, resourceGroupName, sqlServerInstanceName, subscriptionId` |  |
| `create` | `INSERT` | `api-version, databaseName, resourceGroupName, sqlServerInstanceName, subscriptionId, data__properties` | Creates or replaces an Arc Sql Server Database. |
| `delete` | `DELETE` | `api-version, databaseName, resourceGroupName, sqlServerInstanceName, subscriptionId` | Deletes an Arc Sql Server database resource. |
| `_list` | `EXEC` | `api-version, resourceGroupName, sqlServerInstanceName, subscriptionId` |  |
| `update` | `EXEC` | `api-version, databaseName, resourceGroupName, sqlServerInstanceName, subscriptionId` | Updates an existing database. |
