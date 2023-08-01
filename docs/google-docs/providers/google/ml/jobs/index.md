---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - ml
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
<tr><td><b>Id</b></td><td><code>google.ml.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `jobs` | `array` | The list of jobs. |
| `nextPageToken` | `string` | Optional. Pass this token as the `page_token` field of the request for a subsequent call. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_jobs_list` | `SELECT` | `projectsId` | Lists the jobs in the project. If there are no jobs that match the request parameters, the list request returns an empty response body: &#123;&#125;. |
| `projects_jobs_create` | `INSERT` | `projectsId` | Creates a training or a batch prediction job. |
| `projects_jobs_cancel` | `EXEC` | `jobsId, projectsId` | Cancels a running job. |
| `projects_jobs_get` | `EXEC` | `jobsId, projectsId` | Describes a job. |
| `projects_jobs_patch` | `EXEC` | `jobsId, projectsId` | Updates a specific job resource. Currently the only supported fields to update are `labels`. |
