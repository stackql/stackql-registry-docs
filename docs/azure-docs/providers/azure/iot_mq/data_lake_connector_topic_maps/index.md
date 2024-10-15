---
title: data_lake_connector_topic_maps
hide_title: false
hide_table_of_contents: false
keywords:
  - data_lake_connector_topic_maps
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

Creates, updates, deletes, gets or lists a <code>data_lake_connector_topic_maps</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>data_lake_connector_topic_maps</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.iot_mq.data_lake_connector_topic_maps" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_lake_connector_topic_maps', value: 'view', },
        { label: 'data_lake_connector_topic_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="dataLakeConnectorName" /> | `text` | field from the `properties` object |
| <CopyableCode code="data_lake_connector_ref" /> | `text` | field from the `properties` object |
| <CopyableCode code="extended_location" /> | `text` | field from the `properties` object |
| <CopyableCode code="location" /> | `text` | The geo-location where the resource lives |
| <CopyableCode code="mapping" /> | `text` | field from the `properties` object |
| <CopyableCode code="mqName" /> | `text` | field from the `properties` object |
| <CopyableCode code="provisioning_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="tags" /> | `text` | Resource tags. |
| <CopyableCode code="topicMapName" /> | `text` | field from the `properties` object |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="extendedLocation" /> | `object` | ExtendedLocation properties |
| <CopyableCode code="location" /> | `string` | The geo-location where the resource lives |
| <CopyableCode code="properties" /> | `object` | MQ DataLakeConnector TopicMap Resource properties |
| <CopyableCode code="tags" /> | `object` | Resource tags. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName" /> | Get a DataLakeTopicMapResource |
| <CopyableCode code="list_by_data_lake_connector_resource" /> | `SELECT` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId" /> | List DataLakeTopicMapResource resources by DataLakeConnectorResource |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName, data__extendedLocation" /> | Create a DataLakeTopicMapResource |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName" /> | Delete a DataLakeTopicMapResource |
| <CopyableCode code="update" /> | `UPDATE` | <CopyableCode code="dataLakeConnectorName, mqName, resourceGroupName, subscriptionId, topicMapName" /> | Update a DataLakeTopicMapResource |

## `SELECT` examples

List DataLakeTopicMapResource resources by DataLakeConnectorResource

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_data_lake_connector_topic_maps', value: 'view', },
        { label: 'data_lake_connector_topic_maps', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
dataLakeConnectorName,
data_lake_connector_ref,
extended_location,
location,
mapping,
mqName,
provisioning_state,
resourceGroupName,
subscriptionId,
tags,
topicMapName
FROM azure.iot_mq.vw_data_lake_connector_topic_maps
WHERE dataLakeConnectorName = '{{ dataLakeConnectorName }}'
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
FROM azure.iot_mq.data_lake_connector_topic_maps
WHERE dataLakeConnectorName = '{{ dataLakeConnectorName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>data_lake_connector_topic_maps</code> resource.

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
INSERT INTO azure.iot_mq.data_lake_connector_topic_maps (
dataLakeConnectorName,
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
'{{ dataLakeConnectorName }}',
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
        - name: dataLakeConnectorRef
          value: string
        - name: mapping
          value:
            - name: allowedLatencySecs
              value: integer
            - name: clientId
              value: string
            - name: maxMessagesPerBatch
              value: integer
            - name: messagePayloadType
              value: string
            - name: mqttSourceTopic
              value: string
            - name: qos
              value: integer
            - name: table
              value:
                - name: schema
                  value:
                    - - name: format
                        value: []
                      - name: mapping
                        value: string
                      - name: name
                        value: string
                      - name: optional
                        value: boolean
                - name: tableName
                  value: string
                - name: tablePath
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

Updates a <code>data_lake_connector_topic_maps</code> resource.

```sql
/*+ update */
UPDATE azure.iot_mq.data_lake_connector_topic_maps
SET 
tags = '{{ tags }}',
properties = '{{ properties }}'
WHERE 
dataLakeConnectorName = '{{ dataLakeConnectorName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicMapName = '{{ topicMapName }}';
```

## `DELETE` example

Deletes the specified <code>data_lake_connector_topic_maps</code> resource.

```sql
/*+ delete */
DELETE FROM azure.iot_mq.data_lake_connector_topic_maps
WHERE dataLakeConnectorName = '{{ dataLakeConnectorName }}'
AND mqName = '{{ mqName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}'
AND topicMapName = '{{ topicMapName }}';
```
