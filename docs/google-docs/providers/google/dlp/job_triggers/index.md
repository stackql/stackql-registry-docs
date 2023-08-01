---
title: job_triggers
hide_title: false
hide_table_of_contents: false
keywords:
  - job_triggers
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
<tr><td><b>Name</b></td><td><code>job_triggers</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dlp.job_triggers</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `jobTriggers` | `array` | List of triggeredJobs, up to page_size in ListJobTriggersRequest. |
| `nextPageToken` | `string` | If the next page is available then the next page token to be used in following ListJobTriggers request. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_locations_job_triggers_get` | `SELECT` | `jobTriggersId, locationsId, organizationsId` | Gets a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `organizations_locations_job_triggers_list` | `SELECT` | `locationsId, organizationsId` | Lists job triggers. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_job_triggers_get` | `SELECT` | `jobTriggersId, projectsId` | Gets a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_job_triggers_list` | `SELECT` | `projectsId` | Lists job triggers. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_locations_job_triggers_get` | `SELECT` | `jobTriggersId, locationsId, projectsId` | Gets a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_locations_job_triggers_list` | `SELECT` | `locationsId, projectsId` | Lists job triggers. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `organizations_locations_job_triggers_create` | `INSERT` | `locationsId, organizationsId` | Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_job_triggers_create` | `INSERT` | `projectsId` | Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_locations_job_triggers_create` | `INSERT` | `locationsId, projectsId` | Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `organizations_locations_job_triggers_delete` | `DELETE` | `jobTriggersId, locationsId, organizationsId` | Deletes a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_job_triggers_delete` | `DELETE` | `jobTriggersId, projectsId` | Deletes a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_locations_job_triggers_delete` | `DELETE` | `jobTriggersId, locationsId, projectsId` | Deletes a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `organizations_locations_job_triggers_patch` | `EXEC` | `jobTriggersId, locationsId, organizationsId` | Updates a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_job_triggers_activate` | `EXEC` | `jobTriggersId, projectsId` | Activate a job trigger. Causes the immediate execute of a trigger instead of waiting on the trigger event to occur. |
| `projects_job_triggers_patch` | `EXEC` | `jobTriggersId, projectsId` | Updates a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_locations_job_triggers_activate` | `EXEC` | `jobTriggersId, locationsId, projectsId` | Activate a job trigger. Causes the immediate execute of a trigger instead of waiting on the trigger event to occur. |
| `projects_locations_job_triggers_hybrid_inspect` | `EXEC` | `jobTriggersId, locationsId, projectsId` | Inspect hybrid content and store findings to a trigger. The inspection will be processed asynchronously. To review the findings monitor the jobs within the trigger. |
| `projects_locations_job_triggers_patch` | `EXEC` | `jobTriggersId, locationsId, projectsId` | Updates a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
