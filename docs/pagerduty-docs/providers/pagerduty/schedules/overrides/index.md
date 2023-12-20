---
title: overrides
hide_title: false
hide_table_of_contents: false
keywords:
  - overrides
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
<tr><td><b>Name</b></td><td><code>overrides</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.schedules.overrides</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` |  |
| `_id` | `string` |  |
| `end` | `string` | The end date and time for the override. |
| `html_url` | `string` | a URL at which the entity is uniquely displayed in the Web app |
| `self` | `string` | the API show URL at which the object is accessible |
| `start` | `string` | The start date and time for the override. |
| `summary` | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| `type` | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| `user` | `object` |  |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `list_schedule_overrides` | `SELECT` | `id, since, until` | List overrides for a given time range.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.read`<br /> |
| `create_schedule_override` | `INSERT` | `id` | Create one or more overrides, each for a specific user covering a specified time range. If you create an override on top of an existing override, the last created override will have priority.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />Note: An older implementation of this endpoint only supported creating a single ocverride per request. That functionality is still supported, but deprecated and may be removed in the future.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.write`<br /> |
| `delete_schedule_override` | `DELETE` | `id, override_id` | Remove an override.<br /><br />You cannot remove a past override.<br /><br />If the override start time is before the current time, but the end time is after the current time, the override will be truncated to the current time.<br /><br />If the override is truncated, the status code will be 200 OK, as opposed to a 204 No Content for a successful delete.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.write`<br /> |
| `_list_schedule_overrides` | `EXEC` | `id, since, until` | List overrides for a given time range.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.read`<br /> |
