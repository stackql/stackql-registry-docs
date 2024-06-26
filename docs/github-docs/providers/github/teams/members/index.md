---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - teams
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
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="github.teams.members" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="id" /> | `integer` |
| <CopyableCode code="name" /> | `string` |
| <CopyableCode code="avatar_url" /> | `string` |
| <CopyableCode code="email" /> | `string` |
| <CopyableCode code="events_url" /> | `string` |
| <CopyableCode code="followers_url" /> | `string` |
| <CopyableCode code="following_url" /> | `string` |
| <CopyableCode code="gists_url" /> | `string` |
| <CopyableCode code="gravatar_id" /> | `string` |
| <CopyableCode code="html_url" /> | `string` |
| <CopyableCode code="login" /> | `string` |
| <CopyableCode code="node_id" /> | `string` |
| <CopyableCode code="organizations_url" /> | `string` |
| <CopyableCode code="received_events_url" /> | `string` |
| <CopyableCode code="repos_url" /> | `string` |
| <CopyableCode code="site_admin" /> | `boolean` |
| <CopyableCode code="starred_at" /> | `string` |
| <CopyableCode code="starred_url" /> | `string` |
| <CopyableCode code="subscriptions_url" /> | `string` |
| <CopyableCode code="type" /> | `string` |
| <CopyableCode code="url" /> | `string` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_members_in_org" /> | `SELECT` | <CopyableCode code="org, team_slug" /> | Team members will include the members of child teams.<br /><br />To list members in a team, the team must be visible to the authenticated user. |
| <CopyableCode code="list_members_legacy" /> | `SELECT` | <CopyableCode code="team_id" /> | **Deprecation Notice:** This endpoint route is deprecated and will be removed from the Teams API. We recommend migrating your existing code to use the new [`List team members`](https://docs.github.com/rest/teams/members#list-team-members) endpoint.<br /><br />Team members will include the members of child teams. |
| <CopyableCode code="remove_member_legacy" /> | `DELETE` | <CopyableCode code="team_id, username" /> | The "Remove team member" endpoint (described below) is deprecated.<br /><br />We recommend using the [Remove team membership for a user](https://docs.github.com/rest/teams/members#remove-team-membership-for-a-user) endpoint instead. It allows you to remove both active and pending memberships.<br /><br />Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />To remove a team member, the authenticated user must have 'admin' permissions to the team or be an owner of the org that the team is associated with. Removing a team member does not delete the user, it just removes them from the team.<br /><br />**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)." |
| <CopyableCode code="add_member_legacy" /> | `EXEC` | <CopyableCode code="team_id, username" /> | The "Add team member" endpoint (described below) is deprecated.<br /><br />We recommend using the [Add or update team membership for a user](https://docs.github.com/rest/teams/members#add-or-update-team-membership-for-a-user) endpoint instead. It allows you to invite new organization members to your teams.<br /><br />Team synchronization is available for organizations using GitHub Enterprise Cloud. For more information, see [GitHub's products](https://docs.github.com/github/getting-started-with-github/githubs-products) in the GitHub Help documentation.<br /><br />To add someone to a team, the authenticated user must be an organization owner or a team maintainer in the team they're changing. The person being added to the team must be a member of the team's organization.<br /><br />**Note:** When you have team synchronization set up for a team with your organization's identity provider (IdP), you will see an error if you attempt to use the API for making changes to the team's membership. If you have access to manage group membership in your IdP, you can manage GitHub team membership through your identity provider, which automatically adds and removes team members in an organization. For more information, see "[Synchronizing teams between your identity provider and GitHub](https://docs.github.com/articles/synchronizing-teams-between-your-identity-provider-and-github/)."<br /><br />Note that you'll need to set `Content-Length` to zero when calling out to this endpoint. For more information, see "[HTTP verbs](https://docs.github.com/rest/overview/resources-in-the-rest-api#http-verbs)." |
| <CopyableCode code="get_member_legacy" /> | `EXEC` | <CopyableCode code="team_id, username" /> | The "Get team member" endpoint (described below) is deprecated.<br /><br />We recommend using the [Get team membership for a user](https://docs.github.com/rest/teams/members#get-team-membership-for-a-user) endpoint instead. It allows you to get both active and pending memberships.<br /><br />To list members in a team, the team must be visible to the authenticated user. |
