---
title: mqtt_bridge_connector
hide_title: false
hide_table_of_contents: false
keywords:
  - mqtt_bridge_connector
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
<tr><td><b>Name</b></td><td><code>mqtt_bridge_connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_mq.mqtt_bridge_connector</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | ExtendedLocation properties |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | MqttBridgeConnector Properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId` | Get a MqttBridgeConnectorResource |
| `list_by_mq_resource` | `SELECT` | `mqName, resourceGroupName, subscriptionId` | List MqttBridgeConnectorResource resources by MqResource |
| `create_or_update` | `INSERT` | `mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, data__extendedLocation` | Create a MqttBridgeConnectorResource |
| `delete` | `DELETE` | `mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId` | Delete a MqttBridgeConnectorResource |
| `_list_by_mq_resource` | `EXEC` | `mqName, resourceGroupName, subscriptionId` | List MqttBridgeConnectorResource resources by MqResource |
| `update` | `EXEC` | `mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId` | Update a MqttBridgeConnectorResource |
