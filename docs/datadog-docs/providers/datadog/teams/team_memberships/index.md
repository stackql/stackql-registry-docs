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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>team_memberships</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.teams.team_memberships" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The ID of a user's relationship with a team |
| <CopyableCode code="attributes" /> | `object` | Team membership attributes |
| <CopyableCode code="relationships" /> | `object` | Relationship between membership and a user |
| <CopyableCode code="type" /> | `string` | Team membership type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_team_memberships" /> | `SELECT` | <CopyableCode code="team_id, dd_site" /> | Get a paginated list of members for a team |
| <CopyableCode code="create_team_membership" /> | `INSERT` | <CopyableCode code="team_id, data__data, dd_site" /> | Add a user to a team. |
| <CopyableCode code="delete_team_membership" /> | `DELETE` | <CopyableCode code="team_id, user_id, dd_site" /> | Remove a user from a team. |
| <CopyableCode code="_get_team_memberships" /> | `EXEC` | <CopyableCode code="team_id, dd_site" /> | Get a paginated list of members for a team |
| <CopyableCode code="update_team_membership" /> | `EXEC` | <CopyableCode code="team_id, user_id, data__data, dd_site" /> | Update a user's membership attributes on a team. |
