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
| `html_url` | `string` |  |
| `closed_at` | `string` |  |
| `node_id` | `string` |  |
| `issue_url` | `string` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `_links` | `object` |  |
| `assignees` | `array` |  |
| `base` | `object` |  |
| `number` | `integer` |  |
| `statuses_url` | `string` |  |
| `title` | `string` |  |
| `head` | `object` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `merged_at` | `string` |  |
| `updated_at` | `string` |  |
| `labels` | `array` |  |
| `body` | `string` |  |
| `commits_url` | `string` |  |
| `state` | `string` |  |
| `patch_url` | `string` |  |
| `comments_url` | `string` |  |
| `user` | `object` | Simple User |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `created_at` | `string` |  |
| `assignee` | `object` | Simple User |
| `review_comment_url` | `string` |  |
| `merge_commit_sha` | `string` |  |
| `url` | `string` |  |
| `review_comments_url` | `string` |  |
| `active_lock_reason` | `string` |  |
| `diff_url` | `string` |  |
| `requested_reviewers` | `array` |  |
| `requested_teams` | `array` |  |
| `locked` | `boolean` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pull_requests_associated_with_commit` | `SELECT` | `commit_sha, owner, repo` |
