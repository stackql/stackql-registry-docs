---
title: replication_links
hide_title: false
hide_table_of_contents: false
keywords:
  - replication_links
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
<tr><td><b>Name</b></td><td><code>replication_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.replication_links</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `databaseName, linkId, resourceGroupName, serverName, subscriptionId` | Gets a replication link. |
| `list_by_database` | `SELECT` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a list of replication links on database. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Gets a list of replication links. |
| `delete` | `DELETE` | `databaseName, linkId, resourceGroupName, serverName, subscriptionId` | Deletes the replication link. |
| `_list_by_database` | `EXEC` | `databaseName, resourceGroupName, serverName, subscriptionId` | Gets a list of replication links on database. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Gets a list of replication links. |
| `failover` | `EXEC` | `databaseName, linkId, resourceGroupName, serverName, subscriptionId` | Fails over from the current primary server to this server. |
| `failover_allow_data_loss` | `EXEC` | `databaseName, linkId, resourceGroupName, serverName, subscriptionId` | Fails over from the current primary server to this server allowing data loss. |
