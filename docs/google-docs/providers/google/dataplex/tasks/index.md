---
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - dataplex
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
<tr><td><b>Name</b></td><td><code>tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.dataplex.tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Output only. The relative resource name of the task, of the form: projects/{project_number}/locations/{location_id}/lakes/{lake_id}/ tasks/{task_id}. |
| `description` | `string` | Optional. Description of the task. |
| `labels` | `object` | Optional. User-defined labels for the task. |
| `executionSpec` | `object` | Execution related settings, like retry and service_account. |
| `uid` | `string` | Output only. System generated globally unique ID for the task. This ID will be different if the task is deleted and re-created with the same name. |
| `state` | `string` | Output only. Current state of the task. |
| `executionStatus` | `object` | Status of the task execution (e.g. Jobs). |
| `createTime` | `string` | Output only. The time when the task was created. |
| `displayName` | `string` | Optional. User friendly display name. |
| `spark` | `object` | User-specified config for running a Spark task. |
| `triggerSpec` | `object` | Task scheduling and trigger settings. |
| `updateTime` | `string` | Output only. The time when the task was last updated. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_tasks_get` | `SELECT` | `lakesId, locationsId, projectsId, tasksId` | Get task resource. |
| `projects_locations_lakes_tasks_list` | `SELECT` | `lakesId, locationsId, projectsId` | Lists tasks under the given lake. |
| `projects_locations_lakes_tasks_create` | `INSERT` | `lakesId, locationsId, projectsId` | Creates a task resource within a lake. |
| `projects_locations_lakes_tasks_delete` | `DELETE` | `lakesId, locationsId, projectsId, tasksId` | Delete the task resource. |
| `projects_locations_lakes_tasks_patch` | `EXEC` | `lakesId, locationsId, projectsId, tasksId` | Update the task resource. |
