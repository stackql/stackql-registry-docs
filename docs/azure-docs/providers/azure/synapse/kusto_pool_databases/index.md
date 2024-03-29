---
title: kusto_pool_databases
hide_title: false
hide_table_of_contents: false
keywords:
  - kusto_pool_databases
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
<tr><td><b>Name</b></td><td><code>kusto_pool_databases</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.synapse.kusto_pool_databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind of the database |
| `location` | `string` | Resource location. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Returns a database. |
| `list_by_kusto_pool` | `SELECT` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Returns the list of databases of the given Kusto pool. |
| `create_or_update` | `INSERT` | `databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__kind` | Creates or updates a database. |
| `delete` | `DELETE` | `databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Deletes the database with the given name. |
| `_list_by_kusto_pool` | `EXEC` | `kustoPoolName, resourceGroupName, subscriptionId, workspaceName` | Returns the list of databases of the given Kusto pool. |
| `update` | `EXEC` | `databaseName, kustoPoolName, resourceGroupName, subscriptionId, workspaceName, data__kind` | Updates a database. |
