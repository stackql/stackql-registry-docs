---
title: mqtt_bridge_topic_map
hide_title: false
hide_table_of_contents: false
keywords:
  - mqtt_bridge_topic_map
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
<tr><td><b>Name</b></td><td><code>mqtt_bridge_topic_map</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_mq.mqtt_bridge_topic_map</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | ExtendedLocation properties |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | MqttBridgeTopicMap Properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, topicMapName` | Get a MqttBridgeTopicMapResource |
| `list_by_mqtt_bridge_connector_resource` | `SELECT` | `mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId` | List MqttBridgeTopicMapResource resources by MqttBridgeConnectorResource |
| `create_or_update` | `INSERT` | `mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, topicMapName, data__extendedLocation` | Create a MqttBridgeTopicMapResource |
| `delete` | `DELETE` | `mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, topicMapName` | Delete a MqttBridgeTopicMapResource |
| `_list_by_mqtt_bridge_connector_resource` | `EXEC` | `mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId` | List MqttBridgeTopicMapResource resources by MqttBridgeConnectorResource |
| `update` | `EXEC` | `mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, topicMapName` | Update a MqttBridgeTopicMapResource |
