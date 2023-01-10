---
title: realtime
hide_title: false
hide_table_of_contents: false
keywords:
  - realtime
  - analytics
  - googleanalytics    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleanalytics/stackql-googleanalytics-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>realtime</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.realtime</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Unique ID for this data response. |
| `selfLink` | `string` | Link to this page. |
| `columnHeaders` | `array` | Column headers that list dimension names followed by the metric names. The order of dimensions and metrics is same as specified in the request. |
| `profileInfo` | `object` | Information for the view (profile), for which the real time data was requested. |
| `kind` | `string` | Resource type. |
| `rows` | `array` | Real time data rows, where each row contains a list of dimension values followed by the metric values. The order of dimensions and metrics is same as specified in the request. |
| `totalResults` | `integer` | The total number of rows for the query, regardless of the number of rows in the response. |
| `query` | `object` | Real time data request query parameters. |
| `totalsForAllResults` | `object` | Total values for the requested metrics over all the results, not just the results returned in this response. The order of the metric totals is same as the metric order specified in the request. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `data_realtime_get` | `SELECT` | `ids, metrics` |
