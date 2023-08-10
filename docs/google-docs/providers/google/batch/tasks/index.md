---
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
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
<tr><td><b>Name</b></td><td><code>tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>google.batch.tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | Task name. The name is generated from the parent TaskGroup name and 'id' field. For example: "projects/123456/locations/us-west1/jobs/job01/taskGroups/group01/tasks/task01". |
| `status` | `object` | Status of a task |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobsId, locationsId, projectsId, taskGroupsId, tasksId` | Return a single Task. |
| `list` | `SELECT` | `jobsId, locationsId, projectsId, taskGroupsId` | List Tasks associated with a job. |
| `_list` | `EXEC` | `jobsId, locationsId, projectsId, taskGroupsId` | List Tasks associated with a job. |
