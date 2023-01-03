---
title: collaborators
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
<tr><td><b>Name</b></td><td><code>collaborators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.collaborators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `node_id` | `string` |
| `following_url` | `string` |
| `html_url` | `string` |
| `permissions` | `object` |
| `subscriptions_url` | `string` |
| `starred_url` | `string` |
| `url` | `string` |
| `avatar_url` | `string` |
| `organizations_url` | `string` |
| `repos_url` | `string` |
| `events_url` | `string` |
| `received_events_url` | `string` |
| `login` | `string` |
| `gists_url` | `string` |
| `email` | `string` |
| `followers_url` | `string` |
| `type` | `string` |
| `gravatar_id` | `string` |
| `site_admin` | `boolean` |
| `role_name` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_collaborators` | `SELECT` | `owner, repo` | For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.<br /><br />Team members will include the members of child teams.<br /><br />You must authenticate using an access token with the `read:org` and `repo` scopes with push access to use this<br />endpoint. GitHub Apps must have the `members` organization permission and `metadata` repository permission to use this<br />endpoint. |
| `add_collaborator` | `INSERT` | `owner, repo, username` | This endpoint triggers [notifications](https://docs.github.com/en/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.<br /><br />For more information on permission levels, see "[Repository permission levels for an organization](https://docs.github.com/en/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)". There are restrictions on which permissions can be granted to organization members when an organization base role is in place. In this case, the permission being given must be equal to or higher than the org base permission. Otherwise, the request will fail with:<br /><br />```<br />Cannot assign {member} permission of {role name}<br />```<br /><br />Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)."<br /><br />The invitee will receive a notification that they have been invited to the repository, which they must accept or decline. They may do this via the notifications page, the email they receive, or by using the [repository invitations API endpoints](https://docs.github.com/rest/reference/repos#invitations).<br /><br />**Rate limits**<br /><br />You are limited to sending 50 invitations to a repository per 24 hour period. Note there is no limit if you are inviting organization members to an organization repository. |
| `remove_collaborator` | `DELETE` | `owner, repo, username` |  |
| `check_collaborator` | `EXEC` | `owner, repo, username` | For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.<br /><br />Team members will include the members of child teams.<br /><br />You must authenticate using an access token with the `read:org` and `repo` scopes with push access to use this<br />endpoint. GitHub Apps must have the `members` organization permission and `metadata` repository permission to use this<br />endpoint. |
