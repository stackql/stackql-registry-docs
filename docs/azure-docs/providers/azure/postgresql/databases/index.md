---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - postgresql
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
<tr><td><b>Id</b></td><td><code>azure.postgresql.databases</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets information about a database. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | List all the databases in a given server. |
| `create` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Creates a new database or updates an existing database. |
| `delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId` | Deletes a database. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | List all the databases in a given server. |
