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
| `name` | `string` | Output only. The relative resource name of the DataScanJob, of the form: projects/&#123;project&#125;/locations/&#123;location_id&#125;/dataScans/&#123;datascan_id&#125;/jobs/&#123;job_id&#125;, where project refers to a project_id or project_number and location_id refers to a GCP region. |
| `startTime` | `string` | Output only. The time when the DataScanJob was started. |
| `dataProfileResult` | `object` | DataProfileResult defines the output of DataProfileScan. Each field of the table will have field type specific profile result. |
| `endTime` | `string` | Output only. The time when the DataScanJob ended. |
| `type` | `string` | Output only. The type of the parent DataScan. |
| `uid` | `string` | Output only. System generated globally unique ID for the DataScanJob. |
| `dataProfileSpec` | `object` | DataProfileScan related setting. |
| `dataQualitySpec` | `object` | DataQualityScan related setting. |
| `dataQualityResult` | `object` | The output of a DataQualityScan. |
| `state` | `string` | Output only. Execution state for the DataScanJob. |
| `message` | `string` | Output only. Additional information about the current state. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_data_scans_jobs_get` | `SELECT` | `dataScansId, jobsId, locationsId, projectsId` | Gets a DataScanJob resource. |
| `projects_locations_data_scans_jobs_list` | `SELECT` | `dataScansId, locationsId, projectsId` | Lists DataScanJobs under the given DataScan. |
| `projects_locations_lakes_tasks_jobs_list` | `SELECT` | `lakesId, locationsId, projectsId, tasksId` | Lists Jobs under the given task. |
| `_projects_locations_data_scans_jobs_list` | `EXEC` | `dataScansId, locationsId, projectsId` | Lists DataScanJobs under the given DataScan. |
| `_projects_locations_lakes_tasks_jobs_list` | `EXEC` | `lakesId, locationsId, projectsId, tasksId` | Lists Jobs under the given task. |
| `projects_locations_lakes_tasks_jobs_cancel` | `EXEC` | `jobsId, lakesId, locationsId, projectsId, tasksId` | Cancel jobs running for the task resource. |
| `projects_locations_lakes_tasks_jobs_get` | `EXEC` | `jobsId, lakesId, locationsId, projectsId, tasksId` | Get job resource. |
