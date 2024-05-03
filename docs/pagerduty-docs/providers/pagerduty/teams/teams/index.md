---
title: teams
hide_title: false
hide_table_of_contents: false
keywords:
  - teams
  - teams
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
<tr><td><b>Name</b></td><td><code>teams</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.teams.teams" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | The name of the team. |
| <CopyableCode code="description" /> | `string` | The description of the team. |
| <CopyableCode code="_type" /> | `string` | The type of object being created. |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="parent" /> | `object` |  |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_team" /> | `SELECT` | <CopyableCode code="id" /> | Get details about an existing team.<br /><br />A team is a collection of Users and Escalation Policies that represent a group of people within an organization.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#teams)<br /><br />Scoped OAuth requires: `teams.read`<br /> |
| <CopyableCode code="list_teams" /> | `SELECT` |  | List teams of your PagerDuty account, optionally filtered by a search query.<br /><br />A team is a collection of Users and Escalation Policies that represent a group of people within an organization.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#teams)<br /><br />Scoped OAuth requires: `teams.read`<br /> |
| <CopyableCode code="create_team" /> | `INSERT` | <CopyableCode code="data__team" /> | Create a new Team.<br /><br />A team is a collection of Users and Escalation Policies that represent a group of people within an organization.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#teams)<br /><br />Scoped OAuth requires: `teams.write`<br /> |
| <CopyableCode code="delete_team" /> | `DELETE` | <CopyableCode code="id" /> | Remove an existing team.<br /><br />Succeeds only if the team has no associated Escalation Policies, Services, Schedules and Subteams.<br /><br />All associated unresovled incidents will be reassigned to another team (if specified) or will loose team association, thus becoming account-level (with visibility implications).<br /><br />Note that the incidents reassignment process is asynchronous and has no guarantee to complete before the API call return.<br /><br />A team is a collection of Users and Escalation Policies that represent a group of people within an organization.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#teams)<br /><br />Scoped OAuth requires: `teams.write`<br /> |
| <CopyableCode code="_get_team" /> | `EXEC` | <CopyableCode code="id" /> | Get details about an existing team.<br /><br />A team is a collection of Users and Escalation Policies that represent a group of people within an organization.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#teams)<br /><br />Scoped OAuth requires: `teams.read`<br /> |
| <CopyableCode code="_list_teams" /> | `EXEC` |  | List teams of your PagerDuty account, optionally filtered by a search query.<br /><br />A team is a collection of Users and Escalation Policies that represent a group of people within an organization.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#teams)<br /><br />Scoped OAuth requires: `teams.read`<br /> |
| <CopyableCode code="update_team" /> | `EXEC` | <CopyableCode code="id, data__team" /> | Update an existing team.<br /><br />A team is a collection of Users and Escalation Policies that represent a group of people within an organization.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#teams)<br /><br />Scoped OAuth requires: `teams.write`<br /> |
