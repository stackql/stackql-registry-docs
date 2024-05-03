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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="vercel.teams.teams" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The Team's unique identifier. |
| <CopyableCode code="name" /> | `string` | Name associated with the Team account, or `null` if none has been provided. |
| <CopyableCode code="avatar" /> | `string` | The ID of the file used as avatar for this Team. |
| <CopyableCode code="slug" /> | `string` | The Team's slug, which is unique across the Vercel platform. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_team" /> | `SELECT` | <CopyableCode code="teamId" /> | Get information for the Team specified by the `teamId` parameter. |
| <CopyableCode code="get_teams" /> | `SELECT` |  | Get a paginated list of all the Teams the authenticated User is a member of. |
| <CopyableCode code="create_team" /> | `INSERT` | <CopyableCode code="data__slug" /> | Create a new Team under your account. You need to send a POST request with the desired Team slug, and optionally the Team name. |
| <CopyableCode code="delete_team" /> | `DELETE` | <CopyableCode code="teamId" /> | Delete a team under your account. You need to send a `DELETE` request with the desired team `id`. An optional array of reasons for deletion may also be sent. |
| <CopyableCode code="_get_teams" /> | `EXEC` |  | Get a paginated list of all the Teams the authenticated User is a member of. |
| <CopyableCode code="join_team" /> | `EXEC` | <CopyableCode code="teamId" /> | Join a team with a provided invite code or team ID. |
| <CopyableCode code="patch_team" /> | `EXEC` | <CopyableCode code="teamId" /> | Update the information of a Team specified by the `teamId` parameter. The request body should contain the information that will be updated on the Team. |
