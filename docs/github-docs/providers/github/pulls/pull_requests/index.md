---
title: pull_requests
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
<tr><td><b>Name</b></td><td><code>pull_requests</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.pull_requests</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `base` | `object` |  |
| `review_comments_url` | `string` |  |
| `rebaseable` | `boolean` |  |
| `deletions` | `integer` |  |
| `number` | `integer` | Number uniquely identifying the pull request within its repository. |
| `commits` | `integer` |  |
| `comments_url` | `string` |  |
| `active_lock_reason` | `string` |  |
| `title` | `string` | The title of the pull request. |
| `updated_at` | `string` |  |
| `maintainer_can_modify` | `boolean` | Indicates whether maintainers can modify the pull request. |
| `author_association` | `string` | How the author is associated with the repository. |
| `merge_commit_sha` | `string` |  |
| `url` | `string` |  |
| `changed_files` | `integer` |  |
| `html_url` | `string` |  |
| `merged` | `boolean` |  |
| `merged_by` | `object` | Simple User |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `head` | `object` |  |
| `mergeable_state` | `string` |  |
| `requested_teams` | `array` |  |
| `_links` | `object` |  |
| `state` | `string` | State of this Pull Request. Either `open` or `closed`. |
| `statuses_url` | `string` |  |
| `issue_url` | `string` |  |
| `assignee` | `object` | Simple User |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `comments` | `integer` |  |
| `merged_at` | `string` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `diff_url` | `string` |  |
| `created_at` | `string` |  |
| `requested_reviewers` | `array` |  |
| `review_comment_url` | `string` |  |
| `labels` | `array` |  |
| `assignees` | `array` |  |
| `body` | `string` |  |
| `patch_url` | `string` |  |
| `node_id` | `string` |  |
| `commits_url` | `string` |  |
| `review_comments` | `integer` |  |
| `closed_at` | `string` |  |
| `mergeable` | `boolean` |  |
| `user` | `object` | Simple User |
| `locked` | `boolean` |  |
| `additions` | `integer` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `owner, pull_number, repo` | Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Lists details of a pull request by providing its number.<br /><br />When you get, [create](https://docs.github.com/rest/reference/pulls/#create-a-pull-request), or [edit](https://docs.github.com/rest/reference/pulls#update-a-pull-request) a pull request, GitHub creates a merge commit to test whether the pull request can be automatically merged into the base branch. This test commit is not added to the base branch or the head branch. You can review the status of the test commit using the `mergeable` key. For more information, see "[Checking mergeability of pull requests](https://docs.github.com/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".<br /><br />The value of the `mergeable` attribute can be `true`, `false`, or `null`. If the value is `null`, then GitHub has started a background job to compute the mergeability. After giving the job time to complete, resubmit the request. When the job finishes, you will see a non-`null` value for the `mergeable` attribute in the response. If `mergeable` is `true`, then `merge_commit_sha` will be the SHA of the _test_ merge commit.<br /><br />The value of the `merge_commit_sha` attribute changes depending on the state of the pull request. Before merging a pull request, the `merge_commit_sha` attribute holds the SHA of the _test_ merge commit. After merging a pull request, the `merge_commit_sha` attribute changes depending on how you merged the pull request:<br /><br />*   If merged as a [merge commit](https://docs.github.com/articles/about-merge-methods-on-github/), `merge_commit_sha` represents the SHA of the merge commit.<br />*   If merged via a [squash](https://docs.github.com/articles/about-merge-methods-on-github/#squashing-your-merge-commits), `merge_commit_sha` represents the SHA of the squashed commit on the base branch.<br />*   If [rebased](https://docs.github.com/articles/about-merge-methods-on-github/#rebasing-and-merging-your-commits), `merge_commit_sha` represents the commit that the base branch was updated to.<br /><br />Pass the appropriate [media type](https://docs.github.com/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to fetch diff and patch formats. |
| `list` | `SELECT` | `owner, repo` | Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation. |
| `create` | `INSERT` | `owner, repo, data__base, data__head` | Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />To open or update a pull request in a public repository, you must have write access to the head or the source branch. For organization-owned repositories, you must be a member of the organization that owns the repository to open or update a pull request.<br /><br />You can create a new pull request.<br /><br />This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-rate-limits)" for details. |
| `check_if_merged` | `EXEC` | `owner, pull_number, repo` |  |
| `merge` | `EXEC` | `owner, pull_number, repo` | This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| `update` | `EXEC` | `owner, pull_number, repo` | Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />To open or update a pull request in a public repository, you must have write access to the head or the source branch. For organization-owned repositories, you must be a member of the organization that owns the repository to open or update a pull request. |
| `update_branch` | `EXEC` | `owner, pull_number, repo` | Updates the pull request branch with the latest upstream changes by merging HEAD from the base branch into the pull request branch. |
