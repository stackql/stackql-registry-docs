---
title: oncall_handoff_notification_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - oncall_handoff_notification_rules
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
<tr><td><b>Name</b></td><td><code>oncall_handoff_notification_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.users.oncall_handoff_notification_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="contact_method" /> | `object` |  |
| <CopyableCode code="handoff_type" /> | `string` | The type of handoff being created. |
| <CopyableCode code="notify_advance_in_minutes" /> | `integer` | The delay before firing the rule, in minutes. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_user_handoff_notifiaction_rule" /> | `SELECT` | <CopyableCode code="id, oncall_handoff_notification_rule_id" /> | Get details about a User's Handoff Notification Rule.<br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.read`<br /> |
| <CopyableCode code="get_user_handoff_notification_rules" /> | `SELECT` | <CopyableCode code="id" /> | List Handoff Notification Rules of your PagerDuty User.<br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.read`<br /> |
| <CopyableCode code="create_user_handoff_notification_rule" /> | `INSERT` | <CopyableCode code="id, data__oncall_handoff_notification_rule" /> | Create a new Handoff Notification Rule.<br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.write`<br /> |
| <CopyableCode code="delete_user_handoff_notification_rule" /> | `DELETE` | <CopyableCode code="id, oncall_handoff_notification_rule_id" /> | Remove a User's Handoff Notification Rule.<br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.write`<br /> |
| <CopyableCode code="_get_user_handoff_notifiaction_rule" /> | `EXEC` | <CopyableCode code="id, oncall_handoff_notification_rule_id" /> | Get details about a User's Handoff Notification Rule.<br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.read`<br /> |
| <CopyableCode code="_get_user_handoff_notification_rules" /> | `EXEC` | <CopyableCode code="id" /> | List Handoff Notification Rules of your PagerDuty User.<br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.read`<br /> |
| <CopyableCode code="update_user_handoff_notification" /> | `EXEC` | <CopyableCode code="id, oncall_handoff_notification_rule_id, data__oncall_handoff_notification_rule" /> | Update a User's Handoff Notification Rule.<br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users.write`<br /> |
