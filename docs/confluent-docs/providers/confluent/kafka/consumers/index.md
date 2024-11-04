---
title: consumers
hide_title: false
hide_table_of_contents: false
keywords:
  - consumers
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
<tr><td><b>Name</b></td><td><code>consumers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.consumers" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="assignments" /> | `object` |
| <CopyableCode code="client_id" /> | `string` |
| <CopyableCode code="cluster_id" /> | `string` |
| <CopyableCode code="consumer_group_id" /> | `string` |
| <CopyableCode code="consumer_id" /> | `string` |
| <CopyableCode code="instance_id" /> | `string` |
| <CopyableCode code="kind" /> | `string` |
| <CopyableCode code="metadata" /> | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_kafka_consumer" /> | `SELECT` | <CopyableCode code="cluster_id, consumer_group_id, consumer_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Return the consumer specified by the ``consumer_id``. |
| <CopyableCode code="list_kafka_consumers" /> | `SELECT` | <CopyableCode code="cluster_id, consumer_group_id" /> | [![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Return a list of consumers that belong to the specified consumer<br />group. |
