---
title: consumers_lag_summary
hide_title: false
hide_table_of_contents: false
keywords:
  - consumers_lag_summary
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

Creates, updates, deletes, gets or lists a <code>consumers_lag_summary</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>consumers_lag_summary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.consumers_lag_summary" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="cluster_id" /> | `string` |  |
| <CopyableCode code="consumer_group_id" /> | `string` |  |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="max_lag" /> | `integer` |  |
| <CopyableCode code="max_lag_client_id" /> | `string` |  |
| <CopyableCode code="max_lag_consumer" /> | `object` |  |
| <CopyableCode code="max_lag_consumer_id" /> | `string` |  |
| <CopyableCode code="max_lag_instance_id" /> | `string` |  |
| <CopyableCode code="max_lag_partition" /> | `object` |  |
| <CopyableCode code="max_lag_partition_id" /> | `integer` |  |
| <CopyableCode code="max_lag_topic_name" /> | `string` |  |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="total_lag" /> | `integer` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_consumer_group_lag_summary" /> | `SELECT` | <CopyableCode code="cluster_id, consumer_group_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Available in dedicated clusters only](https://img.shields.io/badge/-Available%20in%20dedicated%20clusters%20only-%23bc8540)](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#dedicated-cluster)

Return the maximum and total lag of the consumers belonging to the
specified consumer group. |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Available in dedicated clusters only](https://img.shields.io/badge/-Available%20in%20dedicated%20clusters%20only-%23bc8540)](https://docs.confluent.io/cloud/current/clusters/cluster-types.html#dedicated-cluster)

Return the maximum and total lag of the consumers belonging to the
specified consumer group.


```sql
SELECT
cluster_id,
consumer_group_id,
kind,
max_lag,
max_lag_client_id,
max_lag_consumer,
max_lag_consumer_id,
max_lag_instance_id,
max_lag_partition,
max_lag_partition_id,
max_lag_topic_name,
metadata,
total_lag
FROM confluent.kafka.consumers_lag_summary
WHERE cluster_id = '{{ cluster_id }}'
AND consumer_group_id = '{{ consumer_group_id }}';
```