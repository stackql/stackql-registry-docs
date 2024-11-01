---
title: topics
hide_title: false
hide_table_of_contents: false
keywords:
  - topics
  - kafka
  - confluent    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Confluent Cloud resources using SQL.
custom_edit_url: null
image: /img/providers/confluent/stackql-confluent-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.topics" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_kafka_topic" /> | `INSERT` | <CopyableCode code="cluster_id, data__topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Create a topic.<br />Also supports a dry-run mode that only validates whether the topic creation would succeed<br />if the ``validate_only`` request property is explicitly specified and set to true. Note that<br />when dry-run mode is being used the response status would be 200 OK instead of 201 Created. |
| <CopyableCode code="delete_kafka_topic" /> | `DELETE` | <CopyableCode code="cluster_id, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Delete the topic with the given `topic_name`. |
| <CopyableCode code="update_partition_count_kafka_topic" /> | `UPDATE` | <CopyableCode code="cluster_id, topic_name, data__partitions_count" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Increase the number of partitions for a topic. |
| <CopyableCode code="get_kafka_topic" /> | `EXEC` | <CopyableCode code="cluster_id, topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Return the topic with the given `topic_name`. |
| <CopyableCode code="list_kafka_topics" /> | `EXEC` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Return the list of topics that belong to the specified Kafka cluster. |
