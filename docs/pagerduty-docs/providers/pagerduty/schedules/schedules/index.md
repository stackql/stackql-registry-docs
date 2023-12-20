---
title: schedules
hide_title: false
hide_table_of_contents: false
keywords:
  - schedules
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
<tr><td><b>Name</b></td><td><code>schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.schedules.schedules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `name` | `string` | The name of the schedule |
| `description` | `string` | The description of the schedule |
| `_type` | `string` | The type of object being created. |
| `escalation_policies` | `array` | An array of all of the escalation policies that uses this schedule. |
| `final_schedule` | `object` |  |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `overrides_subschedule` | `object` |  |
| `schedule_layers` | `array` | A list of schedule layers. |
| `self` | `string` | the API show URL at which the object is accessible |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `teams` | `array` | An array of all of the teams on the schedule. |
| `time_zone` | `string` | The time zone of the schedule. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `users` | `array` | An array of all of the users on the schedule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_schedule` | `SELECT` | `id` | Show detailed information about a schedule, including entries for each layer and sub-schedule.<br />Scoped OAuth requires: `schedules.read`<br /> |
| `list_schedules` | `SELECT` |  | List the on-call schedules.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.read`<br /> |
| `create_schedule` | `INSERT` | `data__schedule` | Create a new on-call schedule.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.write`<br /> |
| `create_schedule_preview` | `INSERT` | `data__schedule` | Preview what an on-call schedule would look like without saving it.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.write`<br /> |
| `delete_schedule` | `DELETE` | `id` | Delete an on-call schedule.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.write`<br /> |
| `_get_schedule` | `EXEC` | `id` | Show detailed information about a schedule, including entries for each layer and sub-schedule.<br />Scoped OAuth requires: `schedules.read`<br /> |
| `_list_schedules` | `EXEC` |  | List the on-call schedules.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.read`<br /> |
| `update_schedule` | `EXEC` | `id, data__schedule` | Update an existing on-call schedule.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.write`<br /> |
