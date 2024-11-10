---
title: cluster_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_configs
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

Creates, updates, deletes, gets or lists a <code>cluster_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>cluster_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.cluster_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="cluster_id" /> | `string` |  |
| <CopyableCode code="config_type" /> | `string` |  |
| <CopyableCode code="is_default" /> | `boolean` |  |
| <CopyableCode code="is_read_only" /> | `boolean` |  |
| <CopyableCode code="is_sensitive" /> | `boolean` |  |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="source" /> | `string` |  |
| <CopyableCode code="synonyms" /> | `array` |  |
| <CopyableCode code="value" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_cluster_config" /> | `SELECT` | <CopyableCode code="cluster_id, name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Return the dynamic cluster-wide broker configuration parameter specified by ``name``. |
| <CopyableCode code="list_kafka_cluster_configs" /> | `SELECT` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Return a list of dynamic cluster-wide broker configuration parameters for the specified Kafka cluster. Returns an empty list if there are no dynamic cluster-wide broker configuration parameters. |
| <CopyableCode code="delete_kafka_cluster_config" /> | `DELETE` | <CopyableCode code="cluster_id, name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Reset the configuration parameter specified by ``name`` to its default value by deleting a dynamic cluster-wide configuration. |
| <CopyableCode code="update_kafka_cluster_configs" /> | `UPDATE` | <CopyableCode code="cluster_id, data__data" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Update or delete a set of dynamic cluster-wide broker configuration parameters. |
| <CopyableCode code="update_kafka_cluster_config" /> | `EXEC` | <CopyableCode code="cluster_id, name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Update the dynamic cluster-wide broker configuration parameter specified by ``name``. |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Return a list of dynamic cluster-wide broker configuration parameters for the specified Kafka cluster. Returns an empty list if there are no dynamic cluster-wide broker configuration parameters.


```sql
SELECT
name,
cluster_id,
config_type,
is_default,
is_read_only,
is_sensitive,
kind,
metadata,
source,
synonyms,
value
FROM confluent.kafka.cluster_configs
WHERE cluster_id = '{{ cluster_id }}';
```
## `UPDATE` example

Updates a <code>cluster_configs</code> resource.

```sql
/*+ update */
UPDATE confluent.kafka.cluster_configs
SET 
data = '{{ data }}'
WHERE 
cluster_id = '{{ cluster_id }}'
AND data__data = '{{ data__data }}';
```

## `DELETE` example

Deletes the specified <code>cluster_configs</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.kafka.cluster_configs
WHERE cluster_id = '{{ cluster_id }}'
AND name = '{{ name }}';
```
