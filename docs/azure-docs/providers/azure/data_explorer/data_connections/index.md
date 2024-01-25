---
title: data_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - data_connections
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
<tr><td><b>Name</b></td><td><code>data_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.data_explorer.data_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind of the endpoint for the data connection |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, dataConnectionName, databaseName, resourceGroupName, subscriptionId` | Returns a data connection. |
| `list_by_database` | `SELECT` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Returns the list of data connections of the given Kusto database. |
| `create_or_update` | `INSERT` | `clusterName, dataConnectionName, databaseName, resourceGroupName, subscriptionId, data__kind` | Creates or updates a data connection. |
| `delete` | `DELETE` | `clusterName, dataConnectionName, databaseName, resourceGroupName, subscriptionId` | Deletes the data connection with the given name. |
| `_list_by_database` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Returns the list of data connections of the given Kusto database. |
| `check_name_availability` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__name, data__type` | Checks that the data connection name is valid and is not already in use. |
| `data_connection_validation` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Checks that the data connection parameters are valid. |
| `update` | `EXEC` | `clusterName, dataConnectionName, databaseName, resourceGroupName, subscriptionId, data__kind` | Updates a data connection. |
