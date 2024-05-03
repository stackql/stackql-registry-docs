---
title: monitor_downtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - monitor_downtimes
  - downtimes
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>monitor_downtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.downtimes.monitor_downtimes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The downtime ID. |
| <CopyableCode code="attributes" /> | `object` | Downtime match details. |
| <CopyableCode code="type" /> | `string` | Monitor Downtime Match resource type. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_monitor_downtimes" /> | `SELECT` | <CopyableCode code="monitor_id, dd_site" /> |
| <CopyableCode code="_list_monitor_downtimes" /> | `EXEC` | <CopyableCode code="monitor_id, dd_site" /> |
