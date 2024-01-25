---
title: flow_logs
hide_title: false
hide_table_of_contents: false
keywords:
  - flow_logs
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
<tr><td><b>Name</b></td><td><code>flow_logs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.flow_logs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | Parameters that define the configuration of flow log. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `flowLogName, networkWatcherName, resourceGroupName, subscriptionId` | Gets a flow log resource by name. |
| `list` | `SELECT` | `networkWatcherName, resourceGroupName, subscriptionId` | Lists all flow log resources for the specified Network Watcher. |
| `create_or_update` | `INSERT` | `flowLogName, networkWatcherName, resourceGroupName, subscriptionId` | Create or update a flow log for the specified network security group. |
| `delete` | `DELETE` | `flowLogName, networkWatcherName, resourceGroupName, subscriptionId` | Deletes the specified flow log resource. |
| `_list` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId` | Lists all flow log resources for the specified Network Watcher. |
