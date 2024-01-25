---
title: static_sites_database_connection
hide_title: false
hide_table_of_contents: false
keywords:
  - static_sites_database_connection
  - app_service
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
<tr><td><b>Name</b></td><td><code>static_sites_database_connection</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.app_service.static_sites_database_connection</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource Id. |
| `name` | `string` | Resource Name. |
| `kind` | `string` | Kind of resource. |
| `properties` | `object` | DatabaseConnection resource specific properties |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseConnectionName, name, resourceGroupName, subscriptionId` |  |
| `create_or_update` | `INSERT` | `databaseConnectionName, name, resourceGroupName, subscriptionId` | Description for Create or update a database connection for a static site |
| `delete` | `DELETE` | `databaseConnectionName, name, resourceGroupName, subscriptionId` |  |
| `update` | `EXEC` | `databaseConnectionName, name, resourceGroupName, subscriptionId` | Description for Create or update a database connection for a static site |
