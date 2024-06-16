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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>network_packet_brokers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.managed_network_fabric.network_packet_brokers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | Network Packet Broker Properties defines the properties of the resource. |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="networkPacketBrokerName, resourceGroupName, subscriptionId" /> | Retrieves details of this Network Packet Broker. |
| <CopyableCode code="list_by_resource_group" /> | `SELECT` | <CopyableCode code="resourceGroupName, subscriptionId" /> | Displays NetworkPacketBrokers list by resource group GET method. |
| <CopyableCode code="list_by_subscription" /> | `SELECT` | <CopyableCode code="subscriptionId" /> | Displays Network Packet Brokers list by subscription GET method. |
| <CopyableCode code="create" /> | `INSERT` | <CopyableCode code="networkPacketBrokerName, resourceGroupName, subscriptionId, data__properties" /> | Creates a Network Packet Broker. |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="networkPacketBrokerName, resourceGroupName, subscriptionId" /> | Deletes Network Packet Broker. |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="networkPacketBrokerName, resourceGroupName, subscriptionId" /> | API to update certain properties of the Network Packet Broker resource. |
