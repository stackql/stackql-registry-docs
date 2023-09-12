---
title: repos_notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_notifications
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
<tr><td><b>Name</b></td><td><code>repos_notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.activity.repos_notifications</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `repository` | `object` | Minimal Repository |
| `last_read_at` | `string` |  |
| `unread` | `boolean` |  |
| `updated_at` | `string` |  |
| `subscription_url` | `string` |  |
| `url` | `string` |  |
| `subject` | `object` |  |
| `reason` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_repo_notifications_for_authenticated_user` | `SELECT` | `owner, repo` | Lists all notifications for the current user in the specified repository. |
| `mark_repo_notifications_as_read` | `EXEC` | `owner, repo` | Marks all notifications in a repository as "read" for the current user. If the number of notifications is too large to complete in one request, you will receive a `202 Accepted` status and GitHub will run an asynchronous process to mark notifications as "read." To check whether any "unread" notifications remain, you can use the [List repository notifications for the authenticated user](https://docs.github.com/rest/activity/notifications#list-repository-notifications-for-the-authenticated-user) endpoint and pass the query parameter `all=false`. |
