---
title: repos_issues
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_issues
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
<tr><td><b>Name</b></td><td><code>repos_issues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.reactions.repos_issues</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `created_at` | `string` |  |
| `node_id` | `string` |  |
| `user` | `object` | A GitHub user. |
| `content` | `string` | The reaction to use |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_for_issue` | `SELECT` | `issue_number, owner, repo` | List the reactions to an [issue](https://docs.github.com/rest/issues/issues#get-an-issue). |
| `create_for_issue` | `INSERT` | `issue_number, owner, repo, data__content` | Create a reaction to an [issue](https://docs.github.com/rest/issues/issues#get-an-issue). A response with an HTTP `200` status means that you already added the reaction type to this issue. |
| `delete_for_issue` | `DELETE` | `issue_number, owner, reaction_id, repo` | **Note:** You can also specify a repository by `repository_id` using the route `DELETE /repositories/:repository_id/issues/:issue_number/reactions/:reaction_id`.<br /><br />Delete a reaction to an [issue](https://docs.github.com/rest/issues/issues#get-an-issue). |
