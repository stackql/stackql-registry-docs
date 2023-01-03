---
title: pull_request_review_comment_reactions
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
<tr><td><b>Name</b></td><td><code>pull_request_review_comment_reactions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.reactions.pull_request_review_comment_reactions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `user` | `object` | Simple User |
| `content` | `string` | The reaction to use |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_for_pull_request_review_comment` | `SELECT` | `comment_id, owner, repo` | List the reactions to a [pull request review comment](https://docs.github.com/rest/reference/pulls#review-comments). |
| `create_for_pull_request_review_comment` | `INSERT` | `comment_id, owner, repo, data__content` | Create a reaction to a [pull request review comment](https://docs.github.com/rest/reference/pulls#comments). A response with an HTTP `200` status means that you already added the reaction type to this pull request review comment. |
| `delete_for_pull_request_comment` | `DELETE` | `comment_id, owner, reaction_id, repo` | **Note:** You can also specify a repository by `repository_id` using the route `DELETE /repositories/:repository_id/pulls/comments/:comment_id/reactions/:reaction_id.`<br /><br />Delete a reaction to a [pull request review comment](https://docs.github.com/rest/reference/pulls#review-comments). |
