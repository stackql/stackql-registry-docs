---
title: assignees
hide_title: false
hide_table_of_contents: false
keywords:
  - assignees
  - issues
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
<tr><td><b>Name</b></td><td><code>assignees</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.issues.assignees" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="avatar_url" /> | `string` |
| <CopyableCode code="email" /> | `string` |
| <CopyableCode code="events_url" /> | `string` |
| <CopyableCode code="followers_url" /> | `string` |
| <CopyableCode code="following_url" /> | `string` |
| <CopyableCode code="gists_url" /> | `string` |
| <CopyableCode code="gravatar_id" /> | `string` |
| <CopyableCode code="html_url" /> | `string` |
| <CopyableCode code="login" /> | `string` |
| <CopyableCode code="node_id" /> | `string` |
| <CopyableCode code="organizations_url" /> | `string` |
| <CopyableCode code="received_events_url" /> | `string` |
| <CopyableCode code="repos_url" /> | `string` |
| <CopyableCode code="site_admin" /> | `boolean` |
| <CopyableCode code="starred_at" /> | `string` |
| <CopyableCode code="starred_url" /> | `string` |
| <CopyableCode code="subscriptions_url" /> | `string` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_assignees" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists the [available assignees](https://docs.github.com/articles/assigning-issues-and-pull-requests-to-other-github-users/) for issues in a repository. |
| <CopyableCode code="add_assignees" /> | `INSERT` | <CopyableCode code="issue_number, owner, repo" /> | Adds up to 10 assignees to an issue. Users already assigned to an issue are not replaced. |
| <CopyableCode code="remove_assignees" /> | `DELETE` | <CopyableCode code="issue_number, owner, repo" /> | Removes one or more assignees from an issue. |
| <CopyableCode code="check_user_can_be_assigned" /> | `EXEC` | <CopyableCode code="assignee, owner, repo" /> | Checks if a user has permission to be assigned to an issue in this repository.<br /><br />If the `assignee` can be assigned to issues in the repository, a `204` header with no content is returned.<br /><br />Otherwise a `404` status code is returned. |
| <CopyableCode code="check_user_can_be_assigned_to_issue" /> | `EXEC` | <CopyableCode code="assignee, issue_number, owner, repo" /> | Checks if a user has permission to be assigned to a specific issue.<br /><br />If the `assignee` can be assigned to this issue, a `204` status code with no content is returned.<br /><br />Otherwise a `404` status code is returned. |
