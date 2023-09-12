---
title: repos_comments
hide_title: false
hide_table_of_contents: false
keywords:
  - repos_comments
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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>repos_comments</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.repos_comments</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | The ID of the pull request review comment. |
| `node_id` | `string` | The node ID of the pull request review comment. |
| `pull_request_review_id` | `integer` | The ID of the pull request review to which the comment belongs. |
| `diff_hunk` | `string` | The diff of the line that the comment refers to. |
| `_links` | `object` |  |
| `body_text` | `string` |  |
| `original_line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `position` | `integer` | The line index in the diff to which the comment applies. This field is deprecated; use `line` instead. |
| `original_start_line` | `integer` | The first line of the range for a multi-line comment. |
| `html_url` | `string` | HTML URL for the pull request review comment. |
| `created_at` | `string` |  |
| `start_line` | `integer` | The first line of the range for a multi-line comment. |
| `pull_request_url` | `string` | URL for the pull request that the review comment belongs to. |
| `side` | `string` | The side of the diff to which the comment applies. The side of the last line of the range for a multi-line comment |
| `start_side` | `string` | The side of the first line of the range for a multi-line comment. |
| `body_html` | `string` |  |
| `line` | `integer` | The line of the blob to which the comment applies. The last line of the range for a multi-line comment |
| `original_commit_id` | `string` | The SHA of the original commit to which the comment applies. |
| `updated_at` | `string` |  |
| `commit_id` | `string` | The SHA of the commit to which the comment applies. |
| `reactions` | `object` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `path` | `string` | The relative path of the file to which the comment applies. |
| `url` | `string` | URL for the pull request review comment |
| `body` | `string` | The text of the comment. |
| `subject_type` | `string` | The level at which the comment is targeted, can be a diff line or a file. |
| `in_reply_to_id` | `integer` | The comment ID to reply to. |
| `original_position` | `integer` | The index of the original line in the diff to which the comment applies. This field is deprecated; use `original_line` instead. |
| `user` | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_review_comment` | `SELECT` | `comment_id, owner, repo` | Provides details for a review comment. |
| `list_review_comments` | `SELECT` | `owner, pull_number, repo` | Lists all review comments for a pull request. By default, review comments are in ascending order by ID. |
| `list_review_comments_for_repo` | `SELECT` | `owner, repo` | Lists review comments for all pull requests in a repository. By default, review comments are in ascending order by ID. |
| `create_review_comment` | `INSERT` | `owner, pull_number, repo, data__body, data__commit_id, data__path` | <br />Creates a review comment in the pull request diff. To add a regular comment to a pull request timeline, see "[Create an issue comment](https://docs.github.com/rest/issues/comments#create-an-issue-comment)." We recommend creating a review comment using `line`, `side`, and optionally `start_line` and `start_side` if your comment applies to more than one line in the pull request diff.<br /><br />The `position` parameter is deprecated. If you use `position`, the `line`, `side`, `start_line`, and `start_side` parameters are not required.<br /><br />**Note:** The position value equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file.<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| `delete_review_comment` | `DELETE` | `comment_id, owner, repo` | Deletes a review comment. |
| `update_review_comment` | `EXEC` | `comment_id, owner, repo, data__body` | Enables you to edit a review comment. |
