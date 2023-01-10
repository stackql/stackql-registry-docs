---
title: tracequery_status
hide_title: false
hide_table_of_contents: false
keywords:
  - tracequery_status
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
<tr><td><b>Name</b></td><td><code>tracequery_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.tracing.tracequery_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `queryRows` | `array` | A list of trace queries. |
| `status` | `string` | Status of the query. Possible values: `Processing`, `Finished`, `Error`, `Canceled`. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getTraceQueryStatus` | `SELECT` | `queryId` |
