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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>traces_spans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.tracing.traces_spans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Identifier of the span. |
| `remoteServiceType` | `string` | Defines type of service. |
| `remoteServiceColor` | `string` | Color hex code assigned to the remote service. |
| `info` | `object` |  |
| `operationName` | `string` | The name of the operation given to the span. |
| `duration` | `integer` | Number of nanoseconds the span lasted. |
| `remoteService` | `string` | Name of the possible remote span's service. |
| `parentId` | `string` | Identifier of the parent span, if any. If the span has no parent it's considered a root span. |
| `serviceColor` | `string` | Color hex code assigned to the service. |
| `errorMessage` | `string` | Produced error message (could be a stack trace, database error code, ..) |
| `numberOfLinks` | `integer` | Number of span links in this span. |
| `resource` | `string` | The name of the resource attached to the span. |
| `status` | `object` |  |
| `criticalPathContribution` | `object` |  |
| `links` | `array` | List of casually related spans. |
| `fields` | `object` | Fields attached to this span. |
| `kind` | `string` | Span kind describes the relationship between the Span, its parents, and its children in a Trace. Possible values: `CLIENT`, `SERVER`, `PRODUCER`, `CONSUMER`, `INTERNAL`. |
| `logs` | `array` | Logs attached to this span. |
| `startedAt` | `string` | Date and time the span was started in the [ISO 8601 / RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `serviceType` | `string` | Defines type of service. |
| `events` | `array` | Events attached to this span. |
| `service` | `string` | The name of the service this span is part of. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getSpan` | `SELECT` | `spanId, traceId` | Get details of a span with the given identifier. |
| `getSpans` | `SELECT` | `traceId` | Get a list of spans for the given trace. The response is paginated with a default limit of 100 spans per page. |
