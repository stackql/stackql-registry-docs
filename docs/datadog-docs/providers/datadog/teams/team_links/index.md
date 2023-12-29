---
title: team_links
hide_title: false
hide_table_of_contents: false
keywords:
  - team_links
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
<tr><td><b>Name</b></td><td><code>team_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.teams.team_links</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The team link's identifier |
| `attributes` | `object` | Team link attributes |
| `type` | `string` | Team link type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_team_link` | `SELECT` | `link_id, team_id, dd_site` | Get a single link for a team. |
| `get_team_links` | `SELECT` | `team_id, dd_site` | Get all links for a given team. |
| `create_team_link` | `INSERT` | `team_id, data__data, dd_site` | Add a new link to a team. |
| `delete_team_link` | `DELETE` | `link_id, team_id, dd_site` | Remove a link from a team. |
| `_get_team_link` | `EXEC` | `link_id, team_id, dd_site` | Get a single link for a team. |
| `_get_team_links` | `EXEC` | `team_id, dd_site` | Get all links for a given team. |
| `update_team_link` | `EXEC` | `link_id, team_id, data__data, dd_site` | Update a team link. |
