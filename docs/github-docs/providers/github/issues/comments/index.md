---
title: comments
hide_title: false
hide_table_of_contents: false
keywords:
  - comments
  - issues
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
<tr><td><b>Id</b></td><td><code>github.issues.comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the issue comment |
| `body` | `string` | Contents of the issue comment |
| `reactions` | `object` |  |
| `url` | `string` | URL for the issue comment |
| `created_at` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `node_id` | `string` |  |
| `body_text` | `string` |  |
| `body_html` | `string` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `html_url` | `string` |  |
| `user` | `object` | A GitHub user. |
| `issue_url` | `string` |  |
| `updated_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_comment` | `SELECT` | `comment_id, owner, repo` | You can use the REST API to get comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request. |
| `list_comments` | `SELECT` | `issue_number, owner, repo` | You can use the REST API to list comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request.<br /><br />Issue comments are ordered by ascending ID. |
| `list_comments_for_repo` | `SELECT` | `owner, repo` | You can use the REST API to list comments on issues and pull requests for a repository. Every pull request is an issue, but not every issue is a pull request.<br /><br />By default, issue comments are ordered by ascending ID. |
| `create_comment` | `INSERT` | `issue_number, owner, repo, data__body` | <br />You can use the REST API to create comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request.<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).<br />Creating content too quickly using this endpoint may result in secondary rate limiting.<br />See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)"<br />and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)"<br />for details. |
| `delete_comment` | `DELETE` | `comment_id, owner, repo` | You can use the REST API to delete comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request. |
| `update_comment` | `EXEC` | `comment_id, owner, repo, data__body` | You can use the REST API to update comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request. |
