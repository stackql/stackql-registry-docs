---
title: segments
hide_title: false
hide_table_of_contents: false
keywords:
  - segments
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
<tr><td><b>Name</b></td><td><code>segments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleanalytics.analytics.segments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Segment ID. |
| `name` | `string` | Segment name. |
| `kind` | `string` | Resource type for Analytics segment. |
| `created` | `string` | Time the segment was created. |
| `updated` | `string` | Time the segment was last modified. |
| `segmentId` | `string` | Segment ID. Can be used with the 'segment' parameter in Core Reporting API. |
| `type` | `string` | Type for a segment. Possible values are "BUILT_IN" or "CUSTOM". |
| `definition` | `string` | Segment definition. |
| `selfLink` | `string` | Link for this segment. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `management_segments_list` | `SELECT` |  |
