---
title: issues
hide_title: false
hide_table_of_contents: false
keywords:
  - issues
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
<tr><td><b>Name</b></td><td><code>issues</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.issues.issues</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `integer` |  |
| `repository_url` | `string` |  |
| `comments_url` | `string` |  |
| `updated_at` | `string` |  |
| `body_html` | `string` |  |
| `timeline_url` | `string` |  |
| `created_at` | `string` |  |
| `locked` | `boolean` |  |
| `active_lock_reason` | `string` |  |
| `node_id` | `string` |  |
| `title` | `string` | Title of the issue |
| `html_url` | `string` |  |
| `draft` | `boolean` |  |
| `body_text` | `string` |  |
| `closed_by` | `object` | Simple User |
| `author_association` | `string` | How the author is associated with the repository. |
| `url` | `string` | URL for the issue |
| `labels` | `array` | Labels to associate with this issue; pass one or more label names to replace the set of labels on this issue; send an empty array to clear all labels from the issue; note that the labels are silently dropped for users without push access to the repository |
| `pull_request` | `object` |  |
| `state` | `string` | State of the issue; either 'open' or 'closed' |
| `assignee` | `object` | Simple User |
| `body` | `string` | Contents of the issue |
| `labels_url` | `string` |  |
| `number` | `integer` | Number uniquely identifying the issue within its repository |
| `comments` | `integer` |  |
| `reactions` | `object` |  |
| `milestone` | `object` | A collection of related issues and pull requests. |
| `repository` | `object` | A git repository |
| `events_url` | `string` |  |
| `user` | `object` | Simple User |
| `performed_via_github_app` | `object` | GitHub apps are a new way to extend GitHub. They can be installed directly on organizations and user accounts and granted access to specific repositories. They come with granular permissions and built-in webhooks. GitHub apps are first class actors within GitHub. |
| `assignees` | `array` |  |
| `closed_at` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get` | `SELECT` | `issue_number, owner, repo` | The API returns a [`301 Moved Permanently` status](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-redirects-redirects) if the issue was<br />[transferred](https://docs.github.com/articles/transferring-an-issue-to-another-repository/) to another repository. If<br />the issue was transferred to or deleted from a repository where the authenticated user lacks read access, the API<br />returns a `404 Not Found` status. If the issue was deleted from a repository where the authenticated user has read<br />access, the API returns a `410 Gone` status. To receive webhook events for transferred and deleted issues, subscribe<br />to the [`issues`](https://docs.github.com/webhooks/event-payloads/#issues) webhook.<br /><br />**Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. For this<br />reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by<br />the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull<br />request id, use the "[List pull requests](https://docs.github.com/rest/reference/pulls#list-pull-requests)" endpoint. |
| `list` | `SELECT` |  | List issues assigned to the authenticated user across all visible repositories including owned repositories, member<br />repositories, and organization repositories. You can use the `filter` query parameter to fetch issues that are not<br />necessarily assigned to you.<br /><br /><br />**Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. For this<br />reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by<br />the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull<br />request id, use the "[List pull requests](https://docs.github.com/rest/reference/pulls#list-pull-requests)" endpoint. |
| `list_for_org` | `SELECT` | `org` | List issues in an organization assigned to the authenticated user.<br /><br />**Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. For this<br />reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by<br />the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull<br />request id, use the "[List pull requests](https://docs.github.com/rest/reference/pulls#list-pull-requests)" endpoint. |
| `list_for_repo` | `SELECT` | `owner, repo` | List issues in a repository.<br /><br />**Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. For this<br />reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by<br />the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull<br />request id, use the "[List pull requests](https://docs.github.com/rest/reference/pulls#list-pull-requests)" endpoint. |
| `create` | `INSERT` | `owner, repo, data__title` | Any user with pull access to a repository can create an issue. If [issues are disabled in the repository](https://docs.github.com/articles/disabling-issues/), the API returns a `410 Gone` status.<br /><br />This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details. |
| `list_for_authenticated_user` | `EXEC` |  | List issues across owned and member repositories assigned to the authenticated user.<br /><br />**Note**: GitHub's REST API v3 considers every pull request an issue, but not every issue is a pull request. For this<br />reason, "Issues" endpoints may return both issues and pull requests in the response. You can identify pull requests by<br />the `pull_request` key. Be aware that the `id` of a pull request returned from "Issues" endpoints will be an _issue id_. To find out the pull<br />request id, use the "[List pull requests](https://docs.github.com/rest/reference/pulls#list-pull-requests)" endpoint. |
| `lock` | `EXEC` | `issue_number, owner, repo` | Users with push access can lock an issue or pull request's conversation.<br /><br />Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| `unlock` | `EXEC` | `issue_number, owner, repo` | Users with push access can unlock an issue's conversation. |
| `update` | `EXEC` | `issue_number, owner, repo` | Issue owners and users with push access can edit an issue. |
