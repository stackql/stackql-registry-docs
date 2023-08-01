---
title: packet_core_data_planes
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_core_data_planes
  - mobile_network
  - azure_extras    
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
<tr><td><b>Id</b></td><td><code>azure_extras.mobile_network.packet_core_data_planes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Packet core data plane properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PacketCoreDataPlanes_Get` | `SELECT` | `packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId` | Gets information about the specified packet core data plane. |
| `PacketCoreDataPlanes_ListByPacketCoreControlPlane` | `SELECT` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Lists all the packet core data planes associated with a packet core control plane. |
| `PacketCoreDataPlanes_CreateOrUpdate` | `INSERT` | `packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a packet core data plane. |
| `PacketCoreDataPlanes_Delete` | `DELETE` | `packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId` | Deletes the specified packet core data plane. |
| `PacketCoreDataPlanes_UpdateTags` | `EXEC` | `packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId` | Updates packet core data planes tags. |
