---
title: pull_request
hide_title: false
hide_table_of_contents: false
keywords:
  - pull_request
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
<tr><td><b>Name</b></td><td><code>pull_request</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.pulls.pull_request</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `auto_merge` | `object` | The status of auto merging a pull request. |
| `additions` | `integer` |  |
| `closed_at` | `string` |  |
| `changed_files` | `integer` |  |
| `diff_url` | `string` |  |
| `html_url` | `string` |  |
| `mergeable` | `boolean` |  |
| `statuses_url` | `string` |  |
| `requested_teams` | `array` |  |
| `review_comments` | `integer` |  |
| `merged` | `boolean` |  |
| `title` | `string` | The title of the pull request. |
| `updated_at` | `string` |  |
| `labels` | `array` |  |
| `state` | `string` | State of this Pull Request. Either `open` or `closed`. |
| `mergeable_state` | `string` |  |
| `draft` | `boolean` | Indicates whether or not the pull request is a draft. |
| `merged_by` | `object` | A GitHub user. |
| `head` | `object` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `user` | `object` | A GitHub user. |
| `node_id` | `string` |  |
| `issue_url` | `string` |  |
| `comments` | `integer` |  |
| `created_at` | `string` |  |
| `commits_url` | `string` |  |
| `review_comment_url` | `string` |  |
| `number` | `integer` | Number uniquely identifying the pull request within its repository. |
| `active_lock_reason` | `string` |  |
| `comments_url` | `string` |  |
| `requested_reviewers` | `array` |  |
| `commits` | `integer` |  |
| `review_comments_url` | `string` |  |
| `_links` | `object` |  |
| `deletions` | `integer` |  |
| `assignees` | `array` |  |
| `merged_at` | `string` |  |
| `patch_url` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `url` | `string` |  |
| `assignee` | `object` | A GitHub user. |
| `merge_commit_sha` | `string` |  |
| `rebaseable` | `boolean` |  |
| `base` | `object` |  |
| `locked` | `boolean` |  |
| `maintainer_can_modify` | `boolean` | Indicates whether maintainers can modify the pull request. |
| `body` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `owner, pull_number, repo` | Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />Lists details of a pull request by providing its number.<br /><br />When you get, [create](https://docs.github.com/rest/pulls/pulls/#create-a-pull-request), or [edit](https://docs.github.com/rest/pulls/pulls#update-a-pull-request) a pull request, GitHub creates a merge commit to test whether the pull request can be automatically merged into the base branch. This test commit is not added to the base branch or the head branch. You can review the status of the test commit using the `mergeable` key. For more information, see "[Checking mergeability of pull requests](https://docs.github.com/rest/guides/getting-started-with-the-git-database-api#checking-mergeability-of-pull-requests)".<br /><br />The value of the `mergeable` attribute can be `true`, `false`, or `null`. If the value is `null`, then GitHub has started a background job to compute the mergeability. After giving the job time to complete, resubmit the request. When the job finishes, you will see a non-`null` value for the `mergeable` attribute in the response. If `mergeable` is `true`, then `merge_commit_sha` will be the SHA of the _test_ merge commit.<br /><br />The value of the `merge_commit_sha` attribute changes depending on the state of the pull request. Before merging a pull request, the `merge_commit_sha` attribute holds the SHA of the _test_ merge commit. After merging a pull request, the `merge_commit_sha` attribute changes depending on how you merged the pull request:<br /><br />*   If merged as a [merge commit](https://docs.github.com/articles/about-merge-methods-on-github/), `merge_commit_sha` represents the SHA of the merge commit.<br />*   If merged via a [squash](https://docs.github.com/articles/about-merge-methods-on-github/#squashing-your-merge-commits), `merge_commit_sha` represents the SHA of the squashed commit on the base branch.<br />*   If [rebased](https://docs.github.com/articles/about-merge-methods-on-github/#rebasing-and-merging-your-commits), `merge_commit_sha` represents the commit that the base branch was updated to.<br /><br />Pass the appropriate [media type](https://docs.github.com/rest/overview/media-types/#commits-commit-comparison-and-pull-requests) to fetch diff and patch formats. |
| `create` | `INSERT` | `owner, repo, data__base, data__head` | Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />To open or update a pull request in a public repository, you must have write access to the head or the source branch. For organization-owned repositories, you must be a member of the organization that owns the repository to open or update a pull request.<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-rate-limits)" for details. |
| `check_if_merged` | `EXEC` | `owner, pull_number, repo` | Checks if a pull request has been merged into the base branch. The HTTP status of the response indicates whether or not the pull request has been merged; the response body is empty. |
| `merge` | `EXEC` | `owner, pull_number, repo` | Merges a pull request into the base branch.<br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| `update` | `EXEC` | `owner, pull_number, repo` | Draft pull requests are available in public repositories with GitHub Free and GitHub Free for organizations, GitHub Pro, and legacy per-repository billing plans, and in public and private repositories with GitHub Team and GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />To open or update a pull request in a public repository, you must have write access to the head or the source branch. For organization-owned repositories, you must be a member of the organization that owns the repository to open or update a pull request. |
| `update_branch` | `EXEC` | `owner, pull_number, repo` | Updates the pull request branch with the latest upstream changes by merging HEAD from the base branch into the pull request branch. |
