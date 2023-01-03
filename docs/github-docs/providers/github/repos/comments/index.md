---
title: comments
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
<tr><td><b>Name</b></td><td><code>comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `body` | `string` |  |
| `created_at` | `string` |  |
| `html_url` | `string` |  |
| `node_id` | `string` |  |
| `path` | `string` |  |
| `reactions` | `object` |  |
| `commit_id` | `string` |  |
| `position` | `integer` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `line` | `integer` |  |
| `updated_at` | `string` |  |
| `url` | `string` |  |
| `user` | `object` | Simple User |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_commit_comment` | `SELECT` | `comment_id, owner, repo` |  |
| `list_comments_for_commit` | `SELECT` | `commit_sha, owner, repo` | Use the `:commit_sha` to specify the commit that will have its comments listed. |
| `list_commit_comments_for_repo` | `SELECT` | `owner, repo` | Commit Comments use [these custom media types](https://docs.github.com/rest/reference/repos#custom-media-types). You can read more about the use of media types in the API [here](https://docs.github.com/rest/overview/media-types/).<br /><br />Comments are ordered by ascending ID. |
| `create_commit_comment` | `INSERT` | `commit_sha, owner, repo, data__body` | Create a comment for a commit using its `:commit_sha`.<br /><br />This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| `delete_commit_comment` | `DELETE` | `comment_id, owner, repo` |  |
| `update_commit_comment` | `EXEC` | `comment_id, owner, repo, data__body` |  |
