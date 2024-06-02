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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>dlp_jobs</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="dlp.dlp_jobs" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The server-assigned name. |
| <CopyableCode code="actionDetails" /> | `array` | Events that should occur after the job has completed. |
| <CopyableCode code="createTime" /> | `string` | Time when the job was created. |
| <CopyableCode code="endTime" /> | `string` | Time when the job finished. |
| <CopyableCode code="errors" /> | `array` | A stream of errors encountered running the job. |
| <CopyableCode code="inspectDetails" /> | `object` | The results of an inspect DataSource job. |
| <CopyableCode code="jobTriggerName" /> | `string` | If created by a job trigger, the resource name of the trigger that instantiated the job. |
| <CopyableCode code="lastModified" /> | `string` | Time when the job was last modified by the system. |
| <CopyableCode code="riskDetails" /> | `object` | Result of a risk analysis operation request. |
| <CopyableCode code="startTime" /> | `string` | Time when the job started. |
| <CopyableCode code="state" /> | `string` | State of a job. |
| <CopyableCode code="type" /> | `string` | The type of job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="organizations_locations_dlp_jobs_list" /> | `SELECT` | <CopyableCode code="locationsId, organizationsId" /> | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_dlp_jobs_get" /> | `SELECT` | <CopyableCode code="dlpJobsId, projectsId" /> | Gets the latest state of a long-running DlpJob. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_dlp_jobs_list" /> | `SELECT` | <CopyableCode code="projectsId" /> | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_locations_dlp_jobs_get" /> | `SELECT` | <CopyableCode code="dlpJobsId, locationsId, projectsId" /> | Gets the latest state of a long-running DlpJob. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_locations_dlp_jobs_list" /> | `SELECT` | <CopyableCode code="locationsId, projectsId" /> | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_dlp_jobs_create" /> | `INSERT` | <CopyableCode code="projectsId" /> | Creates a new job to inspect storage or calculate risk metrics. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated. |
| <CopyableCode code="projects_locations_dlp_jobs_create" /> | `INSERT` | <CopyableCode code="locationsId, projectsId" /> | Creates a new job to inspect storage or calculate risk metrics. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. When no InfoTypes or CustomInfoTypes are specified in inspect jobs, the system will automatically choose what detectors to run. By default this may be all types, but may change over time as detectors are updated. |
| <CopyableCode code="projects_dlp_jobs_delete" /> | `DELETE` | <CopyableCode code="dlpJobsId, projectsId" /> | Deletes a long-running DlpJob. This method indicates that the client is no longer interested in the DlpJob result. The job will be canceled if possible. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_locations_dlp_jobs_delete" /> | `DELETE` | <CopyableCode code="dlpJobsId, locationsId, projectsId" /> | Deletes a long-running DlpJob. This method indicates that the client is no longer interested in the DlpJob result. The job will be canceled if possible. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="_organizations_locations_dlp_jobs_list" /> | `EXEC` | <CopyableCode code="locationsId, organizationsId" /> | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="_projects_dlp_jobs_list" /> | `EXEC` | <CopyableCode code="projectsId" /> | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="_projects_locations_dlp_jobs_list" /> | `EXEC` | <CopyableCode code="locationsId, projectsId" /> | Lists DlpJobs that match the specified filter in the request. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_dlp_jobs_cancel" /> | `EXEC` | <CopyableCode code="dlpJobsId, projectsId" /> | Starts asynchronous cancellation on a long-running DlpJob. The server makes a best effort to cancel the DlpJob, but success is not guaranteed. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_locations_dlp_jobs_cancel" /> | `EXEC` | <CopyableCode code="dlpJobsId, locationsId, projectsId" /> | Starts asynchronous cancellation on a long-running DlpJob. The server makes a best effort to cancel the DlpJob, but success is not guaranteed. See https://cloud.google.com/sensitive-data-protection/docs/inspecting-storage and https://cloud.google.com/sensitive-data-protection/docs/compute-risk-analysis to learn more. |
| <CopyableCode code="projects_locations_dlp_jobs_finish" /> | `EXEC` | <CopyableCode code="dlpJobsId, locationsId, projectsId" /> | Finish a running hybrid DlpJob. Triggers the finalization steps and running of any enabled actions that have not yet run. |
| <CopyableCode code="projects_locations_dlp_jobs_hybrid_inspect" /> | `EXEC` | <CopyableCode code="dlpJobsId, locationsId, projectsId" /> | Inspect hybrid content and store findings to a job. To review the findings, inspect the job. Inspection will occur asynchronously. |
