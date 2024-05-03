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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>schedules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.schedules.schedules" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="id" /> | `string` |  |
| <CopyableCode code="name" /> | `string` | The name of the schedule |
| <CopyableCode code="description" /> | `string` | The description of the schedule |
| <CopyableCode code="_type" /> | `string` | The type of object being created. |
| <CopyableCode code="escalation_policies" /> | `array` | An array of all of the escalation policies that uses this schedule. |
| <CopyableCode code="final_schedule" /> | `object` |  |
| <CopyableCode code="html_url" /> | `string` | a URL at which the entity is uniquely displayed in the Web app |
| <CopyableCode code="overrides_subschedule" /> | `object` |  |
| <CopyableCode code="schedule_layers" /> | `array` | A list of schedule layers. |
| <CopyableCode code="self" /> | `string` | the API show URL at which the object is accessible |
| <CopyableCode code="summary" /> | `string` | A short-form, server-generated string that provides succinct, important information about an object suitable for primary labeling of an entity in a client. In many cases, this will be identical to `name`, though it is not intended to be an identifier. |
| <CopyableCode code="teams" /> | `array` | An array of all of the teams on the schedule. |
| <CopyableCode code="time_zone" /> | `string` | The time zone of the schedule. |
| <CopyableCode code="type" /> | `string` | A string that determines the schema of the object. This must be the standard name for the entity, suffixed by `_reference` if the object is a reference. |
| <CopyableCode code="users" /> | `array` | An array of all of the users on the schedule. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_schedule" /> | `SELECT` | <CopyableCode code="id" /> | Show detailed information about a schedule, including entries for each layer and sub-schedule.<br />Scoped OAuth requires: `schedules.read`<br /> |
| <CopyableCode code="list_schedules" /> | `SELECT` |  | List the on-call schedules.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.read`<br /> |
| <CopyableCode code="create_schedule" /> | `INSERT` | <CopyableCode code="data__schedule" /> | Create a new on-call schedule.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.write`<br /> |
| <CopyableCode code="create_schedule_preview" /> | `INSERT` | <CopyableCode code="data__schedule" /> | Preview what an on-call schedule would look like without saving it.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.write`<br /> |
| <CopyableCode code="delete_schedule" /> | `DELETE` | <CopyableCode code="id" /> | Delete an on-call schedule.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.write`<br /> |
| <CopyableCode code="_get_schedule" /> | `EXEC` | <CopyableCode code="id" /> | Show detailed information about a schedule, including entries for each layer and sub-schedule.<br />Scoped OAuth requires: `schedules.read`<br /> |
| <CopyableCode code="_list_schedules" /> | `EXEC` |  | List the on-call schedules.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.read`<br /> |
| <CopyableCode code="update_schedule" /> | `EXEC` | <CopyableCode code="id, data__schedule" /> | Update an existing on-call schedule.<br /><br />A Schedule determines the time periods that users are On-Call.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#schedules)<br /><br />Scoped OAuth requires: `schedules.write`<br /> |
