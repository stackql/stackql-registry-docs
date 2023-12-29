---
title: incident_teams
hide_title: false
hide_table_of_contents: false
keywords:
  - incident_teams
  - incidents
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
<tr><td><b>Name</b></td><td><code>incident_teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>datadog.incidents.incident_teams</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | The incident team's ID. |
| `attributes` | `object` | The incident team's attributes from a response. |
| `relationships` | `object` | The incident team's relationships. |
| `type` | `string` | Incident Team resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_incident_team` | `SELECT` | `team_id, dd_site` | Get details of an incident team. If the `include[users]` query parameter is provided,<br />the included attribute will contain the users related to these incident teams. |
| `list_incident_teams` | `SELECT` | `dd_site` | Get all incident teams for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident teams. |
| `create_incident_team` | `INSERT` | `data__data, dd_site` | Creates a new incident team. |
| `delete_incident_team` | `DELETE` | `team_id, dd_site` | Deletes an existing incident team. |
| `_get_incident_team` | `EXEC` | `team_id, dd_site` | Get details of an incident team. If the `include[users]` query parameter is provided,<br />the included attribute will contain the users related to these incident teams. |
| `_list_incident_teams` | `EXEC` | `dd_site` | Get all incident teams for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident teams. |
| `update_incident_team` | `EXEC` | `team_id, data__data, dd_site` | Updates an existing incident team. Only provide the attributes which should be updated as this request is a partial update. |
