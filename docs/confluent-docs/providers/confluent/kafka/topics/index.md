---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
  - kafka
  - azure
  - microsoft azure
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Microsoft Azure infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/azure/stackql-azure-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>topics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.topics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="authorized_operations" /> | `array` |  |
| <CopyableCode code="cluster_id" /> | `string` |  |
| <CopyableCode code="configs" /> | `object` |  |
| <CopyableCode code="is_internal" /> | `boolean` |  |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="partition_reassignments" /> | `object` |  |
| <CopyableCode code="partitions" /> | `object` |  |
| <CopyableCode code="partitions_count" /> | `integer` |  |
| <CopyableCode code="replication_factor" /> | `integer` |  |
| <CopyableCode code="topic_name" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_topic" /> | `SELECT` | <CopyableCode code="cluster_id, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Return the topic with the given `topic_name`. |
| <CopyableCode code="list_kafka_topics" /> | `SELECT` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Return the list of topics that belong to the specified Kafka cluster. |
| <CopyableCode code="create_kafka_topic" /> | `INSERT` | <CopyableCode code="cluster_id, data__topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Create a topic.
Also supports a dry-run mode that only validates whether the topic creation would succeed
if the ``validate_only`` request property is explicitly specified and set to true. Note that
when dry-run mode is being used the response status would be 200 OK instead of 201 Created. |
| <CopyableCode code="delete_kafka_topic" /> | `DELETE` | <CopyableCode code="cluster_id, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Delete the topic with the given `topic_name`. |
| <CopyableCode code="update_partition_count_kafka_topic" /> | `UPDATE` | <CopyableCode code="cluster_id, topic_name, data__partitions_count" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Increase the number of partitions for a topic. |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Return the list of topics that belong to the specified Kafka cluster.


```sql
SELECT
authorized_operations,
cluster_id,
configs,
is_internal,
kind,
metadata,
partition_reassignments,
partitions,
partitions_count,
replication_factor,
topic_name
FROM confluent.kafka.topics
WHERE cluster_id = '{{ cluster_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>topics</code> resource.

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
INSERT INTO confluent.kafka.topics (
data__topic_name,
cluster_id
)
SELECT 
'{{ topic_name }}',
'{{ cluster_id }}',
'{{ data__topic_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: topics
  props:
    - name: cluster_id
      value: string
    - name: data__topic_name
      value: string
    - name: topic_name
      value: string
    - name: partitions_count
      value: integer
    - name: replication_factor
      value: integer
    - name: configs
      value: array
      props:
        - name: name
          value: string
        - name: value
          value: string
    - name: validate_only
      value: boolean

```
</TabItem>
</Tabs>

## `UPDATE` example

Updates a <code>topics</code> resource.

```sql
/*+ update */
UPDATE confluent.kafka.topics
SET 
partitions_count = '{{ partitions_count }}'
WHERE 
cluster_id = '{{ cluster_id }}'
AND topic_name = '{{ topic_name }}'
AND data__partitions_count = '{{ data__partitions_count }}';
```

## `DELETE` example

Deletes the specified <code>topics</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.kafka.topics
WHERE cluster_id = '{{ cluster_id }}'
AND topic_name = '{{ topic_name }}';
```
