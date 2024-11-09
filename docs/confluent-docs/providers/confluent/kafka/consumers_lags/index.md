---
title: consumers_lags
hide_title: false
hide_table_of_contents: false
keywords:
  - consumers_lags
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

Creates, updates, deletes, gets or lists a <code>consumers_lags</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumers_lags</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.consumers_lags" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="client_id" /> | `string` |  |
| <CopyableCode code="cluster_id" /> | `string` |  |
| <CopyableCode code="consumer_group_id" /> | `string` |  |
| <CopyableCode code="consumer_id" /> | `string` |  |
| <CopyableCode code="current_offset" /> | `integer` |  |
| <CopyableCode code="instance_id" /> | `string` |  |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="lag" /> | `integer` |  |
| <CopyableCode code="log_end_offset" /> | `integer` |  |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="partition_id" /> | `integer` |  |
| <CopyableCode code="topic_name" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_consumer_lag" /> | `SELECT` | <CopyableCode code="cluster_id, consumer_group_id, partition_id, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Available in dedicated clusters only](https://img.shields.io/badge/-Available%20in%20dedicated%20clusters%20only-%23bc8540)](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#dedicated-cluster)

Return the consumer lag on a partition with the given `partition_id`. |
| <CopyableCode code="list_kafka_consumer_lags" /> | `SELECT` | <CopyableCode code="cluster_id, consumer_group_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Available in dedicated clusters only](https://img.shields.io/badge/-Available%20in%20dedicated%20clusters%20only-%23bc8540)](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#dedicated-cluster)

Return a list of consumer lags of the consumers belonging to the
specified consumer group. |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Available in dedicated clusters only](https://img.shields.io/badge/-Available%20in%20dedicated%20clusters%20only-%23bc8540)](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#dedicated-cluster)

Return a list of consumer lags of the consumers belonging to the
specified consumer group.


```sql
SELECT
client_id,
cluster_id,
consumer_group_id,
consumer_id,
current_offset,
instance_id,
kind,
lag,
log_end_offset,
metadata,
partition_id,
topic_name
FROM confluent.kafka.consumers_lags
WHERE cluster_id = '{{ cluster_id }}'
AND consumer_group_id = '{{ consumer_group_id }}';
```