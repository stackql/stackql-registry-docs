---
title: kafka_connector_topic_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - kafka_connector_topic_maps
  - iot_mq
  - google
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>kafka_connector_topic_maps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kafka_connector_topic_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.kafka_connector_topic_maps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kafka_connector_topic_maps', value: 'view', },
        { label: 'kafka_connector_topic_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="batching" /> | `text` | field from the `properties` object |
| <CopyableCode code="compression" /> | `text` | field from the `properties` object |
| <CopyableCode code="copy_mqtt_properties" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="kafkaConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="kafka_connector_ref" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mqName" /> | `text` | field from the `properties` object |
| <CopyableCode code="partition_key_property" /> | `text` | field from the `properties` object |
| <CopyableCode code="partition_strategy" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="routes" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="topicMapName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | KafkaTopicMap Properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName" /> | Get a KafkaTopicMapResource |
| <CopyableCode code="list_by_kafka_connector_resource" /> | `SELECT` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId" /> | List KafkaTopicMapResource resources by KafkaConnectorResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName, data__extendedLocation" /> | Create a KafkaTopicMapResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName" /> | Delete a KafkaTopicMapResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="kafkaConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName" /> | Update a KafkaTopicMapResource |

## `SELECT` examples

List KafkaTopicMapResource resources by KafkaConnectorResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kafka_connector_topic_maps', value: 'view', },
        { label: 'kafka_connector_topic_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
batching,
compression,
copy_mqtt_properties,
extended_location,
kafkaConnectorName,
kafka_connector_ref,
location,
mqName,
partition_key_property,
partition_strategy,
provisioning_state,
resourceGroupName,
routes,
subscriptionId,
tags,
topicMapName
FROM azure.iot_mq.vw_kafka_connector_topic_maps
WHERE kafkaConnectorName = '{{ kafkaConnectorName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
extendedLocation,
location,
properties,
tags
FROM azure.iot_mq.kafka_connector_topic_maps
WHERE kafkaConnectorName = '{{ kafkaConnectorName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>kafka_connector_topic_maps</code> resource.

<Tabs
    defaultValue="all"
    values={[
        { label: 'All Properties', value: 'all', },
        { label: 'Manifest', value: 'manifest', },
    ]
}>
<TabItem value="all">

```sql
/*+ create */
INSERT INTO azure.iot_mq.kafka_connector_topic_maps (
kafkaConnectorName,
mqName,
resourceGroupName,
subscriptionId,
topicMapName,
data__extendedLocation,
properties,
extendedLocation,
tags,
location
)
SELECT 
'{{ kafkaConnectorName }}',
'{{ mqName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ topicMapName }}',
'{{ data__extendedLocation }}',
'{{ properties }}',
'{{ extendedLocation }}',
'{{ tags }}',
'{{ location }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: properties
      value:
        - name: batching
          value:
            - name: enabled
              value: boolean
            - name: latencyMs
              value: integer
            - name: maxBytes
              value: integer
            - name: maxMessages
              value: integer
        - name: compression
          value: string
        - name: copyMqttProperties
          value: string
        - name: kafkaConnectorRef
          value: string
        - name: partitionKeyProperty
          value: string
        - name: partitionStrategy
          value: string
        - name: routes
          value:
            - - name: kafkaToMqtt
                value:
                  - name: consumerGroupId
                    value: string
                  - name: kafkaTopic
                    value: string
                  - name: mqttTopic
                    value: string
                  - name: name
                    value: string
                  - name: qos
                    value: integer
              - name: mqttToKafka
                value:
                  - name: kafkaAcks
                    value: []
                  - name: kafkaTopic
                    value: string
                  - name: mqttTopic
                    value: string
                  - name: name
                    value: string
                  - name: qos
                    value: integer
                  - name: sharedSubscription
                    value:
                      - name: groupMinimumShareNumber
                        value: integer
                      - name: groupName
                        value: string
        - name: provisioningState
          value: []
    - name: extendedLocation
      value:
        - name: name
          value: string
        - name: type
          value: []
    - name: tags
      value: object
    - name: location
      value: string

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>kafka_connector_topic_maps</code> resource.

```sql
/*+ update */
UPDATE azure.iot_mq.kafka_connector_topic_maps
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
kafkaConnectorName = '{{ kafkaConnectorName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicMapName = '{{ topicMapName }}';
```

## `DELETE` example

Deletes the specified <code>kafka_connector_topic_maps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_mq.kafka_connector_topic_maps
WHERE kafkaConnectorName = '{{ kafkaConnectorName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicMapName = '{{ topicMapName }}';
```
