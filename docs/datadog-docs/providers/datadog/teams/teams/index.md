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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.teams.teams" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The team's identifier |
| <CopyableCode code="attributes" /> | `object` | Team attributes |
| <CopyableCode code="relationships" /> | `object` | Resources related to a team |
| <CopyableCode code="type" /> | `string` | Team type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_team" /> | `SELECT` | <CopyableCode code="team_id, dd_site" /> | Get a single team using the team's `id`. |
| <CopyableCode code="list_teams" /> | `SELECT` | <CopyableCode code="dd_site" /> | Get all teams.<br />Can be used to search for teams using the `filter[keyword]` and `filter[me]` query parameters. |
| <CopyableCode code="create_team" /> | `INSERT` | <CopyableCode code="data__data, dd_site" /> | Create a new team.<br />User IDs passed through the `users` relationship field are added to the team. |
| <CopyableCode code="delete_team" /> | `DELETE` | <CopyableCode code="team_id, dd_site" /> | Remove a team using the team's `id`. |
| <CopyableCode code="_get_team" /> | `EXEC` | <CopyableCode code="team_id, dd_site" /> | Get a single team using the team's `id`. |
| <CopyableCode code="_list_teams" /> | `EXEC` | <CopyableCode code="dd_site" /> | Get all teams.<br />Can be used to search for teams using the `filter[keyword]` and `filter[me]` query parameters. |
| <CopyableCode code="update_team" /> | `EXEC` | <CopyableCode code="team_id, data__data, dd_site" /> | Update a team using the team's `id`.<br />If the `team_links` relationship is present, the associated links are updated to be in the order they appear in the array, and any existing team links not present are removed. |
