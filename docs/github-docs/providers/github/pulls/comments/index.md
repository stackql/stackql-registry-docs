---
title: comments
hide_title: false
hide_table_of_contents: false
keywords:
  - comments
  - pulls
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
<tr><td><b>Id</b></td><td><CopyableCode code="github.pulls.comments" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | The ID of the pull request review comment. |
| <CopyableCode code="_links" /> | `object` |  |
| <CopyableCode code="author_association" /> | `string` | How the author is associated with the repository. |
| <CopyableCode code="body" /> | `string` | The text of the comment. |
| <CopyableCode code="body_html" /> | `string` |  |
| <CopyableCode code="body_text" /> | `string` |  |
| <CopyableCode code="commit_id" /> | `string` | The SHA of the commit to which the comment applies. |
| <CopyableCode code="created_at" /> | `string` |  |
| <CopyableCode code="diff_hunk" /> | `string` | The diff of the line that the comment refers to. |
| <CopyableCode code="html_url" /> | `string` | HTML URL for the pull request review comment. |
| <CopyableCode code="in_reply_to_id" /> | `integer` | The comment ID to reply to. |
| <CopyableCode code="line" /> | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| <CopyableCode code="node_id" /> | `string` | The node ID of the pull request review comment. |
| <CopyableCode code="original_commit_id" /> | `string` | The SHA of the original commit to which the comment applies. |
| <CopyableCode code="original_line" /> | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| <CopyableCode code="original_position" /> | `integer` | The index of the original line in the diff to which the comment applies. This field is deprecated; use `original_line` instead. |
| <CopyableCode code="original_start_line" /> | `integer` | The first line of the range for a multi-line comment. |
| <CopyableCode code="path" /> | `string` | The relative path of the file to which the comment applies. |
| <CopyableCode code="position" /> | `integer` | The line index in the diff to which the comment applies. This field is deprecated; use `line` instead. |
| <CopyableCode code="pull_request_review_id" /> | `integer` | The ID of the pull request review to which the comment belongs. |
| <CopyableCode code="pull_request_url" /> | `string` | URL for the pull request that the review comment belongs to. |
| <CopyableCode code="reactions" /> | `object` |  |
| <CopyableCode code="side" /> | `string` | The side of the diff to which the comment applies. The side of the last line of the range for a multi-line comment |
| <CopyableCode code="start_line" /> | `integer` | The first line of the range for a multi-line comment. |
| <CopyableCode code="start_side" /> | `string` | The side of the first line of the range for a multi-line comment. |
| <CopyableCode code="subject_type" /> | `string` | The level at which the comment is targeted, can be a diff line or a file. |
| <CopyableCode code="updated_at" /> | `string` |  |
| <CopyableCode code="url" /> | `string` | URL for the pull request review comment |
| <CopyableCode code="user" /> | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_review_comment" /> | `SELECT` | <CopyableCode code="comment_id, owner, repo" /> | Provides details for a review comment. |
| <CopyableCode code="list_review_comments" /> | `SELECT` | <CopyableCode code="owner, pull_number, repo" /> | Lists all review comments for a pull request. By default, review comments are in ascending order by ID. |
| <CopyableCode code="list_review_comments_for_repo" /> | `SELECT` | <CopyableCode code="owner, repo" /> | Lists review comments for all pull requests in a repository. By default, review comments are in ascending order by ID. |
| <CopyableCode code="create_review_comment" /> | `INSERT` | <CopyableCode code="owner, pull_number, repo, data__body, data__commit_id, data__path" /> | <br />Creates a review comment in the pull request diff. To add a regular comment to a pull request timeline, see "[Create an issue comment](https://docs.github.com/rest/issues/comments#create-an-issue-comment)." We recommend creating a review comment using `line`, `side`, and optionally `start_line` and `start_side` if your comment applies to more than one line in the pull request diff.<br /><br />The `position` parameter is deprecated. If you use `position`, the `line`, `side`, `start_line`, and `start_side` parameters are not required.<br /><br />**Note:** The position value equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| <CopyableCode code="delete_review_comment" /> | `DELETE` | <CopyableCode code="comment_id, owner, repo" /> | Deletes a review comment. |
| <CopyableCode code="create_reply_for_review_comment" /> | `EXEC` | <CopyableCode code="comment_id, owner, pull_number, repo, data__body" /> | Creates a reply to a review comment for a pull request. For the `comment_id`, provide the ID of the review comment you are replying to. This must be the ID of a _top-level review comment_, not a reply to that comment. Replies to replies are not supported.<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| <CopyableCode code="update_review_comment" /> | `EXEC` | <CopyableCode code="comment_id, owner, repo, data__body" /> | Enables you to edit a review comment. |
