---
title: commits_pulls
hide_title: false
hide_table_of_contents: false
keywords:
  - commits_pulls
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
<tr><td><b>Name</b></td><td><code>commits_pulls</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.commits_pulls</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `review_comments_url` | `string` |  |
| `statuses_url` | `string` |  |
| `locked` | `boolean` |  |
| `html_url` | `string` |  |
| `assignee` | `object` | A GitHub user. |
| `diff_url` | `string` |  |
| `body` | `string` |  |
| `requested_reviewers` | `array` |  |
| `number` | `integer` |  |
| `requested_teams` | `array` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `active_lock_reason` | `string` |  |
| `labels` | `array` |  |
| `title` | `string` |  |
| `commits_url` | `string` |  |
| `node_id` | `string` |  |
| `user` | `object` | A GitHub user. |
| `base` | `object` |  |
| `state` | `string` |  |
| `head` | `object` |  |
| `issue_url` | `string` |  |
| `merge_commit_sha` | `string` |  |
| `closed_at` | `string` |  |
| `assignees` | `array` |  |
| `merged_at` | `string` |  |
| `patch_url` | `string` |  |
| `comments_url` | `string` |  |
| `url` | `string` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `review_comment_url` | `string` |  |
| `created_at` | `string` |  |
| `updated_at` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `_links` | `object` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pull_requests_associated_with_commit` | `SELECT` | `commit_sha, owner, repo` |
