---
title: traces_critical_path
hide_title: false
hide_table_of_contents: false
keywords:
  - traces_critical_path
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
<tr><td><b>Name</b></td><td><code>traces_critical_path</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.tracing.traces_critical_path</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `segments` | `array` | List of span segments from the critical path. |
| `next` | `string` | Next continuation token. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getCriticalPath` | `SELECT` | `traceId` |
