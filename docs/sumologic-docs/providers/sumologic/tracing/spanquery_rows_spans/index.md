---
title: spanquery_rows_spans
hide_title: false
hide_table_of_contents: false
keywords:
  - spanquery_rows_spans
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
<tr><td><b>Name</b></td><td><code>spanquery_rows_spans</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.tracing.spanquery_rows_spans</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `spanPage` | `array` | List of trace spans. |
| `next` | `string` | Next continuation token. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getSpanQueryResult` | `SELECT` | `queryId, rowId, region` |
