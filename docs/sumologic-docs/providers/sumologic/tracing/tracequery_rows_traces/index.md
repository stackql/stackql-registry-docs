---
title: tracequery_rows_traces
hide_title: false
hide_table_of_contents: false
keywords:
  - tracequery_rows_traces
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
<tr><td><b>Name</b></td><td><code>tracequery_rows_traces</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.tracing.tracequery_rows_traces</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `next` | `string` | Next continuation token. |
| `results` | `array` | List of traces matching the query. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getTraceQueryResult` | `SELECT` | `queryId, rowId, region` |
