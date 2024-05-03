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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>team_links</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.teams.team_links" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The team link's identifier |
| <CopyableCode code="attributes" /> | `object` | Team link attributes |
| <CopyableCode code="type" /> | `string` | Team link type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_team_link" /> | `SELECT` | <CopyableCode code="link_id, team_id, dd_site" /> | Get a single link for a team. |
| <CopyableCode code="get_team_links" /> | `SELECT` | <CopyableCode code="team_id, dd_site" /> | Get all links for a given team. |
| <CopyableCode code="create_team_link" /> | `INSERT` | <CopyableCode code="team_id, data__data, dd_site" /> | Add a new link to a team. |
| <CopyableCode code="delete_team_link" /> | `DELETE` | <CopyableCode code="link_id, team_id, dd_site" /> | Remove a link from a team. |
| <CopyableCode code="_get_team_link" /> | `EXEC` | <CopyableCode code="link_id, team_id, dd_site" /> | Get a single link for a team. |
| <CopyableCode code="_get_team_links" /> | `EXEC` | <CopyableCode code="team_id, dd_site" /> | Get all links for a given team. |
| <CopyableCode code="update_team_link" /> | `EXEC` | <CopyableCode code="link_id, team_id, data__data, dd_site" /> | Update a team link. |
