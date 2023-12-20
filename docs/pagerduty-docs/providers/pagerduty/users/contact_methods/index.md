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
  
    

## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>contact_methods</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.users.contact_methods</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `EmailContactMethod__type` | `string` |  |
| `EmailContactMethod_address` | `string` | The "address" to deliver to: email, phone number, etc., depending on the type. |
| `EmailContactMethod_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `EmailContactMethod_id` | `string` |  |
| `EmailContactMethod_label` | `string` | The label (e.g., "Work", "Mobile", etc.). |
| `EmailContactMethod_self` | `string` | the API show URL at which the object is accessible |
| `EmailContactMethod_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `EmailContactMethod_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `PushContactMethod__type` | `string` |  |
| `PushContactMethod_address` | `string` | The "address" to deliver to: email, phone number, etc., depending on the type. |
| `PushContactMethod_blacklisted` | `boolean` | If true, this phone has been blacklisted by PagerDuty and no messages will be sent to it. |
| `PushContactMethod_html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `PushContactMethod_id` | `string` |  |
| `PushContactMethod_label` | `string` | The label (e.g., "Work", "Mobile", etc.). |
| `PushContactMethod_self` | `string` | the API show URL at which the object is accessible |
| `PushContactMethod_summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `PushContactMethod_type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `_type` | `string` |  |
| `address` | `string` | The "address" to deliver to: email, phone number, etc., depending on the type. |
| `blacklisted` | `boolean` | If true, this phone has been blacklisted by PagerDuty and no messages will be sent to it. |
| `country_code` | `integer` | The 1-to-3 digit country calling code. |
| `created_at` | `string` | Time at which the contact method was created. |
| `device_type` | `string` | The type of device. |
| `enabled` | `boolean` | If true, this phone is capable of receiving SMS messages. |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `label` | `string` | The label (e.g., "Work", "Mobile", etc.). |
| `self` | `string` | the API show URL at which the object is accessible |
| `send_short_email` | `boolean` | Send an abbreviated email message instead of the standard email output. Useful for email-to-SMS gateways and email based pagers. |
| `sounds` | `array` |  |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_user_contact_method` | `SELECT` | `contact_method_id, id` | Get details about a User's contact method.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.read`<br /> |
| `get_user_contact_methods` | `SELECT` | `id` | List contact methods of your PagerDuty user.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.read`<br /> |
| `create_user_contact_method` | `INSERT` | `id, data__contact_method` | Create a new contact method for the User.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.write`<br /> |
| `delete_user_contact_method` | `DELETE` | `contact_method_id, id` | Remove a user's contact method.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.write`<br /> |
| `_get_user_contact_method` | `EXEC` | `contact_method_id, id` | Get details about a User's contact method.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.read`<br /> |
| `_get_user_contact_methods` | `EXEC` | `id` | List contact methods of your PagerDuty user.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.read`<br /> |
| `update_user_contact_method` | `EXEC` | `contact_method_id, id, data__contact_method` | Update a User's contact method.<br /><br />Users are members of a PagerDuty account that have the ability to interact with Incidents and other data on the account.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#users)<br /><br />Scoped OAuth requires: `users:contact_methods.write`<br /> |
