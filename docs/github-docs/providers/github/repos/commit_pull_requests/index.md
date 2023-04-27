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
| `comments_url` | `string` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `html_url` | `string` |  |
| `body` | `string` |  |
| `user` | `object` | Simple User |
| `commits_url` | `string` |  |
| `patch_url` | `string` |  |
| `merged_at` | `string` |  |
| `number` | `integer` |  |
| `labels` | `array` |  |
| `title` | `string` |  |
| `assignees` | `array` |  |
| `closed_at` | `string` |  |
| `created_at` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `issue_url` | `string` |  |
| `locked` | `boolean` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `updated_at` | `string` |  |
| `merge_commit_sha` | `string` |  |
| `head` | `object` |  |
| `review_comments_url` | `string` |  |
| `review_comment_url` | `string` |  |
| `state` | `string` |  |
| `_links` | `object` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `url` | `string` |  |
| `active_lock_reason` | `string` |  |
| `diff_url` | `string` |  |
| `base` | `object` |  |
| `assignee` | `object` | Simple User |
| `requested_teams` | `array` |  |
| `statuses_url` | `string` |  |
| `requested_reviewers` | `array` |  |
| `node_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pull_requests_associated_with_commit` | `SELECT` | `commit_sha, owner, repo` |
