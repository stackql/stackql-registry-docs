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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kafka_connector_topic_map</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>azure.iot_mq.kafka_connector_topic_map</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `extendedLocation` | `object` | ExtendedLocation properties |
| `location` | `string` | The geo-location where the resource lives |
| `properties` | `object` | KafkaTopicMap Properties |
| `tags` | `object` | Resource tags. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `kafkaConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName` | Get a KafkaTopicMapResource |
| `list_by_kafka_connector_resource` | `SELECT` | `kafkaConnectorName, mqName, resourceGroupName, subscriptionId` | List KafkaTopicMapResource resources by KafkaConnectorResource |
| `create_or_update` | `INSERT` | `kafkaConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName, data__extendedLocation` | Create a KafkaTopicMapResource |
| `delete` | `DELETE` | `kafkaConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName` | Delete a KafkaTopicMapResource |
| `_list_by_kafka_connector_resource` | `EXEC` | `kafkaConnectorName, mqName, resourceGroupName, subscriptionId` | List KafkaTopicMapResource resources by KafkaConnectorResource |
| `update` | `EXEC` | `kafkaConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName` | Update a KafkaTopicMapResource |
