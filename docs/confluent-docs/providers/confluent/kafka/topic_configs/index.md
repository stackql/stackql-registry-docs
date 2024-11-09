---
title: topic_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - topic_configs
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

Creates, updates, deletes, gets or lists a <code>topic_configs</code> resource.

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topic_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.topic_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` |  |
| <CopyableCode code="cluster_id" /> | `string` |  |
| <CopyableCode code="is_default" /> | `boolean` |  |
| <CopyableCode code="is_read_only" /> | `boolean` |  |
| <CopyableCode code="is_sensitive" /> | `boolean` |  |
| <CopyableCode code="kind" /> | `string` |  |
| <CopyableCode code="metadata" /> | `object` |  |
| <CopyableCode code="source" /> | `string` |  |
| <CopyableCode code="synonyms" /> | `array` |  |
| <CopyableCode code="topic_name" /> | `string` |  |
| <CopyableCode code="value" /> | `string` |  |

## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_topic_config" /> | `SELECT` | <CopyableCode code="cluster_id, name, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Return the configuration parameter with the given `name`. |
| <CopyableCode code="list_kafka_all_topic_configs" /> | `SELECT` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Return the list of configuration parameters for all topics hosted by the specified
cluster. |
| <CopyableCode code="list_kafka_topic_configs" /> | `SELECT` | <CopyableCode code="cluster_id, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Return the list of configuration parameters that belong to the specified topic. |
| <CopyableCode code="delete_kafka_topic_config" /> | `DELETE` | <CopyableCode code="cluster_id, name, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Reset the configuration parameter with given `name` to its default value. |
| <CopyableCode code="update_kafka_topic_config_batch" /> | `UPDATE` | <CopyableCode code="cluster_id, topic_name, data__data" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Update or delete a set of topic configuration parameters.
Also supports a dry-run mode that only validates whether the operation would succeed if the
``validate_only`` request property is explicitly specified and set to true. |
| <CopyableCode code="update_kafka_topic_config" /> | `EXEC` | <CopyableCode code="cluster_id, name, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Update the configuration parameter with given `name`. |

## `SELECT` examples

[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)

Return the list of configuration parameters for all topics hosted by the specified
cluster.


```sql
SELECT
name,
cluster_id,
is_default,
is_read_only,
is_sensitive,
kind,
metadata,
source,
synonyms,
topic_name,
value
FROM confluent.kafka.topic_configs
WHERE cluster_id = '{{ cluster_id }}';
```
## `UPDATE` example

Updates a <code>topic_configs</code> resource.

```sql
/*+ update */
UPDATE confluent.kafka.topic_configs
SET 

WHERE 
cluster_id = '{{ cluster_id }}'
AND topic_name = '{{ topic_name }}'
AND data__data = '{{ data__data }}';
```

## `DELETE` example

Deletes the specified <code>topic_configs</code> resource.

```sql
/*+ delete */
DELETE FROM confluent.kafka.topic_configs
WHERE cluster_id = '{{ cluster_id }}'
AND name = '{{ name }}'
AND topic_name = '{{ topic_name }}';
```
