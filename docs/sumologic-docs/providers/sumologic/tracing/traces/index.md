---
title: traces
hide_title: false
hide_table_of_contents: false
keywords:
  - traces
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
<tr><td><b>Name</b></td><td><code>traces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.tracing.traces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Trace identifier. |
| `rootStatus` | `object` |  |
| `startedAt` | `string` | Date and time the trace was started in [ISO 8601 / RFC3339](https://tools.ietf.org/html/rfc3339) format. |
| `criticalPathServiceBreakdownSummary` | `object` |  |
| `metrics` | `object` | Calculated trace metrics. |
| `rootOperationName` | `string` | The name of the operation given to the root span. |
| `rootResource` | `string` | Root resource on which the trace was started. Examples: `db.query`, `http.request`, `rpc.call`, `container` |
| `rootService` | `string` | Root service which started the trace. Examples: `user-service`, `authentication-service`, `payment-service`, `/shopping-cart` |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getTrace` | `SELECT` | `traceId` |
