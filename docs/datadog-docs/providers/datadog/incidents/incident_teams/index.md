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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>incident_teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.incidents.incident_teams" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The incident team's ID. |
| <CopyableCode code="attributes" /> | `object` | The incident team's attributes from a response. |
| <CopyableCode code="relationships" /> | `object` | The incident team's relationships. |
| <CopyableCode code="type" /> | `string` | Incident Team resource type. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_incident_team" /> | `SELECT` | <CopyableCode code="team_id, dd_site" /> | Get details of an incident team. If the `include[users]` query parameter is provided,<br />the included attribute will contain the users related to these incident teams. |
| <CopyableCode code="list_incident_teams" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get all incident teams for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident teams. |
| <CopyableCode code="create_incident_team" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Creates a new incident team. |
| <CopyableCode code="delete_incident_team" /> | `DELETE` | <CopyableCode code="team_id, dd_site" /> | Deletes an existing incident team. |
| <CopyableCode code="_get_incident_team" /> | `EXEC` | <CopyableCode code="team_id, dd_site" /> | Get details of an incident team. If the `include[users]` query parameter is provided,<br />the included attribute will contain the users related to these incident teams. |
| <CopyableCode code="_list_incident_teams" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get all incident teams for the requesting user's organization. If the `include[users]` query parameter is provided, the included attribute will contain the users related to these incident teams. |
| <CopyableCode code="update_incident_team" /> | `EXEC` | <CopyableCode code="team_id, data__data, dd_site" /> | Updates an existing incident team. Only provide the attributes which should be updated as this request is a partial update. |
