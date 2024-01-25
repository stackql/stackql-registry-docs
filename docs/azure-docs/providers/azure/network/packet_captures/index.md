---
title: packet_captures
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_captures
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
<tr><td><b>Name</b></td><td><code>packet_captures</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.network.packet_captures</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the packet capture operation. |
| `name` | `string` | Name of the packet capture session. |
| `etag` | `string` | A unique read-only string that changes whenever the resource is updated. |
| `properties` | `object` | The properties of a packet capture session. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId` | Gets a packet capture session by name. |
| `list` | `SELECT` | `networkWatcherName, resourceGroupName, subscriptionId` | Lists all packet capture sessions within the specified resource group. |
| `create` | `INSERT` | `networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId, data__properties` | Create and start a packet capture on the specified VM. |
| `delete` | `DELETE` | `networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId` | Deletes the specified packet capture session. |
| `_list` | `EXEC` | `networkWatcherName, resourceGroupName, subscriptionId` | Lists all packet capture sessions within the specified resource group. |
| `stop` | `EXEC` | `networkWatcherName, packetCaptureName, resourceGroupName, subscriptionId` | Stops a specified packet capture session. |
