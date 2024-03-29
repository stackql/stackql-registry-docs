---
title: kusto_pool_data_connections
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pool_data_connections
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
<tr><td><b>Name</b></td><td><code>kusto_pool_data_connections</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.kusto_pool_data_connections</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind of the endpoint for the data connection |
| `location` | `string` | Resource location. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `dataConnectionName, databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Returns a data connection. |
| `list_by_database` | `SELECT` | `databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Returns the list of data connections of the given Kusto pool database. |
| `create_or_update` | `INSERT` | `dataConnectionName, databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__kind` | Creates or updates a data connection. |
| `delete` | `DELETE` | `dataConnectionName, databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Deletes the data connection with the given name. |
| `_list_by_database` | `EXEC` | `databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Returns the list of data connections of the given Kusto pool database. |
| `check_name_availability` | `EXEC` | `databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__name, data__type` | Checks that the data connection name is valid and is not already in use. |
| `data_connection_validation` | `EXEC` | `databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Checks that the data connection parameters are valid. |
| `update` | `EXEC` | `dataConnectionName, databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__kind` | Updates a data connection. |
