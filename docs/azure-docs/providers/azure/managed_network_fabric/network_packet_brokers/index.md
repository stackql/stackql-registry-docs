---
title: network_packet_brokers
hide_title: false
hide_table_of_contents: false
keywords:
  - network_packet_brokers
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
<tr><td><b>Name</b></td><td><code>network_packet_brokers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.managed_network_fabric.network_packet_brokers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Network Packet Broker Properties defines the properties of the resource. |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `networkPacketBrokerName, resourceGroupName, subscriptionId` | Retrieves details of this Network Packet Broker. |
| `list_by_resource_group` | `SELECT` | `resourceGroupName, subscriptionId` | Displays NetworkPacketBrokers list by resource group GET method. |
| `list_by_subscription` | `SELECT` | `subscriptionId` | Displays Network Packet Brokers list by subscription GET method. |
| `create` | `INSERT` | `networkPacketBrokerName, resourceGroupName, subscriptionId, data__properties` | Creates a Network Packet Broker. |
| `delete` | `DELETE` | `networkPacketBrokerName, resourceGroupName, subscriptionId` | Deletes Network Packet Broker. |
| `_list_by_resource_group` | `EXEC` | `resourceGroupName, subscriptionId` | Displays NetworkPacketBrokers list by resource group GET method. |
| `_list_by_subscription` | `EXEC` | `subscriptionId` | Displays Network Packet Brokers list by subscription GET method. |
| `update` | `EXEC` | `networkPacketBrokerName, resourceGroupName, subscriptionId` | API to update certain properties of the Network Packet Broker resource. |
