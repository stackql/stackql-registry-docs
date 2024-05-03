---
title: downtimes
hide_title: false
hide_table_of_contents: false
keywords:
  - downtimes
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
<tr><td><b>Name</b></td><td><code>downtimes</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.downtimes.downtimes" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The downtime ID. |
| <CopyableCode code="attributes" /> | `object` | Downtime details. |
| <CopyableCode code="relationships" /> | `object` | All relationships associated with downtime. |
| <CopyableCode code="type" /> | `string` | Downtime resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_downtime" /> | `SELECT` | <CopyableCode code="downtime_id, dd_site" /> | Get downtime detail by `downtime_id`. |
| <CopyableCode code="list_downtimes" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get all scheduled downtimes. |
| <CopyableCode code="create_downtime" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Schedule a downtime. |
| <CopyableCode code="_get_downtime" /> | `EXEC` | <CopyableCode code="downtime_id, dd_site" /> | Get downtime detail by `downtime_id`. |
| <CopyableCode code="_list_downtimes" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get all scheduled downtimes. |
| <CopyableCode code="cancel_downtime" /> | `EXEC` | <CopyableCode code="downtime_id, dd_site" /> | Cancel a downtime. |
| <CopyableCode code="update_downtime" /> | `EXEC` | <CopyableCode code="downtime_id, data__data, dd_site" /> | Update a downtime by `downtime_id`. |
