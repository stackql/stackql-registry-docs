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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `jobs` | `array` | A list of DlpJobs that matches the specified filter in the request. |
| `nextPageToken` | `string` | The standard List next-page token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_locations_dlp_jobs_list` | `SELECT` | `locationsId, organizationsId` | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_dlp_jobs_get` | `SELECT` | `dlpJobsId, projectsId` | Gets the latest state of a long-running DlpJob. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_dlp_jobs_list` | `SELECT` | `projectsId` | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_locations_dlp_jobs_get` | `SELECT` | `dlpJobsId, locationsId, projectsId` | Gets the latest state of a long-running DlpJob. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_locations_dlp_jobs_list` | `SELECT` | `locationsId, projectsId` | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_dlp_jobs_create` | `INSERT` | `projectsId` | Creates a new job to inspect storage or calculate risk metrics. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated. |
| `projects_locations_dlp_jobs_create` | `INSERT` | `locationsId, projectsId` | Creates a new job to inspect storage or calculate risk metrics. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated. |
| `projects_dlp_jobs_delete` | `DELETE` | `dlpJobsId, projectsId` | Deletes a long-running DlpJob. This method indicates that the client is no longer interested in the DlpJob result. The job will be canceled if possible. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_locations_dlp_jobs_delete` | `DELETE` | `dlpJobsId, locationsId, projectsId` | Deletes a long-running DlpJob. This method indicates that the client is no longer interested in the DlpJob result. The job will be canceled if possible. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_dlp_jobs_cancel` | `EXEC` | `dlpJobsId, projectsId` | Starts asynchronous cancellation on a long-running DlpJob. The server makes a best effort to cancel the DlpJob, but success is not guaranteed. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_locations_dlp_jobs_cancel` | `EXEC` | `dlpJobsId, locationsId, projectsId` | Starts asynchronous cancellation on a long-running DlpJob. The server makes a best effort to cancel the DlpJob, but success is not guaranteed. See https://cloud.google.com/dlp/docs/inspecting-storage and https://cloud.google.com/dlp/docs/compute-risk-analysis to learn more. |
| `projects_locations_dlp_jobs_finish` | `EXEC` | `dlpJobsId, locationsId, projectsId` | Finish a running hybrid DlpJob. Triggers the finalization steps and running of any enabled actions that have not yet run. |
| `projects_locations_dlp_jobs_hybrid_inspect` | `EXEC` | `dlpJobsId, locationsId, projectsId` | Inspect hybrid content and store findings to a job. To review the findings, inspect the job. Inspection will occur asynchronously. |
