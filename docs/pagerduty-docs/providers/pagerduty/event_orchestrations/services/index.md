---
title: services
hide_title: false
hide_table_of_contents: false
keywords:
  - services
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
<tr><td><b>Name</b></td><td><code>services</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><CopyableCode code="pagerduty.event_orchestrations.services" /></td></tr>
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
| <CopyableCode code="get_orch_path_service" /> | `SELECT` | <CopyableCode code="service_id" /> | Get a Service Orchestration.<br /><br />A Service Orchestration allows you to create a set of Event Rules. The Service Orchestration evaluates Events sent to this Service against each of its rules, beginning with the rules in the "start" set. When a matching rule is found, it can modify and enhance the event and can route the event to another set of rules within this Service Orchestration for further processing.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="_get_orch_path_service" /> | `EXEC` | <CopyableCode code="service_id" /> | Get a Service Orchestration.<br /><br />A Service Orchestration allows you to create a set of Event Rules. The Service Orchestration evaluates Events sent to this Service against each of its rules, beginning with the rules in the "start" set. When a matching rule is found, it can modify and enhance the event and can route the event to another set of rules within this Service Orchestration for further processing.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `services.read`<br /> |
| <CopyableCode code="update_orch_path_service" /> | `EXEC` | <CopyableCode code="service_id" /> | Update a Service Orchestration.<br /><br />A Service Orchestration allows you to create a set of Event Rules. The Service Orchestration evaluates Events sent to this Service against each of its rules, beginning with the rules in the "start" set. When a matching rule is found, it can modify and enhance the event and can route the event to another set of rules within this Service Orchestration for further processing.<br /><br />For more information see the [API Concepts Document](../../api-reference/ZG9jOjI3NDc5Nzc-api-concepts#event-orchestrations)<br /><br />Scoped OAuth requires: `services.write`<br /> |
