---
title: failover_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - failover_groups
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
<tr><td><b>Name</b></td><td><code>failover_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.sql.failover_groups</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | Resource location. |
| `properties` | `object` | Properties of a failover group. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `failoverGroupName, resourceGroupName, serverName, subscriptionId` | Gets a failover group. |
| `list_by_server` | `SELECT` | `resourceGroupName, serverName, subscriptionId` | Lists the failover groups in a server. |
| `create_or_update` | `INSERT` | `failoverGroupName, resourceGroupName, serverName, subscriptionId` | Creates or updates a failover group. |
| `delete` | `DELETE` | `failoverGroupName, resourceGroupName, serverName, subscriptionId` | Deletes a failover group. |
| `_list_by_server` | `EXEC` | `resourceGroupName, serverName, subscriptionId` | Lists the failover groups in a server. |
| `failover` | `EXEC` | `failoverGroupName, resourceGroupName, serverName, subscriptionId` | Fails over from the current primary server to this server. |
| `force_failover_allow_data_loss` | `EXEC` | `failoverGroupName, resourceGroupName, serverName, subscriptionId` | Fails over from the current primary server to this server. This operation might result in data loss. |
| `try_planned_before_forced_failover` | `EXEC` | `failoverGroupName, resourceGroupName, serverName, subscriptionId` | Fails over from the current primary server to this server. This operation tries planned before forced failover but might still result in data loss. |
| `update` | `EXEC` | `failoverGroupName, resourceGroupName, serverName, subscriptionId` | Updates a failover group. |
