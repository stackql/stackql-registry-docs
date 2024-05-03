---
title: router
hide_title: false
hide_table_of_contents: false
keywords:
  - router
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

import CopyableCode from '@site/src/components/CopyableCode/CopyableCode';




## Overview
<table><tbody>
<tr><td><b>Name</b></td><td><code>router</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.event_orchestrations.router" /></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| <CopyableCode code="catch_all" /> | `object` | When none of the Rules in a set match an event, we apply the catch_all actions to the event. |
| <CopyableCode code="created_at" /> | `string` | The date/time the object was created. |
| <CopyableCode code="created_by" /> | `object` | Reference to the user that created the object. |
| <CopyableCode code="parent" /> | `object` |  |
| <CopyableCode code="sets" /> | `array` | Must contain at least a "start" set, but can contain any number of additional sets that are routed to by other rules to form a directional graph of rules. |
| <CopyableCode code="type" /> | `string` |  |
| <CopyableCode code="updated_at" /> | `string` | The date/time the object was last updated. |
| <CopyableCode code="updated_by" /> | `object` | Reference to the user that last updated the object. |
| <CopyableCode code="version" /> | `string` | Version of these Orchestration Rules |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| <CopyableCode code="get_orch_path_router" /> | `SELECT` | <CopyableCode code="id" /> | Get a Global Orchestration's Routing Rules.<br /><br />An Orchestration Router allows you to create a set of Event Rules. The Router evaluates Events you send to this Global Orchestration against each of its rules, one at a time, and routes the event to a specific Service based on the first rule that matches. If an event doesn't match any rules, it'll be sent to service specified in as the `catch_all` or the "Unrouted" Orchestration if no service is specified.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.read`<br /> |
| <CopyableCode code="_get_orch_path_router" /> | `EXEC` | <CopyableCode code="id" /> | Get a Global Orchestration's Routing Rules.<br /><br />An Orchestration Router allows you to create a set of Event Rules. The Router evaluates Events you send to this Global Orchestration against each of its rules, one at a time, and routes the event to a specific Service based on the first rule that matches. If an event doesn't match any rules, it'll be sent to service specified in as the `catch_all` or the "Unrouted" Orchestration if no service is specified.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.read`<br /> |
| <CopyableCode code="update_orch_path_router" /> | `EXEC` | <CopyableCode code="id" /> | Update a Global Orchestration's Routing Rules.<br /><br />An Orchestration Router allows you to create a set of Event Rules. The Router evaluates Events you send to this Global Orchestration against each of its rules, one at a time, and routes the event to a specific Service based on the first rule that matches. If an event doesn't match any rules, it'll be sent to service specified in as the `catch_all` or the "Unrouted" Orchestration if no service is specified.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `event_orchestrations.write`<br /> |
