---
title: commits_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - commits_comments
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
<tr><td><b>Name</b></td><td><code>commits_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.commits_comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `commit_id` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `position` | `integer` |  |
| `reactions` | `object` |  |
| `html_url` | `string` |  |
| `user` | `object` | A GitHub user. |
| `url` | `string` |  |
| `created_at` | `string` |  |
| `path` | `string` |  |
| `node_id` | `string` |  |
| `updated_at` | `string` |  |
| `body` | `string` |  |
| `line` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_comments_for_commit` | `SELECT` | `commit_sha, owner, repo` | Use the `:commit_sha` to specify the commit that will have its comments listed. |
| `create_commit_comment` | `INSERT` | `commit_sha, owner, repo, data__body` | Create a comment for a commit using its `:commit_sha`.<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
