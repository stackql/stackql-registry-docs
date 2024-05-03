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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>team_permission_settings</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="datadog.teams.team_permission_settings" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` | The team permission setting's identifier |
| <CopyableCode code="attributes" /> | `object` | Team permission setting attributes |
| <CopyableCode code="type" /> | `string` | Team permission setting type |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_team_permission_settings" /> | `SELECT` | <CopyableCode code="team_id, dd_site" /> | Get all permission settings for a given team. |
| <CopyableCode code="_get_team_permission_settings" /> | `EXEC` | <CopyableCode code="team_id, dd_site" /> | Get all permission settings for a given team. |
| <CopyableCode code="update_team_permission_setting" /> | `EXEC` | <CopyableCode code="action, team_id, data__data, dd_site" /> | Update a team permission setting for a given team. |
