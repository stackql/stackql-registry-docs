---
title: tasks
hide_title: false
hide_table_of_contents: false
keywords:
  - tasks
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
<tr><td><b>Name</b></td><td><code>tasks</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>googleworkspace.tasks.tasks</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | Task identifier. |
| `kind` | `string` | Type of the resource. This is always "tasks#task". |
| `updated` | `string` | Last modification time of the task (as a RFC 3339 timestamp). |
| `parent` | `string` | Parent task identifier. This field is omitted if it is a top-level task. This field is read-only. Use the "move" method to move the task under a different parent or to the top level. |
| `position` | `string` | String indicating the position of the task among its sibling tasks under the same parent task or at the top level. If this string is greater than another task's corresponding position string according to lexicographical ordering, the task is positioned after the other task under the same parent task (or at the top level). This field is read-only. Use the "move" method to move the task to another position. |
| `selfLink` | `string` | URL pointing to this task. Used to retrieve, update, or delete this task. |
| `notes` | `string` | Notes describing the task. Optional. |
| `hidden` | `boolean` | Flag indicating whether the task is hidden. This is the case if the task had been marked completed when the task list was last cleared. The default is False. This field is read-only. |
| `title` | `string` | Title of the task. |
| `status` | `string` | Status of the task. This is either "needsAction" or "completed". |
| `completed` | `string` | Completion date of the task (as a RFC 3339 timestamp). This field is omitted if the task has not been completed. |
| `links` | `array` | Collection of links. This collection is read-only. |
| `deleted` | `boolean` | Flag indicating whether the task has been deleted. The default is False. |
| `due` | `string` | Due date of the task (as a RFC 3339 timestamp). Optional. The due date only records date information; the time portion of the timestamp is discarded when setting the due date. It isn't possible to read or write the time that a task is due via the API. |
| `etag` | `string` | ETag of the resource. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `task, tasklist` | Returns the specified task. |
| `list` | `SELECT` | `tasklist` | Returns all tasks in the specified task list. |
| `insert` | `INSERT` | `tasklist` | Creates a new task on the specified task list. |
| `delete` | `DELETE` | `task, tasklist` | Deletes the specified task from the task list. |
| `clear` | `EXEC` | `tasklist` | Clears all completed tasks from the specified task list. The affected tasks will be marked as 'hidden' and no longer be returned by default when retrieving all tasks for a task list. |
| `move` | `EXEC` | `task, tasklist` | Moves the specified task to another position in the task list. This can include putting it as a child task under a new parent and/or move it to a different position among its sibling tasks. |
| `patch` | `EXEC` | `task, tasklist` | Updates the specified task. This method supports patch semantics. |
| `update` | `EXEC` | `task, tasklist` | Updates the specified task. |
