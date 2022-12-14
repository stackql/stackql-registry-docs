---
title: databases
hide_title: false
hide_table_of_contents: false
keywords:
  - databases
  - redis_enterprise
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
<tr><td><b>Id</b></td><td><code>azure.redis_enterprise.databases</code></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `Databases_Get` | `SELECT` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Gets information about a database in a RedisEnterprise cluster. |
| `Databases_ListByCluster` | `SELECT` | `clusterName, resourceGroupName, subscriptionId` | Gets all databases in the specified RedisEnterprise cluster. |
| `Databases_Create` | `INSERT` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Creates a database |
| `Databases_Delete` | `DELETE` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Deletes a single database |
| `Databases_Export` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__sasUri` | Exports a database file from target database. |
| `Databases_ForceUnlink` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__ids` | Forcibly removes the link to the specified database resource. |
| `Databases_Import` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__sasUris` | Imports database files to target database. |
| `Databases_ListKeys` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Retrieves the access keys for the RedisEnterprise database. |
| `Databases_RegenerateKey` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId, data__keyType` | Regenerates the RedisEnterprise database's access keys. |
| `Databases_Update` | `EXEC` | `clusterName, databaseName, resourceGroupName, subscriptionId` | Updates a database |
