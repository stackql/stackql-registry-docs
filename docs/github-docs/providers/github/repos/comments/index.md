---
title: comments
hide_title: false
hide_table_of_contents: false
keywords:
  - comments
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
<tr><td><b>Name</b></td><td><code>comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `line` | `integer` |  |
| `created_at` | `string` |  |
| `updated_at` | `string` |  |
| `path` | `string` |  |
| `user` | `object` | A GitHub user. |
| `commit_id` | `string` |  |
| `html_url` | `string` |  |
| `reactions` | `object` |  |
| `url` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `body` | `string` |  |
| `position` | `integer` |  |
| `node_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_commit_comment` | `SELECT` | `comment_id, owner, repo` |  |
| `list_commit_comments_for_repo` | `SELECT` | `owner, repo` | Commit Comments use [these custom media types](https://docs.github.com/rest/overview/media-types). You can read more about the use of media types in the API [here](https://docs.github.com/rest/overview/media-types/).<br /><br />Comments are ordered by ascending ID. |
| `delete_commit_comment` | `DELETE` | `comment_id, owner, repo` |  |
| `update_commit_comment` | `EXEC` | `comment_id, owner, repo, data__body` |  |
