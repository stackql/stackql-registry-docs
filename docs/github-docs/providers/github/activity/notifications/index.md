---
title: notifications
hide_title: false
hide_table_of_contents: false
keywords:
  - notifications
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>notifications</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.activity.notifications" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="last_read_at" /> | `string` |  |
| <CopyableCode code="reason" /> | `string` |  |
| <CopyableCode code="repository" /> | `object` | Minimal Repository |
| <CopyableCode code="subject" /> | `object` |  |
| <CopyableCode code="subscription_url" /> | `string` |  |
| <CopyableCode code="unread" /> | `boolean` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_thread" /> | `SELECT` | <CopyableCode code="thread_id" /> | Gets information about a notification thread. |
| <CopyableCode code="list_notifications_for_authenticated_user" /> | `SELECT` |  | List all notifications for the current user, sorted by most recently updated. |
| <CopyableCode code="list_repo_notifications_for_authenticated_user" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists all notifications for the current user in the specified repository. |
| <CopyableCode code="mark_notifications_as_read" /> | `EXEC` |  | Marks all notifications as "read" for the current user. If the number of notifications is too large to complete in one request, you will receive a `202 Accepted` status and GitHub will run an asynchronous process to mark notifications as "read." To check whether any "unread" notifications remain, you can use the [List notifications for the authenticated user](https://docs.github.com/rest/activity/notifications#list-notifications-for-the-authenticated-user) endpoint and pass the query parameter `all=false`. |
| <CopyableCode code="mark_repo_notifications_as_read" /> | `EXEC` | <CopyableCode code="owner, repo" /> | Marks all notifications in a repository as "read" for the current user. If the number of notifications is too large to complete in one request, you will receive a `202 Accepted` status and GitHub will run an asynchronous process to mark notifications as "read." To check whether any "unread" notifications remain, you can use the [List repository notifications for the authenticated user](https://docs.github.com/rest/activity/notifications#list-repository-notifications-for-the-authenticated-user) endpoint and pass the query parameter `all=false`. |
| <CopyableCode code="mark_thread_as_read" /> | `EXEC` | <CopyableCode code="thread_id" /> | Marks a thread as "read." Marking a thread as "read" is equivalent to clicking a notification in your notification inbox on GitHub: https://github.com/notifications. |
