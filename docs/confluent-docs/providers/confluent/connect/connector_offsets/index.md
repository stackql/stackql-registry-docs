---
title: connector_offsets
hide_title: false
hide_table_of_contents: false
keywords:
  - connector_offsets
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
<tr><td><b>Name</b></td><td><code>connector_offsets</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.connect.connector_offsets" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of the connector. |
| <CopyableCode code="name" /> | `string` | The name of the connector. |
| <CopyableCode code="metadata" /> | `object` | Metadata of the connector offset. |
| <CopyableCode code="offsets" /> | `array` | Array of offsets which are categorised into partitions. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_connectv1connector_offsets" /> | `SELECT` | <CopyableCode code="connector_name, environment_id, kafka_cluster_id" /> |
