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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>users</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.schedules.users" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | The name of the user. |
| <CopyableCode code="description" /> | `string` | The user's bio. |
| <CopyableCode code="_type" /> | `string` | The type of object being created. |
| <CopyableCode code="avatar_url" /> | `string` | The URL of the user's avatar. |
| <CopyableCode code="color" /> | `string` | The schedule color. |
| <CopyableCode code="contact_methods" /> | `array` | The list of contact methods for the user. |
| <CopyableCode code="email" /> | `string` | The user's email address. |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="invitation_sent" /> | `boolean` | If true, the user has an outstanding invitation. |
| <CopyableCode code="job_title" /> | `string` | The user's title. |
| <CopyableCode code="license" /> | `object` | The License assigned to the User |
| <CopyableCode code="notification_rules" /> | `array` | The list of notification rules for the user. |
| <CopyableCode code="role" /> | `string` | The user role. Account must have the `read_only_users` ability to set a user as a `read_only_user` or a `read_only_limited_user`, and must have advanced permissions abilities to set a user as `observer` or `restricted_access`. |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="teams" /> | `array` | The list of teams to which the user belongs. Account must have the `teams` ability to set this. |
| <CopyableCode code="time_zone" /> | `string` | The preferred time zone name. If null, the account's time zone will be used. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
## Methods
| Name | Accessible by | Required Params |
|:-----|:--------------|:----------------|
| <CopyableCode code="list_schedule_users" /> | `SELECT` | <CopyableCode code="id" /> |
| <CopyableCode code="_list_schedule_users" /> | `EXEC` | <CopyableCode code="id" /> |
