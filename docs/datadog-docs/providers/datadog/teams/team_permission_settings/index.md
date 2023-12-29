---
title: team_permission_settings
hide_title: false
hide_table_of_contents: false
keywords:
  - team_permission_settings
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
<tr><td><b>Name</b></td><td><code>team_permission_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.teams.team_permission_settings</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The team permission setting's identifier |
| `attributes` | `object` | Team permission setting attributes |
| `type` | `string` | Team permission setting type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_team_permission_settings` | `SELECT` | `team_id, dd_site` | Get all permission settings for a given team. |
| `_get_team_permission_settings` | `EXEC` | `team_id, dd_site` | Get all permission settings for a given team. |
| `update_team_permission_setting` | `EXEC` | `action, team_id, data__data, dd_site` | Update a team permission setting for a given team. |
