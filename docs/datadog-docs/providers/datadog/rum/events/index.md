---
title: events
hide_title: false
hide_table_of_contents: false
keywords:
  - events
  - rum
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
<tr><td><b>Name</b></td><td><code>events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.rum.events" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Unique ID of the event. |
| <CopyableCode code="attributes" /> | `object` | JSON object containing all event attributes and their associated values. |
| <CopyableCode code="type" /> | `string` | Type of the event. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_rum_events" /> | `SELECT` | <CopyableCode code="dd_site" /> | List endpoint returns events that match a RUM search query.<br />[Results are paginated][1].<br /><br />Use this endpoint to see your latest RUM events.<br /><br />[1]: https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination |
| <CopyableCode code="_list_rum_events" /> | `EXEC` | <CopyableCode code="dd_site" /> | List endpoint returns events that match a RUM search query.<br />[Results are paginated][1].<br /><br />Use this endpoint to see your latest RUM events.<br /><br />[1]: https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination |
| <CopyableCode code="aggregate_rum_events" /> | `EXEC` | <CopyableCode code="dd_site" /> | The API endpoint to aggregate RUM events into buckets of computed metrics and timeseries. |
| <CopyableCode code="search_rum_events" /> | `EXEC` | <CopyableCode code="dd_site" /> | List endpoint returns RUM events that match a RUM search query.<br />[Results are paginated][1].<br /><br />Use this endpoint to build complex RUM events filtering and search.<br /><br />[1]: https://docs.datadoghq.com/logs/guide/collect-multiple-logs-with-pagination |
