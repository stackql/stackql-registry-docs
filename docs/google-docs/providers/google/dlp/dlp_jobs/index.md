---
title: dlp_jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - dlp_jobs
  - dlp
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
<tr><td><b>Name</b></td><td><code>dlp_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dlp.dlp_jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The server-assigned name. |
| `type` | `string` | The type of job. |
| `jobTriggerName` | `string` | If created by a job trigger, the resource name of the trigger that instantiated the job. |
| `endTime` | `string` | Time when the job finished. |
| `state` | `string` | State of a job. |
| `createTime` | `string` | Time when the job was created. |
| `inspectDetails` | `object` | The results of an inspect DataSource job. |
| `errors` | `array` | A stream of errors encountered running the job. |
| `startTime` | `string` | Time when the job started. |
| `riskDetails` | `object` | Result of a risk analysis operation request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_locations_dlpJobs_list` | `SELECT` | `locationsId, organizationsId` | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_dlpJobs_get` | `SELECT` | `dlpJobsId, projectsId` | Gets the latest state of a long-running DlpJob. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_dlpJobs_list` | `SELECT` | `projectsId` | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_locations_dlpJobs_get` | `SELECT` | `dlpJobsId, locationsId, projectsId` | Gets the latest state of a long-running DlpJob. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_locations_dlpJobs_list` | `SELECT` | `locationsId, projectsId` | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_dlpJobs_create` | `INSERT` | `projectsId` | Creates a new job to inspect storage or calculate risk metrics. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated. |
| `projects_locations_dlpJobs_create` | `INSERT` | `locationsId, projectsId` | Creates a new job to inspect storage or calculate risk metrics. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated. |
| `projects_dlpJobs_delete` | `DELETE` | `dlpJobsId, projectsId` | Deletes a long-running DlpJob. This method indicates that the client is no longer interested in the DlpJob result. The job will be cancelled if possible. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_locations_dlpJobs_delete` | `DELETE` | `dlpJobsId, locationsId, projectsId` | Deletes a long-running DlpJob. This method indicates that the client is no longer interested in the DlpJob result. The job will be cancelled if possible. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_dlpJobs_cancel` | `EXEC` | `dlpJobsId, projectsId` | Starts asynchronous cancellation on a long-running DlpJob. The server makes a best effort to cancel the DlpJob, but success is not guaranteed. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_locations_dlpJobs_cancel` | `EXEC` | `dlpJobsId, locationsId, projectsId` | Starts asynchronous cancellation on a long-running DlpJob. The server makes a best effort to cancel the DlpJob, but success is not guaranteed. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_locations_dlpJobs_finish` | `EXEC` | `dlpJobsId, locationsId, projectsId` | Finish a running hybrid DlpJob. Triggers the finalization steps and running of any enabled actions that have not yet run. |
| `projects_locations_dlpJobs_hybridInspect` | `EXEC` | `dlpJobsId, locationsId, projectsId` | Inspect hybrid content and store findings to a job. To review the findings, inspect the job. Inspection will occur asynchronously. |
