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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>pull_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.pull_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `head` | `object` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `diff_url` | `string` |  |
| `merge_commit_sha` | `string` |  |
| `locked` | `boolean` |  |
| `title` | `string` |  |
| `number` | `integer` |  |
| `comments_url` | `string` |  |
| `body` | `string` |  |
| `created_at` | `string` |  |
| `_links` | `object` |  |
| `user` | `object` | A GitHub user. |
| `statuses_url` | `string` |  |
| `commits_url` | `string` |  |
| `merged_at` | `string` |  |
| `assignees` | `array` |  |
| `closed_at` | `string` |  |
| `active_lock_reason` | `string` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `review_comment_url` | `string` |  |
| `node_id` | `string` |  |
| `assignee` | `object` | A GitHub user. |
| `html_url` | `string` |  |
| `issue_url` | `string` |  |
| `patch_url` | `string` |  |
| `state` | `string` |  |
| `base` | `object` |  |
| `labels` | `array` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `requested_reviewers` | `array` |  |
| `requested_teams` | `array` |  |
| `updated_at` | `string` |  |
| `review_comments_url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `url` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `owner, repo` |
