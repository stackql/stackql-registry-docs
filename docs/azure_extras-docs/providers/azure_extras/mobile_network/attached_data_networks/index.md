---
title: attached_data_networks
hide_title: false
hide_table_of_contents: false
keywords:
  - attached_data_networks
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
<tr><td><b>Name</b></td><td><code>attached_data_networks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure_extras.mobile_network.attached_data_networks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tags` | `object` | Resource tags. |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Data network properties. |
| `systemData` | `object` | Metadata pertaining to creation and last modification of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `AttachedDataNetworks_Get` | `SELECT` | `attachedDataNetworkName, packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId` | Gets information about the specified attached data network. |
| `AttachedDataNetworks_ListByPacketCoreDataPlane` | `SELECT` | `packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId` | Gets all the attached data networks associated with a packet core data plane. |
| `AttachedDataNetworks_CreateOrUpdate` | `INSERT` | `attachedDataNetworkName, packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId, data__properties` | Creates or updates an attached data network. |
| `AttachedDataNetworks_Delete` | `DELETE` | `attachedDataNetworkName, packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId` | Deletes the specified attached data network. |
| `AttachedDataNetworks_UpdateTags` | `EXEC` | `attachedDataNetworkName, packetCoreControlPlaneName, packetCoreDataPlaneName, resourceGroupName, subscriptionId` | Updates an attached data network tags. |
