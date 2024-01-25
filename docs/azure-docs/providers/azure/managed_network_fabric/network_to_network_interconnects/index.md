---
title: network_to_network_interconnects
hide_title: false
hide_table_of_contents: false
keywords:
  - network_to_network_interconnects
  - managed_network_fabric
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
<tr><td><b>Name</b></td><td><code>network_to_network_interconnects</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.network_to_network_interconnects</code></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId` | Implements NetworkToNetworkInterconnects GET method. |
| `list_by_network_fabric` | `SELECT` | `networkFabricName, resourceGroupName, subscriptionId` | Implements Network To Network Interconnects list by Network Fabric GET method. |
| `create` | `INSERT` | `networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId, data__properties` | Configuration used to setup CE-PE connectivity PUT Method. |
| `delete` | `DELETE` | `networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId` | Implements NetworkToNetworkInterconnects DELETE method. |
| `_list_by_network_fabric` | `EXEC` | `networkFabricName, resourceGroupName, subscriptionId` | Implements Network To Network Interconnects list by Network Fabric GET method. |
| `update` | `EXEC` | `networkFabricName, networkToNetworkInterconnectName, resourceGroupName, subscriptionId` | Update certain properties of the Network To NetworkInterconnects resource. |
