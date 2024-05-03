---
title: kafka_connector_topic_map
hide_title: false
hide_table_of_contents: false
keywords:
  - kafka_connector_topic_map
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
<tr><td><b>Name</b></td><td><code>kafka_connector_topic_map</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.kafka_connector_topic_map" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | KafkaTopicMap Properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName" /> | Get a KafkaTopicMapResource |
| <CopyableCode code="list_by_kafka_connector_resource" /> | `SELECT` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId" /> | List KafkaTopicMapResource resources by KafkaConnectorResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName, data__extendedLocation" /> | Create a KafkaTopicMapResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName" /> | Delete a KafkaTopicMapResource |
| <CopyableCode code="_list_by_kafka_connector_resource" /> | `EXEC` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId" /> | List KafkaTopicMapResource resources by KafkaConnectorResource |
| <CopyableCode code="update" /> | `EXEC` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName" /> | Update a KafkaTopicMapResource |
