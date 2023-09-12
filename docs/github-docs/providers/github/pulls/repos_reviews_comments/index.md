---
title: repos_reviews_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_reviews_comments
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
<tr><td><b>Name</b></td><td><code>repos_reviews_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.repos_reviews_comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `diff_hunk` | `string` |  |
| `original_start_line` | `integer` | The original first line of the range for a multi-line comment. |
| `position` | `integer` |  |
| `html_url` | `string` |  |
| `start_line` | `integer` | The first line of the range for a multi-line comment. |
| `body_text` | `string` |  |
| `in_reply_to_id` | `integer` |  |
| `original_commit_id` | `string` |  |
| `user` | `object` | A GitHub user. |
| `line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `start_side` | `string` | The side of the first line of the range for a multi-line comment. |
| `_links` | `object` |  |
| `created_at` | `string` |  |
| `original_line` | `integer` | The original line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `pull_request_review_id` | `integer` |  |
| `pull_request_url` | `string` |  |
| `original_position` | `integer` |  |
| `url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `node_id` | `string` |  |
| `reactions` | `object` |  |
| `updated_at` | `string` |  |
| `path` | `string` |  |
| `body` | `string` |  |
| `commit_id` | `string` |  |
| `side` | `string` | The side of the first line of the range for a multi-line comment. |
| `body_html` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_comments_for_review` | `SELECT` | `owner, pull_number, repo, review_id` |
