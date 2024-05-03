---
title: actions_teams
hide_title: false
hide_table_of_contents: false
keywords:
  - actions_teams
  - automation_actions
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>actions_teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.automation_actions.actions_teams" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="_type" /> | `string` |  |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_automation_actions_action_team_association" /> | `SELECT` | <CopyableCode code="id, team_id" /> | Gets the details of an Automation Action / team relation |
| <CopyableCode code="get_automation_actions_action_team_associations" /> | `SELECT` | <CopyableCode code="id" /> | Gets all team references associated with an Automation Action |
| <CopyableCode code="create_automation_action_team_association" /> | `INSERT` | <CopyableCode code="id, data__team" /> | Associate an Automation Action with a team<br /> |
| <CopyableCode code="delete_automation_action_team_association" /> | `DELETE` | <CopyableCode code="id, team_id" /> | Disassociate an Automation Action from a team<br /> |
| <CopyableCode code="_get_automation_actions_action_team_association" /> | `EXEC` | <CopyableCode code="id, team_id" /> | Gets the details of an Automation Action / team relation |
| <CopyableCode code="_get_automation_actions_action_team_associations" /> | `EXEC` | <CopyableCode code="id" /> | Gets all team references associated with an Automation Action |
