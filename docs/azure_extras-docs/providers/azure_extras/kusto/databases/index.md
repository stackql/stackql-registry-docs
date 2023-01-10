---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - kusto
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.kusto.databases</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `kind` | `string` | Kind of the database |
| `location` | `string` | Resource location. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Databases_Get` | `SELECT` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Returns a database. |
| `Databases_ListByCluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Returns the list of databases of the given Kusto cluster. |
| `Databases_CreateOrUpdate` | `INSERT` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__kind` | Creates or updates a database. |
| `Databases_Delete` | `DELETE` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Deletes the database with the given name. |
| `Databases_AddPrincipals` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Add Database principals permissions. |
| `Databases_CheckNameAvailability` | `EXEC` | `clusterName, resourceGroupName, subscriptionId, data__name, data__type` | Checks that the databases resource name is valid and is not already in use. |
| `Databases_ListPrincipals` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Returns a list of database principals of the given Kusto cluster and database. |
| `Databases_RemovePrincipals` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Remove Database principals permissions. |
| `Databases_Update` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__kind` | Updates a database. |
