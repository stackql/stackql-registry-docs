---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - redis_enterprise
  - azure_isv    
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
<tr><td><b>Id</b></td><td><code>azure_isv.redis_enterprise.databases</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Gets information about a database in a RedisEnterprise cluster. |
| `list_by_cluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets all databases in the specified RedisEnterprise cluster. |
| `create` | `INSERT` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Creates a database |
| `delete` | `DELETE` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Deletes a single database |
| `_list_by_cluster` | `EXEC` | `clusterName, resourceGroupName, subscriptionId` | Gets all databases in the specified RedisEnterprise cluster. |
| `export` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__sasUri` | Exports a database file from target database. |
| `flush` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Flushes all the keys in this database and also from its linked databases. |
| `force_unlink` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__ids` | Forcibly removes the link to the specified database resource. |
| `import` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__sasUris` | Imports database files to target database. |
| `regenerate_key` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the RedisEnterprise database's access keys. |
| `update` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Updates a database |
