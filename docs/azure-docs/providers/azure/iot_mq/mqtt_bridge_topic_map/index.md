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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mqtt_bridge_topic_map</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.mqtt_bridge_topic_map" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | MqttBridgeTopicMap Properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, topicMapName" /> | Get a MqttBridgeTopicMapResource |
| <CopyableCode code="list_by_mqtt_bridge_connector_resource" /> | `SELECT` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId" /> | List MqttBridgeTopicMapResource resources by MqttBridgeConnectorResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, topicMapName, data__extendedLocation" /> | Create a MqttBridgeTopicMapResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, topicMapName" /> | Delete a MqttBridgeTopicMapResource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, topicMapName" /> | Update a MqttBridgeTopicMapResource |
