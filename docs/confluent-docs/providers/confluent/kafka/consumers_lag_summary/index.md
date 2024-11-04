---
title: consumers_lag_summary
hide_title: false
hide_table_of_contents: false
keywords:
  - consumers_lag_summary
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
<tr><td><b>Name</b></td><td><code>consumers_lag_summary</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.consumers_lag_summary" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="cluster_id" /> | `string` |
| <CopyableCode code="consumer_group_id" /> | `string` |
| <CopyableCode code="kind" /> | `string` |
| <CopyableCode code="max_lag" /> | `integer` |
| <CopyableCode code="max_lag_client_id" /> | `string` |
| <CopyableCode code="max_lag_consumer" /> | `object` |
| <CopyableCode code="max_lag_consumer_id" /> | `string` |
| <CopyableCode code="max_lag_instance_id" /> | `string` |
| <CopyableCode code="max_lag_partition" /> | `object` |
| <CopyableCode code="max_lag_partition_id" /> | `integer` |
| <CopyableCode code="max_lag_topic_name" /> | `string` |
| <CopyableCode code="metadata" /> | `object` |
| <CopyableCode code="total_lag" /> | `integer` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_kafka_consumer_group_lag_summary" /> | `SELECT` | <CopyableCode code="cluster_id, consumer_group_id" /> |
