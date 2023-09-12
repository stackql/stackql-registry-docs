---
title: collaborators
hide_title: false
hide_table_of_contents: false
keywords:
  - collaborators
  - repos
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
<tr><td><b>Name</b></td><td><code>collaborators</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>github.repos.collaborators</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| `id` | `integer` |
| `name` | `string` |
| `email` | `string` |
| `type` | `string` |
| `site_admin` | `boolean` |
| `following_url` | `string` |
| `avatar_url` | `string` |
| `permissions` | `object` |
| `starred_url` | `string` |
| `received_events_url` | `string` |
| `repos_url` | `string` |
| `subscriptions_url` | `string` |
| `organizations_url` | `string` |
| `gravatar_id` | `string` |
| `followers_url` | `string` |
| `url` | `string` |
| `events_url` | `string` |
| `html_url` | `string` |
| `node_id` | `string` |
| `login` | `string` |
| `gists_url` | `string` |
| `role_name` | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_collaborators` | `SELECT` | `owner, repo` | For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.<br />Organization members with write, maintain, or admin privileges on the organization-owned repository can use this endpoint.<br /><br />Team members will include the members of child teams.<br /><br />You must authenticate using an access token with the `read:org` and `repo` scopes with push access to use this<br />endpoint. GitHub Apps must have the `members` organization permission and `metadata` repository permission to use this<br />endpoint. |
| `remove_collaborator` | `DELETE` | `owner, repo, username` | Removes a collaborator from a repository.<br /><br />To use this endpoint, the authenticated user must either be an administrator of the repository or target themselves for removal.<br /><br />This endpoint also:<br />- Cancels any outstanding invitations<br />- Unasigns the user from any issues<br />- Removes access to organization projects if the user is not an organization member and is not a collaborator on any other organization repositories.<br />- Unstars the repository<br />- Updates access permissions to packages<br /><br />Removing a user as a collaborator has the following effects on forks:<br /> - If the user had access to a fork through their membership to this repository, the user will also be removed from the fork.<br /> - If the user had their own fork of the repository, the fork will be deleted.<br /> - If the user still has read access to the repository, open pull requests by this user from a fork will be denied.<br /><br />**Note**: A user can still have access to the repository through organization permissions like base repository permissions.<br /><br />Although the API responds immediately, the additional permission updates might take some extra time to complete in the background.<br /><br />For more information on fork permissions, see "[About permissions and visibility of forks](https://docs.github.com/pull-requests/collaborating-with-pull-requests/working-with-forks/about-permissions-and-visibility-of-forks)". |
| `add_collaborator` | `EXEC` | `owner, repo, username` | This endpoint triggers [notifications](https://docs.github.com/github/managing-subscriptions-and-notifications-on-github/about-notifications). Creating content too quickly using this endpoint may result in secondary rate limiting. See "[Secondary rate limits](https://docs.github.com/rest/overview/resources-in-the-rest-api#secondary-rate-limits)" and "[Dealing with secondary rate limits](https://docs.github.com/rest/guides/best-practices-for-integrators#dealing-with-secondary-rate-limits)" for details.<br /><br />Adding an outside collaborator may be restricted by enterprise administrators. For more information, see "[Enforcing repository management policies in your enterprise](https://docs.github.com/admin/policies/enforcing-policies-for-your-enterprise/enforcing-repository-management-policies-in-your-enterprise#enforcing-a-policy-for-inviting-outside-collaborators-to-repositories)."<br /><br />For more information on permission levels, see "[Repository permission levels for an organization](https://docs.github.com/github/setting-up-and-managing-organizations-and-teams/repository-permission-levels-for-an-organization#permission-levels-for-repositories-owned-by-an-organization)". There are restrictions on which permissions can be granted to organization members when an organization base role is in place. In this case, the permission being given must be equal to or higher than the org base permission. Otherwise, the request will fail with:<br /><br />```<br />Cannot assign &#123;member&#125; permission of &#123;role name&#125;<br />```<br /><br />Note that, if you choose not to pass any parameters, you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)."<br /><br />The invitee will receive a notification that they have been invited to the repository, which they must accept or decline. They may do this via the notifications page, the email they receive, or by using the [API](https://docs.github.com/rest/collaborators/invitations).<br /><br />**Updating an existing collaborator's permission level**<br /><br />The endpoint can also be used to change the permissions of an existing collaborator without first removing and re-adding the collaborator. To change the permissions, use the same endpoint and pass a different `permission` parameter. The response will be a `204`, with no other indication that the permission level changed.<br /><br />**Rate limits**<br /><br />You are limited to sending 50 invitations to a repository per 24 hour period. Note there is no limit if you are inviting organization members to an organization repository. |
| `check_collaborator` | `EXEC` | `owner, repo, username` | For organization-owned repositories, the list of collaborators includes outside collaborators, organization members that are direct collaborators, organization members with access through team memberships, organization members with access through default organization permissions, and organization owners.<br /><br />Team members will include the members of child teams.<br /><br />You must authenticate using an access token with the `read:org` and `repo` scopes with push access to use this<br />endpoint. GitHub Apps must have the `members` organization permission and `metadata` repository permission to use this<br />endpoint. |
