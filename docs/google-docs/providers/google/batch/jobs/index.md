---
title: jobs
hide_title: false
hide_table_of_contents: false
keywords:
  - jobs
  - batch
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
<tr><td><b>Id</b></td><td><code>google.batch.jobs</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. Job name. For example: "projects/123456/locations/us-central1/jobs/job01". |
| `labels` | `object` | Labels for the Job. Labels could be user provided or system generated. For example, "labels": &#123; "department": "finance", "environment": "test" &#125; You can assign up to 64 labels. [Google Compute Engine label restrictions](https://cloud.google.com/compute/docs/labeling-resources#restrictions) apply. Label names that start with "goog-" or "google-" are reserved. |
| `priority` | `string` | Priority of the Job. The valid value range is [0, 100). A job with higher priority value is more likely to run earlier if all other requirements are satisfied. |
| `notifications` | `array` | Notification configurations. |
| `updateTime` | `string` | Output only. The last time the Job was updated. |
| `logsPolicy` | `object` | LogsPolicy describes how outputs from a Job's Tasks (stdout/stderr) will be preserved. |
| `taskGroups` | `array` | Required. TaskGroups in the Job. Only one TaskGroup is supported now. |
| `status` | `object` | Job status. |
| `allocationPolicy` | `object` | A Job's resource allocation policy describes when, where, and how compute resources should be allocated for the Job. |
| `createTime` | `string` | Output only. When the Job was created. |
| `uid` | `string` | Output only. A system generated unique ID (in UUID4 format) for the Job. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_jobs_get` | `SELECT` | `jobsId, locationsId, projectsId` | Get a Job specified by its resource name. |
| `projects_locations_jobs_list` | `SELECT` | `locationsId, projectsId` | List all Jobs for a project within a region. |
| `projects_locations_jobs_create` | `INSERT` | `locationsId, projectsId` | Create a Job. |
| `projects_locations_jobs_delete` | `DELETE` | `jobsId, locationsId, projectsId` | Delete a Job. |
