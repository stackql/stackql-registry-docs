---
title: comments
hide_title: false
hide_table_of_contents: false
keywords:
  - comments
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.repos.comments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="author_association" /> | `string` | How the author is associated with the repository. |
| <CopyableCode code="body" /> | `string` |  |
| <CopyableCode code="commit_id" /> | `string` |  |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="line" /> | `integer` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="path" /> | `string` |  |
| <CopyableCode code="position" /> | `integer` |  |
| <CopyableCode code="reactions" /> | `object` |  |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` |  |
| <CopyableCode code="user" /> | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_commit_comment" /> | `SELECT` | <CopyableCode code="comment_id, owner, repo" /> |  |
| <CopyableCode code="list_comments_for_commit" /> | `SELECT` | <CopyableCode code="commit_sha, owner, repo" /> | Use the `:commit_sha` to specify the commit that will have its comments listed. |
| <CopyableCode code="list_commit_comments_for_repo" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Commit Comments use [these custom media types](https://docs.github.com/rest/overview/media-types). You can read more about the use of media types in the API [here](https://docs.github.com/rest/overview/media-types/).<br /><br />Comments are ordered by ascending ID. |
| <CopyableCode code="create_commit_comment" /> | `INSERT` | <CopyableCode code="commit_sha, owner, repo, data__body" /> | Create a comment for a commit using its `:commit_sha`.<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| <CopyableCode code="delete_commit_comment" /> | `DELETE` | <CopyableCode code="comment_id, owner, repo" /> |  |
| <CopyableCode code="update_commit_comment" /> | `EXEC` | <CopyableCode code="comment_id, owner, repo, data__body" /> |  |
