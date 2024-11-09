---
title: topic_partitions
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_partitions
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

Creates, updates, deletes, gets or lists a <code>topic_partitions</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_partitions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.topic_partitions" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cluster_id" /> | `string` |  |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="leader" /> | `object` |  |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="partition_id" /> | `integer` |  |
| <CopyableCode code="reassignment" /> | `object` |  |
| <CopyableCode code="replicas" /> | `object` |  |
| <CopyableCode code="topic_name" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_partition" /> | `SELECT` | <CopyableCode code="cluster_id, partition_id, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Return the partition with the given `partition_id`. |
| <CopyableCode code="list_kafka_partitions" /> | `SELECT` | <CopyableCode code="cluster_id, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Return the list of partitions that belong to the specified topic. |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Return the list of partitions that belong to the specified topic.


```sql
SELECT
cluster_id,
kind,
leader,
metadata,
partition_id,
reassignment,
replicas,
topic_name
FROM confluent.kafka.topic_partitions
WHERE cluster_id = '{{ cluster_id }}'
AND topic_name = '{{ topic_name }}';
```