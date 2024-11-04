---
title: exporter_status
hide_title: false
hide_table_of_contents: false
keywords:
  - exporter_status
  - schema_registry
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
<tr><td><b>Name</b></td><td><code>exporter_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="confluent.schema_registry.exporter_status" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | Name of exporter. |
| <CopyableCode code="offset" /> | `integer` | Offset of the exporter |
| <CopyableCode code="state" /> | `string` | State of the exporter. Could be STARTING, RUNNING or PAUSED |
| <CopyableCode code="trace" /> | `string` | Error trace of the exporter |
| <CopyableCode code="ts" /> | `integer` | Timestamp of the exporter |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="get_exporter_status_by_name" /> | `SELECT` | <CopyableCode code="name" /> |
