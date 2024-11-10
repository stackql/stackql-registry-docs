---
title: consumer_groups
hide_title: false
hide_table_of_contents: false
keywords:
  - consumer_groups
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

Creates, updates, deletes, gets or lists a <code>consumer_groups</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumer_groups</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.consumer_groups" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cluster_id" /> | `string` |  |
| <CopyableCode code="consumer" /> | `object` |  |
| <CopyableCode code="consumer_group_id" /> | `string` |  |
| <CopyableCode code="coordinator" /> | `object` |  |
| <CopyableCode code="is_simple" /> | `boolean` |  |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="lag_summary" /> | `object` |  |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="partition_assignor" /> | `string` |  |
| <CopyableCode code="state" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_consumer_group" /> | `SELECT` | <CopyableCode code="cluster_id, consumer_group_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Return the consumer group specified by the ``consumer_group_id``. |
| <CopyableCode code="list_kafka_consumer_groups" /> | `SELECT` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Return the list of consumer groups that belong to the specified Kafka cluster. |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Return the list of consumer groups that belong to the specified Kafka cluster.


```sql
SELECT
cluster_id,
consumer,
consumer_group_id,
coordinator,
is_simple,
kind,
lag_summary,
metadata,
partition_assignor,
state
FROM confluent.kafka.consumer_groups
WHERE cluster_id = '{{ cluster_id }}';
```