---
title: traces_trace_events
hide_title: false
hide_table_of_contents: false
keywords:
  - traces_trace_events
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
<tr><td><b>Name</b></td><td><code>traces_trace_events</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.tracing.traces_trace_events</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `spanEvents` | `object` | Map of span ids to lists of their events, without their attributes. |
| `next` | `string` | Next continuation token. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getTraceLightEvents` | `SELECT` | `traceId` |
