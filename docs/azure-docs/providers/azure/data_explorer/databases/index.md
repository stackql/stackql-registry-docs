---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - data_explorer
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
<tr><td><b>Name</b></td><td><code>databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_explorer.databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind of the database |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Returns a database. |
| `list_by_cluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Returns the list of databases of the given Kusto cluster. |
| `create_or_update` | `INSERT` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__kind` | Creates or updates a database. |
| `delete` | `DELETE` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Deletes the database with the given name. |
| `_list_by_cluster` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Returns the list of databases of the given Kusto cluster. |
| `add_principals` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Add Database principals permissions. |
| `check_name_availability` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, data__name, data__type` | Checks that the databases resource name is valid and is not already in use. |
| `remove_principals` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Remove Database principals permissions. |
| `update` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__kind` | Updates a database. |
