---
title: sync_members
hide_title: false
hide_table_of_contents: false
keywords:
  - sync_members
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
<tr><td><b>Name</b></td><td><code>sync_members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.sync_members</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName` | Gets a sync member. |
| `list_by_sync_group` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Lists sync members in the given sync group. |
| `create_or_update` | `INSERT` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName` | Creates or updates a sync member. |
| `delete` | `DELETE` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName` | Deletes a sync member. |
| `_list_by_sync_group` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName` | Lists sync members in the given sync group. |
| `refresh_member_schema` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName` | Refreshes a sync member database schema. |
| `update` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId, syncGroupName, syncMemberName` | Updates an existing sync member. |
