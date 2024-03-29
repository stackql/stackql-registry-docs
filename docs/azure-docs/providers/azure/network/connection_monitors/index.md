---
title: connection_monitors
hide_title: false
hide_table_of_contents: false
keywords:
  - connection_monitors
  - network
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
<tr><td><b>Name</b></td><td><code>connection_monitors</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.connection_monitors</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the connection monitor. |
| `name` | `string` | Name of the connection monitor. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Connection monitor location. |
| `properties` | `object` | Describes the properties of a connection monitor. |
| `tags` | `object` | Connection monitor tags. |
| `type` | `string` | Connection monitor type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId` | Gets a connection monitor by name. |
| `list` | `SELECT` | `networkWatcherName, resourceGroupName, subscriptionId` | Lists all connection monitors for the specified Network Watcher. |
| `create_or_update` | `INSERT` | `connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId, data__properties` | Create or update a connection monitor. |
| `delete` | `DELETE` | `connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId` | Deletes the specified connection monitor. |
| `_list` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId` | Lists all connection monitors for the specified Network Watcher. |
| `query` | `EXEC` | `connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId` | Query a snapshot of the most recent connection states. |
| `start` | `EXEC` | `connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId` | Starts the specified connection monitor. |
| `stop` | `EXEC` | `connectionMonitorName, networkWatcherName, resourceGroupName, subscriptionId` | Stops the specified connection monitor. |
