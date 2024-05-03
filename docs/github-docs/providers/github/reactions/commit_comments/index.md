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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>commit_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.reactions.commit_comments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` |  |
| <CopyableCode code="content" /> | `string` | The reaction to use |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="user" /> | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_for_commit_comment" /> | `SELECT` | <CopyableCode code="comment_id, owner, repo" /> | List the reactions to a [commit comment](https://docs.github.com/rest/commits/comments#get-a-commit-comment). |
| <CopyableCode code="create_for_commit_comment" /> | `INSERT` | <CopyableCode code="comment_id, owner, repo, data__content" /> | Create a reaction to a [commit comment](https://docs.github.com/rest/commits/comments#get-a-commit-comment). A response with an HTTP `200` status means that you already added the reaction type to this commit comment. |
| <CopyableCode code="delete_for_commit_comment" /> | `DELETE` | <CopyableCode code="comment_id, owner, reaction_id, repo" /> | **Note:** You can also specify a repository by `repository_id` using the route `DELETE /repositories/:repository_id/comments/:comment_id/reactions/:reaction_id`.<br /><br />Delete a reaction to a [commit comment](https://docs.github.com/rest/commits/comments#get-a-commit-comment). |
