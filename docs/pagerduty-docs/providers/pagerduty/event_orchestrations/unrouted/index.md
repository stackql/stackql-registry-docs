---
title: unrouted
hide_title: false
hide_table_of_contents: false
keywords:
  - unrouted
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
<tr><td><b>Name</b></td><td><code>unrouted</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.event_orchestrations.unrouted</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `catch_all` | `object` | When none of the Rules in a set match an event, we apply the catch_all actions to the event. |
| `created_at` | `string` | The date/time the object was created. |
| `created_by` | `object` | Reference to the user that created the object. |
| `parent` | `object` |  |
| `sets` | `array` | Must contain at least a "start" set, but can contain any number of additional sets that are routed to by other rules to form a directional graph of rules. |
| `type` | `string` |  |
| `updated_at` | `string` | The date/time the object was last updated. |
| `updated_by` | `object` | Reference to the user that last updated the object. |
| `version` | `string` | Version of these Orchestration Rules |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_orch_path_unrouted` | `SELECT` | `id` | Get a Global Event Orchestration's Rules for Unrouted events.<br /><br />An Unrouted Orchestration allows you to create a set of Event Rules that will be evaluated against all events that don't match any rules in the Global Orchestration's Router. Events that reach the Unrouted Orchestration will never be routed to a specific Service.<br /><br />The Unrouted Orchestration evaluates Events sent to it against each of its rules, beginning with the rules in the "start" set. When a matching rule is found, it can modify and enhance the event and can route the event to another set of rules within this Unrouted Orchestration for further processing.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.read`<br /> |
| `_get_orch_path_unrouted` | `EXEC` | `id` | Get a Global Event Orchestration's Rules for Unrouted events.<br /><br />An Unrouted Orchestration allows you to create a set of Event Rules that will be evaluated against all events that don't match any rules in the Global Orchestration's Router. Events that reach the Unrouted Orchestration will never be routed to a specific Service.<br /><br />The Unrouted Orchestration evaluates Events sent to it against each of its rules, beginning with the rules in the "start" set. When a matching rule is found, it can modify and enhance the event and can route the event to another set of rules within this Unrouted Orchestration for further processing.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.read`<br /> |
| `update_orch_path_unrouted` | `EXEC` | `id` | Update a Global Event Orchestration's Rules for Unrouted events.<br /><br />An Unrouted Orchestration allows you to create a set of Event Rules that will be evaluated against all events that don't match any rules in the Global Orchestration's Router. Events that reach the Unrouted Orchestration will never be routed to a specific Service.<br /><br />The Unrouted Orchestration evaluates Events sent to it against each of its rules, beginning with the rules in the "start" set. When a matching rule is found, it can modify and enhance the event and can route the event to another set of rules within this Unrouted Orchestration for further processing.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.write`<br /> |
