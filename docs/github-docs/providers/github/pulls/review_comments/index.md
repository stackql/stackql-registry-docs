---
title: review_comments
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
<tr><td><b>Name</b></td><td><code>review_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.review_comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `body_html` | `string` |  |
| `in_reply_to_id` | `integer` |  |
| `user` | `object` | Simple User |
| `original_commit_id` | `string` |  |
| `created_at` | `string` |  |
| `path` | `string` |  |
| `_links` | `object` |  |
| `commit_id` | `string` |  |
| `original_start_line` | `integer` | The original first line of the range for a multi-line comment. |
| `start_side` | `string` | The side of the first line of the range for a multi-line comment. |
| `body_text` | `string` |  |
| `side` | `string` | The side of the first line of the range for a multi-line comment. |
| `reactions` | `object` |  |
| `body` | `string` |  |
| `diff_hunk` | `string` |  |
| `line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `updated_at` | `string` |  |
| `node_id` | `string` |  |
| `original_line` | `integer` | The original line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `pull_request_url` | `string` |  |
| `html_url` | `string` |  |
| `url` | `string` |  |
| `original_position` | `integer` |  |
| `start_line` | `integer` | The first line of the range for a multi-line comment. |
| `position` | `integer` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `pull_request_review_id` | `integer` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_comments_for_review` | `SELECT` | `owner, pull_number, repo, review_id` |
