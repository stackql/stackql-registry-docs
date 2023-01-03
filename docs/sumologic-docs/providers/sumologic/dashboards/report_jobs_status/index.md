---
title: report_jobs_status
hide_title: false
hide_table_of_contents: false
keywords:
  - report_jobs_status
  - dashboards
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
<tr><td><b>Name</b></td><td><code>report_jobs_status</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>sumologic.dashboards.report_jobs_status</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `statusMessage` | `string` | Additional status message generated if the status is not `Failed`. |
| `error` | `object` |  |
| `status` | `string` | Whether or not the request is in progress (`InProgress`), has completed successfully (`Success`), or has completed with an error (`Failed`). |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `getAsyncReportGenerationStatus` | `SELECT` | `jobId` |
