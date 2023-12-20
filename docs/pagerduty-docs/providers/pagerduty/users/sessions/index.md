---
title: sessions
hide_title: false
hide_table_of_contents: false
keywords:
  - sessions
  - users
  - pagerduty    
  - stackql
  - infrastructure-as-code
  - configuration-as-data
  - cloud inventory
description: Query, manage, and integrate PagerDuty resources using SQL
custom_edit_url: null
image: /img/providers/pagerduty/stackql-pagerduty-provider-featured-image.png
---
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>sessions</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.users.sessions</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `created_at` | `string` | The date/time the user session was first created. |
| `summary` | `string` | The summary of the session |
| `type` | `string` | The type of the session |
| `user_id` | `string` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_user_session` | `SELECT` | `id, session_id, type` | Get details about a user's session.<br /><br />Beginning November 2021, user sessions no longer includes newly issued OAuth tokens.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:sessions.read`<br /> |
| `get_user_sessions` | `SELECT` | `id` | List active sessions of a PagerDuty user.<br /><br />Beginning November 2021, active sessions no longer includes newly issued OAuth tokens.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:sessions.read`<br /> |
| `delete_user_session` | `DELETE` | `id, session_id, type` | Delete a user's session.<br /><br />Beginning November 2021, user sessions no longer includes newly issued OAuth tokens.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:sessions.write`<br /> |
| `delete_user_sessions` | `DELETE` | `id` | Delete all user sessions.<br /><br />Beginning November 2021, user sessions no longer includes newly issued OAuth tokens.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:sessions.write`<br /> |
| `_get_user_session` | `EXEC` | `id, session_id, type` | Get details about a user's session.<br /><br />Beginning November 2021, user sessions no longer includes newly issued OAuth tokens.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:sessions.read`<br /> |
| `_get_user_sessions` | `EXEC` | `id` | List active sessions of a PagerDuty user.<br /><br />Beginning November 2021, active sessions no longer includes newly issued OAuth tokens.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:sessions.read`<br /> |
