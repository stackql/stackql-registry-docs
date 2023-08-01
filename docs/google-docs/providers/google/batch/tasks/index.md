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
| `tasks` | `array` | Tasks. |
| `unreachable` | `array` | Locations that could not be reached. |
| `nextPageToken` | `string` | Next page token. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `jobsId, locationsId, projectsId, taskGroupsId, tasksId` | Return a single Task. |
| `list` | `SELECT` | `jobsId, locationsId, projectsId, taskGroupsId` | List Tasks associated with a job. |
