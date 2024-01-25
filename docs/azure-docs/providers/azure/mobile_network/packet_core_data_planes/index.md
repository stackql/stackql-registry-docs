---
title: packet_core_data_planes
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_core_data_planes
  - mobile_network
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
<tr><td><b>Name</b></td><td><code>packet_core_data_planes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mobile_network.packet_core_data_planes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Packet core data plane properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId` | Gets information about the specified packet core data plane. |
| `list_by_packet_core_control_plane` | `SELECT` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Lists all the packet core data planes associated with a packet core control plane. |
| `create_or_update` | `INSERT` | `packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a packet core data plane. Must be created in the same location as its parent packet core control plane. |
| `delete` | `DELETE` | `packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId` | Deletes the specified packet core data plane. |
| `_list_by_packet_core_control_plane` | `EXEC` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Lists all the packet core data planes associated with a packet core control plane. |
