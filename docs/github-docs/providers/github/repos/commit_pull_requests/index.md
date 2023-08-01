---
title: commit_pull_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - commit_pull_requests
  - repos
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
<tr><td><b>Name</b></td><td><code>commit_pull_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.commit_pull_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `node_id` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `url` | `string` |  |
| `merged_at` | `string` |  |
| `issue_url` | `string` |  |
| `active_lock_reason` | `string` |  |
| `comments_url` | `string` |  |
| `commits_url` | `string` |  |
| `statuses_url` | `string` |  |
| `diff_url` | `string` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `patch_url` | `string` |  |
| `locked` | `boolean` |  |
| `assignee` | `object` | Simple User |
| `merge_commit_sha` | `string` |  |
| `user` | `object` | Simple User |
| `created_at` | `string` |  |
| `requested_teams` | `array` |  |
| `head` | `object` |  |
| `number` | `integer` |  |
| `title` | `string` |  |
| `closed_at` | `string` |  |
| `html_url` | `string` |  |
| `assignees` | `array` |  |
| `_links` | `object` |  |
| `base` | `object` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `labels` | `array` |  |
| `review_comments_url` | `string` |  |
| `updated_at` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `review_comment_url` | `string` |  |
| `requested_reviewers` | `array` |  |
| `state` | `string` |  |
| `body` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pull_requests_associated_with_commit` | `SELECT` | `commit_sha, owner, repo` |
