---
title: jobs__metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs__metrics
  - dataflow
  - google    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/google/stackql-google-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>jobs__metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataflow.jobs__metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `metrics` | `array` | All metrics for this job. |
| `metricTime` | `string` | Timestamp as of which metric values are current. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_jobs_getMetrics` | `SELECT` | `jobId, projectId` |
| `projects_locations_jobs_getMetrics` | `SELECT` | `jobId, location, projectId` |
