---
title: review_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - review_comments
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
<tr><td><b>Name</b></td><td><code>review_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.review_comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `updated_at` | `string` |  |
| `original_start_line` | `integer` | The original first line of the range for a multi-line comment. |
| `in_reply_to_id` | `integer` |  |
| `position` | `integer` |  |
| `pull_request_url` | `string` |  |
| `diff_hunk` | `string` |  |
| `body` | `string` |  |
| `line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `html_url` | `string` |  |
| `side` | `string` | The side of the first line of the range for a multi-line comment. |
| `url` | `string` |  |
| `commit_id` | `string` |  |
| `start_line` | `integer` | The first line of the range for a multi-line comment. |
| `original_line` | `integer` | The original line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `user` | `object` | Simple User |
| `reactions` | `object` |  |
| `created_at` | `string` |  |
| `original_position` | `integer` |  |
| `_links` | `object` |  |
| `original_commit_id` | `string` |  |
| `start_side` | `string` | The side of the first line of the range for a multi-line comment. |
| `pull_request_review_id` | `integer` |  |
| `path` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `body_html` | `string` |  |
| `node_id` | `string` |  |
| `body_text` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_comments_for_review` | `SELECT` | `owner, pull_number, repo, review_id` |
