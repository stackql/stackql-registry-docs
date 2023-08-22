---
title: jobs_metrics
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_metrics
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
<tr><td><b>Name</b></td><td><code>jobs_metrics</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataflow.jobs_metrics</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `metricTime` | `string` | Timestamp as of which metric values are current. |
| `metrics` | `array` | All metrics for this job. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_jobs_get_metrics` | `SELECT` | `jobId, projectId` |
| `projects_locations_jobs_get_metrics` | `SELECT` | `jobId, location, projectId` |
