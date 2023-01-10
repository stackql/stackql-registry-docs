---
title: packet_core_control_planes
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_core_control_planes
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
<tr><td><b>Name</b></td><td><code>packet_core_control_planes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.mobile_network.packet_core_control_planes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Packet core control plane properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
| `tags` | `object` | Resource tags. |
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `PacketCoreControlPlanes_Get` | `SELECT` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Gets information about the specified packet core control plane. |
| `PacketCoreControlPlanes_ListByResourceGroup` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the packet core control planes in a resource group. |
| `PacketCoreControlPlanes_ListBySubscription` | `SELECT` | `subscriptionId` | Lists all the packet core control planes in a subscription. |
| `PacketCoreControlPlanes_CreateOrUpdate` | `INSERT` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a packet core control plane. |
| `PacketCoreControlPlanes_Delete` | `DELETE` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Deletes the specified packet core control plane. |
| `PacketCoreControlPlanes_UpdateTags` | `EXEC` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Updates packet core control planes tags. |
