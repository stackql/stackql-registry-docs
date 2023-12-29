---
title: span_query
hide_title: false
hide_table_of_contents: false
keywords:
  - span_query
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>span_query</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.spans.span_query</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID of the Span. |
| `attributes` | `object` | JSON object containing all span attributes and their associated values. |
| `type` | `string` | Type of the span. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_spans_get` | `SELECT` | `dd_site` |
| `_list_spans_get` | `EXEC` | `dd_site` |
