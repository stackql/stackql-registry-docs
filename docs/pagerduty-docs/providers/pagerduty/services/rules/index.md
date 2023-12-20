---
title: rules
hide_title: false
hide_table_of_contents: false
keywords:
  - rules
  - services
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
<tr><td><b>Name</b></td><td><code>rules</code></td></tr>
<tr><td><b>Type</b></td><td>Resource</td></tr>
<tr><td><b>Id</b></td><td><code>pagerduty.services.rules</code></td></tr>
</tbody></table>

## Fields
| Name | Datatype | Description |
|:-----|:---------|:------------|
| `id` | `string` | ID of the Event Rule. |
| `actions` | `object` | When an event matches this Event Rule, the actions that will be taken to change the resulting Alert and Incident. |
| `conditions` | `object` | Conditions evaluated to check if an event matches this Event Rule. Is always empty for the catch_all rule, though. |
| `disabled` | `boolean` | Indicates whether the Event Rule is disabled and would therefore not be evaluated. |
| `position` | `integer` | Position/index of the Event Rule on the Service.  Starting from position 0 (the first rule), rules are evaluated one-by-one until a matching Event Rule is found or the end of the list is reached. |
| `self` | `string` | the API show URL at which the object is accessible. |
| `time_frame` | `object` | Time-based conditions for limiting when the rule is active. |
| `variables` | `array` | [Early Access] Populate variables from event payloads and use those variables in other event actions. |
## Methods
| Name | Accessible by | Required Params | Description |
|:-----|:--------------|:----------------|:------------|
| `get_service_event_rule` | `SELECT` | `id, rule_id` | Get an Event Rule from a Service.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `list_service_event_rules` | `SELECT` | `id` | List Event Rules on a Service.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `create_service_event_rule` | `INSERT` | `id, data__rule` | Create a new Event Rule on a Service.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Scoped OAuth requires: `services.write`<br /> |
| `delete_service_event_rule` | `DELETE` | `id, rule_id` | Delete an Event Rule from a Service.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Scoped OAuth requires: `services.write`<br /> |
| `_get_service_event_rule` | `EXEC` | `id, rule_id` | Get an Event Rule from a Service.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `_list_service_event_rules` | `EXEC` | `id` | List Event Rules on a Service.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Scoped OAuth requires: `services.read`<br /> |
| `update_service_event_rule` | `EXEC` | `id, rule_id, data__rule_id` | Update an Event Rule on a Service. Note that the endpoint supports partial updates, so any number of the writable fields can be provided.<br />&lt;!-- theme: warning --&gt;<br />&gt; ### End-of-life<br />&gt; Rulesets and Event Rules will end-of-life soon. We highly recommend that you [migrate to Event Orchestration](https://support.pagerduty.com/docs/migrate-to-event-orchestration) as soon as possible so you can take advantage of the new functionality, such as improved UI, rule creation, APIs and Terraform support, advanced conditions, and rule nesting.<br /><br />Scoped OAuth requires: `services.write`<br /> |
