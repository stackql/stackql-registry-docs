---
title: team_memberships
hide_title: false
hide_table_of_contents: false
keywords:
  - team_memberships
  - teams
  - datadog    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, monitor, and manage Datadog resources using SQL
custom_edit_url: null
image: /img/providers/datadog/stackql-datadog-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>team_memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.teams.team_memberships</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The ID of a user's relationship with a team |
| `attributes` | `object` | Team membership attributes |
| `relationships` | `object` | Relationship between membership and a user |
| `type` | `string` | Team membership type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_team_memberships` | `SELECT` | `team_id, dd_site` | Get a paginated list of members for a team |
| `create_team_membership` | `INSERT` | `team_id, data__data, dd_site` | Add a user to a team. |
| `delete_team_membership` | `DELETE` | `team_id, user_id, dd_site` | Remove a user from a team. |
| `_get_team_memberships` | `EXEC` | `team_id, dd_site` | Get a paginated list of members for a team |
| `update_team_membership` | `EXEC` | `team_id, user_id, data__data, dd_site` | Update a user's membership attributes on a team. |
