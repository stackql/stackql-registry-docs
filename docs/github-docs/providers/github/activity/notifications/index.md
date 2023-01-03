---
title: notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.notifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `updated_at` | `string` |  |
| `subject` | `object` |  |
| `last_read_at` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `unread` | `boolean` |  |
| `url` | `string` |  |
| `reason` | `string` |  |
| `subscription_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_thread` | `SELECT` | `thread_id` |  |
| `list_notifications_for_authenticated_user` | `SELECT` |  | List all notifications for the current user, sorted by most recently updated. |
| `list_repo_notifications_for_authenticated_user` | `SELECT` | `owner, repo` | List all notifications for the current user. |
| `mark_notifications_as_read` | `EXEC` |  | Marks all notifications as "read" removes it from the [default view on GitHub](https://github.com/notifications). If the number of notifications is too large to complete in one request, you will receive a `202 Accepted` status and GitHub will run an asynchronous process to mark notifications as "read." To check whether any "unread" notifications remain, you can use the [List notifications for the authenticated user](https://docs.github.com/rest/reference/activity#list-notifications-for-the-authenticated-user) endpoint and pass the query parameter `all=false`. |
| `mark_repo_notifications_as_read` | `EXEC` | `owner, repo` | Marks all notifications in a repository as "read" removes them from the [default view on GitHub](https://github.com/notifications). If the number of notifications is too large to complete in one request, you will receive a `202 Accepted` status and GitHub will run an asynchronous process to mark notifications as "read." To check whether any "unread" notifications remain, you can use the [List repository notifications for the authenticated user](https://docs.github.com/rest/reference/activity#list-repository-notifications-for-the-authenticated-user) endpoint and pass the query parameter `all=false`. |
| `mark_thread_as_read` | `EXEC` | `thread_id` |  |
