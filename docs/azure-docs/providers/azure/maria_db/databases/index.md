---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - maria_db
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
<tr><td><b>Id</b></td><td><code>azure.maria_db.databases</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Databases_Get` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets information about a database. |
| `Databases_ListByServer` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | List all the databases in a given server. |
| `Databases_CreateOrUpdate` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Creates a new database or updates an existing database. |
| `Databases_Delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId` | Deletes a database. |
