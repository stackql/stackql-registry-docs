---
title: sync_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_groups
  - sql
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
<tr><td><b>Name</b></td><td><code>sync_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.sync_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `properties` | `object` | Properties of a sync group. |
| `sku` | `object` | An ARM Resource SKU. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Gets a sync group. |
| `list_by_database` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Lists sync groups under a hub database. |
| `create_or_update` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Creates or updates a sync group. |
| `delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Deletes a sync group. |
| `_list_by_database` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Lists sync groups under a hub database. |
| `cancel_sync` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Cancels a sync group synchronization. |
| `refresh_hub_schema` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Refreshes a hub database schema. |
| `trigger_sync` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Triggers a sync group synchronization. |
| `update` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Updates a sync group. |
