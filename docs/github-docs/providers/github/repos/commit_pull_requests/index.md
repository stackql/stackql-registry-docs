---
title: commit_pull_requests
hide_title: false
hide_table_of_contents: false
keywords:
  - stackql
  - github
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy and manage GitHub resources using SQL
custom_edit_url: null
image: https://storage.googleapis.com/stackql-web-assets/blog/stackql-blog-post-featured-image.png
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
| `requested_reviewers` | `array` |  |
| `number` | `integer` |  |
| `merged_at` | `string` |  |
| `diff_url` | `string` |  |
| `user` | `object` | Simple User |
| `locked` | `boolean` |  |
| `issue_url` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `_links` | `object` |  |
| `base` | `object` |  |
| `state` | `string` |  |
| `assignee` | `object` | Simple User |
| `patch_url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `html_url` | `string` |  |
| `comments_url` | `string` |  |
| `commits_url` | `string` |  |
| `head` | `object` |  |
| `updated_at` | `string` |  |
| `requested_teams` | `array` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `assignees` | `array` |  |
| `labels` | `array` |  |
| `title` | `string` |  |
| `review_comments_url` | `string` |  |
| `node_id` | `string` |  |
| `statuses_url` | `string` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `created_at` | `string` |  |
| `closed_at` | `string` |  |
| `url` | `string` |  |
| `body` | `string` |  |
| `merge_commit_sha` | `string` |  |
| `review_comment_url` | `string` |  |
| `active_lock_reason` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_pull_requests_associated_with_commit` | `SELECT` | `commit_sha, owner, repo` |
