---
title: reviews
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
<tr><td><b>Name</b></td><td><code>reviews</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.reviews</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` | Unique identifier of the review |
| `body_html` | `string` |  |
| `body_text` | `string` |  |
| `pull_request_url` | `string` |  |
| `commit_id` | `string` | A commit SHA for the review. |
| `state` | `string` |  |
| `html_url` | `string` |  |
| `user` | `object` | Simple User |
| `node_id` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `_links` | `object` |  |
| `body` | `string` | The text of the review. |
| `submitted_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_review` | `SELECT` | `owner, pull_number, repo, review_id` |  |
| `list_reviews` | `SELECT` | `owner, pull_number, repo` | The list of reviews returns in chronological order. |
| `create_review` | `INSERT` | `owner, pull_number, repo` | This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.<br /><br />Pull request reviews created in the `PENDING` state do not include the `submitted_at` property in the response.<br /><br />**Note:** To comment on a specific line in a file, you need to first determine the _position_ of that line in the diff. The GitHub REST API v3 offers the `application/vnd.github.v3.diff` [media type](https://docs.github.com/rest/overview/media-types#commits-commit-comparison-and-pull-requests). To see a pull request diff, add this media type to the `Accept` header of a call to the [single pull request](https://docs.github.com/rest/reference/pulls#get-a-pull-request) endpoint.<br /><br />The `position` value equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file. |
| `delete_pending_review` | `DELETE` | `owner, pull_number, repo, review_id` |  |
| `dismiss_review` | `EXEC` | `owner, pull_number, repo, review_id, data__message` | **Note:** To dismiss a pull request review on a [protected branch](https://docs.github.com/rest/reference/repos#branches), you must be a repository administrator or be included in the list of people or teams who can dismiss pull request reviews. |
| `submit_review` | `EXEC` | `owner, pull_number, repo, review_id, data__event` |  |
| `update_review` | `EXEC` | `owner, pull_number, repo, review_id, data__body` | Update the review summary comment with new text. |
