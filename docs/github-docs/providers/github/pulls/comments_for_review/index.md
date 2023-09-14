---
title: comments_for_review
hide_title: false
hide_table_of_contents: false
keywords:
  - comments_for_review
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
<tr><td><b>Name</b></td><td><code>comments_for_review</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.comments_for_review</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `user` | `object` | A GitHub user. |
| `path` | `string` |  |
| `commit_id` | `string` |  |
| `node_id` | `string` |  |
| `diff_hunk` | `string` |  |
| `html_url` | `string` |  |
| `original_line` | `integer` | The original line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `start_side` | `string` | The side of the first line of the range for a multi-line comment. |
| `original_start_line` | `integer` | The original first line of the range for a multi-line comment. |
| `body_text` | `string` |  |
| `in_reply_to_id` | `integer` |  |
| `original_commit_id` | `string` |  |
| `pull_request_url` | `string` |  |
| `pull_request_review_id` | `integer` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `url` | `string` |  |
| `updated_at` | `string` |  |
| `body_html` | `string` |  |
| `created_at` | `string` |  |
| `start_line` | `integer` | The first line of the range for a multi-line comment. |
| `reactions` | `object` |  |
| `side` | `string` | The side of the first line of the range for a multi-line comment. |
| `original_position` | `integer` |  |
| `position` | `integer` |  |
| `body` | `string` |  |
| `_links` | `object` |  |
| `line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_comments_for_review` | `SELECT` | `owner, pull_number, repo, review_id` |
