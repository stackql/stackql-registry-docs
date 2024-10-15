---
title: mqtt_bridge_topic_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - mqtt_bridge_topic_maps
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

Creates, updates, deletes, gets or lists a <code>mqtt_bridge_topic_maps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mqtt_bridge_topic_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.mqtt_bridge_topic_maps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mqtt_bridge_topic_maps', value: 'view', },
        { label: 'mqtt_bridge_topic_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mqName" /> | `text` | field from the `properties` object |
| <CopyableCode code="mqttBridgeConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="mqtt_bridge_connector_ref" /> | `text` | field from the `properties` object |
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
| <CopyableCode code="properties" /> | `object` | MqttBridgeTopicMap Properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, topicMapName" /> | Get a MqttBridgeTopicMapResource |
| <CopyableCode code="list_by_mqtt_bridge_connector_resource" /> | `SELECT` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId" /> | List MqttBridgeTopicMapResource resources by MqttBridgeConnectorResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, topicMapName, data__extendedLocation" /> | Create a MqttBridgeTopicMapResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, topicMapName" /> | Delete a MqttBridgeTopicMapResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="mqName, mqttBridgeConnectorName, resourceGroupName, subscriptionId, topicMapName" /> | Update a MqttBridgeTopicMapResource |

## `SELECT` examples

List MqttBridgeTopicMapResource resources by MqttBridgeConnectorResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_mqtt_bridge_topic_maps', value: 'view', },
        { label: 'mqtt_bridge_topic_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
extended_location,
location,
mqName,
mqttBridgeConnectorName,
mqtt_bridge_connector_ref,
provisioning_state,
resourceGroupName,
routes,
subscriptionId,
tags,
topicMapName
FROM azure.iot_mq.vw_mqtt_bridge_topic_maps
WHERE mqName = '{{ mqName }}'
AND mqttBridgeConnectorName = '{{ mqttBridgeConnectorName }}'
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
FROM azure.iot_mq.mqtt_bridge_topic_maps
WHERE mqName = '{{ mqName }}'
AND mqttBridgeConnectorName = '{{ mqttBridgeConnectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mqtt_bridge_topic_maps</code> resource.

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
INSERT INTO azure.iot_mq.mqtt_bridge_topic_maps (
mqName,
mqttBridgeConnectorName,
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
'{{ mqName }}',
'{{ mqttBridgeConnectorName }}',
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
        - name: mqttBridgeConnectorRef
          value: string
        - name: routes
          value:
            - - name: direction
                value: []
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
              - name: source
                value: string
              - name: target
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

Updates a <code>mqtt_bridge_topic_maps</code> resource.

```sql
/*+ update */
UPDATE azure.iot_mq.mqtt_bridge_topic_maps
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
mqName = '{{ mqName }}'
AND mqttBridgeConnectorName = '{{ mqttBridgeConnectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicMapName = '{{ topicMapName }}';
```

## `DELETE` example

Deletes the specified <code>mqtt_bridge_topic_maps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_mq.mqtt_bridge_topic_maps
WHERE mqName = '{{ mqName }}'
AND mqttBridgeConnectorName = '{{ mqttBridgeConnectorName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicMapName = '{{ topicMapName }}';
```
