---
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
  - run
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
<tr><td><b>Id</b></td><td><code>google.run.tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `tasks` | `array` | The resulting list of Tasks. |
| `nextPageToken` | `string` | A token indicating there are more items than page_size. Use it in the next ListTasks request to continue. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `executionsId, jobsId, locationsId, projectsId, tasksId` | Gets information about a Task. |
| `list` | `SELECT` | `executionsId, jobsId, locationsId, projectsId` | Lists Tasks from an Execution of a Job. |
