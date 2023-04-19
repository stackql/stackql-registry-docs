---
title: traces_spans_billing_info
hide_title: false
hide_table_of_contents: false
keywords:
  - traces_spans_billing_info
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
<tr><td><b>Name</b></td><td><code>traces_spans_billing_info</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.tracing.traces_spans_billing_info</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `billedFormat` | `string` | Billing format of the span. Number of bytes of this representation of the span is equal to `billedBytes`. |
| `billedBytes` | `integer` | Number of bytes that were charged for the span. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getSpanBillingInfo` | `SELECT` | `spanId, traceId` |
