---
title: kafka_configurations
hide_title: false
hide_table_of_contents: false
keywords:
  - kafka_configurations
  - purview
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

Creates, updates, deletes, gets or lists a <code>kafka_configurations</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>kafka_configurations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="azure.purview.kafka_configurations" /></td></tr>
</tbody></table>

## Fields
<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kafka_configurations', value: 'view', },
        { label: 'kafka_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `text` | Gets or sets the identifier. |
| <CopyableCode code="name" /> | `text` | Gets or sets the name. |
| <CopyableCode code="accountName" /> | `text` | field from the `properties` object |
| <CopyableCode code="consumer_group" /> | `text` | field from the `properties` object |
| <CopyableCode code="credentials" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_hub_partition_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_hub_resource_id" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_hub_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_streaming_state" /> | `text` | field from the `properties` object |
| <CopyableCode code="event_streaming_type" /> | `text` | field from the `properties` object |
| <CopyableCode code="kafkaConfigurationName" /> | `text` | field from the `properties` object |
| <CopyableCode code="resourceGroupName" /> | `text` | field from the `properties` object |
| <CopyableCode code="subscriptionId" /> | `text` | field from the `properties` object |
| <CopyableCode code="system_data" /> | `text` | field from the `properties` object |
| <CopyableCode code="type" /> | `text` | Gets or sets the type. |
</TabItem>
<TabItem value="resource">

| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Gets or sets the identifier. |
| <CopyableCode code="name" /> | `string` | Gets or sets the name. |
| <CopyableCode code="properties" /> | `object` | The kafka configuration properties of the event streaming service attached to the Purview account for kafka notifications. |
| <CopyableCode code="systemData" /> | `object` | Metadata pertaining to creation and last modification of the resource. |
| <CopyableCode code="type" /> | `string` | Gets or sets the type. |
</TabItem></Tabs>

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get" /> | `SELECT` | <CopyableCode code="accountName, kafkaConfigurationName, resourceGroupName, subscriptionId" /> | Gets the kafka configuration for the account |
| <CopyableCode code="list_by_account" /> | `SELECT` | <CopyableCode code="accountName, resourceGroupName, subscriptionId" /> | Lists the Kafka configurations in the Account |
| <CopyableCode code="create_or_update" /> | `INSERT` | <CopyableCode code="accountName, kafkaConfigurationName, resourceGroupName, subscriptionId" /> | Create or update Kafka Configuration |
| <CopyableCode code="delete" /> | `DELETE` | <CopyableCode code="accountName, kafkaConfigurationName, resourceGroupName, subscriptionId" /> | Deletes a KafkaConfiguration resource. |

## `SELECT` examples

Lists the Kafka configurations in the Account

<Tabs
    defaultValue="view"
    values={[
        { label: 'vw_kafka_configurations', value: 'view', },
        { label: 'kafka_configurations', value: 'resource', },
    ]
}>
<TabItem value="view">

```sql
SELECT
id,
name,
accountName,
consumer_group,
credentials,
event_hub_partition_id,
event_hub_resource_id,
event_hub_type,
event_streaming_state,
event_streaming_type,
kafkaConfigurationName,
resourceGroupName,
subscriptionId,
system_data,
type
FROM azure.purview.vw_kafka_configurations
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem>
<TabItem value="resource">


```sql
SELECT
id,
name,
properties,
systemData,
type
FROM azure.purview.kafka_configurations
WHERE accountName = '{{ accountName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
</TabItem></Tabs>


## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>kafka_configurations</code> resource.

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
INSERT INTO azure.purview.kafka_configurations (
accountName,
kafkaConfigurationName,
resourceGroupName,
subscriptionId,
properties
)
SELECT 
'{{ accountName }}',
'{{ kafkaConfigurationName }}',
'{{ resourceGroupName }}',
'{{ subscriptionId }}',
'{{ properties }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: your_resource_model_name
  props:
    - name: id
      value: string
    - name: name
      value: string
    - name: systemData
      value: string
    - name: type
      value: string
    - name: properties
      value:
        - name: consumerGroup
          value: string
        - name: credentials
          value:
            - name: identityId
              value: string
            - name: type
              value: string
        - name: eventHubPartitionId
          value: string
        - name: eventHubResourceId
          value: string
        - name: eventHubType
          value: string
        - name: eventStreamingState
          value: string
        - name: eventStreamingType
          value: string

```
</TabItem>
</Tabs>

## `DELETE` example

Deletes the specified <code>kafka_configurations</code> resource.

```sql
/*+ delete */
DELETE FROM azure.purview.kafka_configurations
WHERE accountName = '{{ accountName }}'
AND kafkaConfigurationName = '{{ kafkaConfigurationName }}'
AND resourceGroupName = '{{ resourceGroupName }}'
AND subscriptionId = '{{ subscriptionId }}';
```
