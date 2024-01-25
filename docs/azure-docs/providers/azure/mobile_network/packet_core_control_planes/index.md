---
title: packet_core_control_planes
hide_title: false
hide_table_of_contents: false
keywords:
  - packet_core_control_planes
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
<tr><td><b>Name</b></td><td><code>packet_core_control_planes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.mobile_network.packet_core_control_planes</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `identity` | `object` | Managed service identity (system assigned and/or user assigned identities) |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Packet core control plane properties. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Gets information about the specified packet core control plane. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Lists all the packet core control planes in a resource group. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Lists all the packet core control planes in a subscription. |
| `create_or_update` | `INSERT` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId, data__properties` | Creates or updates a packet core control plane. |
| `delete` | `DELETE` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Deletes the specified packet core control plane. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Lists all the packet core control planes in a resource group. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Lists all the packet core control planes in a subscription. |
| `collect_diagnostics_package` | `EXEC` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId, data__storageAccountBlobUrl` | Collect a diagnostics package for the specified packet core control plane. This action will upload the diagnostics to a storage account. |
| `reinstall` | `EXEC` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Reinstall the specified packet core control plane. This action will remove any transaction state from the packet core to return it to a known state. This action will cause a service outage. |
| `rollback` | `EXEC` | `packetCoreControlPlaneName, resourceGroupName, subscriptionId` | Roll back the specified packet core control plane to the previous version, "rollbackVersion". Multiple consecutive rollbacks are not possible. This action may cause a service outage. |
