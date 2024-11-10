---
title: mirror_topics
hide_title: false
hide_table_of_contents: false
keywords:
  - mirror_topics
  - kafka
  - confluent
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage confluent resources using SQL
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';
import Tabs from '@theme/Tabs';
import TabItem from '@theme/TabItem';

Creates, updates, deletes, gets or lists a <code>mirror_topics</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>mirror_topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.mirror_topics" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="link_name" /> | `string` |  |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="mirror_lags" /> | `array` |  |
| <CopyableCode code="mirror_state_transition_errors" /> | `array` |  |
| <CopyableCode code="mirror_status" /> | `string` |  |
| <CopyableCode code="mirror_topic_name" /> | `string` |  |
| <CopyableCode code="num_partitions" /> | `integer` |  |
| <CopyableCode code="source_topic_name" /> | `string` |  |
| <CopyableCode code="state_time_ms" /> | `integer` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_kafka_mirror_topics" /> | `SELECT` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) List all mirror topics in the cluster |
| <CopyableCode code="list_kafka_mirror_topics_under_link" /> | `SELECT` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) List all mirror topics under the link |
| <CopyableCode code="read_kafka_mirror_topic" /> | `SELECT` | <CopyableCode code="cluster_id, link_name, mirror_topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="create_kafka_mirror_topic" /> | `INSERT` | <CopyableCode code="cluster_id, link_name, data__source_topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Create a topic in the destination cluster mirroring a topic in the source cluster |
| <CopyableCode code="update_kafka_mirror_topics_failover" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_mirror_topics_pause" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_mirror_topics_promote" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_mirror_topics_resume" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_mirror_topics_reverse_and_pause_mirror" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_mirror_topics_reverse_and_start_mirror" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_mirror_topics_truncate_and_restore_mirror" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) List all mirror topics in the cluster


```sql
SELECT
kind,
link_name,
metadata,
mirror_lags,
mirror_state_transition_errors,
mirror_status,
mirror_topic_name,
num_partitions,
source_topic_name,
state_time_ms
FROM confluent.kafka.mirror_topics
WHERE cluster_id = '{{ cluster_id }}';
```
## `INSERT` example

Use the following StackQL query and manifest file to create a new <code>mirror_topics</code> resource.

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
INSERT INTO confluent.kafka.mirror_topics (
data__source_topic_name,
cluster_id,
link_name
)
SELECT 
'{{ source_topic_name }}',
'{{ cluster_id }}',
'{{ link_name }}',
'{{ data__source_topic_name }}'
;
```
</TabItem>
<TabItem value="manifest">

```yaml
- name: mirror_topics
  props:
    - name: cluster_id
      value: string
    - name: link_name
      value: string
    - name: data__source_topic_name
      value: string
    - name: source_topic_name
      value: string
    - name: mirror_topic_name
      value: string
    - name: replication_factor
      value: integer
    - name: configs
      value: array

```
</TabItem>
</Tabs>
