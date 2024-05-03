---
title: contact_methods
hide_title: false
hide_table_of_contents: false
keywords:
  - contact_methods
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
<tr><td><b>Name</b></td><td><code>contact_methods</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.users.contact_methods" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="EmailContactMethod__type" /> | `string` |  |
| <CopyableCode code="EmailContactMethod_address" /> | `string` | The "address" to deliver to: email, phone number, etc., depending on the type. |
| <CopyableCode code="EmailContactMethod_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="EmailContactMethod_id" /> | `string` |  |
| <CopyableCode code="EmailContactMethod_label" /> | `string` | The label (e.g., "Work", "Mobile", etc.). |
| <CopyableCode code="EmailContactMethod_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="EmailContactMethod_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="EmailContactMethod_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="PushContactMethod__type" /> | `string` |  |
| <CopyableCode code="PushContactMethod_address" /> | `string` | The "address" to deliver to: email, phone number, etc., depending on the type. |
| <CopyableCode code="PushContactMethod_blacklisted" /> | `boolean` | If true, this phone has been blacklisted by PagerDuty and no messages will be sent to it. |
| <CopyableCode code="PushContactMethod_html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="PushContactMethod_id" /> | `string` |  |
| <CopyableCode code="PushContactMethod_label" /> | `string` | The label (e.g., "Work", "Mobile", etc.). |
| <CopyableCode code="PushContactMethod_self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="PushContactMethod_summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="PushContactMethod_type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="_type" /> | `string` |  |
| <CopyableCode code="address" /> | `string` | The "address" to deliver to: email, phone number, etc., depending on the type. |
| <CopyableCode code="blacklisted" /> | `boolean` | If true, this phone has been blacklisted by PagerDuty and no messages will be sent to it. |
| <CopyableCode code="country_code" /> | `integer` | The 1-to-3 digit country calling code. |
| <CopyableCode code="created_at" /> | `string` | Time at which the contact method was created. |
| <CopyableCode code="device_type" /> | `string` | The type of device. |
| <CopyableCode code="enabled" /> | `boolean` | If true, this phone is capable of receiving SMS messages. |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="label" /> | `string` | The label (e.g., "Work", "Mobile", etc.). |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="send_short_email" /> | `boolean` | Send an abbreviated email message instead of the standard email output. Useful for email-to-SMS gateways and email based pagers. |
| <CopyableCode code="sounds" /> | `array` |  |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_user_contact_method" /> | `SELECT` | <CopyableCode code="contact_method_id, id" /> | Get details about a User's contact method.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.read`<br /> |
| <CopyableCode code="get_user_contact_methods" /> | `SELECT` | <CopyableCode code="id" /> | List contact methods of your PagerDuty user.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.read`<br /> |
| <CopyableCode code="create_user_contact_method" /> | `INSERT` | <CopyableCode code="id, data__contact_method" /> | Create a new contact method for the User.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.write`<br /> |
| <CopyableCode code="delete_user_contact_method" /> | `DELETE` | <CopyableCode code="contact_method_id, id" /> | Remove a user's contact method.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.write`<br /> |
| <CopyableCode code="_get_user_contact_method" /> | `EXEC` | <CopyableCode code="contact_method_id, id" /> | Get details about a User's contact method.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.read`<br /> |
| <CopyableCode code="_get_user_contact_methods" /> | `EXEC` | <CopyableCode code="id" /> | List contact methods of your PagerDuty user.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.read`<br /> |
| <CopyableCode code="update_user_contact_method" /> | `EXEC` | <CopyableCode code="contact_method_id, id, data__contact_method" /> | Update a User's contact method.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.write`<br /> |
