---
title: connector_offsets_request_status
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_offsets_request_status
  - connect
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
<tr><td><b>Name</b></td><td><code>connector_offsets_request_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.connect.connector_offsets_request_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="applied_at" /> | `string` | The time at which the offsets were applied. The time is in UTC, ISO 8601 format. |
| <CopyableCode code="previous_offsets" /> | `array` | Array of offsets which are categorised into partitions. |
| <CopyableCode code="request" /> | `object` | The request made to alter offsets. |
| <CopyableCode code="status" /> | `object` | The response of the alter offsets operation. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_connectv1connector_offsets_request_status" /> | `SELECT` | <CopyableCode code="connector_name, environment_id, kafka_cluster_id" /> |
