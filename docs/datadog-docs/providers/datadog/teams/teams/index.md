---
title: teams
hide_title: false
hide_table_of_contents: false
keywords:
  - teams
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
<tr><td><b>Name</b></td><td><code>teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.teams.teams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The team's identifier |
| `attributes` | `object` | Team attributes |
| `relationships` | `object` | Resources related to a team |
| `type` | `string` | Team type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_team` | `SELECT` | `team_id, dd_site` | Get a single team using the team's `id`. |
| `list_teams` | `SELECT` | `dd_site` | Get all teams.<br />Can be used to search for teams using the `filter[keyword]` and `filter[me]` query parameters. |
| `create_team` | `INSERT` | `data__data, dd_site` | Create a new team.<br />User IDs passed through the `users` relationship field are added to the team. |
| `delete_team` | `DELETE` | `team_id, dd_site` | Remove a team using the team's `id`. |
| `_get_team` | `EXEC` | `team_id, dd_site` | Get a single team using the team's `id`. |
| `_list_teams` | `EXEC` | `dd_site` | Get all teams.<br />Can be used to search for teams using the `filter[keyword]` and `filter[me]` query parameters. |
| `update_team` | `EXEC` | `team_id, data__data, dd_site` | Update a team using the team's `id`.<br />If the `team_links` relationship is present, the associated links are updated to be in the order they appear in the array, and any existing team links not present are removed. |
