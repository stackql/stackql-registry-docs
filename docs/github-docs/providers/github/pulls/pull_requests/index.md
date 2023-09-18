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
| `_links` | `object` |  |
| `html_url` | `string` |  |
| `number` | `integer` |  |
| `head` | `object` |  |
| `locked` | `boolean` |  |
| `requested_reviewers` | `array` |  |
| `merge_commit_sha` | `string` |  |
| `url` | `string` |  |
| `statuses_url` | `string` |  |
| `assignees` | `array` |  |
| `commits_url` | `string` |  |
| `assignee` | `object` | A GitHub user. |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `updated_at` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `closed_at` | `string` |  |
| `review_comment_url` | `string` |  |
| `created_at` | `string` |  |
| `issue_url` | `string` |  |
| `merged_at` | `string` |  |
| `state` | `string` |  |
| `labels` | `array` |  |
| `comments_url` | `string` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `base` | `object` |  |
| `body` | `string` |  |
| `node_id` | `string` |  |
| `requested_teams` | `array` |  |
| `user` | `object` | A GitHub user. |
| `active_lock_reason` | `string` |  |
| `patch_url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `diff_url` | `string` |  |
| `review_comments_url` | `string` |  |
| `title` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list` | `SELECT` | `owner, repo` |
