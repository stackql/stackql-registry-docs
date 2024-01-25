---
title: watchers
hide_title: false
hide_table_of_contents: false
keywords:
  - watchers
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
<tr><td><b>Name</b></td><td><code>watchers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.watchers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Resource ID. |
| `name` | `string` | Resource name. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `location` | `string` | Resource location. |
| `properties` | `object` | The network watcher properties. |
| `tags` | `object` | Resource tags. |
| `type` | `string` | Resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkWatcherName, resourceGroupName, subscriptionId` | Gets the specified network watcher by resource group. |
| `list` | `SELECT` | `resourceGroupName, subscriptionId` | Gets all network watchers by resource group. |
| `create_or_update` | `INSERT` | `networkWatcherName, resourceGroupName, subscriptionId` | Creates or updates a network watcher in the specified resource group. |
| `delete` | `DELETE` | `networkWatcherName, resourceGroupName, subscriptionId` | Deletes the specified network watcher resource. |
| `_list` | `EXEC` | `resourceGroupName, subscriptionId` | Gets all network watchers by resource group. |
| `check_connectivity` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId, data__destination, data__source` | Verifies the possibility of establishing a direct TCP connection from a virtual machine to a given endpoint including another VM or an arbitrary remote server. |
| `set_flow_log_configuration` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId, data__properties, data__targetResourceId` | Configures flow log and traffic analytics (optional) on a specified resource. |
| `verify_ip_flow` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId, data__direction, data__localIPAddress, data__localPort, data__protocol, data__remoteIPAddress, data__remotePort, data__targetResourceId` | Verify IP flow from the specified VM to a location given the currently configured NSG rules. |
