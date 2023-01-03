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
<tr><td><b>Id</b></td><td><code>github.issues.comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the issue comment |
| `body_html` | `string` |  |
| `issue_url` | `string` |  |
| `body_text` | `string` |  |
| `node_id` | `string` |  |
| `url` | `string` | URL for the issue comment |
| `user` | `object` | Simple User |
| `updated_at` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `html_url` | `string` |  |
| `body` | `string` | Contents of the issue comment |
| `created_at` | `string` |  |
| `reactions` | `object` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_comment` | `SELECT` | `comment_id, owner, repo` |  |
| `list_comments` | `SELECT` | `issue_number, owner, repo` | Issue Comments are ordered by ascending ID. |
| `list_comments_for_repo` | `SELECT` | `owner, repo` | By default, Issue Comments are ordered by ascending ID. |
| `create_comment` | `INSERT` | `issue_number, owner, repo, data__body` | This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| `delete_comment` | `DELETE` | `comment_id, owner, repo` |  |
| `update_comment` | `EXEC` | `comment_id, owner, repo, data__body` |  |
