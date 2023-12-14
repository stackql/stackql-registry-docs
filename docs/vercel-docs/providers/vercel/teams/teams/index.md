---
title: teams
hide_title: false
hide_table_of_contents: false
keywords:
  - teams
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
<tr><td><b>Name</b></td><td><code>teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>vercel.teams.teams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The Team's unique identifier. |
| `name` | `string` | Name associated with the Team account, or `null` if none has been provided. |
| `avatar` | `string` | The ID of the file used as avatar for this Team. |
| `slug` | `string` | The Team's slug, which is unique across the Vercel platform. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_team` | `SELECT` | `teamId` | Get information for the Team specified by the `teamId` parameter. |
| `get_teams` | `SELECT` |  | Get a paginated list of all the Teams the authenticated User is a member of. |
| `create_team` | `INSERT` | `data__slug` | Create a new Team under your account. You need to send a POST request with the desired Team slug, and optionally the Team name. |
| `delete_team` | `DELETE` | `teamId` | Delete a team under your account. You need to send a `DELETE` request with the desired team `id`. An optional array of reasons for deletion may also be sent. |
| `_get_teams` | `EXEC` |  | Get a paginated list of all the Teams the authenticated User is a member of. |
| `join_team` | `EXEC` | `teamId` | Join a team with a provided invite code or team ID. |
| `patch_team` | `EXEC` | `teamId` | Update the information of a Team specified by the `teamId` parameter. The request body should contain the information that will be updated on the Team. |
