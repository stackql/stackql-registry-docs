---
title: default_topic_configs
hide_title: false
hide_table_of_contents: false
keywords:
  - default_topic_configs
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
<tr><td><b>Name</b></td><td><code>default_topic_configs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.default_topic_configs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="data" /> | `array` |
| <CopyableCode code="kind" /> | `string` |
| <CopyableCode code="metadata" /> | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_kafka_default_topic_configs" /> | `SELECT` | <CopyableCode code="cluster_id, topic_name" /> |
