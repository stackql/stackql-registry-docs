---
title: members
hide_title: false
hide_table_of_contents: false
keywords:
  - members
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
<tr><td><b>Name</b></td><td><code>members</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.teams.members" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype |
|:-----|:---------|
| <CopyableCode code="role" /> | `string` |
| <CopyableCode code="user" /> | `object` |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="list_team_users" /> | `SELECT` | <CopyableCode code="id" /> | Get information about members on a team.<br /><br />A team is a collection of Users and Escalation Policies that represent a group of people within an organization.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#teams)<br /><br />Scoped OAuth requires: `teams.read`<br /> |
| <CopyableCode code="delete_team_user" /> | `DELETE` | <CopyableCode code="id, user_id" /> | Remove a user from a team.<br /><br />A team is a collection of Users and Escalation Policies that represent a group of people within an organization.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#teams)<br /><br />Scoped OAuth requires: `teams.write`<br /> |
| <CopyableCode code="_list_team_users" /> | `EXEC` | <CopyableCode code="id" /> | Get information about members on a team.<br /><br />A team is a collection of Users and Escalation Policies that represent a group of people within an organization.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#teams)<br /><br />Scoped OAuth requires: `teams.read`<br /> |
| <CopyableCode code="update_team_user" /> | `EXEC` | <CopyableCode code="id, user_id" /> | Add a user to a team. Attempting to add a user with the `read_only_user` role will return a 400 error.<br /><br />A team is a collection of Users and Escalation Policies that represent a group of people within an organization.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#teams)<br /><br />Scoped OAuth requires: `teams.write`<br /> |
