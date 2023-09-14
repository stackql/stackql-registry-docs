---
title: commit_pr_branches
hide_title: false
hide_table_of_contents: false
keywords:
  - commit_pr_branches
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
<tr><td><b>Name</b></td><td><code>commit_pr_branches</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.commit_pr_branches</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `closed_at` | `string` |  |
| `merged_at` | `string` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `statuses_url` | `string` |  |
| `node_id` | `string` |  |
| `user` | `object` | A GitHub user. |
| `locked` | `boolean` |  |
| `requested_reviewers` | `array` |  |
| `merge_commit_sha` | `string` |  |
| `patch_url` | `string` |  |
| `review_comment_url` | `string` |  |
| `review_comments_url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `comments_url` | `string` |  |
| `_links` | `object` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `created_at` | `string` |  |
| `active_lock_reason` | `string` |  |
| `updated_at` | `string` |  |
| `title` | `string` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `state` | `string` |  |
| `issue_url` | `string` |  |
| `number` | `integer` |  |
| `body` | `string` |  |
| `base` | `object` |  |
| `diff_url` | `string` |  |
| `assignees` | `array` |  |
| `commits_url` | `string` |  |
| `url` | `string` |  |
| `labels` | `array` |  |
| `requested_teams` | `array` |  |
| `assignee` | `object` | A GitHub user. |
| `head` | `object` |  |
| `html_url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pull_requests_associated_with_commit` | `SELECT` | `commit_sha, owner, repo` |
