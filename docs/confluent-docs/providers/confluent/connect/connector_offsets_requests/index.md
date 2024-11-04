---
title: connector_offsets_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_offsets_requests
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
<tr><td><b>Name</b></td><td><code>connector_offsets_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.connect.connector_offsets_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="applied_at" /> | `string` | The time at which the offsets were applied. The time is in UTC, ISO 8601 format. |
| <CopyableCode code="previous_offsets" /> | `array` | Array of offsets which are categorised into partitions. |
| <CopyableCode code="request" /> | `object` | The request made to alter offsets. |
| <CopyableCode code="status" /> | `object` | The response of the alter offsets operation. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_connectv1connector_offsets_request_status" /> | `SELECT` | <CopyableCode code="connector_name, environment_id, kafka_cluster_id" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Get the status of the previous alter offset request. |
| <CopyableCode code="alter_connectv1connector_offsets_request" /> | `EXEC` | <CopyableCode code="connector_name, environment_id, kafka_cluster_id, data__type" /> | [![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)<br /><br />Request to alter the offsets of a connector. This supports the ability to PATCH/DELETE the offsets of a connector.<br />Note, you will see momentary downtime as this will internally stop the connector, while the offsets are being altered.<br />You can only make one alter offsets request at a time for a connector. |
