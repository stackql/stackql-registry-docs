---
title: repos_issues_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_issues_comments
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
<tr><td><b>Name</b></td><td><code>repos_issues_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.reactions.repos_issues_comments</code></td></tr>
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
| `list_for_issue_comment` | `SELECT` | `comment_id, owner, repo` | List the reactions to an [issue comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment). |
| `create_for_issue_comment` | `INSERT` | `comment_id, owner, repo, data__content` | Create a reaction to an [issue comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment). A response with an HTTP `200` status means that you already added the reaction type to this issue comment. |
| `delete_for_issue_comment` | `DELETE` | `comment_id, owner, reaction_id, repo` | **Note:** You can also specify a repository by `repository_id` using the route `DELETE delete /repositories/:repository_id/issues/comments/:comment_id/reactions/:reaction_id`.<br /><br />Delete a reaction to an [issue comment](https://docs.github.com/rest/issues/comments#get-an-issue-comment). |
