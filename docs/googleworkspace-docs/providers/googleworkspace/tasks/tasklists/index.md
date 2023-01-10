---
title: tasklists
hide_title: false
hide_table_of_contents: false
keywords:
  - tasklists
  - tasks
  - googleworkspace    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage Google Cloud Platform (GCP) infrastructure and resources using SQL
custom_edit_url: null
image: /img/providers/googleworkspace/stackql-googleworkspace-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>tasklists</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.tasks.tasklists</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Task list identifier. |
| `etag` | `string` | ETag of the resource. |
| `kind` | `string` | Type of the resource. This is always "tasks#taskList". |
| `selfLink` | `string` | URL pointing to this task list. Used to retrieve, update, or delete this task list. |
| `title` | `string` | Title of the task list. |
| `updated` | `string` | Last modification time of the task list (as a RFC 3339 timestamp). |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `tasklist` | Returns the authenticated user's specified task list. |
| `list` | `SELECT` |  | Returns all the authenticated user's task lists. |
| `insert` | `INSERT` |  | Creates a new task list and adds it to the authenticated user's task lists. |
| `delete` | `DELETE` | `tasklist` | Deletes the authenticated user's specified task list. |
| `patch` | `EXEC` | `tasklist` | Updates the authenticated user's specified task list. This method supports patch semantics. |
| `update` | `EXEC` | `tasklist` | Updates the authenticated user's specified task list. |
