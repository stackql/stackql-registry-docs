---
title: attached_data_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - attached_data_networks
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
<tr><td><b>Name</b></td><td><code>attached_data_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mobile_network.attached_data_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Data network properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `attachedDataNetworkName, packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId` | Gets information about the specified attached data network. |
| `list_by_packet_core_data_plane` | `SELECT` | `packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId` | Gets all the attached data networks associated with a packet core data plane. |
| `create_or_update` | `INSERT` | `attachedDataNetworkName, packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an attached data network. Must be created in the same location as its parent packet core data plane. |
| `delete` | `DELETE` | `attachedDataNetworkName, packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId` | Deletes the specified attached data network. |
| `_list_by_packet_core_data_plane` | `EXEC` | `packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId` | Gets all the attached data networks associated with a packet core data plane. |
