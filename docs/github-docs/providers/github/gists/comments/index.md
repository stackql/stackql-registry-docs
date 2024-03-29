---
title: comments
hide_title: false
hide_table_of_contents: false
keywords:
  - comments
  - gists
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
<tr><td><b>Name</b></td><td><code>comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.gists.comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `user` | `object` | A GitHub user. |
| `author_association` | `string` | How the author is associated with the repository. |
| `body` | `string` | The comment text. |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `get_comment` | `SELECT` | `comment_id, gist_id` |
| `list_comments` | `SELECT` | `gist_id` |
| `create_comment` | `INSERT` | `gist_id, data__body` |
| `delete_comment` | `DELETE` | `comment_id, gist_id` |
| `update_comment` | `EXEC` | `comment_id, gist_id, data__body` |
