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
| `name` | `string` | Output only. The relative resource name of the job, of the form: projects/&#123;project_number&#125;/locations/&#123;location_id&#125;/lakes/&#123;lake_id&#125;/tasks/&#123;task_id&#125;/jobs/&#123;job_id&#125;. |
| `retryCount` | `integer` | Output only. The number of times the job has been retried (excluding the initial attempt). |
| `message` | `string` | Output only. Additional information about the current state. |
| `state` | `string` | Output only. Execution state for the job. |
| `startTime` | `string` | Output only. The time when the job was started. |
| `serviceJob` | `string` | Output only. The full resource name for the job run under a particular service. |
| `endTime` | `string` | Output only. The time when the job ended. |
| `uid` | `string` | Output only. System generated globally unique ID for the job. |
| `service` | `string` | Output only. The underlying service running a job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_dataScans_jobs_get` | `SELECT` | `dataScansId, jobsId, locationsId, projectsId` | Gets a DataScanJob resource. |
| `projects_locations_dataScans_jobs_list` | `SELECT` | `dataScansId, locationsId, projectsId` | Lists DataScanJobs under the given DataScan. |
| `projects_locations_lakes_tasks_jobs_get` | `SELECT` | `jobsId, lakesId, locationsId, projectsId, tasksId` | Get job resource. |
| `projects_locations_lakes_tasks_jobs_list` | `SELECT` | `lakesId, locationsId, projectsId, tasksId` | Lists Jobs under the given task. |
| `projects_locations_lakes_tasks_jobs_cancel` | `EXEC` | `jobsId, lakesId, locationsId, projectsId, tasksId` | Cancel jobs running for the task resource. |
