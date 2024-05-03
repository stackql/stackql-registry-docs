---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
  - teams
  - vercel    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, deploy, and manage Vercel resources using SQL
custom_edit_url: null
image: /img/providers/vercel/stackql-vercel-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.teams.members" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="name" /> | `string` | The name of this user. |
| <CopyableCode code="accessRequestedAt" /> | `number` | Timestamp in milliseconds for when this team member was accepted by an owner. |
| <CopyableCode code="avatar" /> | `string` | ID of the file for the Avatar of this member. |
| <CopyableCode code="bitbucket" /> | `object` | Information about the Bitbucket account of this user. |
| <CopyableCode code="confirmed" /> | `boolean` | Boolean that indicates if this member was confirmed by an owner. |
| <CopyableCode code="createdAt" /> | `number` | Timestamp in milliseconds when this member was added. |
| <CopyableCode code="email" /> | `string` | The email of this member. |
| <CopyableCode code="github" /> | `object` | Information about the GitHub account for this user. |
| <CopyableCode code="gitlab" /> | `object` | Information about the GitLab account of this user. |
| <CopyableCode code="joinedFrom" /> | `object` | Map with information about the members origin if they joined by requesting access. |
| <CopyableCode code="projects" /> | `array` | Array of project memberships |
| <CopyableCode code="role" /> | `string` | Role of this user in the team. |
| <CopyableCode code="uid" /> | `string` | The ID of this user. |
| <CopyableCode code="username" /> | `string` | The unique username of this user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_team_members" /> | `SELECT` | <CopyableCode code="teamId" /> | Get a paginated list of team members for the provided team. |
| <CopyableCode code="remove_team_member" /> | `DELETE` | <CopyableCode code="teamId, uid" /> | Remove a Team Member from the Team, or dismiss a user that requested access, or leave a team. |
| <CopyableCode code="_get_team_members" /> | `EXEC` | <CopyableCode code="teamId" /> | Get a paginated list of team members for the provided team. |
| <CopyableCode code="invite_user_to_team" /> | `EXEC` | <CopyableCode code="teamId" /> | Invite a user to join the team specified in the URL. The authenticated user needs to be an `OWNER` in order to successfully invoke this endpoint. The user can be specified with an email or an ID. If both email and ID are provided, ID will take priority. |
| <CopyableCode code="update_team_member" /> | `EXEC` | <CopyableCode code="teamId, uid" /> | Update the membership of a Team Member on the Team specified by `teamId`, such as changing the _role_ of the member, or confirming a request to join the Team for an unconfirmed member. The authenticated user must be an `OWNER` of the Team. |
