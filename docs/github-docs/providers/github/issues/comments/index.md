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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.issues.comments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the issue comment |
| <CopyableCode code="author_association" /> | `string` | How the author is associated with the repository. |
| <CopyableCode code="body" /> | `string` | Contents of the issue comment |
| <CopyableCode code="body_html" /> | `string` |  |
| <CopyableCode code="body_text" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="issue_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="performed_via_github_app" /> | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| <CopyableCode code="reactions" /> | `object` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` | URL for the issue comment |
| <CopyableCode code="user" /> | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_comment" /> | `SELECT` | <CopyableCode code="comment_id, owner, repo" /> | You can use the REST API to get comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request. |
| <CopyableCode code="list_comments" /> | `SELECT` | <CopyableCode code="issue_number, owner, repo" /> | You can use the REST API to list comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request.<br /><br />Issue comments are ordered by ascending ID. |
| <CopyableCode code="list_comments_for_repo" /> | `SELECT` | <CopyableCode code="owner, repo" /> | You can use the REST API to list comments on issues and pull requests for a repository. Every pull request is an issue, but not every issue is a pull request.<br /><br />By default, issue comments are ordered by ascending ID. |
| <CopyableCode code="create_comment" /> | `INSERT` | <CopyableCode code="issue_number, owner, repo, data__body" /> | <br />You can use the REST API to create comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request.<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications).<br />Creating content too quickly using this endpoint may result in secondary rate limiting.<br />See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)"<br />and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)"<br />for details. |
| <CopyableCode code="delete_comment" /> | `DELETE` | <CopyableCode code="comment_id, owner, repo" /> | You can use the REST API to delete comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request. |
| <CopyableCode code="update_comment" /> | `EXEC` | <CopyableCode code="comment_id, owner, repo, data__body" /> | You can use the REST API to update comments on issues and pull requests. Every pull request is an issue, but not every issue is a pull request. |
