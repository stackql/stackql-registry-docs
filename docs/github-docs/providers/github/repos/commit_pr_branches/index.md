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
| `state` | `string` |  |
| `node_id` | `string` |  |
| `comments_url` | `string` |  |
| `closed_at` | `string` |  |
| `patch_url` | `string` |  |
| `labels` | `array` |  |
| `merged_at` | `string` |  |
| `issue_url` | `string` |  |
| `review_comment_url` | `string` |  |
| `title` | `string` |  |
| `user` | `object` | A GitHub user. |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `commits_url` | `string` |  |
| `_links` | `object` |  |
| `url` | `string` |  |
| `html_url` | `string` |  |
| `created_at` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `active_lock_reason` | `string` |  |
| `base` | `object` |  |
| `statuses_url` | `string` |  |
| `assignee` | `object` | A GitHub user. |
| `head` | `object` |  |
| `updated_at` | `string` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `requested_teams` | `array` |  |
| `requested_reviewers` | `array` |  |
| `review_comments_url` | `string` |  |
| `locked` | `boolean` |  |
| `diff_url` | `string` |  |
| `merge_commit_sha` | `string` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `body` | `string` |  |
| `number` | `integer` |  |
| `assignees` | `array` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pull_requests_associated_with_commit` | `SELECT` | `commit_sha, owner, repo` |
