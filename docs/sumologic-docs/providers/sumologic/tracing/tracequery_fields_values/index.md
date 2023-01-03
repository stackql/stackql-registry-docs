---
title: tracequery_fields_values
hide_title: false
hide_table_of_contents: false
keywords:
  - tracequery_fields_values
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
<tr><td><b>Name</b></td><td><code>tracequery_fields_values</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.tracing.tracequery_fields_values</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `fieldValues` | `array` | List of filter field values. |
| `next` | `string` | Next continuation token. |
| `totalCount` | `integer` | Total number of values for a field matching the query. Can be approximated when it's above 3000. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getTraceQueryFieldValues` | `SELECT` | `field` |
