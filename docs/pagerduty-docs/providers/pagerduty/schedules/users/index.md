---
title: users
hide_title: false
hide_table_of_contents: false
keywords:
  - users
  - schedules
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
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.schedules.users</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | The name of the user. |
| `description` | `string` | The user's bio. |
| `_type` | `string` | The type of object being created. |
| `avatar_url` | `string` | The URL of the user's avatar. |
| `color` | `string` | The schedule color. |
| `contact_methods` | `array` | The list of contact methods for the user. |
| `email` | `string` | The user's email address. |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `invitation_sent` | `boolean` | If true, the user has an outstanding invitation. |
| `job_title` | `string` | The user's title. |
| `license` | `object` | The License assigned to the User |
| `notification_rules` | `array` | The list of notification rules for the user. |
| `role` | `string` | The user role. Account must have the `read_only_users` ability to set a user as a `read_only_user` or a `read_only_limited_user`, and must have advanced permissions abilities to set a user as `observer` or `restricted_access`. |
| `self` | `string` | the API show URL at which the object is accessible |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `teams` | `array` | The list of teams to which the user belongs. Account must have the `teams` ability to set this. |
| `time_zone` | `string` | The preferred time zone name. If null, the account's time zone will be used. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| `list_schedule_users` | `SELECT` | `id` |
| `_list_schedule_users` | `EXEC` | `id` |
