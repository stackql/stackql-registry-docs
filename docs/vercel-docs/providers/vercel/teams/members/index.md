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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.teams.members</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `name` | `string` | The name of this user. |
| `accessRequestedAt` | `number` | Timestamp in milliseconds for when this team member was accepted by an owner. |
| `avatar` | `string` | ID of the file for the Avatar of this member. |
| `bitbucket` | `object` | Information about the Bitbucket account of this user. |
| `confirmed` | `boolean` | Boolean that indicates if this member was confirmed by an owner. |
| `createdAt` | `number` | Timestamp in milliseconds when this member was added. |
| `email` | `string` | The email of this member. |
| `github` | `object` | Information about the GitHub account for this user. |
| `gitlab` | `object` | Information about the GitLab account of this user. |
| `joinedFrom` | `object` | Map with information about the members origin if they joined by requesting access. |
| `projects` | `array` | Array of project memberships |
| `role` | `string` | Role of this user in the team. |
| `uid` | `string` | The ID of this user. |
| `username` | `string` | The unique username of this user. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_team_members` | `SELECT` | `teamId` | Get a paginated list of team members for the provided team. |
| `remove_team_member` | `DELETE` | `teamId, uid` | Remove a Team Member from the Team, or dismiss a user that requested access, or leave a team. |
| `_get_team_members` | `EXEC` | `teamId` | Get a paginated list of team members for the provided team. |
| `invite_user_to_team` | `EXEC` | `teamId` | Invite a user to join the team specified in the URL. The authenticated user needs to be an `OWNER` in order to successfully invoke this endpoint. The user can be specified with an email or an ID. If both email and ID are provided, ID will take priority. |
| `update_team_member` | `EXEC` | `teamId, uid` | Update the membership of a Team Member on the Team specified by `teamId`, such as changing the _role_ of the member, or confirming a request to join the Team for an unconfirmed member. The authenticated user must be an `OWNER` of the Team. |
