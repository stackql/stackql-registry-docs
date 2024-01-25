---
title: broker_listener
hide_title: false
hide_table_of_contents: false
keywords:
  - broker_listener
  - iot_mq
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
<tr><td><b>Name</b></td><td><code>broker_listener</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_mq.broker_listener</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | ExtendedLocation properties |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | Broker Listener Resource properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `brokerName, listenerName, mqName, resourceGroupName, subscriptionId` | Get a BrokerListenerResource |
| `list_by_broker_resource` | `SELECT` | `brokerName, mqName, resourceGroupName, subscriptionId` | List BrokerListenerResource resources by BrokerResource |
| `create_or_update` | `INSERT` | `brokerName, listenerName, mqName, resourceGroupName, subscriptionId, data__extendedLocation` | Create a BrokerListenerResource |
| `delete` | `DELETE` | `brokerName, listenerName, mqName, resourceGroupName, subscriptionId` | Delete a BrokerListenerResource |
| `_list_by_broker_resource` | `EXEC` | `brokerName, mqName, resourceGroupName, subscriptionId` | List BrokerListenerResource resources by BrokerResource |
| `update` | `EXEC` | `brokerName, listenerName, mqName, resourceGroupName, subscriptionId` | Update a BrokerListenerResource |
