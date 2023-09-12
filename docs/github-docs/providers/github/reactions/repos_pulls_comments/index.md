---
title: repos_pulls_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_pulls_comments
  - reactions
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
<tr><td><b>Name</b></td><td><code>repos_pulls_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.reactions.repos_pulls_comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `content` | `string` | The reaction to use |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `user` | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_for_pull_request_review_comment` | `SELECT` | `comment_id, owner, repo` | List the reactions to a [pull request review comment](https://docs.github.com/pulls/comments#get-a-review-comment-for-a-pull-request). |
| `create_for_pull_request_review_comment` | `INSERT` | `comment_id, owner, repo, data__content` | Create a reaction to a [pull request review comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request). A response with an HTTP `200` status means that you already added the reaction type to this pull request review comment. |
| `delete_for_pull_request_comment` | `DELETE` | `comment_id, owner, reaction_id, repo` | **Note:** You can also specify a repository by `repository_id` using the route `DELETE /repositories/:repository_id/pulls/comments/:comment_id/reactions/:reaction_id.`<br /><br />Delete a reaction to a [pull request review comment](https://docs.github.com/rest/pulls/comments#get-a-review-comment-for-a-pull-request). |
