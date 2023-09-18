---
title: release_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - release_comments
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
<tr><td><b>Name</b></td><td><code>release_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.reactions.release_comments</code></td></tr>
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
| `list_for_release` | `SELECT` | `owner, release_id, repo` | List the reactions to a [release](https://docs.github.com/rest/releases/releases#get-a-release). |
| `create_for_release` | `INSERT` | `owner, release_id, repo, data__content` | Create a reaction to a [release](https://docs.github.com/rest/releases/releases#get-a-release). A response with a `Status: 200 OK` means that you already added the reaction type to this release. |
| `delete_for_release` | `DELETE` | `owner, reaction_id, release_id, repo` | **Note:** You can also specify a repository by `repository_id` using the route `DELETE delete /repositories/:repository_id/releases/:release_id/reactions/:reaction_id`.<br /><br />Delete a reaction to a [release](https://docs.github.com/rest/releases/releases#get-a-release). |
