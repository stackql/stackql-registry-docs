---
title: jobs_aggregated
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs_aggregated
  - dataflow
  - google    
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
<tr><td><b>Name</b></td><td><code>jobs_aggregated</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataflow.jobs_aggregated</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `failedLocation` | `array` | Zero or more messages describing the [regional endpoints] (https://cloud.google.com/dataflow/docs/concepts/regional-endpoints) that failed to respond. |
| `jobs` | `array` | A subset of the requested job information. |
| `nextPageToken` | `string` | Set if there may be more results than fit in this response. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `projects_jobs_aggregated` | `SELECT` | `projectId` |
