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
image: /img/providers/google/stackql-google-provider-featured-image.png
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
| `nextPageToken` | `string` | Token to retrieve the next page of results, or empty if there are no more results in the list. |
| `tasks` | `array` | Tasks under the given parent lake. |
| `unreachableLocations` | `array` | Locations that could not be reached. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `projects_locations_lakes_tasks_list` | `SELECT` | `lakesId, locationsId, projectsId` | Lists tasks under the given lake. |
| `projects_locations_lakes_tasks_create` | `INSERT` | `lakesId, locationsId, projectsId` | Creates a task resource within a lake. |
| `projects_locations_lakes_tasks_delete` | `DELETE` | `lakesId, locationsId, projectsId, tasksId` | Delete the task resource. |
| `projects_locations_lakes_tasks_get` | `EXEC` | `lakesId, locationsId, projectsId, tasksId` | Get task resource. |
| `projects_locations_lakes_tasks_patch` | `EXEC` | `lakesId, locationsId, projectsId, tasksId` | Update the task resource. |
| `projects_locations_lakes_tasks_run` | `EXEC` | `lakesId, locationsId, projectsId, tasksId` | Run an on demand execution of a Task. |
