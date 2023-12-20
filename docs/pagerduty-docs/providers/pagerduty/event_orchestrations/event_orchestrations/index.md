---
title: event_orchestrations
hide_title: false
hide_table_of_contents: false
keywords:
  - event_orchestrations
  - event_orchestrations
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
<tr><td><b>Name</b></td><td><code>event_orchestrations</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.event_orchestrations.event_orchestrations</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the Orchestration. |
| `name` | `string` | Name of the Orchestration. |
| `description` | `string` | A description of this Orchestration's purpose. |
| `created_at` | `string` | The date the Orchestration was created at. |
| `created_by` | `object` | Reference to the user that has created the Orchestration. |
| `integrations` | `array` |  |
| `routes` | `integer` | Number of different Service Orchestration being routed to |
| `self` | `string` | The API show URL at which the object is accessible |
| `team` | `object` | Reference to the team that owns the Orchestration. If none is specified, only admins have access. |
| `updated_at` | `string` | The date the Orchestration was last updated. |
| `updated_by` | `object` | Reference to the user that has updated the Orchestration last. |
| `version` | `string` | Version of the Orchestration. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_orchestration` | `SELECT` | `id` | Get a Global Event Orchestration.<br /><br />Global Event Orchestrations allow you define a set of Global Rules and Router Rules, so that when you ingest events using the Orchestration's Routing Key your events will have actions applied via the Global Rules & then routed to the correct Service by the Router Rules, based on the event's content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.read`<br /> |
| `list_event_orchestrations` | `SELECT` |  | List all Global Event Orchestrations on an Account.<br /><br />Global Event Orchestrations allow you define a set of Global Rules and Router Rules, so that when you ingest events using the Orchestration's Routing Key your events will have actions applied via the Global Rules & then routed to the correct Service by the Router Rules, based on the event's content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.read`<br /> |
| `delete_orchestration` | `DELETE` | `id` | Delete a Global Event Orchestration.<br /><br />Once deleted, you will no longer be able to ingest events into PagerDuty using this Orchestration's Routing Key.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.write`<br /> |
| `_get_orchestration` | `EXEC` | `id` | Get a Global Event Orchestration.<br /><br />Global Event Orchestrations allow you define a set of Global Rules and Router Rules, so that when you ingest events using the Orchestration's Routing Key your events will have actions applied via the Global Rules & then routed to the correct Service by the Router Rules, based on the event's content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.read`<br /> |
| `_list_event_orchestrations` | `EXEC` |  | List all Global Event Orchestrations on an Account.<br /><br />Global Event Orchestrations allow you define a set of Global Rules and Router Rules, so that when you ingest events using the Orchestration's Routing Key your events will have actions applied via the Global Rules & then routed to the correct Service by the Router Rules, based on the event's content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.read`<br /> |
| `post_orchestration` | `EXEC` | `data__orchestration` | Create a Global Event Orchestration.<br /><br />Global Event Orchestrations allow you define a set of Global Rules and Router Rules, so that when you ingest events using the Orchestration's Routing Key your events will have actions applied via the Global Rules & then routed to the correct Service by the Router Rules, based on the event's content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.write`<br /> |
| `update_orchestration` | `EXEC` | `id, data__orchestration` | Update a Global Event Orchestration.<br /><br />Global Event Orchestrations allow you define a set of Global Rules and Router Rules, so that when you ingest events using the Orchestration's Routing Key your events will have actions applied via the Global Rules & then routed to the correct Service by the Router Rules, based on the event's content.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.write`<br /> |
