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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mqtt_bridge_connector</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.mqtt_bridge_connector" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | MqttBridgeConnector Properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId" /> | Get a MqttBridgeConnectorResource |
| <CopyableCode code="list_by_mq_resource" /> | `SELECT` | <CopyableCode code="mqName, resourceGroupName, subscriptionId" /> | List MqttBridgeConnectorResource resources by MqResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, data__extendedLocation" /> | Create a MqttBridgeConnectorResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId" /> | Delete a MqttBridgeConnectorResource |
| <CopyableCode code="_list_by_mq_resource" /> | `EXEC` | <CopyableCode code="mqName, resourceGroupName, subscriptionId" /> | List MqttBridgeConnectorResource resources by MqResource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId" /> | Update a MqttBridgeConnectorResource |
