---
title: migrations
hide_title: false
hide_table_of_contents: false
keywords:
  - migrations
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
<tr><td><b>Name</b></td><td><code>migrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.postgresql.migrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Migration resource properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `migrationName, resourceGroupName, subscriptionId, targetDbServerName` | Gets details of a migration. |
| `list_by_target_server` | `SELECT` | `resourceGroupName, subscriptionId, targetDbServerName` | List all the migrations on a given target server. |
| `create` | `INSERT` | `migrationName, resourceGroupName, subscriptionId, targetDbServerName` | Creates a new migration. |
| `delete` | `DELETE` | `migrationName, resourceGroupName, subscriptionId, targetDbServerName` | Deletes a migration. |
| `_list_by_target_server` | `EXEC` | `resourceGroupName, subscriptionId, targetDbServerName` | List all the migrations on a given target server. |
| `update` | `EXEC` | `migrationName, resourceGroupName, subscriptionId, targetDbServerName` | Updates an existing migration. The request body can contain one to many of the mutable properties present in the migration definition. Certain property updates initiate migration state transitions. |
