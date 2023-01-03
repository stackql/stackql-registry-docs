---
title: traces_critical_path_breakdown_service
hide_title: false
hide_table_of_contents: false
keywords:
  - traces_critical_path_breakdown_service
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
<tr><td><b>Name</b></td><td><code>traces_critical_path_breakdown_service</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.tracing.traces_critical_path_breakdown_service</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `idleTime` | `integer` | Overall time in nanoseconds when no particular operation was in progress. |
| `elements` | `array` | List of elements representing the critical path service breakdown. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getCriticalPathServiceBreakdown` | `SELECT` | `traceId` |
