---
title: commit_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - commit_comments
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
<tr><td><b>Name</b></td><td><code>commit_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.reactions.commit_comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `node_id` | `string` |  |
| `user` | `object` | A GitHub user. |
| `content` | `string` | The reaction to use |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_for_commit_comment` | `SELECT` | `comment_id, owner, repo` | List the reactions to a [commit comment](https://docs.github.com/rest/commits/comments#get-a-commit-comment). |
| `create_for_commit_comment` | `INSERT` | `comment_id, owner, repo, data__content` | Create a reaction to a [commit comment](https://docs.github.com/rest/commits/comments#get-a-commit-comment). A response with an HTTP `200` status means that you already added the reaction type to this commit comment. |
| `delete_for_commit_comment` | `DELETE` | `comment_id, owner, reaction_id, repo` | **Note:** You can also specify a repository by `repository_id` using the route `DELETE /repositories/:repository_id/comments/:comment_id/reactions/:reaction_id`.<br /><br />Delete a reaction to a [commit comment](https://docs.github.com/rest/commits/comments#get-a-commit-comment). |
