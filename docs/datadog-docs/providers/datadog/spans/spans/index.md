---
title: spans
hide_title: false
hide_table_of_contents: false
keywords:
  - spans
  - spans
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
<tr><td><b>Name</b></td><td><code>spans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.spans.spans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="data" /> | `array` | Array of spans matching the request. |
| <CopyableCode code="links" /> | `object` | Links attributes. |
| <CopyableCode code="meta" /> | `object` | The metadata associated with a request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_spans" /> | `SELECT` | <CopyableCode code="dd_site" /> | List endpoint returns spans that match a span search query.<br />[Results are paginated][1].<br /><br />Use this endpoint to build complex spans filtering and search.<br />This endpoint is rate limited to `300` requests per hour.<br /><br />[1]: /logs/guide/collect-multiple-logs-with-pagination?tab=v2api |
| <CopyableCode code="aggregate_spans" /> | `EXEC` | <CopyableCode code="dd_site" /> | The API endpoint to aggregate spans into buckets and compute metrics and timeseries.<br />This endpoint is rate limited to `300` requests per hour. |
