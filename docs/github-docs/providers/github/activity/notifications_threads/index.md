---
title: notifications_threads
hide_title: false
hide_table_of_contents: false
keywords:
  - notifications_threads
  - activity
  - github    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: /img/providers/github/stackql-github-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notifications_threads</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.notifications_threads</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `reason` | `string` |  |
| `url` | `string` |  |
| `subject` | `object` |  |
| `last_read_at` | `string` |  |
| `unread` | `boolean` |  |
| `updated_at` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `subscription_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_thread` | `SELECT` | `thread_id` | Gets information about a notification thread. |
| `mark_thread_as_read` | `EXEC` | `thread_id` | Marks a thread as "read." Marking a thread as "read" is equivalent to clicking a notification in your notification inbox on GitHub: https://github.com/notifications. |
