---
title: status_update_notification_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - status_update_notification_rules
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>status_update_notification_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.users.status_update_notification_rules" /></td></tr>
</tbody></table>

## Fields
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_user_status_update_notification_rule" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS, id, status_update_notification_rule_id" /> | Get details about a user's status update notification rule.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.read`<br /> |
| <CopyableCode code="get_user_status_update_notification_rules" /> | `SELECT` | <CopyableCode code="X-EARLY-ACCESS, id" /> | List status update notification rules of your PagerDuty user.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.read`<br /> |
| <CopyableCode code="create_user_status_update_notification_rule" /> | `INSERT` | <CopyableCode code="X-EARLY-ACCESS, id, data__status_update_notification_rule" /> | Create a new status update notification rule.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.write`<br /> |
| <CopyableCode code="delete_user_status_update_notification_rule" /> | `DELETE` | <CopyableCode code="X-EARLY-ACCESS, id, status_update_notification_rule_id" /> | Remove a user's status update notification rule.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.write`<br /> |
| <CopyableCode code="_get_user_status_update_notification_rule" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, id, status_update_notification_rule_id" /> | Get details about a user's status update notification rule.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.read`<br /> |
| <CopyableCode code="_get_user_status_update_notification_rules" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, id" /> | List status update notification rules of your PagerDuty user.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.read`<br /> |
| <CopyableCode code="update_user_status_update_notification_rule" /> | `EXEC` | <CopyableCode code="X-EARLY-ACCESS, id, status_update_notification_rule_id, data__status_update_notification_rule" /> | Update a user's status update notification rule.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />&lt;!-- theme: warning --&gt;<br />&gt; ### Early Access<br />&gt; This endpoint is in Early Access and may change at any time. You must pass in the X-EARLY-ACCESS header to access it.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.write`<br /> |
