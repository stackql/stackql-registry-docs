---
title: mirror_topics
hide_title: false
hide_table_of_contents: false
keywords:
  - mirror_topics
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
<tr><td><b>Name</b></td><td><code>mirror_topics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.mirror_topics" /></td></tr>
</tbody></table>

## Fields
`SELECT` not supported for this resource, use `SHOW METHODS` to view available operations for the resource and then invoke a supported method using the `EXEC` command  
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="create_kafka_mirror_topic" /> | `INSERT` | <CopyableCode code="cluster_id, link_name, data__source_topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Create a topic in the destination cluster mirroring a topic in<br />the source cluster |
| <CopyableCode code="list_kafka_mirror_topics" /> | `EXEC` | <CopyableCode code="cluster_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />List all mirror topics in the cluster |
| <CopyableCode code="list_kafka_mirror_topics_under_link" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />List all mirror topics under the link |
| <CopyableCode code="read_kafka_mirror_topic" /> | `EXEC` | <CopyableCode code="cluster_id, link_name, mirror_topic_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_mirror_topics_failover" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_mirror_topics_pause" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_mirror_topics_promote" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_mirror_topics_resume" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_mirror_topics_reverse_and_pause_mirror" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_mirror_topics_reverse_and_start_mirror" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_mirror_topics_truncate_and_restore_mirror" /> | `EXEC` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
