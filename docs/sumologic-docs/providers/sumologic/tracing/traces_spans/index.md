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
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `parentId` | `string` | Identifier of the parent span, if any. If the span has no parent it's considered a root span. |
| `fields` | `object` | Fields attached to this span. |
| `remoteService` | `string` | Name of the possible remote span's service. |
| `kind` | `string` | Span kind describes the relationship between the Span, its parents, and its children in a Trace. Possible values: `CLIENT`, `SERVER`, `PRODUCER`, `CONSUMER`, `INTERNAL`. |
| `criticalPathContribution` | `object` |  |
| `serviceType` | `string` | Defines type of service. |
| `remoteServiceColor` | `string` | Color hex code assigned to the remote service. |
| `duration` | `integer` | Number of nanoseconds the span lasted. |
| `operationName` | `string` | The name of the operation given to the span. |
| `status` | `object` |  |
| `remoteServiceType` | `string` | Defines type of service. |
| `logs` | `array` | Logs attached to this span. |
| `serviceColor` | `string` | Color hex code assigned to the service. |
| `events` | `array` | Events attached to this span. |
| `info` | `object` |  |
| `startedAt` | `string` | Date and time the span was started in the [ISO 8601 / RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `resource` | `string` | The name of the resource attached to the span. |
| `service` | `string` | The name of the service this span is part of. |
| `errorMessage` | `string` | Produced error message (could be a stack trace, database error code, ..) |
| `links` | `array` | List of casually related spans. |
| `numberOfLinks` | `integer` | Number of span links in this span. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `getSpan` | `SELECT` | `spanId, traceId` | Get details of a span with the given identifier. |
| `getSpans` | `SELECT` | `traceId` | Get a list of spans for the given trace. The response is paginated with a default limit of 100 spans per page. |
