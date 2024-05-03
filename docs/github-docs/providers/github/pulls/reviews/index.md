---
title: reviews
hide_title: false
hide_table_of_contents: false
keywords:
  - reviews
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
<tr><td><b>Name</b></td><td><code>reviews</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.pulls.reviews" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `integer` | Unique identifier of the review |
| <CopyableCode code="_links" /> | `object` |  |
| <CopyableCode code="author_association" /> | `string` | How the author is associated with the repository. |
| <CopyableCode code="body" /> | `string` | The text of the review. |
| <CopyableCode code="body_html" /> | `string` |  |
| <CopyableCode code="body_text" /> | `string` |  |
| <CopyableCode code="commit_id" /> | `string` | A commit SHA for the review. If the commit object was garbage collected or forcibly deleted, then it no longer exists in Git and this value will be `null`. |
| <CopyableCode code="html_url" /> | `string` |  |
| <CopyableCode code="node_id" /> | `string` |  |
| <CopyableCode code="pull_request_url" /> | `string` |  |
| <CopyableCode code="state" /> | `string` |  |
| <CopyableCode code="submitted_at" /> | `string` |  |
| <CopyableCode code="user" /> | `object` | A GitHub user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_review" /> | `SELECT` | <CopyableCode code="owner, pull_number, repo, review_id" /> | Retrieves a pull request review by its ID. |
| <CopyableCode code="list_reviews" /> | `SELECT` | <CopyableCode code="owner, pull_number, repo" /> | The list of reviews returns in chronological order. |
| <CopyableCode code="create_review" /> | `INSERT` | <CopyableCode code="owner, pull_number, repo" /> | This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.<br /><br />Pull request reviews created in the `PENDING` state are not submitted and therefore do not include the `submitted_at` property in the response. To create a pending review for a pull request, leave the `event` parameter blank. For more information about submitting a `PENDING` review, see "[Submit a review for a pull request](https://docs.github.com/rest/pulls/reviews#submit-a-review-for-a-pull-request)."<br /><br />**Note:** To comment on a specific line in a file, you need to first determine the _position_ of that line in the diff. The GitHub REST API offers the `application/vnd.github.v3.diff` [media type](https://docs.github.com/rest/overview/media-types#commits-commit-comparison-and-pull-requests). To see a pull request diff, add this media type to the `Accept` header of a call to the [single pull request](https://docs.github.com/rest/pulls/pulls#get-a-pull-request) endpoint.<br /><br />The `position` value equals the number of lines down from the first "@@" hunk header in the file you want to add a comment. The line just below the "@@" line is position 1, the next line is position 2, and so on. The position in the diff continues to increase through lines of whitespace and additional hunks until the beginning of a new file. |
| <CopyableCode code="delete_pending_review" /> | `DELETE` | <CopyableCode code="owner, pull_number, repo, review_id" /> | Deletes a pull request review that has not been submitted. Submitted reviews cannot be deleted. |
| <CopyableCode code="dismiss_review" /> | `EXEC` | <CopyableCode code="owner, pull_number, repo, review_id, data__message" /> | **Note:** To dismiss a pull request review on a [protected branch](https://docs.github.com/rest/branches/branch-protection), you must be a repository administrator or be included in the list of people or teams who can dismiss pull request reviews. |
| <CopyableCode code="submit_review" /> | `EXEC` | <CopyableCode code="owner, pull_number, repo, review_id, data__event" /> | Submits a pending review for a pull request. For more information about creating a pending review for a pull request, see "[Create a review for a pull request](https://docs.github.com/rest/pulls/reviews#create-a-review-for-a-pull-request)." |
| <CopyableCode code="update_review" /> | `EXEC` | <CopyableCode code="owner, pull_number, repo, review_id, data__body" /> | Update the review summary comment with new text. |
