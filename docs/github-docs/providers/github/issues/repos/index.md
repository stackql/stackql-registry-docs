---
title: repos
hide_title: false
hide_table_of_contents: false
keywords:
  - repos
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
<tr><td><b>Name</b></td><td><code>repos</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.repos</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `repository_url` | `string` |  |
| `state_reason` | `string` | The reason for the current state |
| `user` | `object` | A GitHub user. |
| `comments` | `integer` |  |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `draft` | `boolean` |  |
| `closed_by` | `object` | A GitHub user. |
| `comments_url` | `string` |  |
| `number` | `integer` | Number uniquely identifying the issue within its repository |
| `assignees` | `array` |  |
| `updated_at` | `string` |  |
| `state` | `string` | State of the issue; either 'open' or 'closed' |
| `body_html` | `string` |  |
| `repository` | `object` | A repository on GitHub. |
| `closed_at` | `string` |  |
| `author_association` | `string` | How the author is associated with the repository. |
| `title` | `string` | Title of the issue |
| `html_url` | `string` |  |
| `body_text` | `string` |  |
| `reactions` | `object` |  |
| `body` | `string` | Contents of the issue |
| `locked` | `boolean` |  |
| `node_id` | `string` |  |
| `active_lock_reason` | `string` |  |
| `pull_request` | `object` |  |
| `timeline_url` | `string` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `assignee` | `object` | A GitHub user. |
| `events_url` | `string` |  |
| `url` | `string` | URL for the issue |
| `labels_url` | `string` |  |
| `labels` | `array` | Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository |
| `created_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `issue_number, owner, repo` | The API returns a [`301 Moved Permanently` status](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-redirects-redirects) if the issue was<br />[transferred](https://docs.github.com/articles/transferring-an-issue-to-another-repository/) to another repository. If<br />the issue was transferred to or deleted from a repository where the authenticated user lacks read access, the API<br />returns a `404 Not Found` status. If the issue was deleted from a repository where the authenticated user has read<br />access, the API returns a `410 Gone` status. To receive webhook events for transferred and deleted issues, subscribe<br />to the [`issues`](https://docs.github.com/webhooks/event-payloads/#issues) webhook.<br /><br />**Note**: GitHub's REST API considers every pull request an issue, but not every issue is a pull request. For this<br />reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by<br />the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull<br />request id, use the "[List pull requests](https://docs.github.com/rest/pulls/pulls#list-pull-requests)" endpoint. |
| `list_for_repo` | `SELECT` | `owner, repo` | List issues in a repository. Only open issues will be listed.<br /><br />**Note**: GitHub's REST API considers every pull request an issue, but not every issue is a pull request. For this<br />reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by<br />the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull<br />request id, use the "[List pull requests](https://docs.github.com/rest/pulls/pulls#list-pull-requests)" endpoint. |
| `create` | `INSERT` | `owner, repo, data__title` | Any user with pull access to a repository can create an issue. If [issues are disabled in the repository](https://docs.github.com/articles/disabling-issues/), the API returns a `410 Gone` status.<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| `lock` | `EXEC` | `issue_number, owner, repo` | Users with push access can lock an issue or pull request's conversation.<br /><br />Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unlock` | `EXEC` | `issue_number, owner, repo` | Users with push access can unlock an issue's conversation. |
| `update` | `EXEC` | `issue_number, owner, repo` | Issue owners and users with push access can edit an issue. |
