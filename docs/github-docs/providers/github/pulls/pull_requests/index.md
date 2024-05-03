---
title: pull_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - pull_requests
  - pulls
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
<tr><td><b>Name</b></td><td><code>pull_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.pulls.pull_requests" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="_links" /> | `object` |  |
| <CopyableCode code="active_lock_reason" /> | `string` |  |
| <CopyableCode code="assignee" /> | `object` | A GitHub user. |
| <CopyableCode code="assignees" /> | `array` |  |
| <CopyableCode code="author_association" /> | `string` | How the author is associated with the repository. |
| <CopyableCode code="auto_merge" /> | `object` | The status of auto merging a pull request. |
| <CopyableCode code="base" /> | `object` |  |
| <CopyableCode code="body" /> | `string` |  |
| <CopyableCode code="closed_at" /> | `string` |  |
| <CopyableCode code="comments_url" /> | `string` |  |
| <CopyableCode code="commits_url" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="diff_url" /> | `string` |  |
| <CopyableCode code="draft" /> | `boolean` | Indicates whether or not the pull request is a draft. |
| <CopyableCode code="head" /> | `object` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="issue_url" /> | `string` |  |
| <CopyableCode code="labels" /> | `array` |  |
| <CopyableCode code="locked" /> | `boolean` |  |
| <CopyableCode code="merge_commit_sha" /> | `string` |  |
| <CopyableCode code="merged_at" /> | `string` |  |
| <CopyableCode code="milestone" /> | `object` | A collection of related issues and pull requests. |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="number" /> | `integer` |  |
| <CopyableCode code="patch_url" /> | `string` |  |
| <CopyableCode code="requested_reviewers" /> | `array` |  |
| <CopyableCode code="requested_teams" /> | `array` |  |
| <CopyableCode code="review_comment_url" /> | `string` |  |
| <CopyableCode code="review_comments_url" /> | `string` |  |
| <CopyableCode code="state" /> | `string` |  |
| <CopyableCode code="statuses_url" /> | `string` |  |
| <CopyableCode code="title" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="user" /> | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list" /> | `SELECT` | <CopyableCode code="owner, repo" /> |
