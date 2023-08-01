---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - dataplex
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
<tr><td><b>Id</b></td><td><code>google.dataplex.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `jobs` | `array` | Jobs under a given task. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_data_scans_jobs_get` | `SELECT` | `dataScansId, jobsId, locationsId, projectsId` | Gets a DataScanJob resource. |
| `projects_locations_data_scans_jobs_list` | `SELECT` | `dataScansId, locationsId, projectsId` | Lists DataScanJobs under the given DataScan. |
| `projects_locations_lakes_tasks_jobs_list` | `SELECT` | `lakesId, locationsId, projectsId, tasksId` | Lists Jobs under the given task. |
| `projects_locations_lakes_tasks_jobs_cancel` | `EXEC` | `jobsId, lakesId, locationsId, projectsId, tasksId` | Cancel jobs running for the task resource. |
| `projects_locations_lakes_tasks_jobs_get` | `EXEC` | `jobsId, lakesId, locationsId, projectsId, tasksId` | Get job resource. |
