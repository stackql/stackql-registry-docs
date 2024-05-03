---
title: notification_rules
hide_title: false
hide_table_of_contents: false
keywords:
  - notification_rules
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
<tr><td><b>Name</b></td><td><code>notification_rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.users.notification_rules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="_type" /> | `string` | The type of object being created. |
| <CopyableCode code="contact_method" /> | `object` |  |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="start_delay_in_minutes" /> | `integer` | The delay before firing the rule, in minutes. |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="urgency" /> | `string` | Which incident urgency this rule is used for. Account must have the `urgencies` ability to have a low urgency notification rule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_user_notification_rule" /> | `SELECT` | <CopyableCode code="id, notification_rule_id" /> | Get details about a user's notification rule.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.read`<br /> |
| <CopyableCode code="get_user_notification_rules" /> | `SELECT` | <CopyableCode code="id" /> | List notification rules of your PagerDuty user.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.read`<br /> |
| <CopyableCode code="create_user_notification_rule" /> | `INSERT` | <CopyableCode code="id, data__notification_rule" /> | Create a new notification rule.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.write`<br /> |
| <CopyableCode code="delete_user_notification_rule" /> | `DELETE` | <CopyableCode code="id, notification_rule_id" /> | Remove a user's notification rule.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.write`<br /> |
| <CopyableCode code="_get_user_notification_rule" /> | `EXEC` | <CopyableCode code="id, notification_rule_id" /> | Get details about a user's notification rule.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.read`<br /> |
| <CopyableCode code="_get_user_notification_rules" /> | `EXEC` | <CopyableCode code="id" /> | List notification rules of your PagerDuty user.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.read`<br /> |
| <CopyableCode code="update_user_notification_rule" /> | `EXEC` | <CopyableCode code="id, notification_rule_id, data__notification_rule" /> | Update a user's notification rule.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.write`<br /> |
