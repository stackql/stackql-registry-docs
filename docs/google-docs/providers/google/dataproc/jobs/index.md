---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - dataproc
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
<tr><td><b>Name</b></td><td><code>jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataproc.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `jobs` | `array` | Output only. Jobs list. |
| `nextPageToken` | `string` | Optional. This token is included in the response if there are more results to fetch. To fetch additional results, provide this value as the page_token in a subsequent ListJobsRequest. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_regions_jobs_list` | `SELECT` | `projectId, region` | Lists regions/&#123;region&#125;/jobs in a project. |
| `projects_regions_jobs_delete` | `DELETE` | `jobId, projectId, region` | Deletes the job from the project. If the job is active, the delete fails, and the response returns FAILED_PRECONDITION. |
| `projects_regions_jobs_cancel` | `EXEC` | `jobId, projectId, region` | Starts a job cancellation request. To access the job resource after cancellation, call regions/&#123;region&#125;/jobs.list (https://cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.jobs/list) or regions/&#123;region&#125;/jobs.get (https://cloud.google.com/dataproc/docs/reference/rest/v1/projects.regions.jobs/get). |
| `projects_regions_jobs_get` | `EXEC` | `jobId, projectId, region` | Gets the resource representation for a job in a project. |
| `projects_regions_jobs_patch` | `EXEC` | `jobId, projectId, region` | Updates a job in a project. |
| `projects_regions_jobs_submit` | `EXEC` | `projectId, region` | Submits a job to a cluster. |
| `projects_regions_jobs_submit_as_operation` | `EXEC` | `projectId, region` | Submits job to a cluster. |
