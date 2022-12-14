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
| `location` | `string` | Resource location. |
| `properties` | `object` | Parameters that define the configuration of flow log. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `FlowLogs_Get` | `SELECT` | `flowLogName, networkWatcherName, resourceGroupName, subscriptionId` | Gets a flow log resource by name. |
| `FlowLogs_List` | `SELECT` | `networkWatcherName, resourceGroupName, subscriptionId` | Lists all flow log resources for the specified Network Watcher. |
| `FlowLogs_CreateOrUpdate` | `INSERT` | `flowLogName, networkWatcherName, resourceGroupName, subscriptionId` | Create or update a flow log for the specified network security group. |
| `FlowLogs_Delete` | `DELETE` | `flowLogName, networkWatcherName, resourceGroupName, subscriptionId` | Deletes the specified flow log resource. |
| `FlowLogs_UpdateTags` | `EXEC` | `flowLogName, networkWatcherName, resourceGroupName, subscriptionId` | Update tags of the specified flow log. |
