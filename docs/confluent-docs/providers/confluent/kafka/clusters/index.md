---
title: clusters
hide_title: false
hide_table_of_contents: false
keywords:
  - clusters
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
<tr><td><b>Name</b></td><td><code>clusters</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.kafka.clusters" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="acls" /> | `object` |
| <CopyableCode code="broker_configs" /> | `object` |
| <CopyableCode code="brokers" /> | `object` |
| <CopyableCode code="cluster_id" /> | `string` |
| <CopyableCode code="consumer_groups" /> | `object` |
| <CopyableCode code="controller" /> | `object` |
| <CopyableCode code="kind" /> | `string` |
| <CopyableCode code="metadata" /> | `object` |
| <CopyableCode code="partition_reassignments" /> | `object` |
| <CopyableCode code="topics" /> | `object` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_kafka_cluster" /> | `SELECT` | <CopyableCode code="cluster_id" /> |
