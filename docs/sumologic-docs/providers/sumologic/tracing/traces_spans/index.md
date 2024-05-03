---
title: traces_spans
hide_title: false
hide_table_of_contents: false
keywords:
  - traces_spans
  - tracing
  - sumologic    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Sumologic resources using SQL
custom_edit_url: null
image: /img/providers/sumologic/stackql-sumologic-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>traces_spans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="sumologic.tracing.traces_spans" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | Identifier of the span. |
| <CopyableCode code="criticalPathContribution" /> | `object` |  |
| <CopyableCode code="duration" /> | `integer` | Number of nanoseconds the span lasted. |
| <CopyableCode code="errorMessage" /> | `string` | Produced error message (could be a stack trace, database error code, ..) |
| <CopyableCode code="events" /> | `array` | Events attached to this span. |
| <CopyableCode code="fields" /> | `object` | Fields attached to this span. |
| <CopyableCode code="info" /> | `object` |  |
| <CopyableCode code="kind" /> | `string` | Span kind describes the relationship between the Span, its parents, and its children in a Trace. Possible values: `CLIENT`, `SERVER`, `PRODUCER`, `CONSUMER`, `INTERNAL`. |
| <CopyableCode code="links" /> | `array` | List of casually related spans. |
| <CopyableCode code="logs" /> | `array` | Logs attached to this span. |
| <CopyableCode code="numberOfLinks" /> | `integer` | Number of span links in this span. |
| <CopyableCode code="operationName" /> | `string` | The name of the operation given to the span. |
| <CopyableCode code="parentId" /> | `string` | Identifier of the parent span, if any. If the span has no parent it's considered a root span. |
| <CopyableCode code="remoteService" /> | `string` | Name of the possible remote span's service. |
| <CopyableCode code="remoteServiceColor" /> | `string` | Color hex code assigned to the remote service. |
| <CopyableCode code="remoteServiceType" /> | `string` | Defines type of service. |
| <CopyableCode code="resource" /> | `string` | The name of the resource attached to the span. |
| <CopyableCode code="service" /> | `string` | The name of the service this span is part of. |
| <CopyableCode code="serviceColor" /> | `string` | Color hex code assigned to the service. |
| <CopyableCode code="serviceType" /> | `string` | Defines type of service. |
| <CopyableCode code="startedAt" /> | `string` | Date and time the span was started in the [ISO 8601 / RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| <CopyableCode code="status" /> | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="getSpan" /> | `SELECT` | <CopyableCode code="spanId, traceId, region" /> | Get details of a span with the given identifier. |
| <CopyableCode code="getSpans" /> | `SELECT` | <CopyableCode code="traceId, region" /> | Get a list of spans for the given trace. The response is paginated with a default limit of 100 spans per page. |
