---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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

Creates, updates, deletes, gets or lists a <code>clusters</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="acls" /> | `object` |  |
| <CopyableCode code="broker_configs" /> | `object` |  |
| <CopyableCode code="brokers" /> | `object` |  |
| <CopyableCode code="cluster_id" /> | `string` |  |
| <CopyableCode code="consumer_groups" /> | `object` |  |
| <CopyableCode code="controller" /> | `object` |  |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="partition_reassignments" /> | `object` |  |
| <CopyableCode code="topics" /> | `object` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_cluster" /> | `SELECT` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Return the Kafka cluster with the specified ``cluster_id``. |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Return the Kafka cluster with the specified ``cluster_id``.


```sql
SELECT
acls,
broker_configs,
brokers,
cluster_id,
consumer_groups,
controller,
kind,
metadata,
partition_reassignments,
topics
FROM confluent.kafka.clusters
WHERE cluster_id = '{{ cluster_id }}';
```