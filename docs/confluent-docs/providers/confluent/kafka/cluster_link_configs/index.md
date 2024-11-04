---
title: cluster_link_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - cluster_link_configs
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
<tr><td><b>Name</b></td><td><code>cluster_link_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.cluster_link_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="cluster_id" /> | `string` |
| <CopyableCode code="kind" /> | `string` |
| <CopyableCode code="link_name" /> | `string` |
| <CopyableCode code="metadata" /> | `object` |
| <CopyableCode code="read_only" /> | `boolean` |
| <CopyableCode code="sensitive" /> | `boolean` |
| <CopyableCode code="source" /> | `string` |
| <CopyableCode code="synonyms" /> | `array` |
| <CopyableCode code="value" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_link_configs" /> | `SELECT` | <CopyableCode code="cluster_id, config_name, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="list_kafka_link_configs" /> | `SELECT` | <CopyableCode code="cluster_id, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="delete_kafka_link_config" /> | `DELETE` | <CopyableCode code="cluster_id, config_name, link_name" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_link_config" /> | `EXEC` | <CopyableCode code="cluster_id, config_name, link_name, data__value" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) |
| <CopyableCode code="update_kafka_link_config_batch" /> | `EXEC` | <CopyableCode code="cluster_id, link_name, data__data" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Batch Alter Cluster Link Configs |
