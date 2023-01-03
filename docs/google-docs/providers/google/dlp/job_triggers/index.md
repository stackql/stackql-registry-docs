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
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `name` | `string` | Unique resource name for the triggeredJob, assigned by the service when the triggeredJob is created, for example `projects/dlp-test-project/jobTriggers/53234423`. |
| `description` | `string` | User provided description (max 256 chars) |
| `errors` | `array` | Output only. A stream of errors encountered when the trigger was activated. Repeated errors may result in the JobTrigger automatically being paused. Will return the last 100 errors. Whenever the JobTrigger is modified this list will be cleared. |
| `updateTime` | `string` | Output only. The last update timestamp of a triggeredJob. |
| `lastRunTime` | `string` | Output only. The timestamp of the last time this trigger executed. |
| `inspectJob` | `object` | Controls what and how to inspect for findings. |
| `createTime` | `string` | Output only. The creation timestamp of a triggeredJob. |
| `displayName` | `string` | Display name (max 100 chars) |
| `triggers` | `array` | A list of triggers which will be OR'ed together. Only one in the list needs to trigger for a job to be started. The list may contain only a single Schedule trigger and must have at least one object. |
| `status` | `string` | Required. A status for this trigger. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `organizations_locations_jobTriggers_get` | `SELECT` | `jobTriggersId, locationsId, organizationsId` | Gets a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `organizations_locations_jobTriggers_list` | `SELECT` | `locationsId, organizationsId` | Lists job triggers. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_jobTriggers_get` | `SELECT` | `jobTriggersId, projectsId` | Gets a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_jobTriggers_list` | `SELECT` | `projectsId` | Lists job triggers. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_locations_jobTriggers_get` | `SELECT` | `jobTriggersId, locationsId, projectsId` | Gets a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_locations_jobTriggers_list` | `SELECT` | `locationsId, projectsId` | Lists job triggers. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `organizations_locations_jobTriggers_create` | `INSERT` | `locationsId, organizationsId` | Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_jobTriggers_create` | `INSERT` | `projectsId` | Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_locations_jobTriggers_create` | `INSERT` | `locationsId, projectsId` | Creates a job trigger to run DLP actions such as scanning storage for sensitive information on a set schedule. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `organizations_locations_jobTriggers_delete` | `DELETE` | `jobTriggersId, locationsId, organizationsId` | Deletes a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_jobTriggers_delete` | `DELETE` | `jobTriggersId, projectsId` | Deletes a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_locations_jobTriggers_delete` | `DELETE` | `jobTriggersId, locationsId, projectsId` | Deletes a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `organizations_locations_jobTriggers_patch` | `EXEC` | `jobTriggersId, locationsId, organizationsId` | Updates a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_jobTriggers_activate` | `EXEC` | `jobTriggersId, projectsId` | Activate a job trigger. Causes the immediate execute of a trigger instead of waiting on the trigger event to occur. |
| `projects_jobTriggers_patch` | `EXEC` | `jobTriggersId, projectsId` | Updates a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
| `projects_locations_jobTriggers_activate` | `EXEC` | `jobTriggersId, locationsId, projectsId` | Activate a job trigger. Causes the immediate execute of a trigger instead of waiting on the trigger event to occur. |
| `projects_locations_jobTriggers_hybridInspect` | `EXEC` | `jobTriggersId, locationsId, projectsId` | Inspect hybrid content and store findings to a trigger. The inspection will be processed asynchronously. To review the findings monitor the jobs within the trigger. |
| `projects_locations_jobTriggers_patch` | `EXEC` | `jobTriggersId, locationsId, projectsId` | Updates a job trigger. See https://cloud.google.com/dlp/docs/creating-job-triggers to learn more. |
